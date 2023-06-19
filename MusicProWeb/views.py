from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

def homeUsuario(request):
    return render(request,'usuario/home.html')

def homeVendedor(request):
    return render (request,'vendedor/home.html')

def homeContador(request):
    return render (request,'contador/home.html')

def homeBodeguero(request):
    return render (request,'bodeguero/home.html')


class EmailAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Correo Electronico'

def login_view(request):
    if request.method == 'POST':
        form = EmailAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")  # Obtén el correo electrónico ingresado
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home_bodeguero")  # Redirige a la página de inicio
            print('fui pal usuario')
            
        # Si la autenticación falla o los datos son inválidos, muestra el formulario con un mensaje de error
        error_message = 'Credenciales inválidas. Inténtalo nuevamente.'
        print(error_message)
    else:
        form = EmailAuthenticationForm(request)
        error_message = None

    return render(request, 'auth/login.html', {'form': form, 'error_message': error_message})


def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Obtén los datos del formulario
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            # Genera un nombre de usuario único basado en el correo electrónico
            username = email  # Utiliza la parte antes del '@' como nombre de usuario

            # Crea el usuario en Django
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            # Redirige a la página de inicio de sesión
            return redirect("login")  # Redirige a una página de éxito
        else:
            error_message = 'Formulario inválido'
    else:
        form = UserCreationForm()
        error_message = None

    return render(request, 'auth/create_user.html', {'form': form, 'error_message': error_message})
