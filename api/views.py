from typing import Any
from django import http
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from .models import Producto
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

import json



class ProductoView(View):
    #saltar metodo seguridad
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    #obtener productos
    def get(self, request, pk=None):
        if pk is not None:
            producto = get_object_or_404(Producto, pk=pk)
            datos = {'message': 'Success', 'producto': {
                'id': producto.pk,
                'serie_del_producto': producto.serie_del_producto,
                'nombre':producto.nombre,
                'marca': producto.marca,
                'stock_tienda':producto.stock_tienda,
                'stock_bodega':producto.stock_bodega,
                'precio':producto.precio,
                'imagen': producto.imagen.url if producto.imagen else None,
               
            }}
        else:
            productos = list(Producto.objects.values())
            if len(productos) > 0:
                datos = {'message': 'Success', 'productos': productos}
            else:
                datos = {'message': 'Productos no encontrados'}
        return JsonResponse(datos)

    #agregar poducto
    def post(self, request):
  
        data = json.loads(request.body)

        producto = Producto(
            serie_del_producto=data.get('serie_del_producto'),
            nombre=data.get('nombre'),
            marca=data.get('marca'),
            stock_tienda=data.get('stock_tienda'),
            stock_bodega=data.get('stock_bodega'),
            precio=data.get('precio'),
            imagen=request.FILES.get('imagen')
        )
        producto.save()

 
        response_data = {'message': 'Producto creado exitosamente', 'producto': {
            'id': producto.pk,
            'serie_del_producto': producto.serie_del_producto,
            'nombre': producto.nombre,
            'marca': producto.marca,
            'stock_tienda': producto.stock_tienda,
            'stock_bodega': producto.stock_bodega,
            'precio': producto.precio,
            'imagen': producto.imagen.url if producto.imagen else None
   
        }}
        return JsonResponse(response_data)
    

    #actualizar producto
    def put(self, request, pk=None):

        producto = get_object_or_404(Producto, pk=pk)

   
        data = json.loads(request.body)

        
        if 'serie_del_producto' in data:
            producto.serie_del_producto = data['serie_del_producto']
        if 'nombre' in data:
            producto.nombre = data['nombre']
        if 'marca' in data:
            producto.marca = data['marca']
        if 'stock_tienda' in data:
            producto.stock_tienda = data['stock_tienda']
        if 'stock_bodega' in data:
            producto.stock_bodega = data['stock_bodega']
        if 'precio' in data:
            producto.precio = data['precio']
        if 'imagen' in data:
            producto.imagen = data['imagen']
    
  
        producto.save()

        response_data = {'message': 'Producto actualizado exitosamente', 'producto': {
            'id': producto.pk,
            'serie_del_producto': producto.serie_del_producto,
            'nombre': producto.nombre,
            'marca': producto.marca,
            'stock_tienda': producto.stock_tienda,
            'stock_bodega': producto.stock_bodega,
            'precio': producto.precio,
            'imagen': producto.imagen.url if producto.imagen else None
        }}
        return JsonResponse(response_data)
    
    # Eliminar el producto
    def delete(self, request, pk=None):
  
        producto = get_object_or_404(Producto, pk=pk)

        producto.delete()

        response_data = {'message': 'Producto eliminado exitosamente'}
        return JsonResponse(response_data)