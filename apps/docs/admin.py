
from django.contrib import admin

from apps.docs.models import File, FileActivity, Folder, FolderActivity

# Register your models here.

admin.site.register(File)
admin.site.register(FileActivity)
admin.site.register(Folder)
admin.site.register(FolderActivity)

