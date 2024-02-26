from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from apps.imovel.filters import ImovelFilter
from django_filters.views import FilterView
from django.views.generic import CreateView, ListView
from django.urls import reverse, reverse_lazy

from apps.imovel.forms import ImovelForm
from apps.imovel.models import Imovel

# Create your views here.
@method_decorator([login_required], name='dispatch')
class ImovelCreateView(CreateView):
    template_name = 'imovel/imovel_form.html'
    form_class = ImovelForm

    def get_success_url(self):
        return reverse_lazy('imovel:imovel_list')
    

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