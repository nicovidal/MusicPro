# Generated by Django 4.2.1 on 2023-07-11 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MusicProWeb', '0006_venta_tranferencia'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venta',
            old_name='tranferencia',
            new_name='transferencia',
        ),
    ]
