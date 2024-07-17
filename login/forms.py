from django.forms import ModelForm

from .models import Cliente, Region, Comuna

class UsuarioForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ["email", "rut_cliente", "pnombre_cliente", "snombre_cliente", "apaterno_cliente", "amaterno_cliente", "direccion"]
        labels = {"email" : "Email", "rut_cliente" : "RUN", "pnombre_cliente" : "Primer Nombre",
                  "snombre_cliente" : "Segundo Nombre", "apaterno_cliente" : "Apellido Paterno", "amaterno_cliente" : "Apellido Materno",
                  "direccion" : "Dirección"}