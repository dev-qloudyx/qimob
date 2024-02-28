# using 'post_save' signal for User model to notify creation of a Profile
# model, due to the fact that we also have the admin app able to create users.

from django.conf import settings
from django.db.models.signals import post_save
from django.middleware.csrf import get_token
from django.dispatch import receiver
from django.http import HttpRequest
from apps.users.models import Profile, User
from allauth.account.views import PasswordResetView
from allauth.account.forms import ResetPasswordForm


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def send_reset_password_email(sender, instance, created, **kwargs):

    if created:
        request = HttpRequest()
        request.method = 'POST'
        request.META['HTTP_HOST'] = '127.0.0.1:8000'
        
        # pass the post form data
        form = ResetPasswordForm({"email": instance.email})
        if form.is_valid():
            form.save(request)

