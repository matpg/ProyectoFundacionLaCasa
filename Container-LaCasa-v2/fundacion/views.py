from django.shortcuts import render, redirect
from .models import Voluntario
from .forms import VoluntarioForm
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
import re 
from .funciones import CalcularEdadVoluntario
from datetime import datetime
from django.shortcuts import get_list_or_404
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class HomePageView(TemplateView):
    def get(self, request, **kwards):
        return render (request, 'fundacion/index.html', context=None)

class Exito_vista(TemplateView):
    def get(self, request, **kwards):
        return render (request, 'fundacion/crea_exito.html', context=None)


def GestionarVoluntarios(request):
    voluntarios = get_list_or_404(Voluntario)
    print(voluntarios)
    return render(request, 'fundacion/gestion_voluntario.html', {'voluntarios': voluntarios})



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
            obj.edad = CalcularEdadVoluntario(fecha)
            obj.fecha_incripcion = datetime.now().date()
            if re.match('\d',obj.celular):
                return render(request,'fundacion/crea_error.html', context=None)
            obj.celular = celu
            obj.comuna = comuna
            obj.save()
            return render(request,'fundacion/crea_exito.html', context=None)
        else:
            return render(request,'fundacion/crea_error.html', context=None)
    return render(request, 'fundacion/crear.html', context=None)

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("fundacion")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request,
                          template_name = "cuentas/register.html",
                          context={"form":form})
    else:
        form = UserCreationForm()
        return render(request = request,
                      template_name = "cuentas/register.html",
                      context={"form":form})    