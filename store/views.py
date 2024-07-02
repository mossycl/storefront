from django.shortcuts import render, redirect

from .models import Producto, Carrito, CarritoProducto
from login.models import Usuario
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
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
            'subtotal': carrito[str(prod.id_producto)]['cantidad'] * prod.precio,
            'imagen_url': prod.imagen.url  # Asegúrate de que los productos tienen imágenes asociadas
        }
        for prod in productos
    ]
    
    context = {
        'productos': productos_detalle,
        'total': total
    }
    return render(request, 'carrito/carrito.html', context)

@require_POST
@csrf_exempt
def modificar_cantidad(request):
    data = json.loads(request.body)
    producto_id = data.get('productoId')
    cambio = data.get('cambio')

    if producto_id and cambio:
        carrito = request.session.get('carrito', {})
        if str(producto_id) in carrito:
            if cambio == -1 and carrito[str(producto_id)]['cantidad'] > 1:
                carrito[str(producto_id)]['cantidad'] -= 1
            elif cambio == 1:
                carrito[str(producto_id)]['cantidad'] += 1
            
            request.session['carrito'] = carrito
            return JsonResponse({'success': True, 'message': 'Carrito actualizado.'})
        else:
            return JsonResponse({'success': False, 'message': 'Producto no encontrado en el carrito.'})
    return JsonResponse({'success': False, 'message': 'Datos incorrectos.'})