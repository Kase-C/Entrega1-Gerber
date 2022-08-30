from django.db import models

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=50)
    contraseña = models.IntegerField()
    email = models.EmailField()

class Mascota(models.Model):
    animal = models.CharField(max_length=50)
    edad = models.IntegerField()

class Estudios(models.Model):
    carrera = models.CharField(max_length=50)
    institucion = models.CharField(max_length=50)
