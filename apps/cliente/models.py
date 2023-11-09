from django.db import models

from apps.docs.models import File

# Create your models here.

class Cliente(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class ClienteDoc(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    client = models.ForeignKey(Cliente, on_delete=models.CASCADE)