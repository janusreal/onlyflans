from django.db import models
import uuid

# Create your models here.

class Contacto(models.Model):
    nombre = models.CharField(max_length=55)
    email = models.CharField(max_length=50)
    mensaje = models.CharField(max_length=64)

class Flan(models.Model):
    flan_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=400, default="")  # Añadir un valor predeterminado
    image_url = models.URLField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)
    is_private = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

