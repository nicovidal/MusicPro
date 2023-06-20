from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('admin', 'Administrador'),
        ('employee', 'Empleado'),
        ('customer', 'Cliente'),
        ('guest', 'Invitado'),
    )
    
    user_type = models.CharField(max_length=20, choices=USER_TYPES)