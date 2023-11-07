from django.urls import path
from .views import home, agregar_contacto, listar_contactos

urlpatterns = [
    path('', home, name="home"),
    path('agregar-contacto/', agregar_contacto, name="agregar_contacto"),
    path('listar-contactos/', listar_contactos, name="listar_contactos"),
   
]
