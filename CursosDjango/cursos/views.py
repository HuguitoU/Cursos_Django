from django.shortcuts import render
from .models import Cursos

# Create your views here.
def cursos(request):
     cursos = Cursos.objects.all()
     return render(request, "cursos/cursos.html",{'cursos': cursos})

def consultar1(request):
    cursos = Cursos.objects.filter(maestro = "Hugo Uribe")
    return render(request, "cursos/consultas.html", {'cursos': cursos})


def consultar2(request):
    cursos = Cursos.objects.filter(matriculaCurso = "UTM29263TI")
    return render(request, "cursos/consultas.html", {'cursos': cursos})

def consultar3(request):
    cursos = Cursos.objects.filter(matriculaCurso__endswith = "GS")
    return render(request, "cursos/consultas.html", {'cursos': cursos})    

def consultar4(request):
    cursos = Cursos.objects.filter(actividad__nombreActividad__startswith = 'Doc')
    return render(request, "cursos/consultas.html", {'cursos': cursos})

def formulario(request, nombre = None, carrera = None, profesor = None):
    nombre = request.GET.get('nombre')
    carrera = request.GET.get('carrera')
    profesor = request.GET.get('profesor')
    return render(request, "cursos/formulario.html", {'nombre':nombre, 'carrera': carrera, 'profesor': profesor})


