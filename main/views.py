from django.shortcuts import render
from django.http import HttpResponse
from main.flanes import flanes

#create views


def index(req):

    context = {
    'titulo':'Lista de productos',
    'epigrafe': 'Portal de OnlyFlans',
    'esAdmin': True,
    'nombre': 'Alejandro Martínez',
    'flanes': flanes
    }
    return render(req, "index.html", context )

def about(req):
    context = {
        'titulo':'Acerca de nosotros'
    }
    return render(req, "about.html", context )

def welcome(req):
    context = {
        'titulo':'Bienvenido',
        'esAdmin': True,
        'nombre': 'Alejandro Martínez',
    }
    return render(req, "welcome.html", context )