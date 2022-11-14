from django.db import models

# Create your models here.


class Jugadores(models.Model):
    nombres_jugador = models.CharField(max_length=40)
    apellidos_jugador = models.CharField(max_length=40)
    numero_camiseta = models.IntegerField()
    pais_jugador = models.CharField(max_length=40)


class DT(models.Model):
    nombre_dt = models.CharField(max_length=40)
    apellido_dt = models.CharField(max_length=40)
    pais_dt = models.CharField(max_length=40)
    seleccion_representada = models.CharField(max_length=40)


class selecciones(models.Model):
    grupo = models.CharField(max_length=10)
    num_jugadores_convocados = models.IntegerField()
    capitan = models.CharField(max_length=40)


class lesionados(models.Model):
    nom_jug_les = models.CharField(max_length=40)
    ape_jug_les = models.CharField(max_length=40)