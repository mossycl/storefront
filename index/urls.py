from django.urls import path
from index import views 
from django.conf import settings
from django.conf.urls.static import static

app_name = 'carrito' 
app_name = 'index'
urlpatterns = [
    path('', views.index, name="index"),
    # path('carrito/', views.mostrar_carrito, name='mostrar_carrito'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)