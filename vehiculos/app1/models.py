from django.db import models


    
class Estado(models.Model):
    
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25, unique=True)


class Vehiculos(models.Model):
    
    patente = models.CharField(max_length=7, null=False, primary_key=True)
    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True)
    registro = models.ForeignKey("RegistroEstacionamiento", null=True, blank=True, on_delete=models.SET_NULL)


class Tarifa(models.Model):
    
    id = models.AutoField(primary_key=True)
    precio = models.PositiveIntegerField()
    
    
class RegistroEstacionamiento(models.Model):
    
    id = models.AutoField(primary_key=True, null=False)
    vehiculo = models.ForeignKey(Vehiculos, on_delete=models.CASCADE)
    tarifa = models.PositiveIntegerField(null=False) # Cambiar por un PositiveIntegerField
    hora_salida = models.DateTimeField(null=True)
    hora_entrada = models.DateTimeField(auto_now_add=True)
    total_pagado = models.PositiveIntegerField()
    
    
