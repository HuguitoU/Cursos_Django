from django.shortcuts import render, HttpResponse
menu = """
    <a href = "/">Inicio</a>
    <a href = "cursos/">Cursos</a>
    <a href = "formulario/">Contacto</a>
"""

# Create your views here.
def principal(request):
    return render(request, "contenido/principal.html")

def cursos(request):
    return render(request, "contenido/cursos.html")

def contacto(request):
    return render(request, "contenido/formCurso.html")

def navegacion(request):
    return render(request, "contenido/navegacion.html")

def nav(request):
    return render(request, "contenido/nav.html")