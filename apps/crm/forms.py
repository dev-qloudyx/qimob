from django import forms
from .validators import only_int, only_char

from apps.crm.models import Client, Lead

class ClientForm(forms.ModelForm):
    postal_code1 = forms.CharField(label= "Código Postal",validators=[only_int],  max_length=4,required=False)
    postal_code2 = forms.CharField(label=False, validators=[only_int],  max_length=3,required=False)
    locality = forms.CharField(label="Localidade", max_length=100,widget=forms.Select(choices=[]), required=False)
    county = forms.CharField(label="Conselho", max_length=100, widget=forms.TextInput(attrs={'readonly': 'readonly'}),required=False)
    district = forms.CharField(label="Distrito", max_length=100, widget=forms.TextInput(attrs={'readonly': 'readonly'}),required=False)
    street = forms.CharField(label="Endereço", max_length=100, widget=forms.Select(choices=[]),required=False)
    moreinfo = forms.CharField(label="Mais Informaçao (porta, andar, ...)", max_length=100 ,required=False)
    
    
    class Meta:
        model = Client
        fields = ['name', 'phone_number', 'email_address', 'nif', 'ident_doc', 'postal_code1', 'postal_code2', 'locality', 'county','district', 'street', 'moreinfo']
        labels = {
            'ident_doc': 'Documento Identificação',
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        return phone_number.replace(" ", "")
    
class ClientUpdateForm(forms.ModelForm):
    postal_code1 = forms.CharField(label= "Código Postal",validators=[only_int],  max_length=4,required=False)
    postal_code2 = forms.CharField(label=False, validators=[only_int],  max_length=3,required=False)
    locality = forms.CharField(label="Localidade", max_length=100, widget=forms.TextInput(attrs={'readonly': 'readonly'}),required=False)
    county = forms.CharField(label="Conselho", max_length=100, widget=forms.TextInput(attrs={'readonly': 'readonly'}),required=False)
    district = forms.CharField(label="Distrito", max_length=100, widget=forms.TextInput(attrs={'readonly': 'readonly'}),required=False)
    street = forms.CharField(label="Endereço", max_length=100, widget=forms.TextInput(attrs={'readonly': 'readonly'}),required=False)
    moreinfo = forms.CharField(label="Mais Informaçao (porta, andar, ...)", max_length=100 ,required=False)
    
    
    class Meta:
        model = Client
        fields = ['name', 'phone_number', 'email_address', 'nif', 'ident_doc', 'postal_code1', 'postal_code2', 'locality', 'county','district', 'street', 'moreinfo']
        labels = {
            'ident_doc': 'Documento Identificação',
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        return phone_number.replace(" ", "")
    
    
class LeadCreateForm(forms.ModelForm):
    class Meta:
        model=Lead
        fields = ['leadtype','short_name', 'district','county', 'client','imovel']