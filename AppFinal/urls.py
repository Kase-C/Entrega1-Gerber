from django.urls import path
from .views import *


urlpatterns = [
    path('formularioUsuario/', formularioUsuario, name='formularioUsuario'),
    path('formularioMascota/', formularioMascota, name='formularioMascota'),
    path('formularioEstudios/', formularioEstudios, name='formularioEstudios'),
    path('busquedaUsuario/', busquedaUsuario, name='busquedaUsuario'),
    path('busquedaMascota/', busquedaMascota, name='busquedaMascota'),
    path('busquedaEstudios/', busquedaEstudios, name='busquedaEstudios'),
    path('buscarUsuario/', buscarUsuario, name='buscarUsuario'),
    path('buscarMascota/', buscarMascota, name='buscarMascota'),
    path('buscarEstudios/', buscarEstudios, name='buscarEstudios'),
    path('', inicio, name='inicio'),
]