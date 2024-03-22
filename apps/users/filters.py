import django_filters
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from .models import Profile


class UserFilter(django_filters.FilterSet):

    # search = django_filters.CharFilter(method='imovel_filter', label='Pesquisar')

    class Meta:
        model = Profile
        fields = {
            'user__email': ['icontains'],
            'user__username': ['icontains'],
            'user__role': ['exact']
        }
        

    # def general_search_filter(self, queryset, name, value):
    #     return Imovel.objects.filter(square_footage__icontains=value)