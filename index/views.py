from django.shortcuts import render, get_object_or_404
from carrito.models import Carrito, ItemCarrito
from django.contrib.auth.models import AnonymousUser


def index(request):
    return render(request, "index/index.html")

# def mostrar_carrito(request):
#     carrito_id = request.session.get('carrito_id')
    
#     if carrito_id:
#         try:
#             carrito = Carrito.objects.get(id=carrito_id)
#         except Carrito.DoesNotExist:
#             carrito = None

#         if carrito:
#             items = carrito.items.all()
#             subtotal = sum(item.total() for item in items)
#             total = subtotal + 3500
#         else:
#             items = []
#             subtotal = 0
#             total = 0
#     else:
#         items = []
#         subtotal = 0
#         total = 0

#     context = {
#         'items': items,
#         'subtotal': subtotal,
#         'total': total,
#     }
#     return render(request, 'carrito/carrito.html', context)
