from django.contrib import admin
from .models import Laboratorio

# Register your models here.
class LaboratorioAdmin(admin.ModelAdmin):    #cambios visuales del sitio admin de django
    list_display = ('id', 'nombre')
    ordering = ('id',)

admin.site.register(Laboratorio, LaboratorioAdmin)