from django import forms
from django.contrib.auth.models import User
from apps.users.models import Profile
from .load_photo_widget import LoadPhotoWidget

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'username']


class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField(widget=LoadPhotoWidget)
    class Meta:
        model = Profile
        fields = ['image', 'full_name', 'about']