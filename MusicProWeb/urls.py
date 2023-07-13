from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from .productos import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('create_user/', create_user, name="create_user"),
    path('create_cliente/', create_cliente, name="create_cliente"),
    path('cliente/', homeUsuario, name="home_cliente"),
    path('bodeguero', homeBodeguero, name="home_bodeguero"),
    path('vendedor', homeVendedor, name="home_vendedor"),
    path('contador/', homeContador, name="home_contador"),
    path('administrador/', homeAdministrador, name="home_administrador"),
    path('pedidosBodega', pedidos, name="pedidos_bodega"),
    path('login/', login_view, name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('contacto/', contacto, name='contacto'),

    path('carrito/',carrito,name="carrito"),
    path('agregar_producto/<int:producto_id>/', agregar_producto, name='agregar_producto'),
    path('agregar_producto_pedido/<int:producto_id>/', agregar_producto_pedido, name='agregar_producto_pedido'),
    path('pagar/', pagar, name='pagar'),
    path('transferencia_page/', transferencia_page, name='transferencia_page'),
    path('transferencia/', transferencia, name='transferencia'),
    path('agregar_btn/<int:id>/', btn_agregar_producto, name="Adds"),
    path('restar/<int:id>/', btn_quitar_producto, name="Sub"),
    path('despacho/',despacho,name="despacho"),
    path('orden_despacho/',orden_despacho,name="orden_despacho"),
    path('orden_rechazada/',orden_despacho,name="orden_rechazada"),
    path('actualizar_estado_venta/<int:venta_id>/<str:estado>/', actualizar_estado_venta, name='actualizar_estado_venta'),
    path('actualizar_estado_pedido/<int:venta_id>/<str:estado>/', actualizar_estado_pedido, name='actualizar_estado_pedido'),
    path('actualizar_estado_despachado/<int:venta_id>/<str:estado>/', actualizar_estado_despachado, name='actualizar_estado_despachado'),
    path('actualizar_estado_cliente/<int:venta_id>/<str:estado>/', actualizar_estado_enviado_cliente, name='actualizar_estado_enviado_cliente'),
    path('actualizar_estado_entregado/<int:venta_id>/<str:estado>/', actualizar_estado_entregado, name='actualizar_estado_entregado'),
    path('actualizar_estado_transferencia/<int:venta_id>/<str:estado>/', actualizar_estado_transferencia, name='actualizar_estado_transferencia'),

    #productos rutas
    path('', obtener_productos, name="home"),
    path('acusticas', obtener_guitarras_acusticas, name="home_acusticas"),
    path('electricas', obtener_guitarras_electricas, name="home_electricas"),
    path('solido',obtener_guitarras_solido,name="home_solido"),
    path('guitarras',obtener_guitarras,name="home_guitarras"),
    path('bajos',obtener_bajos,name="home_bajos"),
    path('bajoCuatro',obtener_bajos_cuatro,name="bajosCuatro"),
    path('bajoCinco',obtener_bajos_cinco,name="bajosCinco"),
    path('bajoPasivo',obtener_bajos_pasivos,name="bajosPasivo"),
    path('bajoActivo',obtener_bajos_activos,name="bajosActivo"),
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
    path('cajaPavey',obtener_cajas_pavey,name="cajaPavey"),
    path('cajaMarshall',obtener_cajas_marshall,name="cajaMarshall"),
    path('pianos',obtener_pianos,name="home_pianos"),
    path('pianoEntera',obtener_pianos_entera,name="piano_entera"),
    path('pianoMedia',obtener_pianos_media,name="piano_media"),
    path('pianolas',obtener_pianolas,name="pianolas"),
    path('bateriaA',obtener_baterias_acusticas,name="baterias_acusticas"),
    path('mapexA',obtener_baterias_acusticas_mapex,name="baterias_acusticas_mapex"),
    path('pearlA',obtener_baterias_acusticas_pearl,name="baterias_acusticas_pearl"),
    path('sonorA',obtener_baterias_acusticas_sonor,name="baterias_acusticas_sonor"),
    path('tamaA',obtener_baterias_acusticas_tama,name="baterias_acusticas_tama"),
    path('bateriaE',obtener_baterias_electricas,name="baterias_electricas"),
    path('alesisE',obtener_baterias_electrica_alesis,name="baterias_electricas_alesis"),
    path('rolandE',obtener_baterias_electrica_roland,name="baterias_electricas_roland"),
    path('cajaPavey',obtener_cajas_pavey,name="cajaPavey"),

    #productos fin


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
