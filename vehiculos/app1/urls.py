
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('ingreso/', views.ingreso_vehiculo, name='create'),
    
    path('list/', views.list_view, name='list'),
    path('salida/', views.salida, name='salida'),
    # path('salida/<str:patente>', views.marcar_salida, name='salidaEstado'),
    
]
