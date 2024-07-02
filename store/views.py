from django.shortcuts import render

from .models import Producto, Carrito, CarritoProducto
from login.models import Usuario
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
    try:
        if request.method == "POST":
            idProd = request.POST['idProd']
            user = request.POST['user']
            precio = request.POST['precio']
            rutCli = Usuario.objects.get(email=user).rut_cliente
            idCarrito = ""

            try:
                idCarrito = Carrito.objects.get(rut_cliente = rutCli).id_carrito
            except Exception as ex:
                print("expecion")
                objCarrito = Carrito.objects.create(
                    rut_cliente = rutCli
                )
                # objCarrito.save()
                # idCarrito = Carrito.objects.get(rut_cliente = rutCli).id_carrito
                # print(idCarrito)

            # agregar = CarritoProducto.objects.create(
            #     id_carrito = idCarrito,
            #     id_producto = idProd,
            #     cantidad = 1,
            #     precio = precio
            # )
            # agregar.save()
        
        producto = Producto.objects.get(id_producto=pk)
        tallas = producto.tallas.all()
        likeProductos = Producto.objects.filter(id_cat = producto.id_cat)
        listaLike = []
        for i in range(len(likeProductos)):
            if i <=2:
                listaLike.append(likeProductos[i])
        context = {"producto" : producto, "tallas" : tallas, "likeProductos" : likeProductos, "listaLike" : listaLike}
        return render(request,'zapatos/detalle.html', context)
    except:
        mensaje = "El producto que está buscando no existe"
        context = {"mensaje" : mensaje}
        return render(request,'zapatos/detalle.html', context)

@login_required
def carrito(request):
    context = {}
    return render(request, 'carrito/carrito.html', context)