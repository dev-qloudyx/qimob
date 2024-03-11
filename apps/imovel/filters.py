import django_filters
from django.db.models import Q
from .models import Imovel


class ImovelFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter()
    
    class Meta:
        model = Imovel
        fields = {
            'name': ['icontains'],
            'imovel_type': ['exact'],
            }