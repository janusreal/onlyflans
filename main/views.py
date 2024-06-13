from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.flanes import flanes
from main.forms import ContactForm
from main.models import Contacto, Flan
from django.contrib.auth.decorators import login_required

#create views

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
def contact(req):
    if req.method == 'GET':
        #se renderiza la página
        form = ContactForm()
        context = {'form': form }
        return render(req, 'contact.html', context)
    else:
        #validamos el formulario
        
        form = ContactForm(req.POST)
        if form.is_valid():
            Contacto.objects.create(
                **form.cleaned_data
            )
            return redirect('/exito')
        context = {'form': form }
        return render(req,'contact.html',context)

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
        return render(req, 'contact.html', context)    
    
    return redirect('/exito')
 

    
    # ahora tengo que validar que 'customer_email' tenga al menos un @ y un .
    # y que customer_name sea de largo maximo 64
    
    # si len(errores) == 0: redirijo a pagina de exito
    # si len(errores) > 0: vuelvo a cargar 'welcome.html', pero ahora mostrando los eorrores 


@login_required
def welcome(req):
    all_flanes = Flan.objects.all()
    return render(req, 'welcome.html', {'all_flanes': all_flanes})

def index(req):
    all_flanes = Flan.objects.filter(is_private=False)
    return render(req, 'index.html', {'all_flanes': all_flanes})

def login(req):
    return render(req, 'login.html')  

def register_form(req):
    
    username = req.POST['username']
    password1 = req.POST['password1']
    password2 = req.POST['password2']

    errores = []
    
    if password1 != password2:
        errores.append('Las contraseñas no coinciden')
                
    if len(password1) < 8:
        errores.append('La contraseña debe contener 8 caracteres como mínimo')
    
    if len(username) >= 15:
        errores.append('El nombre de usuario no debe exceder los 15 caracteres')
        
    if username == '':
        errores.append("No has ingresado un nombre de usuario")
    
    if password1 == '':
        errores.append("No has registrado una contraseña")
            
    if len(errores) > 0:
        context = {
            'errores': errores
            }
        return render(req, 'register.html', context)    
    
    return redirect('/exito')



def register(req):
    return render(req, 'register.html')  
   