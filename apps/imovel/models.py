from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.crm.models import Lead
from apps.users.models import License, User

class BaseModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)
    

class ImovelType(models.Model):
    imovel_type = models.CharField(max_length=50)

    def __str__(self):
        return self.imovel_type


class Imovel(models.Model):
    #license = models.ForeignKey(License, related_name='imovel_license', on_delete=models.CASCADE, default = 1, null=True, blank= True)
    name = models.CharField(_("name"), max_length=200)
    imovel_type = models.ForeignKey(ImovelType, on_delete=models.SET_NULL, blank=True, null=True)
    image = models.ImageField(upload_to='imovel_pics', verbose_name=_('Photo') , blank=True)
    price = models.DecimalField(_("price"), max_digits=10, decimal_places=2)
    description = models.TextField(_("description"), blank=True, null=True)
    bedrooms = models.IntegerField(_("bedrooms"))
    bathrooms = models.IntegerField(_("bathrooms"))
    square_footage = models.IntegerField(_("square footage"))
    url = models.URLField(verbose_name=_('URL'), blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(_("phone number"), max_length=16, blank=True, null=True)
    gps_latitude = models.CharField(max_length=50, verbose_name=_('Latitude'), blank=True, null=True)
    gps_longitude = models.CharField(max_length=50, verbose_name=_('Longitude'), blank=True, null=True)
    url_map = models.URLField(verbose_name=_('URL Map'), blank=True, null=True)
    visit_timeslots = models.CharField(verbose_name=_('Visits Time Slots'), blank=True, null=True)
    availability = models.BooleanField(verbose_name=_('Availability'), default=True)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Created by'))
   
    def __str__(self):
        return self.name


class ImovelLead(models.Model):
    imovel = models.ForeignKey("Imovel", on_delete=models.CASCADE)
    lead = models.ForeignKey("crm.Lead", on_delete=models.CASCADE)


class ImovelDoc(models.Model):
    token =  models.CharField(_("token"), max_length=255)
    imovel = models.ForeignKey('Imovel', on_delete=models.CASCADE)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)
    deleted = models.BooleanField(default=False)

    objects = BaseModelManager()


class ImovelDocStatusDesc(models.Model):
    desc = models.CharField(_("desc"), max_length=255)
    created_on = models.DateTimeField(_("created on"), auto_now_add=True)
    updated_on = models.DateTimeField(_("updated on"), auto_now=True)

    def __str__(self):
        return 'Desc: {}'.format(self.desc)
    
    
class ImovelDocStatus(models.Model): 
    doc_desc = models.ForeignKey(ImovelDocStatusDesc,related_name="imoveldocstatus_imoveldocstatusdesc", verbose_name=_("doc desc"), on_delete=models.CASCADE)
    imovel_doc = models.ForeignKey(ImovelDoc, related_name="imoveldoc_status", verbose_name=_("imoveldoc"), on_delete=models.CASCADE)
    created_on = models.DateTimeField(_("created on"), auto_now_add=True)
    updated_on = models.DateTimeField(_("updated on"), auto_now=True)

    def __str__(self):
        return 'ImovelDoc Status: {} - Status Date: {} - Updated On: {}'.format(self.doc_desc.desc, self.created_on, self.updated_on)

    def next_status(self):
        status_list = list(ImovelDocStatusDesc.objects.values_list('desc', flat=True))
        current_status_index = status_list.index(self.doc_desc.desc)
        if current_status_index < len(status_list) - 1:
            next_status_desc = status_list[current_status_index + 1]
            next_status = ImovelDocStatusDesc.objects.get(desc=next_status_desc)
            self.doc_desc = next_status
            self.save()


class ImovelAddress(models.Model):
    token =  models.CharField(_("token"), max_length=255)
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE, related_name='imovel_address')
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)
    deleted = models.BooleanField(default=False)

    objects = BaseModelManager()