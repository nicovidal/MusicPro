from django.contrib.auth.models import AbstractUser,User
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('administrador', 'Administrador'),
        ('vendedor', 'Vendedor'),
        ('cliente', 'Cliente'),
        ('guest', 'Invitado'),
        ('bodeguero', 'Bodeguero'),
    )
    
    user_type = models.CharField(max_length=20, choices=USER_TYPES)

class Venta(models.Model):
    numero_orden=models.BigIntegerField()
    total=models.IntegerField()
    fch_compra=models.CharField(max_length=40)
    idUser=models.ForeignKey(CustomUser,on_delete=models.SET_NULL,null=True)
    productos = models.TextField()
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        return str(self.numero_orden)
    
