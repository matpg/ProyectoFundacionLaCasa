from django.conf.urls import url
from django.urls import path
<<<<<<< HEAD
from views import RegistroUsuario
=======
from aplicaciones.crearcuentas.views import RegistroUsuario
>>>>>>> 93a2e5252d9403af203fbe263d379bf79801d6c3
from . import views

urlpatterns = [
    path('registrar', views.RegistroUsuario.as_view(), name= "registrar"),
]