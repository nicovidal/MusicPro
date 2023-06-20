from django import forms
from django.contrib.auth.forms import AuthenticationForm


class UserCreationForm(forms.Form):
    first_name = forms.CharField(max_length=50, label='Nombre')
    last_name = forms.CharField(max_length=50, label='Apellido')
    email = forms.EmailField(label='Correo electrónico')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    user_type = forms.ChoiceField(choices=(
        ('bodeguero', 'Bodeguero'),
        ('vendedor', 'Vendedor'),
        ('contador', 'Contador')
    ), label='Tipo de usuario')


class ClienteCreationForm(forms.Form):
    first_name = forms.CharField(max_length=50, label='Nombre')
    last_name = forms.CharField(max_length=50, label='Apellido')
    email = forms.EmailField(label='Correo electrónico')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
