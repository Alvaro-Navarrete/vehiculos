from django import forms
from .models import RegistroEstacionamiento, Vehiculos, Estado

class VehiculoForm(forms.ModelForm):
    
    class Meta:
        model = Vehiculos
        fields = ['patente']
        