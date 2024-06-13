from django.shortcuts import render, HttpResponse
menu = """
    <a href = "/">Inicio</a>
    <a href = "cursos/">Cursos</a>
    <a href = "formulario/">Contacto</a>
"""

# Create your views here.
def principal(request):
    bienvenida = "<h2>Bienvenido a nuestro portal</h2>"
    descripcion = "<h4>Nuestro principal objetivo es enseñarte como usar python</h4>"
    return HttpResponse(menu + bienvenida + descripcion)

def cursos(request):
    cursos = """ <h2>Lista de cursos disponibles</h2>
    <ul>
        <li>
            <p>Base de datos</p>
        </li>
        <li>
            <p>Programación</p>
        </li>
        <li>
            <p>IoT</p>
        </li>
    </ul> """
    return HttpResponse(menu + cursos)

def contacto(request):
    formulario = """ <h2>Curso</h2>
    <p>Nombre: <input type = "text" name = "nombre" /></p>
    <p>Correo electrónico: <input type = "text" name = "correo" /></p>
    <p>Curso: <select>
    <option>Base de datos</option>
    <option>Programacion</option>
    <option>IoT</opcion>
    </select>
    </p>
    <p>Mensaje: </p><p><textarea cols = "50" rows = "10"></textarea></p>
    <p><input type = "button" name = "enviar" value = "Enviar" /></p """
    return HttpResponse(menu + formulario)