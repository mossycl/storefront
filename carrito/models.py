from django.db import models
from store.models import Producto
from login.models import Cliente

class Carrito(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='rut_cliente')
    productos = models.ManyToManyField(Producto, through='ItemCarrito')

    def __str__(self):
        return f'Carrito {self.id}'

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    talla = models.IntegerField(blank=False)

    def total(self):
        return self.producto.precio * self.cantidad

    def eliminar(self):
        self.delete()
