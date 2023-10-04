from django.db import models
#from laboratorio.models import Laboratorio

# Create your models here.
class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    laboratorio3 = models.CharField(max_length=100) #on_delete=models.CASCADE#models.OneToOneField es una clase de campo proporcionada por Django. Indica que se va a establecer una relación uno a uno entre dos modelos.
    especialidad = models.CharField(max_length=100, default='General')        #on_delete es un atributo que se utiliza para especificar qué acción se realizará en el modelo relacionado (Laboratorio) cuando se elimine un objeto del modelo actual (DirectorGeneral).
                                                    
    def __str__(self): 
        return self.nombre
    
    class Meta:
        db_table = 'DirectorGeneral'