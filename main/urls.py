from django.urls import path
from main.views import index, about, contact, exito, welcome, register, detalleFlan


urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('welcome/', welcome, name="welcome"),
    path('exito/', exito, name="exito"),
    path('register', register),
    path('contact/',contact, name="contact"),
    path('productos/<id>/', detalleFlan, name="detalleFlan")
    ]

# name="exito" es una ruta nombrada