from django import forms
from apps.imovel.models import Imovel


class ImovelForm(forms.ModelForm):
    class Meta:
        model = Imovel
        exclude = ['id']

