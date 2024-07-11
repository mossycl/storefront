from django.db import models

from django.conf import settings

# Create your models here.
class Region(models.Model):
    id_region = models.AutoField(db_column='id_region',primary_key=True)
    nombre_region = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return str(self.nombre_region)

class Comuna(models.Model):
    id_comuna = models.AutoField(db_column='id_comuna',primary_key=True)
    nombre_comuna = models.CharField(max_length=50, null=False, blank=False)
    id_region = models.ForeignKey("Region",on_delete=models.CASCADE,db_column='id_region')

    def __str__(self):
        return str(self.nombre_comuna)

class Cliente(models.Model):
    email = models.EmailField(unique=True, null=False, blank=False)
    #password = models.CharField(max_length=10, null=False, blank=False)
    rut_cliente = models.CharField(max_length=10, primary_key=True)
    pnombre_cliente = models.CharField(max_length=50, null=False, blank=False)
    snombre_cliente = models.CharField(max_length=50, null=False, blank=False)
    apaterno_cliente = models.CharField(max_length=50, null=False, blank=False)
    amaterno_cliente = models.CharField(max_length=50, null=False, blank=False)
    id_region = models.ForeignKey('Region', on_delete=models.CASCADE, db_column='id_region')
    id_comuna = models.ForeignKey('Comuna', on_delete=models.CASCADE, db_column='id_comuna')
    direccion = models.CharField(max_length=100, blank=False, null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return str(self.rut_cliente) + " " + str(self.pnombre_cliente) + " " + str(self.apaterno_cliente)