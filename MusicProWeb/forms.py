from django import forms
from django.contrib.auth.forms import AuthenticationForm

class UserCreationForm(forms.Form):
    first_name=forms.CharField(max_length=50,label='Nombre')
    last_name=forms.CharField(max_length=50,label='Apellido')
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

