from django.contrib import admin
from . models import Categoria, Marca, Tag, Talla, Producto, Carrito, CarritoProducto

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Tag)
admin.site.register(Talla)
admin.site.register(Producto)
admin.site.register(Carrito)
admin.site.register(CarritoProducto)