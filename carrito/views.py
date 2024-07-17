from django.shortcuts import render, get_object_or_404, redirect
from .models import Carrito, ItemCarrito, Boleta, ProductoBoleta, MetodoEnvio
from store.models import Producto
from login.models import Cliente
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id_producto=producto_id)
    if request.method=='POST':
        cantidad = request.POST['quantity']
        talla = request.POST['talla']
        userName = request.POST['user']
        user = User.objects.get(username=userName)
        cliente = get_object_or_404(Cliente, user=user)

        carrito = Carrito.objects.get(cliente=cliente)
        item = ""
        try:
            item = ItemCarrito.objects.get(producto=producto)
            if item.talla == int(talla):
                item.cantidad += int(cantidad)
            else:
                item = ItemCarrito.objects.create(
                carrito=carrito,
                producto=producto,
                talla=talla,
                cantidad=cantidad
            )
        except:
            item = ItemCarrito.objects.create(
                carrito=carrito,
                producto=producto,
                talla=talla,
                cantidad=cantidad
            )
        item.save()
    
    return redirect('carrito:mostrar_carrito')

@login_required
def mostrar_carrito(request):
    if request.user.is_authenticated:
        usuario = get_object_or_404(User,username=request.user)
        cliente = get_object_or_404(Cliente, user=usuario)
        carrito = Carrito.objects.get(cliente=cliente)
        metodos = MetodoEnvio.objects.all()
        items = carrito.items.all()
        if items:
            subtotal = sum(item.total() for item in items)
        else:
            items = []
            subtotal = 0

        context = {
            'items': items,
            'subtotal': subtotal,
            'metodos' : metodos
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
    if request.user.is_authenticated:
        usuario = get_object_or_404(User,username=request.user)
        cliente = get_object_or_404(Cliente, user=usuario)
        carrito = Carrito.objects.get(cliente=cliente)
        items = carrito.items.all()
        idMetodo = request.POST['metodo']
        metodo = MetodoEnvio.objects.get(id_metodo=idMetodo)
        generarBoleta = Boleta.objects.create(
            cliente = cliente,
            envio = metodo,
            total=0
        )
        generarBoleta.save()
        # Guarda cada producto en la ultima boleta generada
        boleta = Boleta.objects.raw(f"SELECT * FROM carrito_boleta WHERE rut_cliente = '{cliente.rut_cliente}' ORDER BY numero_boleta DESC LIMIT 1")[0]
        boletaID = boleta.numero_boleta
        subtotal = 0
        iva = 0
        for item in items:
            prod = ProductoBoleta.objects.create(
                boleta = boleta,
                producto = item.producto,
                cantidad = item.cantidad,
                talla = item.talla
            )
            prod.save()
            iva += round(item.producto.precio*0.19)
            subtotal += item.producto.precio - iva
        precioEnvio = metodo.precio_metodo
        total = subtotal + precioEnvio + iva
        # Actualiza la boleta
        boleta = Boleta.objects.get(numero_boleta = boletaID)
        boleta.subtotal = subtotal
        boleta.iva = iva
        boleta.total = total
        boleta.save()

        # GENERAR VISTA
        if boleta:
            nombre = f"{cliente.pnombre_cliente} {cliente.apaterno_cliente} {cliente.amaterno_cliente}"
            email = cliente.email
            direccion = cliente.direccion
            comuna = cliente.id_comuna
            region = cliente.id_region
            context = {
                "items" : items,
                "subtotal" : subtotal,
                "iva" : iva,
                "precioEnvio" : precioEnvio,
                "total" : total,
                "nombre" : nombre,
                "email" : email,
                "direccion" : direccion,
                "comuna" : comuna,
                "region" : region
            }
            return render(request, 'carrito/boleta.html', context)
