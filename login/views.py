from django.shortcuts import render
from .models import Region, Comuna, Usuario
from .forms import UsuarioForm
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

            obj.save()
            form = UsuarioForm()
            mensaje = "Usuario registrado con éxito"
            context = {"form" : form, "regiones" : regiones, "comunas" : comunas, "mensaje" : mensaje}
            return render(request, 'signup/signup.html',context)
    else:
        form = UsuarioForm()
        context = {"form" : form, "regiones" : regiones, "comunas" : comunas}
        return render(request, 'signup/signup.html', context)

def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        
        comprobarLogin = Usuario.objects.filter(email=email, password=password).values()
        if comprobarLogin:
            request.session["logged"] = True
            request.session["nombreUsuario"] = comprobarLogin[0]['pnombre_cliente']
            context = {"usuario" : comprobarLogin[0]['pnombre_cliente']}
            print(comprobarLogin[0])
            return render(request, 'index/index.html', context)
        else:
            msj = "Usuario y/o contraseña incorrectos"
            context = {"mensaje": msj}
            return render(request, 'login/login.html', context)
    else:
        context = {}
        return render(request, 'login/login.html',context)