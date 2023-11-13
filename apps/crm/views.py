
from apps.docs.views import FileDeleteView, FileListView, FileUploadView, FileView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib import messages
from django.views import View
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.core.paginator import Paginator
from apps.crm.models import Client, ClientDoc

# Create your views here.
class ClientCreateView(CreateView):
    model = Client
    fields = ['name']
    template_name = 'client/client_create.html'
    success_url = reverse_lazy('crm:client_create')  

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Client created successfully!')
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.htmx:
            base_template = "partial_base.html"
        else:
            base_template = "base.html"
        context['base_template'] = base_template
        return context

class ClientView(FileListView):
    template_name = 'client/client_view.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        if self.request.htmx:
            context['base_template'] = "partial_base.html"
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        client = get_object_or_404(Client, pk=kwargs['pk'])
        client_docs = ClientDoc.objects.filter(client=client)
        context.update ({
            'client': client, 
            'client_docs': client_docs,
        })
        super().get(request, *args, **kwargs)
        return render(request, self.template_name, context)
        

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(self, *args, **kwargs)
        client = Client.objects.get(id=request.POST['id'])
        client.name = request.POST['name']
        client.save()
        clients = Client.objects.all()
        
        if request.htmx:
            base_template = "partial_base.html"
        else:
            base_template = "base.html"
        
        context.update ({
            'client': client, 
        })

        messages.success(self.request, 'Client created successfully!')
        return render(request, 'client/clients.html', context)

class ClientListView(ListView):
    model = Client
    paginate_by = 5
    template_name = 'client/client_list.html'

    def get_queryset(self):
        return Client.objects.all().order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base_url = self.request.build_absolute_uri(reverse('crm:client_listview'))
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


###########################
# Docs Integration Below. #
########################### 
       
class ClientDocsListView(ListView):
    model = ClientDoc
    paginate_by = 5
    template_name = 'client/client_docs.html'

    def get_queryset(self):
        return ClientDoc.objects.filter(client=self.kwargs.get('pk')).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base_url = self.request.build_absolute_uri(reverse('crm:clientdocs_listview', kwargs={'pk': self.kwargs['pk']}))
        if self.request.htmx:
            base_template = "partial_base.html"
        else:
            base_template = "base.html"
        
        client =  get_object_or_404(Client, pk=self.kwargs.get('pk'))

        context.update({
            'base_url': base_url,
            'docs': context['object_list'],
            'client': client,
            'base_template': base_template, 
        })
        return context
        
class ClientFileUploadView(FileUploadView):
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
        kwargs['app'] = 'crm'
        kwargs['model'] = 'Client'
        tokens = super().post(request, *args, **kwargs)
        client = get_object_or_404(Client, pk=kwargs['pk'])
        for token in tokens:
            ClientDoc.objects.create(token=token, client=client)
        return redirect('crm:clientdocs_listview', pk=kwargs['pk'])

class ClientFileView(FileView):
    base_template = "base.html"
    template_name = 'client/client_doc.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.htmx:
            context['base_template'] = "partial_base.html"
        else:
            context['base_template'] = self.base_template
        return context
    
class ClientFileDeleteView(FileDeleteView):
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
                context = self.get_context_data()
                client_doc = get_object_or_404(ClientDoc, token=kwargs.get('token'))
                docs = ClientDoc.objects.filter(client=client_doc.client).order_by('id')
                context.update({
                    'docs': docs,
                    'client': client_doc.client,
                })
                client_doc.delete()
                return render(request, self.get_template_name(), context)

    def multiple_delete(self, request, *args, **kwargs):
        files_deleted = super().multiple_delete(request, *args, **kwargs)
        if files_deleted:
            context = self.get_context_data()
            tokens = request.POST.getlist('tokens')
            client = None
            for token in tokens:
                client_doc = get_object_or_404(ClientDoc, token=token)
                client_doc.deleted = True
                client_doc.save()
                client = get_object_or_404(Client, pk=client_doc.client.id)
            docs = ClientDoc.objects.filter(client=client).order_by('id')
            context.update({
                'docs': docs,
                'client': client,
            })
            return render(request, self.get_template_name(), context)
        
