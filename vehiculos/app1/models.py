from django.db import models

class Vehiculos(models.Model):
    
    patente = models.CharField(primary_key=True, max_length=7, null=False)
    hora_salida = models.DateTimeField(null=True)
    total_pagar = models.PositiveIntegerField()
    estado = models.CharField(max_length=25)
    hora_entrada = models.DateTimeField(auto_now_add=True)
    tarifa = models.PositiveIntegerField()
    
    
    def __str__(self) -> str:
        return self.patente
    