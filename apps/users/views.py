from typing import Any
from django.db.models.query import QuerySet
from django.utils import timezone
from django.http import JsonResponse
from apps.users.allauth_utils import custom_form_valid
from apps.users.filters import UserFilter
from apps.users.models import Profile, Teams, User, TeamLeader, UserRole
from .forms import CustomSignupForm, UserUpdateForm, ProfileUpdateForm
from apps.users.roles import roles_required
from allauth.account.views import  SignupView, PasswordChangeView
from allauth.account.views import RedirectAuthenticatedUserMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from allauth.account.views import PasswordResetView
from django_filters.views import FilterView

# Create your views here.

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
    queryset = Profile.objects.all()
    template_name = 'users/user_list.html'
    context_object_name = 'users'
    paginate_by = 12

    def get_queryset(self):
        user = self.request.user
        leader = Teams.objects.filter(team_member=user.id).first()
        members = Teams.objects.filter(team_leader=leader)

        cons_role = UserRole.objects.get(role_name="consultor")
        chief_role = UserRole.objects.get(role_name="chefe_equipa")
        
        if user.role == cons_role or user.role == chief_role:
            if not members.exists():
                queryset = Profile.objects.none()
            else:
                queryset = Profile.objects.filter(user_id__in=members)
        else:
            queryset = super().get_queryset()

        self.filterset = UserFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base_template = "base.html"
        context = {
            'form': self.filterset.form,
            'users': context['object_list'],
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
        if user.role == UserRole.objects.get(role_name="chefe_equipa"):
            TeamLeader.objects.create(team_leader=user)

        if user.role == UserRole.objects.get(role_name="consultor"):
            leader_id = self.request.POST.get('team_leader')
            leader = TeamLeader.objects.get(id=leader_id)
            Teams.objects.create(team_leader=leader, team_member=user)

        return redirect('users:users_list')


@method_decorator(login_required, name='dispatch')
class ProfileView(View):

    def get(self, request):
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        
        base_template = "base.html"

        context = {
            'u_form': u_form,
            'p_form': p_form,
            'base_template': base_template,
        }

        return render(request, "profile/profile.html", context)

    def post(self, request):
        u_form = UserUpdateForm(request.POST, instance=request.user)
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
        # context = {
        #     'u_form': u_form,
        #     'p_form': p_form
        # }
        base_template = "base.html"

        context = {
            'u_form': u_form,
            'p_form': p_form,
            'base_template': base_template,
        }

        return render(request, "profile/profile.html", context)
    
@method_decorator(login_required, name='dispatch')
class ProfileUpdate(View):

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        u_form = UserUpdateForm(instance=user)
        p_form = ProfileUpdateForm(instance=user.profile)
        
        base_template = "base.html"

        context = {
            'user': user,
            'u_form': u_form,
            'p_form': p_form,
            'base_template': base_template,
        }

        return render(request, "profile/profile.html", context)

    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        u_form = UserUpdateForm(request.POST, instance=user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=user.profile)
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
        # context = {
        #     'u_form': u_form,
        #     'p_form': p_form
        # }
        base_template = "base.html"

        context = {
            'user': user,
            'u_form': u_form,
            'p_form': p_form,
            'base_template': base_template,
        }

        return render(request, "profile/profile.html", context)