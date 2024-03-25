from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from apps.users.models import Profile, Teams, UserRole, TeamLeader
from .load_photo_widget import LoadPhotoWidget
from allauth.account.forms import SignupForm

User = get_user_model() 

class CustomSignupForm(SignupForm):
    email = forms.EmailField(label='E-mail')
    role = forms.ModelChoiceField(queryset=UserRole.objects.all(), label='Role')
    team_leader = forms.ModelChoiceField(TeamLeader.objects.all(), label='Lider Equipa', required=False)

    class Meta:
        model = User 
        fields = ['email', 'username', 'role', 'is_active', 'team_leader']
        help_texts = {
            'password1': '',
            'password2': ''
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].required = False
        self.fields['password2'].required = False
        self.fields['password1'].widget.attrs['hidden'] = True
        self.fields['password2'].widget.attrs['hidden'] = True
        self.fields['password1'].label = ''
        self.fields['password2'].label = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

    def signup(self, request, user):  # Override signup method
        user.role = self.cleaned_data['role']
        user.save()
        return user

    # def save(self, request):
    #     user = super().save(request)
    #     user.save()
    #     return user


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    role = forms.ModelChoiceField(queryset=UserRole.objects.all(), label='Role')
    team_leader = forms.ModelChoiceField(TeamLeader.objects.all(), label='Lider Equipa', required=False)

    class Meta:
        model = User
        fields = ['email', 'username', 'role', 'is_active', 'team_leader']

    def __init__(self, *args, **kwargs):
        user_auth = kwargs.pop('user_auth', None)
        # user = kwargs.pop('instance', None)                                   ZONA EM TESTES!
        # team_leader = TeamLeader.objects.exclude(team_leader=user.pk)
        super().__init__(*args, **kwargs)
        # self.fields['team_leader'].queryset = team_leader

        if user_auth and not user_auth.is_admin:
            self.fields['role'].widget = forms.HiddenInput()
            self.fields['is_active'].widget = forms.HiddenInput()


class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField(widget=LoadPhotoWidget)

    class Meta:
        model = Profile
        fields = ['image', 'full_name', 'about']