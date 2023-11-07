from django.contrib import admin
from .models import Provincia, Agenda

# Register your models here.

# si quiero tener varias columnas en el admin
class AgendaAdmin(admin.ModelAdmin):
    list_display =[ "DNI", "nombre", "email", "fec_nac", "domicilio" , "provincia"]


admin.site.register(Provincia)
admin.site.register(Agenda, AgendaAdmin)