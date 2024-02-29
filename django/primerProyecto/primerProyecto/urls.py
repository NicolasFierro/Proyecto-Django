"""
URL configuration for primerProyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from miApp import views
import miApp.views

urlpatterns = [
    path('admin/', admin.site.urls),  # para acceder al administrador de Django
    path('holaMundo/', views.holaMundo, name="Hola Mundo"), #Cuando se llama a esta vista se ejecutara la funcion holaMundo
    path('saludo/<int:redirigir>',views.saludo, name="Saludo"), 
    path('Inicio',views.index, name="Index"),
    path('presentacion/',views.presentacion, name="Presentacion"),
    # path('contacto/',miApp.views.contacto, name="Contacto"),
    # path('contacto/<str:nombre>',miApp.views.contacto, name="Contacto"),
    # path('contacto/<str:nombre>/<str:apellido>',miApp.views.contacto, name="Contacto"),
    path('quienesSomos/',views.quienesSomos, name="QuienesSomos"),
    path('productAndServices/',miApp.views.productAndServices, name="Productos  y Servicios"),
    path('contacto/',miApp.views.contacto, name="contacto"),
    path('', views.index, name='Inicio'),
    path('pagina/', miApp.views.pagina, name="Pagina")
]
