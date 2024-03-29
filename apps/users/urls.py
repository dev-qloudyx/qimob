from django.urls import path, reverse_lazy
from apps.users.views import ProfileView, ProfileDetailView, UserUpdateView, CustomSignupView, HomeView, CustomPasswordChangeView, UserListViewJson, ListUsersView
from django.views.generic.base import RedirectView

app_name = "users" 

urlpatterns = [
    path('', RedirectView.as_view(url='accounts/login/', permanent=False) , name='login'),
    path('home/', HomeView.as_view(), name='home'),

    # Account
    path('accounts/profile/', ProfileView.as_view(), name='profile'),
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    path('accounts/password/change/', CustomPasswordChangeView.as_view(), name='account_change_password'),

    # Users
    path('get_users/', UserListViewJson.as_view(), name='get_users'),
    path('users/list/', ListUsersView.as_view(), name='users_list'),
    path('users/update/<int:pk>/', UserUpdateView.as_view(), name='profile_update'),
    path('users/detail/<int:pk>/', ProfileDetailView.as_view(), name='profile_detail'),
]
