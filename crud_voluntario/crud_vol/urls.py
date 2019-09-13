"""crud_voluntario URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    # [...]
    path('voluntarios', views.VoluntarioList.as_view(), name='voluntario_list'),
    path('voluntario/<int:pk>', views.VoluntarioDetail.as_view(), name='voluntario_detail'),
    path('create', views.VoluntarioCreate.as_view(), name='voluntario_create'),
    path('update/<int:pk>', views.VoluntarioUpdate.as_view(), name='voluntario_update'),
    path('delete/<int:pk>', views.VoluntarioDelete.as_view(), name='voluntario_delete'),
]
