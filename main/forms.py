from django import forms

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