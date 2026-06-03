from django.db import models
from django.conf import settings


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Pizza(models.Model):
    settings.AUTH_USER_MODEL
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
      
    def __str__(self):
        return self.nombre

