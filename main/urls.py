from django.urls import path
from main.views import index, about, welcome, exito

urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('welcome/', welcome, name="welcome"),
    path('exito/', exito, name="exito")
]