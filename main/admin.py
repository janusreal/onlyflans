from django.contrib import admin
from main.models import Contacto


class ContactoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Contacto, ContactoAdmin)

# Register your models here.



