from django.shortcuts import render
from django.http import HttpResponse
from main.flanes import flanes

#create views


def index(req):

    context = {
    'titulo':'Portal Onlyflans',
    'esAdmin': True,
    'nombre': 'Alejandro Martínez',
    'flanes': flanes
    }
    return render(req, "index.html", context )

def about(req):
    return render(req, "about.html", {} )

def welcome(req):
    return render(req, "welcome.html", {} )