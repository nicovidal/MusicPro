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
import datetime
import json







def homeUsuario(request):
    ventas = Venta.objects.filter(idUser=request.user)
   

    return render(request, 'cliente/home.html', {"ventas": ventas})

def homeVendedor(request):
    ventas=Venta.objects.all()
    api_url = 'http://127.0.0.1:8000/api/productos/'
    response = requests.get(api_url)

    try:
        data = response.json()
        productos = data.get('productos', [])
    
    except JSONDecodeError:
        productos = []
    

    filtro_nombre = request.GET.get('nombreProducto')

    # Aplicar el filtro por nombre si se proporciona    
    if filtro_nombre:
        productos = [producto for producto in productos if filtro_nombre.lower() in producto['nombre'].lower()]
    return render (request,'vendedor/home.html',{'productos':productos ,'ventas':ventas})


def contacto(request):
    comentario = ""
    
    if request.method == 'POST':
        serie_del_producto= request.POST['serie_del_producto']
        mail_cliente = request.POST['mail_cliente']
        marca = request.POST['marca']
        nombre = request.POST['nombre']
        modelo = request.POST['modelo']
        comentario = request.POST['comentario']

        contacto = ContactoVendedor.objects.create(
            serie_del_producto=serie_del_producto,
            mail_cliente=mail_cliente,
            marca=marca,
            nombre=nombre,
            modelo=modelo,
            comentario=comentario
        )

       
    
        return render(request, 'vendedor/contacto.html')
    else:
        return render(request, 'vendedor/contacto.html', {'comentario': comentario})


def actualizar_estado_venta(request, venta_id, estado):

    venta = Venta.objects.get(id=venta_id)
    
    # Actualizar el estado de la venta
    venta.estado = estado
    venta.save()
    

    return redirect('home_vendedor')

def actualizar_estado_pedido(request, venta_id, estado):

    venta = Venta.objects.get(id=venta_id)
    

    venta.estado = estado
    venta.save()
    
  
    return redirect('home_bodeguero')


def actualizar_estado_despachado(request, venta_id, estado):

    venta = Venta.objects.get(id=venta_id)
    
  
    venta.estado = estado
    venta.save()
    

    return redirect('home_bodeguero')

def actualizar_estado_enviado_cliente(request, venta_id, estado):

    venta = Venta.objects.get(id=venta_id)
    
  
    venta.estado = estado
    venta.save()
    
  
    return redirect('home_vendedor')

def actualizar_estado_entregado(request, venta_id, estado):

    venta = Venta.objects.get(id=venta_id)
    

    venta.estado = estado
    venta.save()

    return redirect('home_contador')

def actualizar_estado_transferencia(request, venta_id, estado):

    venta = Venta.objects.get(id=venta_id)
    
   
    venta.estado = estado
    venta.save()
    
    
    return redirect('home_contador')


def homeContador(request):

    ventas = Venta.objects.filter(idUser=request.user)
    transferencias = Venta.objects.filter(transferencia=True)

    return render(request, 'contador/home.html', {"ventas": ventas, 'transferencias': transferencias})

def homeBodeguero(request):
    ventas=Venta.objects.all()
    api_url = 'http://127.0.0.1:8000/api/productos/'
    response = requests.get(api_url)

    try:
        data = response.json()
        productos = data.get('productos', [])
    
    except JSONDecodeError:
        productos = []
    
     # Obtener el valor del filtro del formulario
    filtro_nombre = request.GET.get('nombreProducto')

    # Aplicar el filtro por nombre si se proporciona    
    if filtro_nombre:
        productos = [producto for producto in productos if filtro_nombre.lower() in producto['nombre'].lower()]
    
    return render (request,'bodeguero/home.html', {'productos': productos ,'ventas':ventas})

def homeAdministrador(request):
    return render (request,'administrador/home.html')

