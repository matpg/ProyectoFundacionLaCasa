from django.db import models
import time

class Voluntario(models.Model):
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=11, primary_key=True)
    fecha = models.CharField(max_length=50)
    edad = models.CharField(max_length=50)
    celular = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50)
    email = models.EmailField()
    fecha_incripcion = models.CharField(max_length=15)
    voluntarios = models.Manager()
    """    
    ocupacion = models.CharField(max_length=50)
    nivel_educacion = models.CharField(max_length=50)
    grupo_interes = models.CharField(max_length=50)
    """
    def __str__ (self):       
        return self.nombre

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField()
    def __str__ (self):       
        return self.nombre
        