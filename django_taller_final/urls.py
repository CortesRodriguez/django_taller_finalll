"""django_taller_final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from seminarioApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    #CRUD
    path('reservas/', views.reservas),
    path('agregar/', views.agregarreserva),
    path('borrar/<int:id>', views.eliminarreserva),
    path('editar/<int:id>/', views.editarreserva),
    #class
    path('class_inscritos/', views.ListaInscrito.as_view()),
    path('class_inscritos/<int:pk>', views.DetalleInscrito.as_view()),
    #api rest
    path('apilista/', views.verinscritosapi),
    #function
    path('funct_inscritos/', views.listar_inscritos),
    path('funct_inscritos/<int:pk>', views.inscrito_detalle),




]
