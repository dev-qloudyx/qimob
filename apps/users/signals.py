# using 'post_save' signal for User model to notify creation of a Profile
# model, due to the fact that we also have the admin app able to create users.

from django.conf import settings
from django.db.models.signals import post_save
from django.middleware.csrf import get_token
from django.dispatch import receiver
from django.http import HttpRequest
from apps.users.models import Profile, User

from allauth.account.forms import ResetPasswordForm

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
