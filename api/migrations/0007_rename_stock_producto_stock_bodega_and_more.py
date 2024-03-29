# Generated by Django 4.2.1 on 2023-07-07 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_producto_clase'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='stock',
            new_name='stock_bodega',
        ),
        migrations.AddField(
            model_name='producto',
            name='stock_tienda',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='clase',
            field=models.CharField(choices=[('Guitarra', 'Guitarra'), ('Bajo', 'Bajo'), ('Piano', 'Piano'), ('bateria_acustica', 'bateria_acustica'), ('bateria_electrica', 'bateria_acustica'), ('cabezales', 'cabezales'), ('caja', 'caja'), ('accesorio', 'accesorio')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='tipo',
            field=models.CharField(choices=[('guitarra_cuerpo_solido', 'guitarra_cuerpo_solido'), ('guitarra_acústica', 'guitarra_acústica'), ('guitarra_eléctrica', 'guitarra_eléctrica'), ('bajo_cuatro_cuerdas', 'bajo_cuatro_cuerdas'), ('bajo_cinco_cuerdas', 'bajo_cinco_cuerdas'), ('bajo_activo', 'bajo_activo'), ('bajo_pasivo', 'bajo_pasivo'), ('piano_media_cola', 'piano_media_cola'), ('piano_cola_entera', 'piano_cola_entera'), ('bateria_acustica_mapex', 'bateria_acustica_mapex'), ('bateria_acustica_pearl', 'bateria_acustica_pearl'), ('bateria_acustica_sonor', 'bateria_acustica_sonor'), ('bateria_acustica_tama', 'bateria_acustica_tama'), ('bateria_electrica_alesis', 'bateria_acustica_alesis'), ('cabezales_engl', 'cabezales_engl'), ('cabezales_marshall', 'cabezales_marshall'), ('cabezales_pavey', 'cabezales_pavey'), ('cabezales_evh', 'cabezales_evh'), ('caja_evh', 'cabezales_evh'), ('caja_engl', 'caja_engl'), ('caja_marshall', 'caja_marshall'), ('caja_pavey', 'caja_pavey'), ('audifonos', 'audifonos'), ('monitores', 'monitores'), ('parlantes', 'parlantes'), ('cables', 'cables'), ('microfono', 'microfono'), ('interfaces', 'interfaces'), ('mixers', 'mixers')], max_length=50, null=True),
        ),
    ]
