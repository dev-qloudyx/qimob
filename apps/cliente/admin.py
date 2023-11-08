from django.contrib import admin

from apps.cliente.models import Client, ClientDoc

# Register your models here.

admin.site.register(Client)
admin.site.register(ClientDoc)

