from django.shortcuts import render
from django.http import HttpResponse

#create views

def home(request):
    return HttpResponse('Página de inicio')
