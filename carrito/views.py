from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def carrito(request):
    context = {}
    return render(request, 'carrito/carrito.html', context)

def confirmar(request):
    context = {}
    return render(request,'carrito/confirmar.html', context)