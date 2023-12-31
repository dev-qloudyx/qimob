import json
import os
from apps.crm.forms import ClientForm
from apps.crm.models import Client, ClientAddress, ClientDoc, ClientDocStatus, ClientDocStatusDesc, ClientMessage
from apps.crm.utils import handle_not_found, is_image
from qaddress.views import AddressView, retrieveAddressDataByToken, updateAddressDataByToken
from qdocs.views import FileDeleteView, FileListView, FileUploadView, FileView
from qmessages.views import MessageCreateView, MessageListView

from django.conf import settings
from django.contrib import messages
from django.http import HttpRequest, HttpResponse, JsonResponse
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

# Create your views here.

class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'client/client_create.html'
    success_url = reverse_lazy('crm:client_create_view')  
    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        super().form_valid(form)
        messages.success(self.request, 'Client created successfully!')
        pk = self.object.pk
        return HttpResponse(json.dumps( pk, ensure_ascii=False), content_type="application/json")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.htmx:
            base_template = "partial_base.html"
        else:
            base_template = "base.html"
        context['base_template'] = base_template
        
        return context

class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'client/client_update.html'
    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Client updated successfully!')
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.htmx:
            context['base_template'] = "partial_base.html"
        else:
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
        if self.request.htmx:
            context['base_template'] = "partial_base.html"
        else:
            context['base_template'] = "base.html"
        return context
    
    def get_success_url(self):
        return reverse_lazy('crm:client_detail_view', kwargs={'pk': self.object.pk})
    
class ClientDetailView(DetailView):
    model = Client
    template_name = 'client/client_detail.html'

    def get(self, request, *args, **kwargs):
        client_id = request.GET.get('client_id', None) or kwargs.get('pk', None)
        self.object = get_object_or_404(Client, pk=client_id)
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.htmx:
            context['base_template'] = "partial_base.html"
        else:
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
        base_url = self.request.build_absolute_uri(reverse('crm:client_list_view'))
        if self.request.htmx:
            base_template = "partial_base.html"
        else:
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
        if self.request.htmx:
            base_template = "partial_base.html"
        else:
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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.htmx:
            context['base_template'] = "partial_base.html"
        else:
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
            #client_doc_status.next_status()
        
        data = [{"size":454536,"name":"test.png","type":"f"}]
        
        return redirect('crm:client_docs_list_view', pk=kwargs['pk'])

class ClientDocsUploadViewJson(FileUploadView):
    base_template = "base.html"
    template_name = 'client/client_upload.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.htmx:
            context['base_template'] = "partial_base.html"
        else:
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
        if self.request.htmx:
            context['base_template'] = "partial_base.html"
        else:
            context['base_template'] = self.base_template
        return context

class ClientDocsDeleteView(FileDeleteView):
    template_name = 'client/client_docs.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.htmx:
            context['base_template'] = "partial_base.html"
        else:
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
        if self.request.htmx:
            context['base_template'] = "partial_base.html"
        else:
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

    
        

        
        
            
        
