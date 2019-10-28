from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy


# Create your views here.

class RegistroUsuario(CreateView):
    model = User
    template_name = "templates/usuario/registrar.html"
    form_class = UserCreationForm
    success_url = "."