from django.urls import path
from apps.users.views import ProfileView, CustomSignupView, HomeView, CustomPasswordChangeView
from django.views.generic.base import RedirectView

app_name = "users"

urlpatterns = [
    path('', RedirectView.as_view(url='accounts/login/', permanent=False)),
    path('home/', HomeView.as_view(), name='home'),
    path('accounts/profile/', ProfileView.as_view(), name='profile'),
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    path('accounts/password/change/', CustomPasswordChangeView.as_view(), name='account_change_password')
]
