# Generated by Django 4.1.2 on 2024-07-02 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_carrito_carritoproducto_carrito_productos_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carritoproducto',
            name='id_carrito',
        ),
        migrations.RemoveField(
            model_name='carritoproducto',
            name='id_producto',
        ),
        migrations.DeleteModel(
            name='Carrito',
        ),
        migrations.DeleteModel(
            name='CarritoProducto',
        ),
    ]