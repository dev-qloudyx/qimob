from django.contrib import admin

from apps.address.models import Address, CPData, CountyData, DistrictData

# Register your models here.

admin.site.register(Address)
admin.site.register(DistrictData)
admin.site.register(CountyData)
admin.site.register(CPData)
