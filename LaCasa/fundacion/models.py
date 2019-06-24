from django.db import models
import time
# Create your models here.

class Voluntario(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    rut = models.CharField(max_length=11, primary_key=True)
    edad = models.IntegerField()
    celular = models.IntegerField()
    comuna = models.CharField(max_length=50)
    fecha_nac = models.CharField(max_length=15)
    ocupacion = models.CharField(max_length=50)
    nivel_educacion = models.CharField(max_length=50)
    grupo_interes = models.CharField(max_length=50)

    def __str__ (self):
        return self.nombre
        

