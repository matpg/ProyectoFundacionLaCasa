from django.urls import path, include
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
#V->voluntarios
#C->cuentas
#P->proyectos
urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name="index"),
    url(r'^crearV/$', views.CrearVoluntarioView, name="crearVoluntarios"),
    url(r'^GestionV/$', views.GestionarVoluntarios, name="GestionVoluntarios"),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^crearC/$', views.register, name="register"),
    url(r'^crearP/$', views.CreaProyecto, name="crearProyectos"),
]  