from django import forms
import datetime 


class VoluntarioForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    rut = forms.CharField(max_length=15)
    fecha = forms.CharField(max_length=50)
    celular = forms.CharField(max_length=15)
    comuna = forms.CharField(max_length=50)
    email = forms.EmailField()
