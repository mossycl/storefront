from django.urls import path
from store import views

urlpatterns = [
    path('zapatos/', views.zapatos, name="zapatos"),
    path('zapatillas/', views.zapatillas, name="zapatillas"),
    path('detalle/<str:pk>/', views.detalle, name="detalle"),
    path('carrito/', views.carrito, name='carrito'),
    path('modificar_cantidad/', views.modificar_cantidad, name='modificar_cantidad'),
    path('eliminar_producto/', views.eliminar_producto, name='eliminar_producto'),
]
