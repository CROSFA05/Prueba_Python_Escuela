from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from miApp.models import Escuela, Maestro, Alumno
from miApp.serializers import EscuelaSerializer, MaestroSerializer, AlumnoSerializer, UserSerializer
from django.contrib.auth.models import Group
from miApp.serializers import GroupSerializer
from django.contrib.auth.models import Permission, permissionsSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = permissionsSerializer

class EscuelaViewSet(viewsets.ModelViewSet):
    queryset = Escuela.objects.all()
    serializer_class = EscuelaSerializer

class MaestroViewSet(viewsets.ModelViewSet):
    queryset = Maestro.objects.all()
    serializer_class = MaestroSerializer

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer