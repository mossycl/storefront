from django.db import models
from store.models import Producto
from login.models import Cliente
from django.utils import timezone

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

class Boleta(models.Model):
    numero_boleta = models.AutoField(db_column='numero_boleta',primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='rut_cliente')
    envio = models.ForeignKey('MetodoEnvio', on_delete=models.CASCADE, db_column='id_metodo')
    productos = models.ManyToManyField(Producto, through='ProductoBoleta')
    subtotal = models.IntegerField(null=True)
    iva = models.IntegerField(null=True)
    total = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return f'N° {self.numero_boleta} - {self.cliente} - Total: {self.total}'

class ProductoBoleta(models.Model):
    boleta = models.ForeignKey(Boleta, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    talla = models.IntegerField()

    def total(self):
        return self.producto.precio * self.cantidad

class MetodoEnvio(models.Model):
    id_metodo = models.AutoField(db_column='id_metodo', primary_key=True)
    desc_metodo = models.CharField(max_length=50)
    precio_metodo = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.id_metodo} {self.desc_metodo}'
