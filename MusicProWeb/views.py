import requests
from django.shortcuts import render, redirect
from .forms import UserCreationForm

# Create your views here.

def homeUsuario(request):
    return render(request,'usuario/home.html')

def homeVendedor(request):
    return render (request,'vendedor/home.html')

def homeContador(request):
    return render (request,'contador/home.html')

def homeBodeguero(request):
    return render (request,'bodeguero/home.html')




def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Obtén los datos del formulario
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
     

            # Envía los datos a la API para crear el usuario
            url = 'http://127.0.0.1:8000/api/new/create_user'
            data = {
                'first_name':first_name,
                'last_name':last_name,
                'email': email,
                'password': password,
                
            }
            response = requests.post(url, data=data)

            if response.status_code == 201:  # Usuario creado exitosamente
                return redirect('usuario')  # Redirige a una página de éxito
            else:
                error_message = 'Error al crear el usuario'
        else:
            error_message = 'Formulario inválido'
    else:
        form = UserCreationForm()
        error_message = None

    return render(request, 'auth/create_user.html', {'form': form, 'error_message': error_message})
