from django.shortcuts import render, redirect, get_list_or_404
from .models import Voluntario, Proyecto
from .forms import VoluntarioForm, SignUpForm, ProyectoForm
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
import re 
from .funciones import CalcularEdadVoluntario
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request,'fundacion/index.html')

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

##########################Registro de Voluntarios###############################################

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


##########################Creacion de Cuentas de usuario###############################################

def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=raw_password)
            return redirect("register")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request,
                          template_name = "cuentas/register.html",
                          context={"form":form})
    else:
        form = SignUpForm()
        return render(request = request,
                      template_name = "cuentas/register.html",
                      context={"form":form})    


###################################Creación de Proyectos###############################################

def CreaProyecto(request):
    if request.method == "POST":
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            print(form_data)
            id_proyecto = form.data.get("id_proyecto")
            nombre = form_data.get("nombre")
            descripcion = form_data.get("descripcion")
            logo = form_data.get("logo")
            jefe = form_data.get("jefe")
            fecha_inicio = form_data.get("fecha_inicio")
            fecha_termino = form_data.get("fecha_termino")
            cantidad_voluntarios = form_data.get("cantidad_voluntarios")
            presupuesto = form_data.get("presupuesto")
            obj = Proyecto()
            obj.id_proyecto = id_proyecto
            obj.nombre = nombre
            obj.descricion = descripcion
            obj.logo = logo
            obj.jefe = jefe
            obj.fecha_inicio = fecha_inicio
            obj.fecha_termino = fecha_termino
            obj.cantidad_voluntarios = cantidad_voluntarios
            obj.presupuesto = presupuesto
            obj.save()

            return render(request,'proyectos/crea_exito.html', context=None)
        else:
            #for msg in form.error_messages:
             #   print(form.error_messages[msg])

            return render(request = request,
                          template_name = "proyectos/crea_proyecto.html",
                          context={"form":form})
    else:
        form = ProyectoForm()
        return render(request = request,
                      template_name = "proyectos/crea_proyecto.html",
                      context={"form":form})    

