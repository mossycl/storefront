from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('zapatos/', views.zapatos, name='zapatos'),
    path('zapatillas/', views.zapatillas, name='zapatillas'),
    path('detalle/<int:pk>/', views.detalle, name='detalle'),
]