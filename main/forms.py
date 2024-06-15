from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(
        max_length=25,
        label = 'Nombre de Usuario',
        widget = forms.TextInput(attrs={'class': 'form-control'})
        )
    
    email = forms.EmailField(
        max_length=55,
        label = 'Correo Electrónico',
        widget = forms.EmailInput(attrs={'class': 'form-control'})
        )
    
    password1 = forms.CharField(
        label = "Ingrese una contraseña",
        widget = forms.PasswordInput(attrs={'class': 'form-control'}))
    
    password2 = forms.CharField(
        label = "Vuelva a ingresar la contraseña",
        widget = forms.PasswordInput(attrs={'class': 'form-control'}))

class ContactForm(forms.Form):
    nombre = forms.CharField(
        max_length = 55,
        widget=forms.TextInput(
            attrs = { 
                     'class':'form-control' 
                    }
            )
        )
    
    email = forms.EmailField(
        max_length=55,
        label = 'Correo Electrónico',
        widget = forms.EmailInput(attrs={'class': 'form-control'})
        )
    
    mensaje = forms.CharField(
        max_length = 400,
        widget=forms.Textarea(
            attrs = { 
                     'class':'form-control',
                     'rows': 8
                    }
            )
        )