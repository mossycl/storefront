from django.shortcuts import render
from .models import Region, Comuna, Usuario
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
            email = request.POST['Email']
            password = request.POST['Contraseña']
            rut = request.POST['RUN']
            pnombre = request.POST['Primer Nombre']
            snombre = request.POST['Segundo Nombre']
            apaterno = request.POST['Apellido Paterno']
            amaterno = request.POST['Apellido Materno']
            direccion = request.POST['Dirección']
            region = request.POST['regiones']
            comuna = request.POST['comunas']

            regId = Region.objects.get(nombre_region = region)
            comId = Comuna.objects.get(nombre_comuna = comuna)
            usuarioExiste = False
            try:
                if Usuario.objects.get(rut_cliente=rut):
                    usuarioExiste = True
            except:
                pass

            if usuarioExiste:
                mensaje = "Un usuario ya existe con este RUT"
                form = UsuarioForm()
                context = {"form" : form, "regiones" : regiones, "comunas" : comunas, "mensaje" : mensaje}
                return render(request, 'signup/signup.html', context)
            else:
                obj = Usuario.objects.create(
                    email = email,
                    password = password,
                    rut_cliente = rut,
                    pnombre_cliente = pnombre,
                    snombre_cliente = snombre,
                    apaterno_cliente = apaterno,
                    amaterno_cliente = amaterno,
                    id_region = regId,
                    id_comuna = comId,
                    direccion = direccion
                )
                hashPass = make_password(password)
                userObj = User.objects.create(
                    username = email,
                    password = hashPass,
                    is_staff = False,
                    is_active = True,
                    is_superuser = False
                )

                obj.save()
                userObj.save()
                form = UsuarioForm()
                mensaje = "Usuario registrado con éxito"
                context = {"form" : form, "regiones" : regiones, "comunas" : comunas, "mensaje" : mensaje}
                return render(request, 'signup/success.html',context)
    else:
        form = UsuarioForm()
        context = {"form" : form, "regiones" : regiones, "comunas" : comunas}
        return render(request, 'signup/signup.html', context)
    
def success(request):
    context = {}
    return render(request, 'signup/success.html', context)