def pedidos(request):
    return render(request,'bodeguero/pedidos.html')


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
        
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
   
            username = email 

            user = CustomUser.objects.create_user(username=username, email=email, password=password)  
            user.last_name = last_name
            user.user_type = form.cleaned_data['user_type']  
            user.save()


            return redirect("login")  
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
       
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
          
            username = email  

          
            user = CustomUser.objects.create_user(username=username, email=email, password=password) 
            user.first_name = first_name
            user.last_name = last_name
            user.user_type = 'Cliente'
            user.save()

           
            return redirect("login") 
        else:
            error_message = 'Formulario inválido'
    else:
        form = ClienteCreationForm()
        error_message = None

    return render(request, 'auth/create_cliente.html', {'form': form, 'error_message': error_message})








"""Carrito"""

def carrito(request):
    carrito = Carrito(request)
    productos = carrito.get_productos() 
    total = total_carrito(request)

    return render(request, 'carro/carrito.html', {'productos': productos, 'total_carrito': total['total_carrito'],'descuento': total['descuento']})

def despacho(request):
    carrito = Carrito(request)
    productos = carrito.get_productos() 
    total = total_carrito(request)
 
    return render(request, 'carro/despacho.html', {'productos': productos, 'total_carrito': total['total_carrito']})




def agregar_producto(request, producto_id):
    try:
        response = requests.get(f'http://127.0.0.1:8000/api/productos/{producto_id}/')
        response.raise_for_status() 
        producto_data = response.json()
        
        carrito = Carrito(request)
        carrito.agregar(producto_data)
        
        messages.success(request, 'Producto agregado correctamente')  
        return redirect(reverse('carrito')) 
    except (requests.exceptions.RequestException, ValueError):
        messages.error(request, 'Error al agregar el producto al carrito') 
        return HttpResponseServerError("Error al agregar el producto al carrito")  
    
def agregar_producto_pedido(request, producto_id):
    try:
        response = requests.get(f'http://127.0.0.1:8000/api/productos/{producto_id}/')
        response.raise_for_status()  
        producto_data = response.json()
        
        carrito = Carrito(request)
        carrito.agregar(producto_data)
        
        messages.success(request, 'Producto agregado correctamente')  
        return redirect(reverse('carrito'))  
    except (requests.exceptions.RequestException, ValueError):
        messages.error(request, 'Error al agregar el producto al carrito')  
        return HttpResponseServerError("Error al agregar el producto al carrito") 

def total_carrito(request):
    total = 0
    if "carrito" in request.session.keys():
        for key, value in request.session["carrito"].items():
            total += int(value["acumulado"])

    descuento = 0
    if request.user.is_authenticated and len(request.session["carrito"]) > 4:
        descuento = total * 0.2  
    total_con_descuento = total - descuento

    return {"total_carrito": total_con_descuento, "descuento": descuento}





def pagar(request):
    monto_total = total_carrito(request)["total_carrito"]

    commerce_code = 597055555532
    api_key = "579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C"
    integration_type = "TEST"
    transaction = Transaction()
    transaction.commerce_code = commerce_code
    transaction.api_key = api_key
    transaction.integration_type = integration_type

    buy_order = "orden_de_compra"
    session_id = "identificador_de_sesion"
    return_url = "http://127.0.0.1:8000/orden_despacho/"

    response = transaction.create(buy_order, session_id, monto_total, return_url)

    redirect_url = response["url"]
    token = response["token"]

    # Obtener los productos del carrito
    carrito = request.session.get('carrito', [])

    # Obtener el nombre de los productos y la suma de la cantidad total
    productos = []
    cantidad_total = 0
    for producto_id, detalle_producto in carrito.items():
        cantidad = detalle_producto["cantidad"]
        nombre = detalle_producto["nombre"]
        productos.append(nombre)
        cantidad_total += cantidad

    # Imprimir el contenido del carrito
    print("Productos:", productos)
    print("Cantidad total:", cantidad_total)

    # Verificar si el pago fue rechazado
    if response.get('status') == 'payment_rejected':
        estado = 'Rechazado'
        print(estado)
    else:
        estado = 'Procesando'
        # Actualizar el stock de los productos
        for producto_id, detalle_producto in carrito.items():
            try:
             
                response = requests.get(f'http://127.0.0.1:8000/api/productos/{producto_id}/')
                response.raise_for_status()
                producto_data = response.json()
                print(producto_data)
                
                # Restar la cantidad del stock_tienda
                producto_data['producto']['stock_tienda'] -= detalle_producto["cantidad"]
         
                response = requests.put(f'http://127.0.0.1:8000/api/productos/{producto_id}/', json=producto_data)
                response.raise_for_status()
            except (requests.exceptions.RequestException, ValueError):
             
                messages.error(request, 'Error al obtener o actualizar el producto')
                return HttpResponseServerError("Error al obtener o actualizar el producto")


    numero_orden = random.randint(100000, 999999)
    venta = Venta.objects.create(
        numero_orden=numero_orden,
        total=monto_total,
        fch_compra=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        idUser=request.user if request.user.is_authenticated else None,
        productos=productos,
        cantidad=cantidad_total,
        estado=estado,
        transferencia=False
    )



    context = {
        'redirect_url': redirect_url,
        'token': token,
        'monto_total': monto_total,
        'numero_orden': numero_orden,
        'productos': productos,
        'cantidad_total': cantidad_total,
    }

    return render(request, 'carro/resumen_pago.html', context)


    

