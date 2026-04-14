from django.db import models

class Pizza(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
