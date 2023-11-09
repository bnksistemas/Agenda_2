from django.shortcuts import render, redirect, get_object_or_404
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


def modificar_contacto(request, id):

    contacto = get_object_or_404(Agenda, id=id)

    data = {
        'form': AgendaForm(instance=contacto)
    }

    if request.method == 'POST':
        formulario = AgendaForm(
            data=request.POST,
            instance=contacto,
            files=request.FILES
        )

        if formulario.is_valid():
            formulario.save()
            return redirect(to='listar_contactos')
        data['form'] = formulario
        data['mensaje'] = formulario.errors

    return render(request, 'agenda/modificar_contacto.html', context=data)

def eliminar_contacto(request, id):
    contacto =get_object_or_404(Agenda, id=id)
    contacto.delete()

    return redirect(to='listar_contactos')