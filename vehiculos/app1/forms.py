from django import forms
from .models import Vehiculos

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculos
        fields = ['patente', 'tarifa', 'total_pagar', 'estado']