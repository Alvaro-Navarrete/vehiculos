from django.contrib import admin
from .models import Vehiculos

@admin.register(Vehiculos)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('patente', 'hora_entrada', 'hora_salida', 'total_pagar')
    search_fields = ('patente', 'hora_entrada')
