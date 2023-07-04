from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import CustomUser 
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
import requests
from django.contrib import messages
from django.http import HttpResponseServerError
from MusicProWeb.carrito import Carrito
from requests.exceptions import JSONDecodeError
from django.http import HttpResponse

# Create your views here.

def homeUsuario(request):
    return render(request,'cliente/home.html')

def homeVendedor(request):
    return render (request,'vendedor/home.html')

def homeContador(request):
    return render (request,'contador/home.html')

def homeBodeguero(request):
    return render (request,'bodeguero/home.html')

def homeAdministrador(request):
    return render (request,'administrador/home.html')



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
                
                # Redirige a diferentes páginas según el tipo de usuario
                if user.user_type == 'bodeguero':
                    return redirect("home_bodeguero")
                elif user.user_type == 'vendedor':
                    return redirect("home_vendedor")
                elif user.user_type == 'contador':
                    return redirect("home_contador")
                elif user.user_type == 'administrador':
                    return redirect("home_administrador")
                elif user.user_type == 'Cliente':
                    return redirect("home_cliente")
                else:
                    return redirect("login")
            
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
            username = email  # Utiliza el correo electrónico como nombre de usuario

            # Crea el usuario en Django
            user = CustomUser.objects.create_user(username=username, email=email, password=password)  # Utiliza CustomUser en lugar de User
            user.first_name = first_name
            user.last_name = last_name
            user.user_type = form.cleaned_data['user_type']  # Guarda el tipo de usuario
            user.save()

            # Redirige a la página de inicio de sesión
            return redirect("login")  # Redirige a una página de éxito
        else:
            error_message = 'Formulario inválido'
    else:
        form = UserCreationForm()
        error_message = None

    return render(request, 'auth/create_user.html', {'form': form, 'error_message': error_message})


def create_cliente(request):
    if request.method == 'POST':
        form = ClienteCreationForm(request.POST)
        if form.is_valid():
            # Obtén los datos del formulario
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            # Genera un nombre de usuario único basado en el correo electrónico
            username = email  # Utiliza el correo electrónico como nombre de usuario

            # Crea el usuario en Django
            user = CustomUser.objects.create_user(username=username, email=email, password=password)  # Utiliza CustomUser en lugar de User
            user.first_name = first_name
            user.last_name = last_name
            user.user_type = 'Cliente'# Guarda el tipo de usuario
            user.save()

            # Redirige a la página de inicio de sesión
            return redirect("login")  # Redirige a una página de éxito
        else:
            error_message = 'Formulario inválido'
    else:
        form = ClienteCreationForm()
        error_message = None

    return render(request, 'auth/create_cliente.html', {'form': form, 'error_message': error_message})

""" !-consumo de api """

def obtener_productos(request):
    api_url = 'http://127.0.0.1:8000/api/productos/' 
    response = requests.get(api_url) 
    data = response.json()  
    productos = data['productos'] 
    return render(request, 'index.html', {'productos': productos})


def obtener_guitarras_acusticas(request):
    api_url = 'http://127.0.0.1:8000/api/productos/' 
    
    response = requests.get(api_url) 
    data = response.json()  
    productos = data['productos']  
    return render(request, 'productos/instrumentosDeCuerdas/guitarras/guitarrasAcusticas.html', {'productos': productos})

def obtener_guitarras_electricas(request):
    api_url = 'http://127.0.0.1:8000/api/productos/'  
    
    response = requests.get(api_url) 
    data = response.json()  
    productos = data['productos']  
    return render(request, 'productos/instrumentosDeCuerdas/guitarras/guitarrasElectricas.html', {'productos': productos})

def obtener_guitarras_solido(request):
    api_url = 'http://127.0.0.1:8000/api/productos/'  
    response = requests.get(api_url)  
    data = response.json() 
    productos = data['productos']
    return render(request, 'productos/instrumentosDeCuerdas/guitarras/guitarrasCuerpoSolido.html', {'productos': productos})

def obtener_guitarras(request):
    api_url = 'http://127.0.0.1:8000/api/productos/'
    response = requests.get(api_url)
    print(response)
    try:
        data = response.json()
        productos = data.get('productos', [])
        print(data)
    except JSONDecodeError:
        productos = []
    
    return render(request, 'productos/instrumentosDeCuerdas/guitarras/guitarras.html', {'productos': productos})


"""Carrito"""
def carrito(request):
    carrito = Carrito(request)
    productos = carrito.get_productos()  # Obtener los productos del carrito
    print(productos)
    return render(request, 'carro/carrito.html', {'productos': productos})




def agregar_producto(request, producto_id):
 
    try:
        response = requests.get(f'http://127.0.0.1:8000/api/productos/{producto_id}/')
        response.raise_for_status()  # Verificar si la solicitud fue exitosa
        producto_data = response.json()
        
        carrito = Carrito(request)
        carrito.agregar(producto_data)
        messages.success(request, 'Agregado al Carrito')
        
        return HttpResponse("Producto agregado al carrito")  # Devolver una respuesta exitosa
    except (requests.exceptions.RequestException, ValueError):
        return HttpResponseServerError("Error al agregar el producto al carrito")

