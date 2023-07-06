from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from .productos import *


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
    path('acusticas', obtener_guitarras_acusticas, name="home_acusticas"),
    path('electricas', obtener_guitarras_electricas, name="home_electricas"),
    path('solido',obtener_guitarras_solido,name="home_solido"),
    path('guitarras',obtener_guitarras,name="home_guitarras"),
    path('bajos',obtener_bajos,name="home_bajos"),
    path('bajoCuatro',obtener_bajos_cuatro,name="bajosCuatro"),
    path('accesoriosGeneral',obtener_accesorios,name="accesorios_general"),
    path('audifonos',obtener_audifonos,name="audifonos"),
    path('cables',obtener_cables,name="cables"),
    path('interfaces',obtener_interfaces,name="interfaces"),
    path('microfonos',obtener_microfonos,name="microfonos"),
    path('mixers',obtener_mixers,name="mixers"),
    path('monitores',obtener_monitores,name="monitores"),
    path('parlantes',obtener_parlantes,name="parlantes"),
    path('cabezales',obtener_cabezales,name="cabezales_general"),
    path('cabezalEngl',obtener_cabezales_engl,name="cabezalEngl"),
    path('cabezalEvh',obtener_cabezales_evh,name="cabezalEvh"),
    path('cabezalMarshall',obtener_cabezales_marshall,name="cabezalMarshall"),
    path('cabezalPavey',obtener_cabezales_pavey,name="cabezalesPavey"),
    path('cajas',obtener_cajas,name="cajas_general"),
    path('cajaEngl',obtener_cajas_engl,name="cajaEngl"),
    path('cajaEvh',obtener_cajas_evh,name="cajaEvh"),
    path('cajaMarshall',obtener_cajas_marshall,name="cajaMarshall"),
    path('cajaPavey',obtener_cajas_pavey,name="cajaPavey"),
    path('carrito/',carrito,name="carrito"),
    path('agregar_producto/<int:producto_id>/', agregar_producto, name='agregar_producto'),
    path('pagar/', pagar, name='pagar'),
    path('agregar_btn/<int:id>/', btn_agregar_producto, name="Adds"),
    path('restar/<int:id>/', btn_quitar_producto, name="Sub"),
    path('despacho/',despacho,name="despacho")


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
