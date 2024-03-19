from django.contrib import admin

from apps.crm.models import (ClientDocStatus, ClientDocStatusDesc, Lead, LeadStatus,
LeadDoc, Contact, Client, ClientDoc, ClientAddress, ClientMessage, LeadType, LeadComment)
# Register your models here.


class LeadsAdmin(admin.ModelAdmin):        
    list_display = ('id','short_name','is_active')


admin.site.register(Lead, LeadsAdmin)
admin.site.register(LeadType)
admin.site.register(LeadStatus)
admin.site.register(LeadDoc)
admin.site.register(LeadComment)
admin.site.register(Contact)
admin.site.register(Client)
admin.site.register(ClientDoc)
admin.site.register(ClientDocStatusDesc)
admin.site.register(ClientDocStatus)
admin.site.register(ClientAddress)
admin.site.register(ClientMessage)
