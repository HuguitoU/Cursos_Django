from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Cursos(models.Model):
    imagen = models.ImageField(null = True, upload_to = "fotos", verbose_name = "Fotografia")
    nombreCurso = models.TextField(verbose_name = "Curso")
    matriculaCurso = models.CharField(max_length=12, verbose_name = "Matricula")
    maestro = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ["created"]

    def __str__(self):
        return self.nombreCurso

class Actividad(models.Model):
    id = models.AutoField(primary_key = True, verbose_name = "Clave")
    nombreCurso = models.ForeignKey(Cursos, on_delete = models.CASCADE, verbose_name = "Nombre del Curso")
    nombreActividad = models.TextField(verbose_name = "Nombre de la Actividad")
    descripcion = RichTextField(verbose_name = "Descripción de la Actividad")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de Creación")

    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"
        ordering = ["created"]

    def __str__(self):
        return self.nombreActividad

