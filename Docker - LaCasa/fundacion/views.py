from django.shortcuts import render, redirect
from .models import Voluntario
from .forms import VoluntarioForm
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
import re 

# Create your views here.

class HomePageView(TemplateView):
    def get(self, request, **kwards):
        return render (request, 'fundacion/index.html', context=None)

class Exito_vista(TemplateView):
    def get(self, request, **kwards):
        return render (request, 'fundacion/crea_exito.html', context=None)

class Crear_Voluntario_view(TemplateView):
    def get(self, request, **kwards):
        if request.method == 'POST':
            form = VoluntarioForm(request.POST or None)
            if form.is_valid():
                form_data = form.cleaned_data
                nom = form_data.get("nombre")
                em = form_data.get("email")
                rut = form_data.get("rut")
                fecha = form_data.get("fecha")
                celu = form_data.get("celular")
                comuna = form_data.get("comuna")
                obj = Voluntario()
                obj.nombre = nom
                obj.email = em
                obj.rut = rut
                obj.fecha = fecha
            
                obj.celular = celu
                obj.comuna = comuna
                obj.save()
                return render(request,'fundacion/crea_exito.html', context=None)
            else:
                return render(request,'fundacion/crea_error.html', context=None)

        return render(request, 'fundacion/crear.html', context=None)

def CrearVoluntarioView(request):
    if request.method == 'POST':
        form = VoluntarioForm(request.POST or None)
        if form.is_valid():
            form_data = form.cleaned_data
            nom = form_data.get("nombre")
            em = form_data.get("email")
            rut = form_data.get("rut")
            fecha = form_data.get("fecha")
            celu = form_data.get("celular")
            comuna = form_data.get("comuna")
            obj = Voluntario()
            obj.nombre = nom
            obj.email = em
            obj.rut = rut
            obj.fecha = fecha
            if re.match('\d',obj.celular):
                return render(request,'fundacion/crea_error.html', context=None)
            obj.celular = celu
            obj.comuna = comuna
            obj.save()
            return render(request,'fundacion/crea_exito.html', context=None)
        else:
            return render(request,'fundacion/crea_error.html', context=None)
    return render(request, 'fundacion/crear.html', context=None)