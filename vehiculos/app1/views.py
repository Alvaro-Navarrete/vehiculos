from django.shortcuts import render, redirect, get_object_or_404
from .models import Vehiculos, Estado, RegistroEstacionamiento, Tarifa
from .forms import VehiculoForm
from django.utils import timezone

def index(request):
    return render(request, 'app1/index.html')


def datos_salida(patente):
    try:
        
        vehiculo = Vehiculos.objects.get(pk = patente)
        
        # Verifica si 'patente' es un str vacio
        if patente == "":
            raise Exception("Debe ingresar una patente valida")
        
        
        
        registro = RegistroEstacionamiento.objects.get(pk = vehiculo.registro.id)
        registro.hora_salida = timezone.now()
        
        
        tiempo_total = registro.hora_salida - registro.hora_entrada
        minutos = int(tiempo_total.total_seconds() / 60)
        
        registro.total_pagado =  minutos * registro.tarifa
        
        datos = {
            "patente" : vehiculo.patente,
            "estado" : vehiculo.estado,
            "hora_entrada" : registro.hora_entrada,
            "hora_salida" : registro.hora_salida,
            "minutos" : minutos,
            "tarifa" : registro.tarifa,
            "total_pagado" : registro.total_pagado
        }
        
        registro.save()
        return datos
        
    except Exception as e:
        print(f"error : {e}")
        
def registrar_salida(patente):
    vehiculo = Vehiculos.objects.get(pk = patente)
    # Variable con el estado 'no estacionado'
    no_estacionado = Estado.objects.get(pk = 2)
    
    vehiculo.estado = no_estacionado
    vehiculo.save()

def salida(request):
    salida = None
    patente = request.GET.get('patente')
    accion = request.GET.get('accion')
    if accion == 'buscar':
        salida = datos_salida(patente)
    
    if accion == 'salida':
        registrar_salida(patente)

    return render(request,'app1/registro_salida.html', {'registro': salida})


def ingreso_vehiculo(request):
    
    if request.method == 'POST':
        try:
            
            patente = request.POST.get('patente').strip().upper()
            
            # Verifica si 'patente' es un str vacio
            if patente == "":
                raise Exception("Debe ingresar una patente valida")
            
            # Variable con el estado 'estacionado'
            estacionado = Estado.objects.get(pk = 1)
            
            try:
                # Vehiculo con la patente obtenida desde el formulario
                vehiculo = Vehiculos.objects.get(pk = patente)
                if vehiculo.estado == Estado.objects.get(pk = 1):
                    raise Exception("Vehiculo ya está estacionado")
            except Vehiculos.DoesNotExist:
                vehiculo = Vehiculos.objects.create(patente = patente, estado = estacionado)
            
            
            obj_tarifa = Tarifa.objects.get(pk = 1)
            
            registro = RegistroEstacionamiento.objects.create(vehiculo = vehiculo, tarifa = obj_tarifa.precio, total_pagado = 0)
            
            # Actualiza el estado del vehiculo si no estaba estacionado
            vehiculo.registro = registro
            vehiculo.estado = estacionado
            vehiculo.save()
            
            return redirect('index')
            
        
        except Exception as e:
            print(f'Error al crear el registro: {e}')
        
    return render(request,'app1/ingreso.html')



def tarifa(request):
    tarifa = Tarifa.objects.get(pk = 1)
    
    if request.method == 'POST':
        
        valor = request.POST.get('tarifa')
        tarifa.precio = int(valor)
        
        tarifa.save()
    
    return render(request, 'app1/tarifa.html', {'tarifa' : tarifa})



def list_view(request):
    registro = RegistroEstacionamiento.objects.all()
    return render(request,'app1/list.html', {'registros' : registro})