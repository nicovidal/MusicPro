from django.db import models

# Create your models here.

class Producto(models.Model):
    serie_del_producto=models.CharField(max_length=50,null=True)
    marca=models.CharField(max_length=50,null=True)
    codigo=models.CharField(max_length=50,null=True)
    nombre=models.CharField(max_length=50,null=True)
    precio=models.CharField(max_length=50,null=True)
    modelo=models.CharField(max_length=50,null=True)
    oferta=models.BooleanField(null=True)
    nuevo=models.BooleanField(null=True)
    stock=models.IntegerField(null=True)
    imagen=models.ImageField(upload_to='imagenProductos',null=True,blank=True)

    
     
    def __str__(self):
        return str(self.serie_del_producto)

