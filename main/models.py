from django.db import models

# Create your models here.

class Contacto(models.Model):
    nombre = models.CharField(max_length=55)
    email = models.CharField(max_length=50)
    mensaje = models.CharField(max_length=64)
    

