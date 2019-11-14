from django import forms
import datetime 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class VoluntarioForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    rut = forms.CharField(max_length=15)
    fecha = forms.CharField(max_length=15)
    celular = forms.CharField(max_length=15)
    comuna = forms.CharField(max_length=50)
    email = forms.EmailField()


class SignUpForm(UserCreationForm):
    Nombre = forms.CharField(max_length=30, required=False, help_text='Obligatorio',)
    Apellido = forms.CharField(max_length=30, required=False, help_text='Obligatorio')
    email = forms.EmailField(max_length=254, help_text='Obligatorio')
    Usuario = forms.CharField(max_length=254, help_text='Obligatorio')

    class Meta:
        model = User
        fields = ('Usuario', 'Nombre', 'Apellido', 'email', 'password1', 'password2', 'is_active', 'is_superuser' )


class ProyectoForm(forms.Form):
    id_proyecto = forms.CharField(max_length=10)
    nombre = forms.CharField(max_length=100)
    descripcion = forms.CharField(widget=forms.Textarea)
    #logo = forms.FileField(required=False)
    jefe = forms.CharField(max_length=50)
    fecha_inicio = forms.CharField(max_length=20)
    fecha_termino = forms.CharField(max_length=20)
    cantidad_voluntarios = forms.IntegerField()
    presupuesto = forms.CharField(max_length=20)        

    
