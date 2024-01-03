from django.contrib import admin

from apps.crm.models import ClientDocStatus, ClientDocStatusDesc, Lead, LeadStatusDesc, LeadStatus, LeadDoc, Contact, Client, ClientDoc, ClientAddress, ClientMessage
# Register your models here.

admin.site.register(Lead)
admin.site.register(LeadStatusDesc)
admin.site.register(LeadStatus)
admin.site.register(LeadDoc)
admin.site.register(Contact)
admin.site.register(Client)
admin.site.register(ClientDoc)
admin.site.register(ClientDocStatusDesc)
admin.site.register(ClientDocStatus)
admin.site.register(ClientAddress)
admin.site.register(ClientMessage)
