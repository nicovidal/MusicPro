from django.db import models

# Create your models here.

class Producto(models.Model):
    serie_del_producto=models.CharField(max_length=50)
    marca=models.CharField(max_length=50)
    codigo=models.CharField(max_length=50)
    nombre=models.CharField(max_length=50)
    precio=models.CharField(max_length=50)
    modelo=models.CharField(max_length=50)


