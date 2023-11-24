import os
import uuid
from django.db import models
from apps.users.models import User
from django.utils.translation import gettext_lazy as _

class BaseModel(models.Model):
    deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def delete(self):
        self.deleted = True
        self.save()
    
    def hard_delete(self):
       
        if self.upload:
            try:
                if os.path.isfile(self.upload.path):
                    os.remove(self.upload.path)
            except Exception as e:
                print(f"Error deleting file: {e}")

        super().delete()

class BaseModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)
    
def user_directory_path(instance, filename):
    return f'uploads/{filename}'

class File(BaseModel):
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    project = models.CharField(max_length=255, null=True)
    app = models.CharField(max_length=255, null=True)
    model = models.CharField(max_length=255, null=True)
    upload = models.FileField(upload_to=user_directory_path)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)
    
    objects = BaseModelManager()

    def __str__(self):
        full_path = self.upload.name
        filename = os.path.basename(full_path)
        return filename

