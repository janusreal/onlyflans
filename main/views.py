from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.flanes import flanes
from main.forms import ContactForm
from main.models import Contacto

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

'''
def welcome(req):
    context = {
        'titulo':'Bienvenido',
        'esAdmin': True,
        'nombre': 'Alejandro Martínez',
    }
    errores = req.session.pop('errores', None)
    context = {'errores': errores}
    return render(req, "welcome.html", context )
'''

#welcome vendría a ser para crear un nuevo contacto
def welcome(req):
    if req.method == 'GET':
        #se renderiza la página
        form = ContactForm()
        context = {'form': form }
        return render(req, 'welcome.html', context)
    else:
        #validamos el formulario
        
        form = ContactForm(req.POST)
        if form.is_valid():
            Contacto.objects.create(
                **form.cleaned_data
            )
            '''Contactos.objects.create({
                'nombre':form.nombre,
                'email': form.email,
                'edad':form.edad
            })'''
            return redirect('/exito')
        context = {'form': form }
        return render(req,'welcome.html',context)

def exito(req):
    return render(req, "exito.html")

def contact_form(req):
    customer_name = req.POST['customer_name']
    customer_email = req.POST['customer_email']
    message = req.POST['message']
    
    errores = []
    
    if not '@' in customer_email:
        errores.append('Falta la arroba en campo de email')
            
    if len(customer_name) >= 64:
        errores.append('Nombre excede el largo de 64 caracteres')
        
    if customer_name == '':
        errores.append("No has ingresado un nombre")
    
    if customer_email == '':
        errores.append("No has ingresado un email")
            
    if len(errores) > 0:
        context = {
            'errores': errores,
            'flag': True
            }
        return render(req, 'welcome.html', context)    
    
    return redirect('/exito')
 

    
    # ahora tengo que validar que 'customer_email' tenga al menos un @ y un .
    # y que customer_name sea de largo maximo 64
    
    # si len(errores) == 0: redirijo a pagina de exito
    # si len(errores) > 0: vuelvo a cargar 'welcome.html', pero ahora mostrando los eorrores 
