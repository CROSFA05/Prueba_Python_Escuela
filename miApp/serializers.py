from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import Group
from miApp.models import Escuela, Maestro, Alumno
from django.core.exceptions import ValidationError
from django.contrib.auth.models import Permission

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "is_staff", "is_active", "is_superuser"]

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]

class permissionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Permission
        fields = ["url", "name"]

class EscuelaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Escuela
        fields = "__all__"

class MaestroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Maestro
        fields = "__all__"

class AlumnoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alumno
        fields = "__all__"

    def validate(self, attrs):
        escuela = attrs.get("escuela")
        maestro = attrs.get("maestro")
        
        if self.instance:
            escuela = escuela or self.instance.escuela
            maestro = maestro or self.instance.maestro
        
        if escuela and maestro.escuela_id != escuela.id:
            raise serializers.ValidationError({"maestro": "El maestro no pertenece a la escuela"})
        return attrs