from django.contrib import admin
from . models import Carrito, ItemCarrito, Boleta, ProductoBoleta, MetodoEnvio
# Register your models here.
admin.site.register(Carrito)
admin.site.register(ItemCarrito)
admin.site.register(Boleta)
admin.site.register(ProductoBoleta)
admin.site.register(MetodoEnvio)