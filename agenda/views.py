from django.shortcuts import render
from .forms import AgendaForm
from .models import Agenda

# Create your views here.

def home(reqquest):
    return render(reqquest, 'agenda/home.html')

def agregar_contacto(request):
    data = {
        'form': AgendaForm()
    }
    if request.method == 'POST' :
        formulario = AgendaForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto nuevo agregado"
        else :
            data["form"] = formulario

    return render(request, 'agenda/agregar_contacto.html',data)

def listar_contactos(request):
    contactos = Agenda.objects.all() 
    data = {
        'contactos': contactos
    }

    return render(request,'agenda/listar_contactos.html', data)
