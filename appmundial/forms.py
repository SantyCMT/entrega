from django import forms


class JugadoresLesionados(forms.Form):
    
    nombres = forms.CharField(max_length=30)
    apellidos = forms.CharField(max_length=30)


class Jugadores_Mundial(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    numeros_remera = forms.IntegerField()
    pais_del_jugador = forms.CharField(max_length=40)


class Director_tecnico_mundial(forms.Form):
    nombre_dt = forms.CharField(max_length=40)
    apellido_dt = forms.CharField(max_length=40)
    pais_dt = forms.CharField(max_length=40)
    seleccion_representada = forms.CharField(max_length=40)