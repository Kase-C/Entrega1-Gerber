from django.http import HttpResponse
from django.shortcuts import render
from .models import *

def inicio(request):
    return render (request, "inicio.html")

def formularioUsuario(request):
    return render(request, "formularioUsuario.html")

def formularioMascota(request):
    return render(request, "formularioMascota.html")

def formularioEstudios(request):
    return render(request, "formularioEstudios.html")

def buscarUsuario(request):
    return render(request, "buscarUsuario.html")

def buscarMascota(request):
    return render(request, "buscarMascota.html")

def buscarEstudios(request):
    return render(request, "buscarEstudios.html")
