import django_filters
from django.db.models import Q
from .models import Lead, Client, LeadStatus, LeadType


class LeadTypeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='lead__short_name', lookup_expr='icontains')
    status = django_filters.ChoiceFilter(field_name='status', choices=LeadStatus.objects.values_list('status', 'status__name').distinct())
    leadtype = django_filters.ChoiceFilter(field_name='lead__leadtype', choices=LeadStatus.objects.values_list('lead__leadtype', 'lead__leadtype__type').distinct())
    district = django_filters.ChoiceFilter(field_name='lead__district', choices=LeadStatus.objects.values_list('lead__district', 'lead__district__DESIG').distinct())
    county = django_filters.ChoiceFilter(field_name='lead__county', choices=LeadStatus.objects.values_list('lead__county', 'lead__county__DESIG').distinct())


    class Meta:
        model = LeadStatus
        fields = ['status', 'name', 'leadtype', 'district', 'county']