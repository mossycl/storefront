from django.urls import path

from login import views

urlpatterns = [
    path('signup', views.signup, name="signup"),
]