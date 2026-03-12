from django.urls import path
from miApp.views import (
    Home,
    Escuelas,
    EscuelaAlta,
    EscuelaEditar,
    EscuelaEliminar,
    Maestros,
    MaestroAlta,
    MaestroEditar,
    MaestroEliminar
)

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('escuelas', Escuelas.as_view(), name='escuelas'),
    path('escuelas/alta', EscuelaAlta.as_view(), name='escuelas_alta'),
    path('escuelas/editar/<int:id>', EscuelaEditar.as_view(), name='escuelas_editar'),
    path('escuelas/eliminar/<int:id>', EscuelaEliminar.as_view(), name='escuelas_eliminar'),
    path('maestros', Maestros.as_view(), name='maestros'),
    path('maestros/alta', MaestroAlta.as_view(), name='maestros_alta'),
    path('maestros/editar/<int:id>', MaestroEditar.as_view(), name='maestros_editar'),
    path('maestros/eliminar/<int:id>', MaestroEliminar.as_view(), name='maestros_eliminar'),
]