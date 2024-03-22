from django import forms
import django_filters
from django.db.models import Q
from django.db import models
from django.utils.translation import gettext_lazy as _
from .models import Profile, TeamLeader, Teams


class UserFilter(django_filters.FilterSet):
    user__email = django_filters.CharFilter(lookup_expr='icontains', field_name='user__email', label='E-mail')
    user__username = django_filters.CharFilter(lookup_expr='icontains', field_name='user__username', label='Username')
    user_leaders = django_filters.ChoiceFilter(method='leaders_search_filter', label='Chefes Equipa', choices=[[t.pk, t] for t in TeamLeader.objects.all()])

    class Meta:
        model = Profile
        fields = {
            'user__role': ['exact'], 
            'user__is_active': ['exact'],
            }

    def leaders_search_filter(self, queryset, name, value):
        leader_id = value
        members = Teams.objects.filter(team_leader_id=leader_id)
        return Profile.objects.filter(user_id__in=members.values_list('team_member', flat=True))


        
# class IBVlogFilter(django_filters.FilterSet):
    # search = django_filters.CharFilter(method='imovel_filter', label='Pesquisar')
    
    
#     class Meta:
#         model = IBBlockStatus
#         fields = ['name', 'block__history', 'block__book']


    # def general_search_filter(self, queryset, name, value):
    #     return Imovel.objects.filter(square_footage__icontains=value)