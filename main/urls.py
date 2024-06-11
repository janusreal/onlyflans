from django.urls import path
from main.views import index, about, contact, exito, welcome


urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('welcome/', welcome, name="welcome"),
    path('contact/', contact, name="contact"),
    path('exito/', exito, name="exito"),
]