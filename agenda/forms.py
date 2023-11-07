from django import forms
from .models import Agenda

class AgendaForm(forms.ModelForm):
    
    class Meta:
        model = Agenda
        #fields = ["DNI", "nombre","correo","etc etc "]
        fields = '__all__'

