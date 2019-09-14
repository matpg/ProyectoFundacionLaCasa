from django import forms
import datetime 


class VoluntarioForm(forms.Form):
    nombre = forms.CharField(max_length=100)
<<<<<<< HEAD
    rut = forms.CharField(max_length=15)
    fecha = forms.CharField(max_length=15)
=======
    apellido = forms.CharField(max_length=100)
    rut = forms.CharField(max_length=15)
    fecha = forms.CharField(max_length=50)
>>>>>>> febfaa839fc2199a90072ff2ee1a10aaa4b2d5fb
    celular = forms.CharField(max_length=15)
    comuna = forms.CharField(max_length=50)
    email = forms.EmailField()
