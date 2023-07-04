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