from django.conf.urls import url
from django.urls import path
from aplicaciones.crearcuentas.views import RegistroUsuario
from . import views

urlpatterns = [
    path('registrar', views.RegistroUsuario.as_view(), name= "registrar"),
]