from django.shortcuts import render, redirect

from .models import Producto, Carrito, CarritoProducto
from login.models import Usuario
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def zapatos(request):
    productos = Producto.objects.raw('SELECT * FROM store_producto WHERE id_cat IN (1, 3, 4)')
    context = {"productos" : productos}
    return render(request,'zapatos/zapatos.html', context)

@login_required
def zapatillas(request):
    productos = Producto.objects.raw('SELECT * FROM store_producto WHERE id_cat = 2')
    context = {"productos" : productos}
    return render(request,'zapatillas/zapatillas.html', context)

@login_required
def detalle(request, pk):
    producto = Producto.objects.get(id_producto=pk)
    if request.method == "POST":
        carrito = request.session.get('carrito', {})
        producto_id = str(producto.id_producto)
        if producto_id in carrito:
            carrito[producto_id]['cantidad'] += 1
        else:
            carrito[producto_id] = {'precio': float(producto.precio), 'cantidad': 1}
        
        request.session['carrito'] = carrito
        return redirect('carrito')  # Redireccionamos al carrito

    context = {
        "producto": producto,
        "tallas": producto.tallas.all()
    }
    return render(request, 'zapatos/detalle.html', context)

@login_required
def carrito(request):
    carrito = request.session.get('carrito', {})
    productos = Producto.objects.filter(id_producto__in=carrito.keys())
    total = sum(item['cantidad'] * item['precio'] for item in carrito.values())
    
    productos_detalle = [
        {
            'producto': prod,
            'cantidad': carrito[str(prod.id_producto)]['cantidad'],
            'subtotal': carrito[str(prod.id_producto)]['cantidad'] * prod.precio
        }
        for prod in productos
    ]
    
    context = {
        'productos': productos_detalle,
        'total': total
    }
    return render(request, 'carrito/carrito.html', context)