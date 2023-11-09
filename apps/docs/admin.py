
from django.contrib import admin

from apps.docs.models import File, Folder

# Register your models here.

admin.site.register(File)
admin.site.register(Folder)

