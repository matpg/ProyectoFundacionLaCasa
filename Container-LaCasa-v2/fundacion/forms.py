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
    first_name = forms.CharField(max_length=30, required=False, help_text='Obligatorio.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Obligatorio')
    email = forms.EmailField(max_length=254, help_text='Obligatorio')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
