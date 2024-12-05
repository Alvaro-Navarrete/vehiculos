from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db import IntegrityError
from .models import Vehiculos
from .forms import VehiculoForm


def index(request):
    return render(request, 'app1/index.html')


def salida(request):
    
    vehiculo = Vehiculos.objects.all()
    return render(request,'app1/salida.html', {'lista_vehiculos':vehiculo})


def marcar_salida(request):
    
    estado = Vehiculos.estado
    if estado == "estacionado":
        estado = "no estacionado"
    
    return


def create_view(request):
    # if request.method == "POST":
    #     patente = request.POST.get("patente")
    #     hora_entrada = request.POST.get("hora_entrada")
    #     hora_salida = request.POST.get("hora_salida")
    #     total_pagar = request.POST.get("total_pagar")
    #     estado = request.POST.get("estado")
        
    #     Vehiculos.objects.create(patente = patente, hora_entrada = hora_entrada, hora_salida = hora_salida, total_pagar = total_pagar, estado = estado)
    #     return redirect('list_view')
        
        # except IntegrityError as e:
        #     error_message = str(e)
        #     if "UNIQUE constraint failed: clientes_cliente.correo_electronico" in error_message:
        #         msg_error = ("Telefono ya existe")
        #     elif "UNIQUE constraint failed" in error_message:
        #         msg_error =("llave duplicada :" + error_message)
        #     elif "NOT NULL constraint failed" in error_message:
        #         msg_error =("Error: Un campo obligatorio está vacío.")
        #     elif "FOREIGN KEY constraint failed" in error_message:
        #         msg_error =("Error: El valor de la clave foránea no es válido.")
        #     else:
        #         msg_error =(f"Error de integridad desconocido: {error_message}")
           

        #     form = ClienteForm() 
        #     return render(request,'create.html', {'form': form, 'error': msg_error})
        
        
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('index')
    else:
        form = VehiculoForm() 
    return render(request,'app1/ingreso.html', {'form': form})

def update_view(request, patente):
    vehiculo: Vehiculos = get_object_or_404(Vehiculos, patente = patente)
    if request.method == "POST":
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid:
            form.save()
            return redirect('list_view')
    else:
        form = VehiculoForm(instance=vehiculo) 
    return render(request,'create.html', {'form': form} )

 
def read_view(request, patente):
    vehiculo: Vehiculos = get_object_or_404(Vehiculos, patente = patente)
    print(vehiculo)
    return render(request,'read.html', {'vehiculo': vehiculo})

def delete_view(request, patente):
    vehiculo: Vehiculos = get_object_or_404(Vehiculos, patente = patente)
    vehiculo.delete()
    return redirect('list_view')
    #return render(request,'delete.html')

def list_view(request):
    vehiculo = Vehiculos.objects.all()
    return render(request,'list.html', {'lista_vehiculos':vehiculo})