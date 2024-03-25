import os
from typing import Any
from django.db.models import Q
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.utils import timezone
from django.http import JsonResponse
from apps.users.allauth_utils import custom_form_valid
from apps.users.filters import UserFilter
from apps.users.models import Profile, Teams, User, TeamLeader, UserRole
from main import settings
from .forms import CustomSignupForm, UserUpdateForm, ProfileUpdateForm
from apps.users.roles import roles_required
from allauth.account.views import  SignupView, PasswordChangeView
from allauth.account.views import RedirectAuthenticatedUserMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import ListView, DetailView
from django.utils.decorators import method_decorator
from allauth.account.views import PasswordResetView
from django_filters.views import FilterView
from django.core.files.base import ContentFile

# Create your views here.

@method_decorator([login_required], name='dispatch')
class HomeView(View):
    def get(self, request):
        context = {}
        return render(request, 'home.html', context )


class CustomRedirectMixin(RedirectAuthenticatedUserMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super(RedirectAuthenticatedUserMixin, self).dispatch(request, *args, **kwargs)
        else:
            return super().dispatch(request, *args, **kwargs)

# USERS
class UserListViewJson(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.all().values('id', 'username', 'email')
        return JsonResponse(list(users), safe=False)


@method_decorator([login_required], name='dispatch')
class ListUsersView(ListView):
    model = Profile
    queryset = Profile.objects.all().filter(user__is_active=True)
    template_name = 'users/user_list.html'
    context_object_name = 'users'
    paginate_by = 5

    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset()
        
        if user.role == UserRole.objects.get(role_name="chefe_equipa"):
            leader = TeamLeader.objects.get(team_leader=user.id)
            members = Teams.objects.filter(team_leader=leader)
            queryset = Profile.objects.filter(user_id__in=members.values_list('team_member', flat=True)).filter(user__is_active=True)
        
        if user.role == UserRole.objects.get(role_name="consultor"):
            leader = Teams.objects.get(team_member=user.id).team_leader
            members = Teams.objects.filter(team_leader=leader)
            queryset = Profile.objects.filter(
                Q(user_id__in=members.values_list('team_member', flat=True)) | 
                Q(user_id=leader.team_leader.pk)).filter(user__is_active=True)

        self.filterset = UserFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # print(context['object_list'])
        users_with_pics = []
        for profile in context['object_list']:
            user = profile.user
            profile_pic = profile.image.url if profile.image else None 

            try:
                user_leader = Teams.objects.get(team_member=user.id).team_leader 
            except Teams.DoesNotExist:
                user_leader = None

            users_with_pics.append({'user': user, 'profile_pic': profile_pic, 'user_leader': user_leader})

        # print(users_with_pics)
        base_template = "base.html"
        context = {
            'user_filter': self.filterset.form,
            'users': users_with_pics,
            'base_template': base_template, 
        }
        return context
    

class CustomPasswordChangeView(PasswordChangeView):
    template_name = "account/password_change.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base_template = "base.html"
        context['base_template'] = base_template

        return context
    
# @method_decorator(roles_required(['admin']), name='dispatch')
class CustomSignupView(CustomRedirectMixin, SignupView):
   template_name = "account/signup.html"

   def form_valid(self, form):
        custom_form_valid(self, form)
        PasswordResetView.as_view()(self.request)

        user = self.user
        leader_role = UserRole.objects.get(role_name="chefe_equipa")
        admin_role = UserRole.objects.get(role_name="admin")
        if user.role == leader_role or user.role == admin_role:
            TeamLeader.objects.create(team_leader=user)

        if user.role == UserRole.objects.get(role_name="consultor"):
            leader_id = self.request.POST.get('team_leader')
            leader = TeamLeader.objects.get(id=leader_id)
            Teams.objects.create(team_leader=leader, team_member=user)

        if not user.profile.image:
      
            default_image_path = os.path.join(settings.STATIC_ROOT, 'images', 'default.png')  # Path to your default image
            with open(default_image_path, 'rb') as f:         
                default_image_content = f.read()
                user.profile.image.save('client.png', ContentFile(default_image_content), save=True)

        return redirect('users:users_list')


@method_decorator(login_required, name='dispatch')
class ProfileView(View):

    def get(self, request):
        u_form = UserUpdateForm(instance=request.user, user_auth=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        
        base_template = "base.html"

        context = {
            'u_form': u_form,
            'p_form': p_form,
            'base_template': base_template,
        }

        return render(request, "profile/profile_form.html", context)

    def post(self, request):
        u_form = UserUpdateForm(request.POST, instance=request.user, user_auth=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():

            this_instance = u_form.save(commit=False)
            original_instance = get_object_or_404(User, pk=this_instance.pk)
            if this_instance.is_active != original_instance.is_active:
                if this_instance.is_active:
                    this_instance.last_active = timezone.now()
                else:
                    this_instance.last_inactive = timezone.now()
            
            this_instance.save()
            u_form.save()
            p_form.save()
            messages.success(request, 'A sua conta foi atualizada!')
        else:
            messages.error(request,
                'Problemas em atualizar a sua conta, veja erros em baixo...')
        base_template = "base.html"

        context = {
            'u_form': u_form,
            'p_form': p_form,
            'base_template': base_template,
        }

        return render(request, "profile/profile_form.html", context)
    
@method_decorator(roles_required(['admin']), name='dispatch')
class UserUpdateView(View):
    template_name = "profile/profile_form.html"
    base_template = "base.html"

    def get_user_data(self, pk):
        user = get_object_or_404(User, pk=pk)
        team_leader = None
        try:
            team = Teams.objects.get(team_member=user)
            team_leader = team.team_leader
        except Teams.DoesNotExist:
            pass
        return user, team_leader
    
    def render_invalid_form(self, request, u_form, p_form, user):
        context = {
            'user': user, 
            'u_form': u_form, 
            'p_form': p_form, 
            'base_template': self.base_template
        }
        return render(request, self.template_name, context)
        # return redirect(reverse_lazy('users:users_list'))

    def get(self, request, pk):
        user, team_leader = self.get_user_data(pk)
        u_form = UserUpdateForm(instance=user, user_auth=request.user, initial={'team_leader': team_leader})
        p_form = ProfileUpdateForm(instance=user.profile)

        context = {
            'user': user, 
            'u_form': u_form, 
            'p_form': p_form, 
            'base_template': self.base_template
            }
        
        return render(request, self.template_name, context)

    def post(self, request, pk):
        user, _ = self.get_user_data(pk)
        u_form = UserUpdateForm(request.POST, instance=user, user_auth=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            this_instance = u_form.save(commit=False)
            original_instance = get_object_or_404(User, pk=this_instance.pk)
            leader_role = UserRole.objects.get(role_name="chefe_equipa")
            admin_role = UserRole.objects.get(role_name="admin")

            # Update active/inactive date
            if this_instance.is_active != original_instance.is_active:
                if this_instance.is_active:
                    this_instance.last_active = timezone.now()
                    if this_instance.role in [leader_role, admin_role]:
                        TeamLeader.objects.get_or_create(team_leader=this_instance)
                else:
                    this_instance.last_inactive = timezone.now()

            # Check for role change
            if this_instance.role != original_instance.role:

                if this_instance.role in [leader_role, admin_role]:
                    Teams.objects.filter(team_member=this_instance.pk).delete()
                    TeamLeader.objects.get_or_create(team_leader=this_instance)

                elif this_instance.role == UserRole.objects.get(role_name="consultor"):
                    if original_instance.role == leader_role:
                        teamleader = get_object_or_404(TeamLeader, team_leader=this_instance.pk)
                        members = Teams.objects.filter(team_leader=teamleader.pk)

                        if members.exists():
                            messages.error(request, 'Ainda tem utilizadores associados a este chefe de equipa...')
                            return self.render_invalid_form(request, u_form, p_form, user)
                        else:
                            leader_id = request.POST.get('team_leader')
                            leader = TeamLeader.objects.get(id=leader_id)
                            Teams.objects.create(team_leader=leader, team_member=this_instance)
                            TeamLeader.objects.get(team_leader=this_instance).delete()

            # Update team leader
            new_team_leader_id = request.POST.get('team_leader')
            if new_team_leader_id:
                new_team_leader = TeamLeader.objects.get(id=new_team_leader_id)
                try:
                    new_team = Teams.objects.get(team_member=this_instance)
                    new_team.team_leader = new_team_leader
                    new_team.save()
                except Teams.DoesNotExist:
                    pass

            this_instance.save()
            u_form.save()
            p_form.save()
            messages.success(request, 'A sua conta foi atualizada!')

        else:
            messages.error(request, 'Problemas em atualizar a sua conta, veja erros em baixo...')
            return self.render_invalid_form(request, u_form, p_form, user)
        
        context = {
            'user': user, 
            'u_form': u_form, 
            'p_form': p_form, 
            'base_template': self.base_template
            }
    
        return render(request, self.template_name, context)

    
@method_decorator(login_required, name='dispatch')
class ProfileDetailView(DetailView):
    model = Profile
    template_name = "users/user_detail.html"

    def get_object(self, queryset=None):
        user_id = self.kwargs.get('pk')
        return get_object_or_404(Profile, user_id=user_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base_template = "base.html"
        context['base_template'] = base_template

        return context
