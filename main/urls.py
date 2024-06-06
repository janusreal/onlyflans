from django.urls import path
from main.views import index, about, welcome, contact_form, exito

urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('welcome/', welcome, name="welcome"),
    path('contact_form', contact_form, name="contact_form"),
    path('exito/', exito, name="exito")
]