from django.shortcuts import render, get_object_or_404
from .models import Producto

def zapatos(request):
    productos = Producto.objects.filter(id_cat__in=[1, 3, 4])
    context = {"productos": productos}
    return render(request, 'zapatos/zapatos.html', context)

def zapatillas(request):
    productos = Producto.objects.filter(id_cat=2)
    context = {"productos": productos}
    return render(request, 'zapatillas/zapatillas.html', context)

def detalle(request, pk):
    producto = get_object_or_404(Producto, id_producto=pk)
    tallas = producto.tallas.all()
    likeProductos = Producto.objects.filter(id_cat=producto.id_cat)[:3]
    context = {"producto": producto, "tallas": tallas, "likeProductos": likeProductos}
    return render(request, 'zapatos/detalle.html', context)
