from django import forms

from apps.crm.models import Client

class ClientForm(forms.ModelForm):
    
    class Meta:
        model = Client
        fields = ['name', 'phone_number', 'email_address']

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        return phone_number.replace(" ", "")