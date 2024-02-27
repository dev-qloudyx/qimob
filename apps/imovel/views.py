from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from apps.imovel.filters import ImovelFilter
from django_filters.views import FilterView
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.urls import reverse, reverse_lazy

from apps.imovel.forms import ImovelForm
from apps.imovel.models import Imovel

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
        if self.request.htmx:
            context['base_template'] = "partial_base.html"
        else:
            context['base_template'] = "base.html"
        return context
    

@method_decorator([login_required], name='dispatch')
class ImovelUpdateView(UpdateView):
    model = Imovel
    fields = '__all__'
    template_name = 'imovel/imovel_form.html'
    success_url = reverse_lazy('imovel:imovel_list')