from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import Producto


# Create your views here.
class ProductoView(View):

    def get(self,request):
        productos=list(Producto.objects.values())
        if len(productos)>0:
            datos={'message':'Success','productos':productos}
        else:
            datos={'message':"Productos no encontrados"}
        return JsonResponse(datos)


    def post(self,request):
        pass
    def put(self,request):
        pass
    def delete(self,request):
        pass