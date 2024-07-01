from typing import Any
from django.db import models

from store.models import Producto
# Create your models here.



# class MetodoEnvio(models.Model):
#     id_metodo = models.AutoField(db_column="id_metodo",primary_key=True)
#     metodo = models.CharField(max_length=100, blank=False, null=False)
#     precio_metodo = models.IntegerField(default=0)

#     def __str__(self):
#         return str(self.metodo)

# class BoletaProducto(models.Model):
#     id_producto = models.ForeignKey("Producto",on_delete=models.CASCADE, db_column="id_producto")
#     num_boleta = models.ForeignKey("Boleta",on_delete=models.CASCADE, db_column="num_boleta")

#     def __str__(self):
#         return str(self.id_producto) + " " + str(self.num_boleta)

# class Boleta(models.Model):
#     num_boleta = models.AutoField(db_column="num_boleta", primary_key=True)
#     fecha_emision = models.DateField()
#     rut_cliente = 0
#     productos = models.ManyToManyField(Producto, through='BoletaProducto')
#     direccion_despacho = models.CharField(max_length=200, null=False, blank=False)
#     id_metodo = models.ForeignKey("MetodoEnvio",on_delete=models.CASCADE, db_column="id_metodo")
#     subtotal = models.IntegerField(default=0)
#     iva = models.IntegerField(default=0)
#     total = models.IntegerField(default=0)

    # def __str__(self):
    #     return str(self.num_boleta)+ " " + str(self.fecha_emision) + " " + str(self.rut_cliente)
    
    # class Meta:
    #     ordering=['num_boleta']
