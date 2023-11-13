from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.crm.models import Lead

class Imovel(models.Model):
    name = models.CharField(_("name"), max_length=200)
    address = models.CharField(_("address"), max_length=200)
    price = models.DecimalField(_("price"), max_digits=10, decimal_places=2)
    description = models.TextField(_("description"))
    bedrooms = models.IntegerField(_("bedrooms"))
    bathrooms = models.IntegerField(_("bathrooms"))
    square_footage = models.IntegerField(_("square footage"))
   
    def __str__(self):
        return self.name

class ImovelLead(models.Model):
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)

class ImovelDoc(models.Model):
    token =  models.CharField(_("token"), max_length=255)
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)