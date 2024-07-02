from django.contrib import admin
from . models import Categoria, Marca, Tag, Talla, Producto
# Register your models here.
admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Tag)
admin.site.register(Talla)
admin.site.register(Producto)