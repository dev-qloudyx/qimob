from django.db import models
from apps.users.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _


class BaseModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)
    
class Lead(models.Model):
    name = models.CharField(_("name"), max_length=100)
    email = models.EmailField(_("email"), max_length=100, unique=True)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)

    def __str__(self):
        return self.name

class LeadScore(models.Model):
    lead = models.ForeignKey(Lead, verbose_name=_("lead"), on_delete=models.CASCADE)
    score = models.PositiveIntegerField(_("score"), validators=[MinValueValidator(0), MaxValueValidator(100)])
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)

    def __str__(self):
        return f'{self.lead.name} - {self.score}%'

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
        return 'Lead Status: {} - Status Date: {} - Updated On: {}'.format(self.lead_desc.desc, self.status_date, self.updated_on)

class LeadDoc(models.Model):
    token =  models.CharField(_("token"), max_length=255)
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, blank=True)

class Contact(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name='contact')
    name = models.CharField(_("name"), max_length=100)
    email = models.EmailField(_("email"), max_length=100, unique=True)
    phone = models.CharField(_("phone"), max_length=15, blank=True)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_on = models.DateTimeField(_("updated on"), auto_now=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    message = models.CharField(_("message"), max_length=500, blank=True)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_on = models.DateTimeField(_("updated on"), auto_now=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return self.message


class Client(models.Model):
    name = models.CharField(_("name"), max_length=255)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    def __str__(self):
        return self.name

class ClientDoc(models.Model):
    token =  models.CharField(_("token"), max_length=255)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)
    deleted = models.BooleanField(default=False)

    objects = BaseModelManager()


class Consultant(models.Model):
    name = models.CharField(_("name"), max_length=100)
    email = models.EmailField(_("email"), max_length=100, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ConsultantLead(models.Model):
    leads = models.ForeignKey(Lead, on_delete=models.CASCADE, blank=True)
    consultant = models.ForeignKey(Consultant, on_delete=models.CASCADE, blank=True)


