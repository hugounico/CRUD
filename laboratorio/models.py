from django.db import models

# Create your models here.
class Laboratorio(models.Model):  
    nombre = models.CharField(max_length=100, unique=True)
    ciudad = models.CharField(max_length=100, default='Santiago')
    pais = models.CharField(max_length=100, default='Chile')

    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'Laboratorio'