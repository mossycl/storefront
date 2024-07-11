from django.shortcuts import render, get_object_or_404
from .models import Region, Comuna, Cliente
from .forms import UsuarioForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Create your views here.

def signup(request):
    context = {}
    regiones = Region.objects.all()
    comunas = Comuna.objects.all()
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid:
            email = request.POST['email']
            password = request.POST['pass1']
            rut = request.POST['rutCliente']
            pnombre = request.POST['pNombre']
            snombre = request.POST['sNombre']
            apaterno = request.POST['aPaterno']
            amaterno = request.POST['aMaterno']
            direccion = request.POST['direccion']
            region = request.POST['regiones']
            comuna = request.POST['comunas']

            regId = Region.objects.get(nombre_region = region)
            comId = Comuna.objects.get(nombre_comuna = comuna)
            usuarioExiste = False

            try:
                if Cliente.objects.get(rut_cliente=rut):
                    usuarioExiste = True
            except:
                pass

            if usuarioExiste:
                mensaje = "Un usuario ya existe con este RUT"
                form = UsuarioForm()
                context = {"form" : form, "regiones" : regiones, "comunas" : comunas, "mensaje" : mensaje}
                return render(request, 'signup/signup.html', context)
            else:
                hashPass = make_password(password)
                userObj = User.objects.create(
                    username = email,
                    email = email,
                    password = hashPass,
                    first_name = pnombre,
                    last_name = apaterno,
                    is_staff = False,
                    is_active = True,
                    is_superuser = False
                )
                userObj.save()

                obj = Cliente.objects.create(
                    email = email,
                    rut_cliente = rut,
                    pnombre_cliente = pnombre,
                    snombre_cliente = snombre,
                    apaterno_cliente = apaterno,
                    amaterno_cliente = amaterno,
                    id_region = regId,
                    id_comuna = comId,
                    direccion = direccion,
                    user = get_object_or_404(User, username=email)
                )
                
                obj.save()
                form = UsuarioForm()
                mensaje = "Usuario registrado con éxito"
                context = {"mensaje" : mensaje}
                return render(request, 'signup/success.html',context)
    else:
        form = UsuarioForm()
        context = {"form" : form, "regiones" : regiones, "comunas" : comunas}
        return render(request, 'signup/signup.html', context)
    
def success(request):
    context = {}
    return render(request, 'signup/success.html', context)