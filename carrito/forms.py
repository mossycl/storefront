from django import forms

class FormularioDespacho(forms.Form):
    nombre=forms.CharField(label="Nombre del Receptor", required=True)
    direccion = forms.CharField(label="Dirección", required=True)
    comuna = forms.CharField(label="Comuna", required=True)