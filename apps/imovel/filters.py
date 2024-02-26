import django_filters
from .models import Imovel


class ImovelFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', field_name='name', label='Nome')
    
    class Meta:
        model = Imovel
        fields = ['name']