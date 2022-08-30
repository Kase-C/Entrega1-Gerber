from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *

def inicio(request):
    return render (request, "inicio.html")

def formularioUsuario(request):
    if request.method=="POST":
        formulario_usuario = FormularioUsuario(request.POST)
        if formulario_usuario.is_valid():
            info = formulario_usuario.cleaned_data
            nombre_usuario = info["nombre_usuario"]
            contraseña = info["contraseña"]
            email = info["email"]
            usuario = Usuario(nombre_usuario = nombre_usuario, contraseña = contraseña , email = email)
            usuario.save()
            return render (request, "inicio.html", {"resultado": "Usuario Creado"})
        else:
            return render (request, "inicio.html", {"resultado": "Error"})
    else:
        formulario_usuario = FormularioUsuario()
    return render(request, "formularioUsuario.html", {"formulario":formulario_usuario})

def formularioMascota(request):
    if request.method=="POST":
        formulario_mascota = FormularioMascota(request.POST)
        if formulario_mascota.is_valid():
            info = formulario_mascota.cleaned_data
            animal = info["animal"]
            edad = info["edad"]
            mascota = Mascota(animal = animal, edad = edad)
            mascota.save()
            return render (request, "inicio.html", {"resultado": "Mascota Registrada"})
        else:
            return render (request, "inicio.html", {"resultado": "Error"})
    else:
        formulario_mascota = FormularioMascota()
    return render(request, "formularioMascota.html", {"formulario":formulario_mascota})

def formularioEstudios(request):
    if request.method=="POST":
        formulario_estudios = FormularioEstudios(request.POST)
        if formulario_estudios.is_valid():
            info = formulario_estudios.cleaned_data
            carrera = info["carrera"]
            institucion = info["institucion"]
            estudios = Estudios(carrera = carrera, institucion = institucion)
            estudios.save()
            return render (request, "inicio.html", {"resultado": "Estudios Guardados"})
        else:
            return render (request, "inicio.html", {"resultado": "Error"})
    else:
        formulario_estudios = FormularioEstudios()
    return render(request, "formularioEstudios.html", {"formulario":formulario_estudios})

def busquedaUsuario(request):
    return render(request, "busquedaUsuario.html")

def busquedaMascota(request):
    return render(request, "busquedaMascota.html")

def busquedaEstudios(request):
    return render(request, "busquedaEstudios.html")

def buscarUsuario(request):
    if request.GET["nombre_usuario"]:
        nombre_usuario = request.GET["nombre_usuario"]
        usuarios = Usuario.objects.filter(nombre_usuario = nombre_usuario)
        if len(usuarios)!=0:
            return render(request, "resultadoBusquedaUsuario.html", {"usuarios":usuarios})
        else:
            return render(request, "resultadoBusquedaUsuario.html", {"mensaje": "No hay usuarios con ese nombre"})
    else:
        return render(request, "busquedaUsuario.html", {"mensaje": "No enviaste datos!"})

def buscarMascota(request):
    if request.GET["animal"]:
        animal = request.GET["animal"]
        mascotas = Mascota.objects.filter(animal = animal)
        if len(mascotas)!=0:
            return render(request, "resultadoBusquedaMascota.html", {"mascotas":mascotas})
        else:
            return render(request, "resultadoBusquedaMascota.html", {"mensaje": "No hay Mascotas de ese tipo"})
    else:
        return render(request, "busquedaMascota.html", {"mensaje": "No enviaste datos!"})

def buscarEstudios(request):
    if request.GET["carrera"]:
        carrera = request.GET["carrera"]
        estudios = Estudios.objects.filter(carrera = carrera)
        if len(estudios)!=0:
            return render(request, "resultadoBusquedaEstudios.html", {"estudios":estudios})
        else:
            return render(request, "resultadoBusquedaEstudios.html", {"mensaje": "No hay Estudios de esa carrera"})
    else:
        return render(request, "busquedaEstudios.html", {"mensaje": "No enviaste datos!"})

