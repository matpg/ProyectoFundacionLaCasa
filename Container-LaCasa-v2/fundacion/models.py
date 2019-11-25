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

class ProyectoVoluntario(models.Model):
    id_proyecto = models.CharField(max_length=10)
    id_voluntario = models.CharField(max_length=11)
    diasAsistidos = models.IntegerField()

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField()
    def __str__ (self):
        return self.nombre

class Proyecto(models.Model):
    id_proyecto = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    logo = models.FileField(default='SOME STRING')
    jefe = models.CharField(max_length=50)
    fecha_inicio = models.CharField(max_length=20)
    fecha_termino = models.CharField(max_length=20)
    cantidad_voluntarios = models.IntegerField()
    presupuesto = models.CharField(max_length=20)
    proyectos = models.Manager()
    def __str__(self):
        return self.nombre
