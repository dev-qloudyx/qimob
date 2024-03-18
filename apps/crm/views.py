import json
import os
import uuid

from django.forms import BaseModelForm
import pandas as pd
from apps.crm.forms import ClientForm, LeadCreateForm, ClientUpdateForm
from apps.crm.models import Client, ClientAddress, ClientDoc, ClientDocStatus, ClientDocStatusDesc, ClientMessage, Lead, LeadDoc, LeadComment
from apps.crm.utils import handle_not_found, is_image
from qaddress.views import AddressView, retrieveAddressDataByToken, updateAddressDataByToken
from qdocs.views import FileDeleteView, FileListView, FileUploadView, FileView
from qmessages.views import MessageCreateView, MessageListView

from django.conf import settings
from django.contrib import messages
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.views import View
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from typing import Any
from urllib.parse import urljoin

from qaddress.models import Address, CountyData, DistrictData, CPData
from qdocs.models import File

from django.db.models import Q
from datetime import datetime

from apps.imovel.models import Imovel
# Create your views here.

class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'client/client_create.html'
   
    def form_valid(self, form):
        # Generate a token for the client
        
        cp4 = self.request.POST.get('postal_code1')
        cp3 = self.request.POST.get('postal_code2')
        district = self.request.POST.get('district')
        county = self.request.POST.get('county')
        locality = self.request.POST.get('locality')
        street = self.request.POST.get('street')
        moreinfo = self.request.POST.get('moreinfo')
        if moreinfo is None:
            moreinfo = ' '


        print(district)
        print(locality)
        print(moreinfo)
             
        client_instance = form.save(commit=False)
        client_instance.save()


        if any(value for value in [cp4, cp3, locality, county, district]):

            token = uuid.uuid4()

            ClientAddress.objects.create(
                client=client_instance,
                token=token
            )
            

            Address.objects.create(
                token=token,
                project="QIMOB",
                app='crm',
                model='client',
                cp4=cp4,
                cp3=cp3,
                postal_code=f"{cp4}-{cp3}",
                district=district,
                county=county,
                locality=locality,
                street=street,
                number=moreinfo,
                created_at=datetime.now(),
                updated_at=datetime.now()
            )

            print(token)

        return super().form_valid(form)
    

    def get_success_url(self):
        previous_url = self.request.session.get('previous_url')

        if previous_url:
            return previous_url
        
        return reverse_lazy('crm:client_list_view')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base_template = "base.html"
        context['base_template'] = base_template
        
        return context

class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientUpdateForm
    template_name = 'client/client_update.html'
    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Client updated successfully!')
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['base_template'] = "base.html"
        return context
    
    def get_success_url(self):
        return reverse_lazy('crm:client_detail_view', kwargs={'pk': self.object.pk})

