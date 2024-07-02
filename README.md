## Storefront hecho con Django, base de datos con SQLite

Como instalar:
1. Crear un ambiente virtual (VENV) con el nombre "ambiente"
2. Activar ambiente virtual por Powershell ".\ambiente\Scripts\activate"
3. En caso de un error de UnauthorizedAccess, ingrese en Powershell "Set-ExecutionPolicy Unrestricted -Scope Process"
4. Actualizar pip (pip install --upgrade pip)
5. Instalar desde requirements.txt "py pip install -r requirements.txt"

Ingresar a admin (usando localhost)
1. Ingresar el comenado "py .\manage.py runserver (puerto opcional)"
2. Ingresa al admin a través de 127.0.0.1:(puerto)/admin
3. Usuario "admin" contraseña "654321"

Aplicaciones instaladas
1. index <-- Contiene el home, se accede usando solo la direccion ip (127.0.0.1:(puerto))
2. store <-- Contiene la tienda, dentro de ella hay 2 vistas "zapatos" y "zapatillas", se ingresa usando 127.0.0.1:(puerto)/store/(nombre del template)
Existe una tercera vista llamada "detalle" que maneja los detalles de cada producto
3. carrito <-- Contiene el carrito de compras
