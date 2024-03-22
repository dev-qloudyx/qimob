from django import forms
import django_filters
from django.db.models import Q
from django.db import models
from django.utils.translation import gettext_lazy as _
from .models import Profile


class UserFilter(django_filters.FilterSet):
    user__email = django_filters.CharFilter(lookup_expr='icontains', field_name='user__email', label='E-mail')
    user__username = django_filters.CharFilter(lookup_expr='icontains', field_name='user__username', label='Username')

    class Meta:
        model = Profile
        fields = {
            'user__role': ['exact'],
            'user__is_active': ['exact'],
        }


        
# class IBVlogFilter(django_filters.FilterSet):
    # search = django_filters.CharFilter(method='imovel_filter', label='Pesquisar')
    
    
#     class Meta:
#         model = IBBlockStatus
#         fields = ['name', 'block__history', 'block__book']


    # def general_search_filter(self, queryset, name, value):
    #     return Imovel.objects.filter(square_footage__icontains=value)