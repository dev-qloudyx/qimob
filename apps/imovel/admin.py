from django.contrib import admin

from apps.imovel.models import Imovel, ImovelType, ImovelLead, ImovelDoc, ImovelDocStatusDesc, ImovelDocStatus

# Register your models here.
admin.site.register(ImovelType)
admin.site.register(Imovel)
admin.site.register(ImovelLead)
admin.site.register(ImovelDoc)
admin.site.register(ImovelDocStatusDesc)
admin.site.register(ImovelDocStatus)