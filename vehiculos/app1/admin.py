from django.contrib import admin
from .models import Vehiculos, Estado, RegistroEstacionamiento, Tarifa

@admin.register(Vehiculos)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ['patente', 'estado']
    search_fields = ['patente']


@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    search_fields = ['nombre']
    

@admin.register(RegistroEstacionamiento)
class RegistroAdmin(admin.ModelAdmin):
    list_display = ['id', 'hora_salida','hora_entrada','tarifa','total_pagado','vehiculo']
    search_fields = ['vehiculo']
    
    
@admin.register(Tarifa)
class TarifaAdmin(admin.ModelAdmin):
    list_display = ['id', 'precio']