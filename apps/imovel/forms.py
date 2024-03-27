from django import forms
from apps.imovel.models import Imovel
from .validators import only_int, only_char
from qaddress.models import Address

class ImovelForm(forms.ModelForm):
    postal_code1 = forms.CharField(label= "Código Postal",validators=[only_int],  max_length=4,required=False)
    postal_code2 = forms.CharField(label=False, validators=[only_int],  max_length=3,required=False)
    locality = forms.CharField(label="Localidade", max_length=100,widget=forms.Select(choices=[]), required=False)
    county = forms.CharField(label="Concelho", max_length=100, widget=forms.TextInput(attrs={'readonly': 'readonly'}),required=False)
    district = forms.CharField(label="Distrito", max_length=100, widget=forms.TextInput(attrs={'readonly': 'readonly'}),required=False)
    street = forms.CharField(label="Endereço", max_length=100, widget=forms.Select(choices=[]),required=False)
    number = forms.CharField(label="Número", max_length=100 ,required=False)
    moreinfo = forms.CharField(label="Mais Informaçao", max_length=100 ,required=False)
    class Meta:
        model = Imovel
        exclude = ['id']
        fields = ['name', 'imovel_type','image','description', 'bedrooms','bathrooms' ,'square_footage','price', 
                  'postal_code1', 'postal_code2', 'locality', 'county','district', 'street', 'number' , 'moreinfo']

class ImovelUpdateForm(forms.ModelForm):
    postal_code1 = forms.CharField(label= "Código Postal",validators=[only_int],  max_length=4,required=False)
    postal_code2 = forms.CharField(label=False, validators=[only_int],  max_length=3,required=False)
    locality = forms.CharField(label="Localidade", max_length=100,widget=forms.Select(choices=[]), required=False)
    county = forms.CharField(label="Concelho", max_length=100, widget=forms.TextInput(attrs={'readonly': 'readonly'}),required=False)
    district = forms.CharField(label="Distrito", max_length=100, widget=forms.TextInput(attrs={'readonly': 'readonly'}),required=False)
    street = forms.CharField(label="Endereço", max_length=100, widget=forms.Select(choices=[]),required=False)
    number = forms.CharField(label="Número", max_length=100 ,required=False)
    moreinfo = forms.CharField(label="Mais Informaçao", max_length=100 ,required=False)
    class Meta:
        model = Imovel
        exclude = ['id']
        fields = ['name', 'imovel_type','image','description', 'bedrooms','bathrooms' ,'square_footage','price', 
                  'postal_code1', 'postal_code2', 'locality', 'county','district', 'street', 'number' , 'moreinfo']
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance:

            imovel_address = self.instance.imovel_address.first()
            if imovel_address:
  
                try:
                    address = Address.objects.get(token=imovel_address.token)
                    print(address.street)
                    if address:
                        self.fields['locality'].widget.choices = [(address.locality, address.locality)]
                        self.fields['street'].widget.choices = [(address.street, address.street)]
                except:
                    pass
