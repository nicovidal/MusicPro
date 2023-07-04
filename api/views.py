from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from .models import Producto


class ProductoView(View):
    def get(self, request, pk=None):
        if pk is not None:
            producto = get_object_or_404(Producto, pk=pk)
            datos = {'message': 'Success', 'producto': {
                'id': producto.pk,
                'serie_del_producto': producto.serie_del_producto,
                'nombre':producto.nombre,
                'marca': producto.marca,
                'stock':producto.stock,
                'precio':producto.precio,
                'imagen': producto.imagen.url if producto.imagen else None,
                # Agrega los demás campos del producto que deseas mostrar
            }}
        else:
            productos = list(Producto.objects.values())
            if len(productos) > 0:
                datos = {'message': 'Success', 'productos': productos}
            else:
                datos = {'message': 'Productos no encontrados'}
        return JsonResponse(datos)

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass