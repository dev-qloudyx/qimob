import os
from django.db import models
from apps.users.models import User

class BaseModel(models.Model):
    deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def delete(self):
        for rel in self._meta.get_fields():
            try:
                if rel.one_to_many or rel.one_to_one:
                    related = getattr(self, rel.get_accessor_name())
                    if rel.one_to_many:
                        related.update(deleted=True)
                    else:
                        related.deleted = True
                        related.save()
            except Exception as e:
                continue

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
    
class Folder(BaseModel):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    objects = BaseModelManager()

    def __str__(self):
        return self.name

def user_directory_path(instance, filename):
    return 'uploads/{0}/{1}'.format(instance.folder.name, filename)

class File(BaseModel):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    upload = models.FileField(upload_to=user_directory_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = BaseModelManager()

    def __str__(self):
        full_path = self.upload.name
        filename = os.path.basename(full_path)
        return filename

