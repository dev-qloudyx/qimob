from typing import Any
from django.db import models
from apps.users.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from qaddress.models import Address, DistrictData, CountyData, CPData



class BaseModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)
    

class License(models.Model):
    name = models.CharField(_('company name'), max_length = 100)
    phone = models.CharField(_("phone number"), max_length=16)
    logo = models.ImageField(_("company logo"),upload_to='media/logos')

    def __str__(self):
        return self.name





class Lead(models.Model):
    license = models.ForeignKey(License,related_name='lead_license' , on_delete=models.CASCADE, default = 1, null=True, blank= True)
    leadtype = models.ForeignKey('LeadType',related_name='lead_type' , on_delete=models.CASCADE, default = 1)
    owner = models.ForeignKey(User, related_name='lead_owner', on_delete=models.CASCADE)
    client = models.ForeignKey('Client', verbose_name=_('lead client'), on_delete=models.CASCADE)
    imovel = models.ForeignKey('imovel.Imovel', verbose_name=_('lead imovel'), on_delete=models.CASCADE)
    short_name = models.CharField(_('short name'), max_length=20)
    short_desc = models.CharField(_('short description'), max_length=50, null=True, blank=True)
    desc = models.CharField(_('description'), max_length=500, null=True, blank=True)
    district = models.ForeignKey(DistrictData,on_delete=models.CASCADE , verbose_name=_('district'))
    county = models.ForeignKey(CountyData, on_delete=models.CASCADE , verbose_name=_('county'))
    # locality = models.ForeignKey(CPData,on_delete=models.CASCADE, verbose_name=_('locality'))
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_by', on_delete=models.CASCADE, default=1)
    com_tip = models.CharField(_('comunication tips'), max_length=100, null=True, blank=True)
    is_active = models.BooleanField(_('is active'), default=True)
    
    def __str__(self):
        return self.short_name
    
class LeadType(models.Model):
    type = models.CharField( _('lead type'), max_length=20)

    def __str__(self):
        return self.type

class LeadScore(models.Model):
    lead = models.ForeignKey(Lead, verbose_name=_("lead"), on_delete=models.CASCADE)
    score = models.PositiveIntegerField(_("score"), validators=[MinValueValidator(0), MaxValueValidator(100)])
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)

    def __str__(self):
        return f'{self.lead.short_name} - {self.score}%'

class LeadStatusDesc(models.Model):
    desc = models.CharField(_("desc"), max_length=255)
    created_on = models.DateTimeField(_("created on"), auto_now_add=True)
    updated_on = models.DateTimeField(_("updated on"), auto_now=True)

    def __str__(self):
        return 'Desc: {}'.format(self.desc)

class LeadStatus(models.Model): 
    lead_desc = models.ForeignKey(LeadStatusDesc,related_name="leadstatus_leadstatusdesc", verbose_name=_("lead desc"), on_delete=models.CASCADE)
    lead = models.ForeignKey(Lead, related_name="lead_status", verbose_name=_("lead"), on_delete=models.CASCADE)
    created_on = models.DateTimeField(_("created on"), auto_now_add=True)
    updated_on = models.DateTimeField(_("updated on"), auto_now=True)

    def __str__(self):
        return 'Lead Status: {} - Status Date: {} - Updated On: {}'.format(self.lead_desc.desc, self.created_on, self.updated_on)

class LeadDoc(models.Model):
    token =  models.CharField(_("token"), max_length=255)
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)


class LeadComment(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    comment = models.CharField(_('comment'), max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_at = models.DateTimeField(_('posted_at'), auto_now_add=True)

    def __str__(self):
        return self.comment

class Prospects(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    short_desc = models.CharField(_('short description'), max_length=100)
    partyname = models.CharField(_('third party name'), max_length=100)
    partyphone = models.BigIntegerField(
        validators=[MinValueValidator(900000000), MaxValueValidator(999999999)]
    )
    partyemail = models.EmailField(_('third party email'))

class Contact(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name='contact')
    name = models.CharField(_("name"), max_length=100)
    email = models.EmailField(_("email"), max_length=100, unique=True)
    phone_number = models.CharField(_("phone number"), max_length=16, blank=True)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_on = models.DateTimeField(_("updated on"), auto_now=True)

    def __str__(self):
        return self.name


class Client(models.Model):
    license = models.ForeignKey(License,related_name='client_license' , on_delete=models.CASCADE, default = 1,null=True, blank= True)
    name = models.CharField(_("name"), max_length=255)
    phone_number = models.CharField(_("phone number"), max_length=16)
    email_address = models.EmailField(_("email address"), max_length=254, null=True, unique=True)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)
    nif = models.CharField(_("NIF"), max_length=9, null=True, unique=True, blank=True)
    ident_doc = models.CharField(_("identity document"), max_length=15, null=True, unique=True, blank=True)
    #created_by = models.CharField(_("created by"),null=True, unique=True)
    #license = models.ForeignKey(Client, on_delete=models.CASCADE)
    #client_type = models.CharField(_("created by"),null=True, unique=True)

    def __str__(self):
        return self.name

class ClientAddress(models.Model):
    token =  models.CharField(_("token"), max_length=255)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)
    deleted = models.BooleanField(default=False)

    objects = BaseModelManager()

class ClientMessage(models.Model):
    token =  models.CharField(_("token"), max_length=255)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)
    deleted = models.BooleanField(default=False)

    objects = BaseModelManager()

    
class ClientDoc(models.Model):
    token =  models.CharField(_("token"), max_length=255)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)
    deleted = models.BooleanField(default=False)

    objects = BaseModelManager()

class ClientDocStatusDesc(models.Model):
    desc = models.CharField(_("desc"), max_length=255)
    created_on = models.DateTimeField(_("created on"), auto_now_add=True)
    updated_on = models.DateTimeField(_("updated on"), auto_now=True)

    def __str__(self):
        return 'Desc: {}'.format(self.desc)

class ClientDocStatus(models.Model): 
    doc_desc = models.ForeignKey(ClientDocStatusDesc,related_name="clientdocstatus_clientdocstatusdesc", verbose_name=_("doc desc"), on_delete=models.CASCADE)
    client_doc = models.ForeignKey(ClientDoc, related_name="clientdoc_status", verbose_name=_("clientdoc"), on_delete=models.CASCADE)
    created_on = models.DateTimeField(_("created on"), auto_now_add=True)
    updated_on = models.DateTimeField(_("updated on"), auto_now=True)

    def __str__(self):
        return 'ClientDoc Status: {} - Status Date: {} - Updated On: {}'.format(self.doc_desc.desc, self.created_on, self.updated_on)

    def next_status(self):
        status_list = list(ClientDocStatusDesc.objects.values_list('desc', flat=True))
        current_status_index = status_list.index(self.doc_desc.desc)
        if current_status_index < len(status_list) - 1:
            next_status_desc = status_list[current_status_index + 1]
            next_status = ClientDocStatusDesc.objects.get(desc=next_status_desc)
            self.doc_desc = next_status
            self.save()

class Consultant(models.Model):
    name = models.CharField(_("name"), max_length=100)
    email = models.EmailField(_("email"), max_length=100, unique=True)
    phone_number = models.CharField(_("phone number"), max_length=16)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ConsultantLead(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, blank=True)
    consultant = models.ForeignKey(Consultant, on_delete=models.CASCADE, blank=True)


