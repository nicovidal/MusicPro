from django.shortcuts import render

# Create your views here.
def homeUsuario(request):

    return render(request,'MusicProWeb/usuario/home.html')

def homeVendedor(request):
    return render (request,'MusicProWeb/vendedor/home.html')

def homeContador(request):
    return render (request,'MusicProWeb/contador/home.html')

def homeBodeguero(request):
    return render (request,'MusicProWeb/bodeguero/home.html')