class ClientUpdateViewJson(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'client/client_update.html'
    
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
        
    def form_valid(self, form):
        super().form_valid(form)
        return JsonResponse({'success': 'Client updated successfully!'}, status=200)
    
    def form_invalid(self, form):
        super().form_invalid(form)
        return JsonResponse({'error': form.errors}, status=400)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['base_template'] = "base.html"
        return context
    
    def get_success_url(self):
        return reverse_lazy('crm:client_detail_view', kwargs={'pk': self.object.pk})
    
class ClientDetailView(DetailView):
    model = Client
    template_name = 'client/client_detail.html'

    def get_object(self, queryset=None):
        client_id = self.request.GET.get('client_id') or self.kwargs.get('pk')
        return get_object_or_404(Client, pk=client_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        client_tokens = self.object.clientdoc_set.values_list('token', flat=True)
        doc_files = []
        if client_tokens:
            for token in client_tokens:
                print(token)
                doc = get_object_or_404(File, token=token)
                print(doc.upload)
                doc_files.append(doc)
            #print(doc_token)
            #doc = get_object_or_404(File, token = doc_token)
            #print(doc.upload)
            #context['doc_file'] = doc

            context['doc_files'] = doc_files
        else:
            context['doc_files'] = None
    

        client_address = self.object.clientaddress_set.first() 
        if client_address:
            address_token = client_address.token
            print(address_token)
            if address_token:
                # Query the Address model based on the token
                address = get_object_or_404(Address, token=address_token)
                print(address.postal_code)
                

                # Create a dictionary to store address data
                address_data = {
                    'district': address.district,
                    'county': address.county,
                    'locality': address.locality,
                    'postal_code': address.postal_code,
                    'street': address.street,
                    'number': address.number,
                    'more_info': address.more_info,
                    # Add more fields as needed
                }
                context['address_data'] = address_data
            else:
                context['address_data'] = None
        else:
            context['address_data'] = None

        context['base_template'] = "base.html"

        return context

class ClientDetailViewJson(View):
    model = Client

    def get(self, request, *args, **kwargs):
        try:
            client_id = request.GET.get('client_id', None) or kwargs.get('pk', None)
            client = self.model.objects.get(id=client_id)
            data = {}
            data['client'] = {
                'id': client.id,
                'name': client.name,
                'email_address': client.email_address,
                'phone_number': client.phone_number
            }
            return JsonResponse(data, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=404)
        
class ClientListView(ListView):
    model = Client
    paginate_by = 5
    template_name = 'client/client_list.html'
    ordering = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        clients = self.get_queryset()  # Get the queryset of clients
        client_address = clients.first().clientaddress_set.first()
        print('hello')

        # if client_address:
        #     address_token = client_address.token
        #     print(address_token)
        #     if address_token:
        #         # Query the Address model based on the token
        #         address = get_object_or_404(Address, token=address_token)
        #         print(address)
        #         print('hello')

        #         # Create a dictionary to store address data
        #         address_data = {
        #             'district': address.district,
        #             'county': address.county,
        #             'locality': address.locality,
        #             'postal_code': address.postal_code,
        #             'street': address.street,
        #             'number': address.number,
        #             'more_info': address.more_info,
        #             # Add more fields as needed
        #         }
        #         context['address_data'] = address_data
        #         print(address_data)
        #     else:
        #         context['address_data'] = None
        # else:
        #     context['address_data'] = None

        base_url = self.request.build_absolute_uri(reverse('crm:client_list_view'))
        
        base_template = "base.html"
 
        context.update({
            'base_url': base_url,
            'clients': context['object_list'],
            'base_template': base_template, 
        })

        return context

# Document Integration Below.

class ClientChangeStatusView(View):
    
    def post(self, request, *args, **kwargs):
        
        try:
            data = json.loads(request.body.decode('utf-8'))
            client_id = data.get('client_id')
            status_desc = data.get('status_desc')
            token = data.get('token')

            if client_id is not None and status_desc is not None:
                client = Client.objects.get(id=client_id)
                client_doc = ClientDoc.objects.get(token=token, client=client)
                client_doc_status_desc = ClientDocStatusDesc.objects.get(desc=status_desc)
                ClientDocStatus.objects.create(client_doc=client_doc, doc_desc=client_doc_status_desc)
                return JsonResponse({'message': 'ClientDocStatus updated successfully.'})
            else:
                return JsonResponse({'error': 'Invalid parameters provided.'}, status=400)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
class StatusDescAllViewJson(View):
    def get(self, request, *args, **kwargs):
        token = request.GET.get('token')
        clientdoc = ClientDoc.objects.get(token=token)
        client_doc_statuses = clientdoc.clientdoc_status.order_by('-created_on')
        last_status = client_doc_statuses.first()
        status_desc = ClientDocStatusDesc.objects.all().values('desc', 'created_on', 'updated_on')
        status_desc_list = list(status_desc)
        status_desc_list = [d for d in status_desc_list if d['desc'] != last_status.doc_desc.desc]
        return JsonResponse(status_desc_list, safe=False)
    
class ClientDocsListViewJson(FileListView):
    paginate_by = 105
    template_name = 'client/client_docs.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base_url = self.request.build_absolute_uri(reverse('crm:client_docs_list_view', kwargs={'pk': self.kwargs['pk']}))
        base_template = "partial_base.html"
        client =  get_object_or_404(Client, pk=self.kwargs.get('pk'))
        clientdocs = ClientDoc.objects.filter(client=self.kwargs.get('pk')).order_by('id')

        status = []

        for i in clientdocs:
            client_doc_statuses = i.clientdoc_status.order_by('-created_on')
            last_status = client_doc_statuses.first()
            token = i.token
            status.append({token:last_status.doc_desc.desc})

        context.update({
            'base_url': base_url,
            'client': client,
            'base_template': base_template,
            'status': status
        })
        return context
    
    def get(self, request, *args, **kwargs):
        self.tokens = [obj.token for obj in ClientDoc.objects.filter(client=self.kwargs.get('pk')).order_by('id')]
        
        objects = super().get(request, *args, **kwargs)
        data = []
        status_list = objects.context_data['status']
        for i in objects.context_data['object_list']:
            file_path = i.upload.name
            directory, full_filename = file_path.rsplit('/', 1)
            base = settings.URL
            full_url = urljoin(base, i.upload.url)
            
            try:
                name, extension = full_filename.split('.', 1)
            except:
                name = os.path.splitext(full_filename)[0]
                extension = None

            for status in status_list:
                for token, status_value in status.items():
                    if token == str(i.token):
                        token_status = status_value
                        break
            
            width, height = is_image(i.upload.path)
            
            response = {
                'id': i.pk,
                'name': name,
                'isDirectory': False,
                'hasDirectories': False,
                'path': i.upload.url,
                'extension': extension,
                'size': i.upload.size,
                'created': i.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                'modified': i.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                'token': i.token,
                'status': token_status,
                'download_path': full_url
            }
            if width and height is not None:
                response['width'] = width
                response['height'] = height
            data.append(response)
        return JsonResponse(data, safe=False, status=200)

class ClientDocsListView(FileListView):
    paginate_by = 5
    template_name = 'client/client_docs.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base_url = self.request.build_absolute_uri(reverse('crm:client_docs_list_view', kwargs={'pk': self.kwargs['pk']}))
        base_template = "base.html"
        
        client =  get_object_or_404(Client, pk=self.kwargs.get('pk'))
        clientdocs = ClientDoc.objects.filter(client=self.kwargs.get('pk')).order_by('id')

        status = []

        for i in clientdocs:
            client_doc_statuses = i.clientdoc_status.order_by('-created_on')
            last_status = client_doc_statuses.first()
            token = i.token
            status.append({token:last_status.doc_desc.desc})

        context.update({
            'base_url': base_url,
            'client': client,
            'base_template': base_template,
            'status': status
        })
        return context
    
    def get(self, request, *args, **kwargs):
        self.tokens = [obj.token for obj in ClientDoc.objects.filter(client=self.kwargs.get('pk')).order_by('id')]
        return super().get(request, *args, **kwargs)
     
class ClientDocsUploadView(FileUploadView):
    base_template = "base.html"
    template_name = 'client/client_upload.html'


    def get_success_url(self):
        return reverse_lazy('crm:client_detail_view', kwargs={'pk': self.object.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['base_template'] = self.base_template
        return context
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = super().get_form()
        client = get_object_or_404(Client, pk=kwargs['pk'])
        context['client'] = client
        context['form'] = form
        return render(request, self.template_name, context)
    
    
    def post(self, request, *args, **kwargs):
        kwargs['project'] = 'qimob'
        kwargs['app'] = 'crm'
        kwargs['model'] = 'Client'
        tokens = super().post(request, *args, **kwargs)
        client = get_object_or_404(Client, pk=kwargs['pk'])
        for token in tokens:
            client_doc = ClientDoc.objects.create(token=token, client=client)
            client_doc_status_desc = ClientDocStatusDesc.objects.get(desc="New")
            client_doc_status = ClientDocStatus.objects.create(client_doc=client_doc, doc_desc=client_doc_status_desc)

        return redirect('crm:client_detail_view', pk=kwargs['pk'])

class ClientDocsUploadViewJson(FileUploadView):
    base_template = "base.html"
    template_name = 'client/client_upload.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['base_template'] = self.base_template
        return context
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = super().get_form()
        client = get_object_or_404(Client, pk=kwargs['pk'])
        context['client'] = client
        context['form'] = form
        return JsonResponse(context, safe=False)
        
    def post(self, request, *args, **kwargs):
        kwargs['project'] = 'qimob'
        kwargs['app'] = 'crm'
        kwargs['model'] = 'Client'
        tokens = super().post(request, *args, **kwargs)
        client = get_object_or_404(Client, pk=kwargs['pk'])
        for token in tokens:
            client_doc = ClientDoc.objects.create(token=token, client=client)
            client_doc_status_desc = ClientDocStatusDesc.objects.get(desc="New")
            client_doc_status = ClientDocStatus.objects.create(client_doc=client_doc, doc_desc=client_doc_status_desc)
            #client_doc_status.next_status()
        
        data = [{"size":454536,"name":"test.png","type":"f"}]
        
        return JsonResponse({"success":"upload finished"}, safe=False, status=200)

class ClientDocsView(FileView):
    base_template = "base.html"
    template_name = 'client/client_doc.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['base_template'] = self.base_template
        return context

class ClientDocsDeleteView(FileDeleteView):
    template_name = 'client/client_docs.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['base_template'] = self.base_template
        return context
    
    def post(self, request, *args, **kwargs):
        if 'multiple_delete' in request.POST:
            return self.multiple_delete(request, *args, **kwargs)
        else:
            files_deleted = super().post(request, *args, **kwargs)
            if files_deleted:
                client_doc = get_object_or_404(ClientDoc, token=kwargs.get('token'))
                pk = client_doc.client.pk
                client_doc.delete()
                return redirect('crm:client_docs_list_view', pk=pk)

    def multiple_delete(self, request, *args, **kwargs):
        files_deleted = super().multiple_delete(request, *args, **kwargs)
        if files_deleted:
            tokens = request.POST.getlist('tokens')
            client = None
            for token in tokens:
                client_doc = get_object_or_404(ClientDoc, token=token)
                client_doc.deleted = True
                client_doc.save()
                client = get_object_or_404(Client, pk=client_doc.client.id)
            return redirect('crm:client_docs_list_view', pk=client.pk)
        
# Address Integration Below.

class ClientAddressCreateView(AddressView):
    base_template = "base.html"
    template_name = 'client/client_address.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['base_template'] = self.base_template
        return context
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = super().get_form()
        client = get_object_or_404(Client, pk=kwargs['pk'])
        context['client'] = client
        context['form'] = form
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        client_id = request.POST.get('client_id')
        client = get_object_or_404(Client, pk=client_id)
        kwargs['project'] = 'qimob'
        kwargs['app'] = 'crm'
        kwargs['model'] = 'Client'
        response = super().post(request, *args, **kwargs)
        
        if response.get('success'):
            
            ClientAddress.objects.create(token=response['success'], client=client)
            return JsonResponse(response.get('success'), safe=False)
        else:
            return JsonResponse(response.get('error'), safe=False)

class ClientAddressView(retrieveAddressDataByToken):
    
    def get(self, request, pk, *args, **kwargs):
        client = Client.objects.get(id=pk)
        client_address = ClientAddress.objects.filter(client=client).order_by('id')
        tokens = [obj.token for obj in client_address]
        kwargs['tokens'] = tokens
        response = super().get(request, *args, **kwargs)
        data = {}
        if response.get('success'):
            data['address'] = response.get('success')
            return JsonResponse(data, safe=False, status=200)
        else:
            data['error'] = response.get('error')
            return JsonResponse(data, safe=False, status=404)
    
class ClientUpdateAddressDataByTokenJsonView(updateAddressDataByToken):
    
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
# Notes Integration Below.

class ClientMessageCreateView(MessageCreateView):
     
    def post(self, request, *args, **kwargs):
        client_id = request.POST.get('client_id') or kwargs.get('pk')
        client = get_object_or_404(Client, pk=client_id)
        kwargs['project'] = 'qimob'
        kwargs['app'] = 'crm'
        kwargs['model'] = 'Client'
        response = super().post(request, *args, **kwargs)
        if 'error' not in response:
            ClientMessage.objects.create(token=response['success'], client=client)
            return JsonResponse({"success":"Message created successfully."}, safe=False)
        else:
            return JsonResponse({"error": "Message not created successfully."}, safe=False)

class ClientMessageListView(MessageListView):

    def get(self, request, pk, *args, **kwargs):
        try:
            client = Client.objects.get(id=pk)
        except Client.DoesNotExist:
            return handle_not_found(request, "Client not found.")
        
        client_message = ClientMessage.objects.filter(client=client).order_by('id')
        if not client_message:
            handle_not_found(request, "ClientMessage not found.")
        client_tokens = [str(msg.token) for msg in client_message]
        kwargs['tokens'] = client_tokens
        return super().get(request, *args, **kwargs)

class LeadCreateView(CreateView):
    model = Lead
    form_class = LeadCreateForm
    template_name = 'client/lead_update.html'
    success_url = reverse_lazy('crm:lead_list_view')

    def form_valid(self, form):

        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['base_template'] = "base.html"
        return context
    
class LeadListView(ListView):
    model = Lead
    template_name = 'client/lead_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()

        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(short_desc__icontains=search_query) |
                Q(short_name__icontains=search_query) |
                Q(client__name__icontains=search_query)
            )

        # Filtering
        type = self.request.GET.get('type')
        if type:
            queryset = queryset.filter(leadtype=type)

        # Ordering
        order_by = self.request.GET.get('order_by', '-created_at')
        if order_by:
            queryset = queryset.order_by(order_by)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        leadslist = self.get_queryset() 
        context['leadslist']=leadslist
       
        context['base_template'] = "base.html"
        return context
    


class LeadDetailView(DetailView):
    model = Lead
    template_name = 'client/lead_detail.html'

    def post(self, request, *args, **kwargs):
        if 'cancel' in request.POST:
            lead = self.get_object()
            lead.is_active = not lead.is_active
            lead.save()
            return HttpResponseRedirect(self.request.path_info)  # Redirect to the same page after processing the POST request
        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        lead = self.get_object()

        if lead.owner.role == 'admin' or lead.owner == self.request.user:
            if lead.is_active:
                context['buttontext'] = 'Cancelar'
            else:
                context['buttontext'] = 'Reabrir'
        else:
            context['buttontext'] = None


        lead_tokens = self.object.leaddoc_set.values_list('token', flat=True)
        doc_files = []
        if lead_tokens:
            for token in lead_tokens:
                print(token)
                doc = get_object_or_404(File, token=token)
                print(doc.upload)
                doc_files.append(doc)
            context['doc_files'] = doc_files

        else:
            context['doc_files'] = None


        lead_comments = LeadComment.objects.filter(lead=self.object)
        comment_list = []
        for comment in lead_comments:
            comment_list.append(comment)
        context['comments'] = comment_list


        clientdata = get_object_or_404(Client, id=lead.client_id)  
        context['clientdata'] = clientdata 

        imoveldata = get_object_or_404(Imovel, id=lead.imovel_id) 
        context['imoveldata'] = imoveldata 

          
        context['base_template'] = "base.html"
        return context
    
    

class LeadUpdateView(UpdateView):
    model = Lead
    fields = ['owner', 'client', 'imovel', 'short_name', 'short_desc','desc', 'district', 'county', 'com_tip']
    template_name = 'client/lead_create.html'

    def get_success_url(self):
        return reverse_lazy('crm:lead_detail_view', kwargs={'pk': self.object.pk})


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
 
        context['base_template'] = "base.html"
        return context



class LeadDocsUploadView(FileUploadView):
    base_template = "base.html"
    template_name = 'client/lead_upload.html'


    def get_success_url(self):
        return reverse_lazy('crm:lead_detail_view', kwargs={'pk': self.object.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['base_template'] = self.base_template
        return context
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = super().get_form()
        lead = get_object_or_404(Lead, pk=kwargs['pk'])
        context['lead'] = lead
        context['form'] = form
        return render(request, self.template_name, context)
    
    
    def post(self, request, *args, **kwargs):
        kwargs['project'] = 'qimob'
        kwargs['app'] = 'crm'
        kwargs['model'] = 'Lead'
        tokens = super().post(request, *args, **kwargs)
        lead = get_object_or_404(Lead, pk=kwargs['pk'])
        for token in tokens:
            LeadDoc.objects.create(token=token, lead=lead)

        return redirect('crm:lead_detail_view', pk=kwargs['pk'])


def get_counties(request):
    if request.method == 'GET' and 'district_id' in request.GET:
        district_id = request.GET.get('district_id')
        try:
            
            counties = CountyData.objects.filter(DD_id=district_id)
            county_data = {county.id: county.DESIG for county in counties}
            return JsonResponse(county_data)
        except CountyData.DoesNotExist:

            return JsonResponse({'error': 'No counties found for the selected district.'}, status=404)
    else:
        
        return JsonResponse({'error': 'Invalid request.'}, status=400)
        

def get_locality(request):
    if request.method == 'GET' and 'county_id' in request.GET:
        county_id = request.GET.get('county_id')
        try:
           
            localities = CPData.objects.filter(CC_id=county_id).distinct('LOCALIDADE')
            locality_data = {locality.id: locality.LOCALIDADE for locality in localities}
            return JsonResponse(locality_data)
        except CountyData.DoesNotExist:
           
            return JsonResponse({'error': 'No localities found for the selected county.'}, status=404)
    else:
        
        return JsonResponse({'error': 'Invalid request.'}, status=400)
            
def get_address_info(request):
    if request.method == 'GET' and 'postal_code' in request.GET:
        postal_code = request.GET.get('postal_code')
        code1 = request.GET.get('code1')
        code2 = request.GET.get('code2')
        print(postal_code)
        print(code1)
        print(code2)
        
        try:
            address_info_list = CPData.objects.filter(CP4=code1, CP3=code2)
            # for record in address_info_list:
            #         print(record.CP4)
            #         print(record.CP3) 
            
            # print(address_info.CP4 + address_info.CP3)
            print(address_info_list)

            if address_info_list.exists():
                streets = []
                localitys = []
                for address_info in address_info_list:
                    street = f'{address_info.ART_TIPO + " " if not (pd.isnull(address_info.ART_TIPO) or address_info.ART_TIPO == "nan") else ""}' \
                             f'{address_info.PRI_PREP + " " if not (pd.isnull(address_info.PRI_PREP) or address_info.PRI_PREP == "nan") else ""}' \
                             f'{address_info.ART_TITULO + " " if not (pd.isnull(address_info.ART_TITULO) or address_info.ART_TITULO == "nan") else ""}' \
                             f'{address_info.SEG_PREP + " " if not (pd.isnull(address_info.SEG_PREP) or address_info.SEG_PREP == "nan") else ""}' \
                             f'{address_info.ART_DESIG + " " if not (pd.isnull(address_info.ART_DESIG) or address_info.ART_DESIG == "nan") else ""}' \
                             f'{address_info.ART_LOCAL if not (pd.isnull(address_info.ART_LOCAL) or address_info.ART_LOCAL == "nan") else ""}'
                    
                    streets.append({
                        'street': street,
                        
                    })
                    print(street)
                    localitys.append({
                        'locality' : address_info.LOCALIDADE
                        })

                data = {
                    'district': address_info.DD.DESIG,  
                    'county': address_info.CC.DESIG,
                    'localitys': localitys,
                    'streets': streets
                }
                print(data)
                return JsonResponse(data)
            else:
                return JsonResponse({'error': 'No address information found for the entered postal codes.'}, status=404)
        except CPData.DoesNotExist:
            return JsonResponse({'error': 'No address information found for the entered postal codes.'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request.'}, status=400)