def transferencia_page(request):

    monto_total = total_carrito(request)["total_carrito"]
    

    return render (request,'carro/transferencia.html',{'monto_total':monto_total})


def transferencia(request):
    monto_total = total_carrito(request)["total_carrito"]
    carrito = request.session.get('carrito', [])


    productos = []
    cantidad_total = 0
    for producto_id, detalle_producto in carrito.items():
        cantidad = detalle_producto["cantidad"]
        nombre = detalle_producto["nombre"]
        productos.append(nombre)
        cantidad_total += cantidad


    print("Productos:", productos)
    print("Cantidad total:", cantidad_total)

 
    numero_orden = random.randint(100000, 999999)
    estado = 'Por Confirmar Tranferencia'
    venta = Venta.objects.create(
        numero_orden=numero_orden,
        total=monto_total,
        fch_compra=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        idUser=request.user if request.user.is_authenticated else None,
        productos=productos,
        cantidad=cantidad_total,
        estado=estado,
        transferencia=True
    )

    carrito = Carrito(request)
    carrito.limpiar()


    return redirect('orden_despacho')

def payment_rejected_logic(token_ws):

    if "rejected" in token_ws:
        return True
    else:
        return False

def orden_despacho(request):
    if request.method == 'POST':

        token_ws = request.POST.get('token_ws')

        if payment_rejected_logic(token_ws):
            return redirect('orden_rechazada')
  
        return render(request, 'carro/orden_despacho.html', {"token": token_ws})

    elif request.method == 'GET':
        token_ws = request.GET.get('token_ws')
        carrito = Carrito(request)
        carrito.limpiar()

        return render(request, 'carro/orden_despacho.html', {"token": token_ws})


    return HttpResponse("Método de solicitud no válido.")



def btn_agregar_producto(request, id):

    if id is not None:
        api_url = f"http://127.0.0.1:8000/api/productos/{id}/"
        response = requests.get(api_url)

        if response.status_code == 200:
            producto = response.json()

            if 'carrito' not in request.session:
                request.session['carrito'] = {}

          
            if str(id) in request.session['carrito']:
       
                request.session['carrito'][str(id)]['cantidad'] += 1
                request.session['carrito'][str(id)]['acumulado'] += producto['producto']['precio']
                print(request.session['carrito'])
            else:
       
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

            request.session.modified = True


            return redirect('carrito') 
        else:
         
            return redirect('error')  
        
def btn_quitar_producto(request, id):

    if 'carrito' in request.session and str(id) in request.session['carrito']:
  
        producto = request.session['carrito'][str(id)]

        if producto['cantidad'] > 0:
            producto['cantidad'] -= 1
            producto['acumulado'] -= producto['precio']
            print(request.session['carrito'])

     
            if producto['cantidad'] == 0:
                del request.session['carrito'][str(id)]

         
            request.session.modified = True


    return redirect('carrito')  
