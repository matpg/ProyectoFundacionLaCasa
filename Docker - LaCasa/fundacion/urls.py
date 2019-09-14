from django.urls import path, include
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name="index"),
    url(r'^crearV/$', views.CrearVoluntarioView, name="crearVoluntarios"),
<<<<<<< HEAD
    url(r'^GestionarV/$', views.GestionarVoluntario, name="GestionarVoluntarios"),
=======
>>>>>>> febfaa839fc2199a90072ff2ee1a10aaa4b2d5fb
    path('accounts/', include('django.contrib.auth.urls')),
]  