import os
from django.db import models
from apps.users.models import User

class Folder(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

def user_directory_path(instance, filename):
    return 'uploads/{0}/{1}'.format(instance.folder.name, filename)

class File(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    upload = models.FileField(upload_to=user_directory_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        full_path = self.upload.name
        filename = os.path.basename(full_path)
        return filename

class FolderActivity(models.Model):
    ACTION_CHOICES = [
        ('C', 'Create'),
        ('U', 'Update')
    ]

    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=1, choices=ACTION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} {self.get_action_display()} folder {self.folder} at {self.timestamp}'

class FileActivity(models.Model):
    ACTION_CHOICES = [
        ('C', 'Create'),
        ('U', 'Update')
    ]

    file = models.ForeignKey(File, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=1, choices=ACTION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} {self.get_action_display()} file {self.file} at {self.timestamp}'