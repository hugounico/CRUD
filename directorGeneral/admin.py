from django.contrib import admin
from .models import DirectorGeneral

# Register your models here.
#class DirectorGeneralAdmin(admin.ModelAdmin):
 #   list_display = ('id', 'nombre') #'laboratorio_id', 
  #  ordering = ('nombre',)

admin.site.register(DirectorGeneral) #DirectorGeneralAdmin