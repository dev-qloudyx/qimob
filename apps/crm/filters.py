import django_filters
from django.db.models import Q
from .models import Lead, Client, LeadStatus, LeadType


class LeadTypeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='lead', lookup_expr='icontains')
    status = django_filters.ChoiceFilter(field_name='status', choices=LeadStatus.objects.values_list('status', 'status__name').distinct())


    class Meta:
        model = LeadStatus
        fields = ['status', 'name']