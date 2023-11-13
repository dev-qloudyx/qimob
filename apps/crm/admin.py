from django.contrib import admin

from apps.crm.models import Lead, LeadStatusDesc, LeadStatus, LeadDoc, Message, Contact, Client, ClientDoc

# Register your models here.

admin.site.register(Lead)
admin.site.register(LeadStatusDesc)
admin.site.register(LeadStatus)
admin.site.register(LeadDoc)
admin.site.register(Message)
admin.site.register(Contact)
admin.site.register(Client)
admin.site.register(ClientDoc)