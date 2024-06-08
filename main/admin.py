from django.contrib import admin
from main.models import Contacto, Flan


class ContactoAdmin(admin.ModelAdmin):
    pass

class FlanAdmin(admin.ModelAdmin):
    pass

admin.site.register(Contacto, ContactoAdmin)
admin.site.register(Flan, FlanAdmin)


# Register your models here.



