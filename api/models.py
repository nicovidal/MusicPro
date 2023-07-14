from django.db import models

# Create your models here.

class Producto(models.Model):
    TIPO_CHOICES=(
        ('guitarra_cuerpo_solido','guitarra_cuerpo_solido'),
        ('guitarra_acústica','guitarra_acústica'),
        ('guitarra_eléctrica','guitarra_eléctrica'),
        ('bajo_cuatro_cuerdas','bajo_cuatro_cuerdas'),
        ('bajo_cinco_cuerdas','bajo_cinco_cuerdas'),
        ('bajo_activo','bajo_activo'),
        ('bajo_pasivo','bajo_pasivo'),
        ('piano_media_cola','piano_media_cola'),
        ('piano_cola_entera','piano_cola_entera'),
        ('pianolas','pianolas'),
        ('bateria_acustica_mapex','bateria_acustica_mapex'),
        ('bateria_acustica_pearl','bateria_acustica_pearl'),
        ('bateria_acustica_sonor','bateria_acustica_sonor'),
        ('bateria_acustica_tama','bateria_acustica_tama'),
        ('bateria_electrica_alesis','bateria_electrica_alesis'),
        ('bateria_electrica_roland','bateria_electrica_roland'),
        ('cabezales_engl','cabezales_engl'),
        ('cabezales_marshall','cabezales_marshall'),
        ('cabezales_pavey','cabezales_pavey'),
        ('cabezales_evh','cabezales_evh'),
        ('caja_evh','caja_evh'),
        ('caja_engl','caja_engl'),
        ('caja_marshall','caja_marshall'),
        ('caja_pavey','caja_pavey'),
        ('audifonos','audifonos'),
        ('monitores','monitores'),
        ('parlantes','parlantes'),
        ('cables','cables'),
        ('microfono','microfono'),
        ('interfaces','interfaces'),
        ('mixers','mixers'),
    

    )
    CLASE_CHOICES=(
        ('Guitarra','Guitarra'),
        ('Bajo','Bajo'),
        ('Piano','Piano'),
        ('bateria_acustica','bateria_acustica'),
        ('bateria_electrica','bateria_electrica'),
        ('cabezales','cabezales'),
        ('caja','caja'),
        ('accesorio','accesorio'),
    
    )
    serie_del_producto=models.CharField(max_length=50,null=True)
    marca=models.CharField(max_length=50,null=True)
    codigo=models.CharField(max_length=50,null=True)
    nombre=models.CharField(max_length=50,null=True)
    precio=models.IntegerField(null=True)
    clase=models.CharField(max_length=50,choices=CLASE_CHOICES,null=True)
    tipo=models.CharField(max_length=50,choices=TIPO_CHOICES,null=True)
    modelo=models.CharField(max_length=50,null=True)
    oferta=models.BooleanField(null=True)
    nuevo=models.BooleanField(null=True)
    stock_tienda=models.IntegerField(null=True)
    stock_bodega=models.IntegerField(null=True)
    imagen=models.ImageField(upload_to='imagenProductos',null=True,blank=True)

    
     
    def __str__(self):
        return str(self.serie_del_producto)

