#from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
#from django.core.urlresolvers import reverse_lazy


# Create your models here.

class RegistroUsuario(CreateView):
    model = User
    template_name = "registration/crearusuario.html"
    form_class = UserCreationForm
    success_url = 'fundacion'

# Create your views here.
