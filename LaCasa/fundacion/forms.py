from django import forms
import datetime 


class VoluntarioForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    rut = forms.CharField(max_length=15)
    fecha_nac = forms.CharField(max_length=50)
    celular = forms.IntegerField()
    comuna = forms.CharField(max_length=50)
    email = forms.EmailField()
    ocupacion = forms.CharField(max_length=50)
    nivel_educacion =forms.CharField(max_length=50)
    grupo_interes = forms.CharField(max_length=50)