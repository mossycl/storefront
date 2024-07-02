from django.db import models

from login.models import Usuario

# Create your models here.
class Marca(models.Model):
    id_marca = models.AutoField(db_column="id_marca",primary_key=True)
    nombre_marca = models.CharField(max_length=50,blank=False,null=False)

    def __str__(self):
        return str(self.nombre_marca)

class Categoria(models.Model):
    id_cat = models.AutoField(db_column="id_cat",primary_key=True)
    nombre_cat = models.CharField(max_length=50,blank=False,null=False)

    def __str__(self):
        return str(self.nombre_cat)
    
class Tag(models.Model):
    id_tag = models.AutoField(db_column='id_tag',primary_key=True)
    nombre_tag = models.CharField(max_length=50,blank=False,null=False)
    def __str__(self):
        return str(self.nombre_tag)

class Talla(models.Model):
    talla = models.IntegerField()

    def __str__(self):
        return str(self.talla)

class Producto(models.Model):
    id_producto = models.AutoField(db_column="id_producto",primary_key=True)
    nombre_prod = models.CharField(max_length=100,blank=False,null=False)
    id_marca = models.ForeignKey("Marca",on_delete=models.CASCADE, db_column='id_marca')
    id_cat = models.ForeignKey("Categoria",on_delete=models.CASCADE, db_column='id_cat')
    descripcion = models.CharField(max_length=300,null=False)
    imagen = models.ImageField(upload_to='tienda',null=True)
    precio = models.IntegerField(null=False, default=0)
    tags = models.ManyToManyField(Tag)
    cantidad = models.IntegerField(null=False)
    tallas = models.ManyToManyField(Talla)
    disponible = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.id_producto)+ " " + str(self.nombre_prod) + " " + str(self.id_marca)
    
    class Meta:
        ordering=['id_marca']

class Carrito(models.Model):
    id_carrito = models.AutoField(db_column='id_carrito', primary_key=True)
    rut_cliente = models.ForeignKey(Usuario,on_delete=models.CASCADE, db_column='rut_cliente')
    productos = models.ManyToManyField(Producto, through='CarritoProducto')
    subtotal = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id_carrito) + " Subtotal:" + str(self.subtotal)

class CarritoProducto(models.Model):
    id_carrito = models.ForeignKey('Carrito', on_delete=models.CASCADE, db_column='id_carrito')
    id_producto = models.ForeignKey('Producto', on_delete=models.CASCADE, db_column='id_producto')
    cantidad = models.IntegerField(default=0)
    precio = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id_carrito) + "-" + str(self.id_producto)