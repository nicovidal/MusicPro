from django.urls import path
from .views import *

urlpatterns = [
    path('create_user/', create_user, name="create_user"),
    path('cliente/', homeUsuario, name="home_cliente"),
    path('bodeguero/', homeBodeguero, name="home_bodeguero"),
    path('vendedor/', homeVendedor, name="home_vendedor"),
    path('contador/', homeContador, name="home_contador"),
    path('login/', login_view, name="login"),
    path('', home, name="home"),
]
