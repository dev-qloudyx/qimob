import django_filters
from django.db.models import Q
from .models import Imovel


class ImovelFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='custom_filter', label='Pesquisar')
    imovel_type = django_filters.ChoiceFilter(field_name='imovel_type__imovel_type', label='Tipo de Imovel', choices=[[i.imovel_type.imovel_type, i.imovel_type.imovel_type] for i in Imovel.objects.all().distinct('imovel_type__imovel_type')])
    # block__history = django_filters.ChoiceFilter(field_name='block__history', label='História', choices=[[b.block.history.pk, b.block.history] for b in IBBlockStatus.objects.all().filter(status=65).distinct('block__history').order_by('block__history')])
    
    class Meta:
        model = Imovel
        fields = ['search']

    def custom_filter(self, queryset, name, value):
        return Imovel.objects.filter(Q(square_footage__icontains=value))