from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
import requests
from django.contrib import messages
from django.http import HttpResponseServerError
from MusicProWeb.carrito import Carrito
from requests.exceptions import JSONDecodeError
from django.http import HttpResponse
import datetime
import random
from django.contrib.auth.models import AbstractUser
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import redirect
from transbank.webpay.webpay_plus.transaction import Transaction






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

    try:
        data = response.json()
        productos = data.get('productos', [])
    
    except JSONDecodeError:
        productos = []
    
    return render(request, 'productos/instrumentosDeCuerdas/guitarras/guitarras.html', {'productos': productos})


"""Carrito"""
def carrito(request):
    carrito = Carrito(request)
    productos = carrito.get_productos()  # Obtener los productos del carrito
    total = total_carrito(request)
 
    return render(request, 'carro/carrito.html', {'productos': productos, 'total_carrito': total['total_carrito']})





def agregar_producto(request, producto_id):
    try:
        response = requests.get(f'http://127.0.0.1:8000/api/productos/{producto_id}/')
        response.raise_for_status()  # Verificar si la solicitud fue exitosa
        producto_data = response.json()
        
        carrito = Carrito(request)
        carrito.agregar(producto_data)
        
        messages.success(request, 'Producto agregado correctamente')  # Agregar el mensaje de éxito
        return redirect(reverse('carrito'))  # Redirigir al carrito de compras
    except (requests.exceptions.RequestException, ValueError):
        messages.error(request, 'Error al agregar el producto al carrito')  # Agregar el mensaje de error
        return HttpResponseServerError("Error al agregar el producto al carrito")  # Redirigir a una página de error

def total_carrito(request):
    total = 0
    if "carrito" in request.session.keys():
        for key, value in request.session["carrito"].items():
            total += int(value["acumulado"])
    return {"total_carrito": total}




def pagar(request):
    # Obtén los datos necesarios para crear la transacción
    # Puedes obtenerlos de tu modelo de carrito de compras o de cualquier otra fuente de datos

    # Obtén el monto total del carrito de compras
    monto_total = total_carrito(request)["total_carrito"]

    # Configuración de las credenciales de Webpay
    commerce_code = 597055555532
    api_key = "579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C"
    integration_type = "TEST"  # Puedes utilizar "LIVE" para producción

    # Crear una nueva instancia de la transacción
    transaction = Transaction()
    transaction.commerce_code = commerce_code
    transaction.api_key = api_key
    transaction.integration_type = integration_type

    # Establecer los datos de la transacción
    transaction.buy_order = "orden_de_compra"
    transaction.session_id = "identificador_de_sesion"
    transaction.amount = monto_total 
    transaction.return_url = " https://webpay3gint.transbank.cl"

    # Crear la transacción
    response = transaction.create(
        transaction.buy_order,
        transaction.session_id,
        transaction.amount,
        transaction.return_url
    )

    redirect_url = response["url"]

    # Redirigir al cliente a la URL de redirección de Transbank
    return redirect(redirect_url)

def btn_agregar_producto(request, id):
    # Hacer una solicitud a la API para obtener los detalles del producto
    if id is not None:
        api_url = f"http://127.0.0.1:8000/api/productos/{id}/"
        response = requests.get(api_url)

        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            producto = response.json()

            # Inicializar el diccionario 'carrito' si no existe
            if 'carrito' not in request.session:
                request.session['carrito'] = {}

            # Verificar si el producto ya está en el carrito
            if str(id) in request.session['carrito']:
                # Si el producto ya está en el carrito, incrementa la cantidad
                request.session['carrito'][str(id)]['cantidad'] += 1
                request.session['carrito'][str(id)]['acumulado'] += producto['producto']['precio']
                print(request.session['carrito'])
            else:
                # Si el producto no está en el carrito, agrégalo con una cantidad de 1
                nombre = producto['nombre']
                precio = producto['precio']
                imagen = producto['imagen']

                request.session['carrito'][str(id)] = {
                    'id': id,
                    'nombre': nombre,
                    'cantidad': 1,
                    'acumulado': precio,
                    'imagen': imagen,
                }

            # Guarda los cambios en el carrito
            request.session.modified = True

            # Redirige al usuario a la página del carrito o a donde desees
            return redirect('carrito')  # Reemplaza 'carrito' con la URL correcta
        else:
            # Si la solicitud a la API falla, muestra un mensaje de error o redirige a una página de error
            return redirect('error')  # Reemplaza 'error' con la URL correcta para la página de error
        
def btn_quitar_producto(request, id):
    # Verificar si el producto ya está en el carrito
    if 'carrito' in request.session and str(id) in request.session['carrito']:
        # Obtener los detalles del producto desde el carrito
        producto = request.session['carrito'][str(id)]

        # Decrementar la cantidad solo si es mayor que 0
        if producto['cantidad'] > 0:
            producto['cantidad'] -= 1
            producto['acumulado'] -= producto['precio']
            print(request.session['carrito'])

            # Eliminar el producto del carrito si la cantidad llega a 0
            if producto['cantidad'] == 0:
                del request.session['carrito'][str(id)]

            # Guardar los cambios en el carrito
            request.session.modified = True

    # Redirigir al usuario a la página del carrito o a donde desees
    return redirect('carrito')  # Reemplaza 'carrito' con la URL correcta