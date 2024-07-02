from django import forms
from store.models import Product

class FormularioDespacho(forms.Form):
    nombre=forms.CharField(label="Nombre del Receptor", required=True)
    direccion = forms.CharField(label="Dirección", required=True)
    comuna = forms.CharField(label="Comuna", required=True)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['nombre_prod', 'descripcion', 'precio', 'imagen']