from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    imagen = serializers.SerializerMethodField()

    class Meta:
        model = Producto
        fields = ['id','serie_del_producto','marca', 'codigo', 'nombre','precio',
                  'modelo','oferta','nuevo','stock_tienda','stock_bodega', 'imagen']

    def get_imagen(self, obj):
        if obj.imagen:
            return obj.imagen.url
        return None