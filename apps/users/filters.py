import django_filters
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from .models import Profile


class UserFilter(django_filters.FilterSet):

    # search = django_filters.CharFilter(method='custom_search', label='Pesquisar')

    

    class Meta:
        model = Profile
        fields = {
            'user__email': ['icontains'],
            'user__username': ['icontains'],
            'user__role': ['exact']
        }

    def __init__(self, *args, **kwargs):
        super(UserFilter, self).__init__(*args, **kwargs)
        
        
        self.filters['user__email__icontains'].label = 'Email'
        self.filters['user__username__icontains'].label = 'Username'
        self.filters['user__role'].label = 'Role'
    

    # def custom_search(self, queryset, name, value):
    #     if value:
    #         # Filter queryset based on multiple fields
    #         queryset = queryset.filter(
    #             django_filters.Q(user__email__icontains=value) |
    #             django_filters.Q(user__username__icontains=value)
    #         )
    #     return queryset