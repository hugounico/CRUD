from django.contrib import admin
from .models import Producto

# Register your models here.
#class ProductoAdmin(admin.ModelAdmin):
  #  list_display = ('id', 'nombre', 'f_fabricacion', 'p_costo', 'p_venta') #'laboratorio_id', 
   # ordering = ('nombre') #'laboratorio_id', 
    #list_filter = ('nombre') #'laboratorio_id', 

admin.site.register(Producto) #ProductoAdmin