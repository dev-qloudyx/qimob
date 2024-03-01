from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from apps.imovel.filters import ImovelFilter
from django_filters.views import FilterView
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from qdocs.views import FileDeleteView, FileListView, FileUploadView, FileView
from django.urls import reverse, reverse_lazy

from apps.imovel.forms import ImovelForm
from apps.imovel.models import Imovel, ImovelDoc, ImovelDocStatus, ImovelDocStatusDesc

# Create your views here.
@method_decorator([login_required], name='dispatch')
class ImovelCreateView(CreateView):
    model = Imovel
    form_class = ImovelForm
    template_name = 'imovel/imovel_form.html'
    success_url = reverse_lazy('imovel:imovel_list')


@method_decorator([login_required], name='dispatch')
class ImovelListView(FilterView, ListView):
    queryset = Imovel.objects.all()
    filterset_class = ImovelFilter
    ordering = ['-created_at']
    template_name = 'imovel/imovel_list.html'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base_template = "base.html"
 
        context = {
            'imoveis': context['object_list'],
            'base_template': base_template, 
        }
        return context

    
@method_decorator([login_required], name='dispatch')
class ImovelDetailView(DetailView):
    model = Imovel
    template_name = 'imovel/imovel_detail.html'

    def get(self, request, *args, **kwargs):
        client_id = request.GET.get('imovel_id', None) or kwargs.get('pk', None)
        self.object = get_object_or_404(Imovel, pk=client_id)
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['base_template'] = "base.html"
        return context
    

@method_decorator([login_required], name='dispatch')
class ImovelUpdateView(UpdateView):
    model = Imovel
    fields = '__all__'
    template_name = 'imovel/imovel_form.html'
    success_url = reverse_lazy('imovel:imovel_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_template'] = True
        return context


class ImovelDocsUploadView(FileUploadView):
    base_template = "base.html"
    template_name = 'imovel/imovel_upload.html'
    
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
        imovel = get_object_or_404(Imovel, pk=kwargs['pk'])
        context['imovel'] = imovel
        context['form'] = form
        return render(request, self.template_name, context)
    
    
    def post(self, request, *args, **kwargs):
        kwargs['project'] = 'qimob'
        kwargs['app'] = 'imovel'
        kwargs['model'] = 'Imovel'
        tokens = super().post(request, *args, **kwargs)
        imovel = get_object_or_404(Imovel, pk=kwargs['pk'])
        for token in tokens:
            imovel_doc = ImovelDoc.objects.create(token=token, imovel=imovel)
            imovel_doc_status_desc = ImovelDocStatusDesc.objects.get(desc="New")
            imovel_doc_status = ImovelDocStatus.objects.create(imovel_doc=imovel_doc, doc_desc=imovel_doc_status_desc)
            #client_doc_status.next_status()
        
        data = [{"size":454536,"name":"test.png","type":"f"}]
        
        return redirect('imovel:imovel_docs_list_view', pk=kwargs['pk'])