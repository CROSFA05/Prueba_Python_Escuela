from django.urls import path, include
from rest_framework import routers
from miApp.views import (
    Home,
    Escuelas,
    EscuelaAlta,
    EscuelaEditar,
    EscuelaEliminar,
    Maestros,
    MaestroAlta,
    MaestroEditar,
    MaestroEliminar,
    Alumnos,
    AlumnoAlta,
    AlumnoEditar,
    AlumnoEliminar
)
from miApp.viewsets import EscuelaViewSet, MaestroViewSet, AlumnoViewSet

router = routers.DefaultRouter()
router.register(r'escuelas', EscuelaViewSet)
router.register(r'maestros', MaestroViewSet)
router.register(r'alumnos', AlumnoViewSet)

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('api/', include(router.urls)),
    path('escuelas', Escuelas.as_view(), name='escuelas'),
    path('escuelas/alta', EscuelaAlta.as_view(), name='escuelas_alta'),
    path('escuelas/editar/<int:id>', EscuelaEditar.as_view(), name='escuelas_editar'),
    path('escuelas/eliminar/<int:id>', EscuelaEliminar.as_view(), name='escuelas_eliminar'),
    path('maestros', Maestros.as_view(), name='maestros'),
    path('maestros/alta', MaestroAlta.as_view(), name='maestros_alta'),
    path('maestros/editar/<int:id>', MaestroEditar.as_view(), name='maestros_editar'),
    path('maestros/eliminar/<int:id>', MaestroEliminar.as_view(), name='maestros_eliminar'),
    path('alumnos', Alumnos.as_view(), name='alumnos'),
    path('alumnos/alta', AlumnoAlta.as_view(), name='alumnos_alta'),
    path('alumnos/editar/<int:id>', AlumnoEditar.as_view(), name='alumnos_editar'),
    path('alumnos/eliminar/<int:id>', AlumnoEliminar.as_view(), name='alumnos_eliminar'),
]