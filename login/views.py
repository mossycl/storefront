from django.shortcuts import render

from .forms import UsuarioForm
# Create your views here.

def signup(request):
    context = {}
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid:
            form.save()
            form = UsuarioForm()
            context = {"form" : form}
            return render(request, 'signup/signup.html',context)
    else:
        form = UsuarioForm()
        context = {"form" : form}
        return render(request, 'signup/signup.html', context)