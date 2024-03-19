from django import forms
from .validators import only_int, only_char
from qaddress.models import Address
from apps.crm.models import Client, Lead, ClientAddress, LeadShare

class ClientForm(forms.ModelForm):
    postal_code1 = forms.CharField(label= "Código Postal",validators=[only_int],  max_length=4,required=False)
    postal_code2 = forms.CharField(label=False, validators=[only_int],  max_length=3,required=False)
    locality = forms.CharField(label="Localidade", max_length=100,widget=forms.Select(choices=[]), required=False)
    county = forms.CharField(label="Concelho", max_length=100, widget=forms.TextInput(attrs={'readonly': 'readonly'}),required=False)
    district = forms.CharField(label="Distrito", max_length=100, widget=forms.TextInput(attrs={'readonly': 'readonly'}),required=False)
    street = forms.CharField(label="Endereço", max_length=100, widget=forms.Select(choices=[]),required=False)
    number = forms.CharField(label="Porta", max_length=100 ,required=False)
    moreinfo = forms.CharField(label="Mais Informaçao", max_length=100 ,required=False)
    
    
    class Meta:
        model = Client
        fields = ['name', 'phone_number', 'email_address', 'nif', 'ident_doc', 'postal_code1', 'postal_code2', 'locality', 'county','district', 'street', 'number' , 'moreinfo']
        labels = {
            'ident_doc': 'Documento Identificação',
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        return phone_number.replace(" ", "")
    
class ClientUpdateForm(forms.ModelForm):
    postal_code1 = forms.CharField(label= "Código Postal",validators=[only_int],  max_length=4,required=False)
    postal_code2 = forms.CharField(label=False, validators=[only_int],  max_length=3,required=False)
    locality = forms.CharField(label="Localidade", max_length=100,widget=forms.Select(choices=[]), required=False)
    county = forms.CharField(label="Concelho", max_length=100, widget=forms.TextInput(attrs={'readonly': 'readonly'}),required=False)
    district = forms.CharField(label="Distrito", max_length=100, widget=forms.TextInput(attrs={'readonly': 'readonly'}),required=False)
    street = forms.CharField(label="Endereço", max_length=100, widget=forms.Select(choices=[]),required=False)
    number = forms.CharField(label="Número", max_length=100 ,required=False)
    moreinfo = forms.CharField(label="Mais Informaçao", max_length=100 ,required=False)
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance:
            # Access the related ClientAddress instance
            client_address = self.instance.client_address.first()
            if client_address:
                # Access the related Address instance using the token
                try:
                    address = Address.objects.get(token=client_address.token)
                    print(address.street)
                    if address:
                        self.fields['locality'].widget.choices = [(address.locality, address.locality)]
                        self.fields['street'].widget.choices = [(address.street, address.street)]
                except:
                    pass


    class Meta:
        model = Client
        fields = ['name', 'phone_number', 'email_address', 'nif', 'ident_doc', 'postal_code1', 'postal_code2', 'locality', 'county','district', 'street', 'number' , 'moreinfo']
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

class LeadShareForm(forms.ModelForm):
    class Meta:
        model = LeadShare
        fields = ['user', 'can_read', 'can_write']