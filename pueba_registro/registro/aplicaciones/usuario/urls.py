from django.conf.urls import url
from aplicaciones.usuario.views import RegistroUsuario
from django.urls import path
from . import views

app_name="usuario_app"

urlpatterns = [
    #path('registrar', views.RegistroUsuario.as_view(), name='registrar')
    path('registrar', views.RegistroUsuario.as_view(), name="registrar")
]

