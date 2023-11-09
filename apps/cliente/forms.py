from apps.cliente.models import ClienteDoc
from django import forms

class ClienteDocForm(forms.ModelForm):
    class Meta:
        model = ClienteDoc
        fields = ('description', 'file', 'client')