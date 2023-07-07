# Generated by Django 4.2.1 on 2023-07-04 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenProductos'),
        ),
        migrations.AddField(
            model_name='producto',
            name='nuevo',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='oferta',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(null=True),
        ),
    ]