from django.urls import path
from .views import homeUsuario,homeBodeguero,homeContador,homeVendedor

urlpatterns = [
    path('',homeUsuario,name="homeUser"),
    path('bodeguero',homeBodeguero,name="homeBodeguero"),
    path('vendedor',homeVendedor,name="homeVendedor"),
    path('contador',homeContador,name="homeContador")
]
