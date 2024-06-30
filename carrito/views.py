from django.shortcuts import render

# Create your views here.
def carrito(request):
    context = {}
    return render(request, 'carrito/carrito.html', context)