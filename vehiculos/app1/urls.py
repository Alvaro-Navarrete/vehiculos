
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('ingreso/', views.ingresar, name='ingresar'),
    path('ingreso/', views.create_view, name='create'),
    path('update/<str:patente>', views.update_view, name='update'),
    path('read/<str:patente>', views.read_view, name='read'),
    path('delete/<str:patente>', views.delete_view, name='delete'),
    path('list/', views.list_view, name='list'),
]
