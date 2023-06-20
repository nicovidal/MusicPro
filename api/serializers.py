from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    imagen = serializers.SerializerMethodField()

    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion', 'imagen']

    def get_imagen(self, obj):
        if obj.imagen:
            return obj.imagen.url
        return None