from django.urls import path
from .views import home, agregar_contacto, listar_contactos, modificar_contacto, eliminar_contacto

urlpatterns = [
    path('', home, name="home"),
    path('agregar-contacto/', agregar_contacto, name="agregar_contacto"),
    path('listar-contactos/', listar_contactos, name="listar_contactos"),
    path('modificar-contacto/<id>/', modificar_contacto, name="modificar_contacto"),
    path('eliminar-contacto/<id>/', eliminar_contacto, name="eliminar_contacto"),
]