from django.db import models
from laboratorio.models import Laboratorio

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.CharField(max_length=100) #models.ForeignKey(Laboratorio)on_delete=models.CASCADE#Esta línea define el campo laboratorio en el modelo Producto como una clave externa (ForeignKey) que establece una relación muchos a uno con el modelo Laboratorio.
    f_fabricacion = models.DateField(verbose_name="Fecha de fabricación", default='2015-01-01')
    p_costo = models.DecimalField(max_digits=10, decimal_places=2)
    p_venta = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'Producto'