from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from apps.cliente.models import Cliente, ClienteDoc
from apps.docs.models import File
from apps.docs.views import FileDeleteView, FileUploadView
from apps.docs.forms import FileForm
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib import messages


class ClienteCreateView(CreateView):
    model = Cliente
    fields = ['name']
    template_name = 'cliente_create.html'
    success_url = reverse_lazy('cliente:cliente_create')  

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Cliente created successfully!')
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.htmx:
            base_template = "partial_base.html"
        else:
            base_template = "base.html"
        context['base_template'] = base_template
        return context

class ClienteView(View):
    def get(self, request, *args, **kwargs):
        clientes = Cliente.objects.all()
        
        if request.htmx:
            base_template = "partial_base.html"
        else:
            base_template = "base.html"
        context = {
            'clientes': clientes,
            'base_template': base_template
                
        }
        context['base_template'] = base_template

        return render(request, 'clientes.html', context)
        

    def post(self, request, *args, **kwargs):
        cliente = Cliente.objects.get(id=request.POST['id'])
        cliente.name = request.POST['name']
        cliente.save()
        clientes = Cliente.objects.all()
        
        if request.htmx:
            base_template = "partial_base.html"
        else:
            base_template = "base.html"
        
        context = {
            'clientes': clientes,
            'base_template': base_template
                
        }
        context['base_template'] = base_template

        messages.success(self.request, 'Cliente created successfully!')
        return render(request, 'clientes.html', context)

class ClienteListView(ListView):
    model = Cliente
    paginate_by = 5
    template_name = 'cliente_list.html'

    def get_queryset(self):
        return Cliente.objects.all().order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.htmx:
            base_template = "partial_base.html"
        else:
            base_template = "base.html"
 
        context.update({
            'clientes': context['object_list'],
            'base_template': base_template, 
        })
        return context
            
class ClienteDocsListView(ListView):
    model = ClienteDoc
    paginate_by = 5
    template_name = 'cliente_docs.html'

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return ClienteDoc.objects.filter(client=pk).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.htmx:
            base_template = "partial_base.html"
        else:
            base_template = "base.html"
        
        try:
            cliente =  self.object_list[0].client
        except:
            cliente = None
        context.update({
            'docs': context['object_list'],
            'cliente': cliente,
            'base_template': base_template, 
        })
        return context
    
     
class ClientFileUploadView(FileUploadView):

    def get(self, request):
            form = FileForm()
            cliente_id = Cliente.objects.get(id=1).id
            if request.htmx:
                base_template = "partial_base.html"
            else:
                base_template = "base.html"
            context = {
                'form': form,
                'base_template': base_template,
                'cliente_id': cliente_id
            }
            return render(request, 'upload.html', context)
    
    def post(self, request):
        cliente_id = request.POST.get('cliente_id') 
        client = Cliente.objects.get(id=cliente_id)

        files = request.FILES.getlist('upload')
        for file in files:
            form = FileForm(request.POST, {'upload': file})
            if form.is_valid():
                new_file = form.save(commit=False)
                new_file.owner = request.user
                new_file.save()
 
                ClienteDoc.objects.create(file=new_file, client=client)

        docs = ClienteDoc.objects.filter(client=client)
        context = {
            'docs': docs
        }
        if request.htmx:
            base_template = "partial_base.html"
        else:
            base_template = "base.html"
        
        context['base_template'] = base_template

        return render(request, 'cliente_docs.html', context)

class ClientFileDeleteView(FileDeleteView):
    model = File
    success_url = reverse_lazy('cliente:cliente_listview')

    def form_valid(self, form):
        self.object = self.get_object()
        self.object.delete()
        #self.object.hard_delete()
        return HttpResponseRedirect(self.get_success_url())