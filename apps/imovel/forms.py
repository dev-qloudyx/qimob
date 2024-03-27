from django import forms
from apps.imovel.models import Imovel


class ImovelForm(forms.ModelForm):
    class Meta:
        model = Imovel
        exclude = ['id']

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)
        self.fields['created_by'].initial = user

