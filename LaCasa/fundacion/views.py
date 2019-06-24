from django.shortcuts import render, redirect
from .models import Voluntario
from .forms import VoluntarioForm
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login

# Create your views here.

class HomePageView(TemplateView):
    def get(self, request, **kwards):
        return render (request, 'fundacion/index.html', context=None)

def Crear_Voluntario_view(request):
    form = VoluntarioForm(request.POST or None)
    print(request.POST)
    if form.is_valid():
        form_data = form.cleaned_data
        nom = form_data.get("nombre")
        em = form_data.get("email")
        rut = form_data.get("rut")
        obj = Voluntario()
        obj.nombre = nom
        obj.email = em
        obj.rut = rut
        obj.save()
        print(form_data.get("fecha_nacim"))
        
    else:
        print("mat poga se la come toda")

    return render(request, 'fundacion/crear.html', context=None)

