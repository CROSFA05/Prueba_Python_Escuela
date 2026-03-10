from django.contrib import admin

# Register your models here.

from miApp.models import *

admin.site.register(Escuela)
admin.site.register(Maestro)
admin.site.register(Alumno)