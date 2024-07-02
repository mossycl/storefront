from django.db import models
from store.models import Producto

class Carrito(models.Model):
    productos = models.ManyToManyField(Producto, through='ItemCarrito')

    def __str__(self):
        return f'Carrito {self.id}'

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

    def total(self):
        return self.producto.precio * self.cantidad

    def eliminar(self):
        self.delete()
