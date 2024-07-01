from django.urls import path
from . import views

app_name = 'carrito'
urlpatterns = [
    path('', views.mostrar_carrito, name='mostrar_carrito'),
    path('agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('actualizar/<int:item_id>/', views.actualizar_item, name='actualizar_item'),
    path('eliminar/<int:item_id>/', views.eliminar_item, name='eliminar_item'),
    path('boleta/', views.generar_boleta, name='generar_boleta'),  # Nueva URL

]