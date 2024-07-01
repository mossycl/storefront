from django.shortcuts import render, get_object_or_404, redirect
from .models import Carrito, ItemCarrito
from store.models import Producto

def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id_producto=producto_id)
    carrito_id = request.session.get('carrito_id', None)
    
    if carrito_id:
        carrito = Carrito.objects.get(id=carrito_id)
    else:
        carrito = Carrito.objects.create()
        request.session['carrito_id'] = carrito.id

    item, created = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
    
    if not created:
        item.cantidad += 1
        item.save()
    
    return redirect('carrito:mostrar_carrito')

def mostrar_carrito(request):
    carrito_id = request.session.get('carrito_id', None)

    if carrito_id:
        carrito = Carrito.objects.get(id=carrito_id)
        items = carrito.items.all()
        subtotal = sum(item.total() for item in items)
        total = subtotal + 3500  
    else:
        items = []
        subtotal = 0
        total = 0

    context = {
        'items': items,
        'subtotal': subtotal,
        'total': total,
    }
    return render(request, 'carrito/carrito.html', context)

def eliminar_item(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id)
    item.delete()
    return redirect('carrito:mostrar_carrito')

def actualizar_item(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id)

    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        item.cantidad = quantity
        item.save()

    return redirect('carrito:mostrar_carrito')

def generar_boleta(request):
    carrito_id = request.session.get('carrito_id')

    if carrito_id:
        carrito = get_object_or_404(Carrito, id=carrito_id)
        items = carrito.items.all()
        subtotal = sum(item.total() for item in items)
        total = subtotal + 3500 
    else:
        items = []
        subtotal = 0
        total = 0

    context = {
        'items': items,
        'subtotal': subtotal,
        'total': total,
    }

    return render(request, 'carrito/boleta.html', context)
