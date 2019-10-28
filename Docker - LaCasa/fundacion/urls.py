from django.urls import path, include
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name="index"),
    url(r'^crearV/$', views.CrearVoluntarioView, name="crearVoluntarios"),
    url(r'^GestionarV/$', views.GestionarVoluntario, name="GestionarVoluntarios"),
    path('accounts/', include('django.contrib.auth.urls')),
]  