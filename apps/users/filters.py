import django_filters
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from .models import Profile, TeamLeader, Teams


class UserFilter(django_filters.FilterSet):
    user__email = django_filters.CharFilter(lookup_expr='icontains', field_name='user__email', label='E-mail')
    user__username = django_filters.CharFilter(lookup_expr='icontains', field_name='user__username', label='Username')
    user_leaders = django_filters.ChoiceFilter(method='leaders_search_filter', label='Chefes Equipa', choices=[[t.pk, t] for t in TeamLeader.objects.all()])

    # search = django_filters.CharFilter(method='custom_search', label='Pesquisar')

    

    class Meta:
        model = Profile
        fields = {
            'user__email': ['icontains'],
            'user__username': ['icontains'],
            'user__role': ['exact']
        }


    def leaders_search_filter(self, queryset, name, value):
        leader_id = value
        members = Teams.objects.filter(team_leader_id=leader_id)
        return Profile.objects.filter(user_id__in=members.values_list('team_member', flat=True))


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