import django_filters
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from .models import Profile, TeamLeader, Teams, UserRole


class UserFilter(django_filters.FilterSet):
    user__email = django_filters.CharFilter(lookup_expr='icontains', field_name='user__email', label=_('By E-mail'))
    user__username = django_filters.CharFilter(lookup_expr='icontains', field_name='user__username', label=_('By Username'))
    user__is_active = django_filters.BooleanFilter(lookup_expr='exact', label=_('Is Active'))
    user__role = django_filters.ChoiceFilter(lookup_expr='exact', label=_('By Role'), choices=[[t.pk, t] for t in UserRole.objects.all()])
    user_leaders = django_filters.ChoiceFilter(method='leaders_search_filter', label=_('By Team Leader'), choices=lambda: [[t.pk, str(t)] for t in TeamLeader.objects.all()] if TeamLeader.objects.exists() else [('', _('No Team Leaders available'))])

    class Meta:
        model = Profile
        exclude = ['id', 'image']

    def leaders_search_filter(self, queryset, name, value):
        leader_id = value
        members = Teams.objects.filter(team_leader_id=leader_id)
        return Profile.objects.filter(user_id__in=members.values_list('team_member', flat=True))
