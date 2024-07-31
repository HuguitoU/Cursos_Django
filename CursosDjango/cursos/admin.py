from django.contrib import admin
from .models import Cursos, Actividad

# Register your models here.

class AdministrarCurso(admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = ('nombreCurso', 'maestro', 'created')
    search_fields = ('nombreCurso', 'maestro', 'matriculaCurso')
    list_filter = ('nombreCurso', 'maestro')
    date_hierarchy = 'created'

admin.site.register(Cursos, AdministrarCurso)

class AdministrarActividad(admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = ('id', 'nombreCurso', 'nombreActividad')
    list_filter = ('nombreCurso', 'nombreActividad')

admin.site.register(Actividad, AdministrarActividad)


