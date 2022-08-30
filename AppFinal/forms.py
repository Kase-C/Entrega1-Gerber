from errno import EDEADLOCK
from django import forms


class FormularioUsuario(forms.Form):
    nombre_usuario = forms.CharField(max_length=50)
    contraseña = forms.IntegerField()
    email = forms.EmailField()

class FormularioMascota(forms.Form):
    animal = forms.CharField(max_length=50)
    edad = forms.IntegerField()

class FormularioEstudios(forms.Form):
    carrera = forms.CharField(max_length=50)
    contraseña = forms.CharField(max_length=50)