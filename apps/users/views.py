
from django.http import JsonResponse
from apps.users.models import User
from .forms import UserUpdateForm, ProfileUpdateForm
from apps.users.roles import roles_required
from allauth.account.views import  SignupView, PasswordChangeView

from allauth.account.views import RedirectAuthenticatedUserMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.utils.decorators import method_decorator

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

class UserListViewJson(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.all().values('id', 'username', 'email')
        return JsonResponse(list(users), safe=False)

class CustomPasswordChangeView(PasswordChangeView):
    template_name = "account/password_change.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.htmx:
            base_template = "partial_base.html"
        else:
            base_template = "base.html"
        context['base_template'] = base_template

        return context

@method_decorator(roles_required(['admin']), name='dispatch')
class CustomSignupView(CustomRedirectMixin, SignupView):
   template_name = "account/signup.html"

@method_decorator(login_required, name='dispatch')
class ProfileView(View):

    def get(self, request):
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        
        if request.htmx:
            base_template = "partial_base.html"
        else:
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
            u_form.save()
            p_form.save()
            messages.success(request, 'A sua conta foi atualizada!')
        else:
            messages.error(request,
                'Problemas em atualizar a sua conta, veja erros em baixo...')
        context = {
            'u_form': u_form,
            'p_form': p_form
        }
        if request.htmx:
            base_template = "partial_base.html"
        else:
            base_template = "base.html"

        context = {
            'u_form': u_form,
            'p_form': p_form,
            'base_template': base_template,
        }

        return render(request, "profile/profile.html", context)