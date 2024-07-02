## Storefront hecho con Django, base de datos con SQLite

### Como instalar:
1. Crear un ambiente virtual (VENV) con el nombre "ambiente"
2. Activar ambiente virtual por Powershell ".\ambiente\Scripts\activate"
3. En caso de un error de UnauthorizedAccess, ingrese en Powershell "Set-ExecutionPolicy Unrestricted -Scope Process"
4. Actualizar pip (pip install --upgrade pip)
5. Instalar desde requirements.txt "py pip install -r requirements.txt" (Contiene Django 4.1.2 y Pillow)

### Ingresar a admin (usando localhost)
1. Ingresar el comenado "py .\manage.py runserver (puerto opcional)"
2. Ingresa al admin a través de 127.0.0.1:(puerto)/admin
3. Usuario "admin" contraseña "654321"

### Aplicaciones instaladas
1. index <-- Contiene el home, se accede usando solo la direccion ip (127.0.0.1:(puerto))
2. store <-- Contiene la tienda, dentro de ella hay 3 vistas "zapatos", "zapatillas" y "detalle
3. carrito <-- Contiene el carrito de compras, se compone de "carrito" y "boleta
4. login <-- Maneja el sistema de registro de usuarios, "login.html" se encuentra como template en la raiz del proyecto usando "accounts" de Django. "signup" se encuentra como vista dentro de login

### Programado por
- Christopher Bahamondes (AutumnZbx)
- Diego Fernández (mossycl)
