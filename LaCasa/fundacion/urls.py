from django.urls import path, re_path, include
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name="index"),
    url(r'^crearV/$', views.CrearVoluntarioView, name="crearVoluntarios"),
    url(r'^GestionV/$', views.GestionarVoluntarios, name="GestionVoluntarios"),
    
    #####################graficos###################
    url(r'^Grafico/$', views.CrearGrafico, name="grafico"),
    url(r'^Grafico/$', views.CrearGrafico2, name="grafico2"),
    path('accounts/', include('django.contrib.auth.urls')),
    #################Cuentas de usuario#############
    
]  