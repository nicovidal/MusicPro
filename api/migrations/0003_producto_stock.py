# Generated by Django 4.2.1 on 2023-06-20 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_producto_nuevo_producto_oferta'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(max_length=50, null=True),
        ),
    ]