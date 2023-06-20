from django.urls import path
from .views import *

urlpatterns = [
    path('create_user/', create_user, name="create_user"),
    path('create_cliente/', create_cliente, name="create_cliente"),
    path('cliente/', homeUsuario, name="home_cliente"),
    path('bodeguero/', homeBodeguero, name="home_bodeguero"),
    path('vendedor/', homeVendedor, name="home_vendedor"),
    path('contador/', homeContador, name="home_contador"),
    path('administrador/', homeAdministrador, name="home_administrador"),
    path('login/', login_view, name="login"),
    path('', obtener_productos, name="home"),

]
