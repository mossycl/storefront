from django.shortcuts import render

from .models import Producto
# Create your views here.
def zapatos(request):
    productos = Producto.objects.raw('SELECT * FROM store_producto WHERE id_cat IN (1, 3, 4)')
    context = {"productos" : productos}
    return render(request,'zapatos/zapatos.html', context)

def zapatillas(request):
    productos = Producto.objects.raw('SELECT * FROM store_producto WHERE id_cat = 2')
    context = {"productos" : productos}
    return render(request,'zapatillas/zapatillas.html', context)

def detalle(request, pk):
    try:
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