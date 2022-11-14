from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def index(request):
    return render(request,"appmundial/base.html")


def Jugadores(request):

    return render(request, "appmundial/jugadores.html")

def Directores_tecnicos(request):

    return render(request, "appmundial/directores_tec.html")

def Selecciones(request):

    return render(request, "appmundial/selecciones.html")
    
def Lesionados(request):

    return render(request, "appmundial/lesionados.html")

def form_Lesionados(request):

    if request.method == "POST":
        nombre_jugador =request.POST["nombre_lesionado"]
        apellido_jugador =request.POST["apellido_lesionado"]

        lesionados = Lesionados(nombres_jugador=nombre_jugador, apellidos_jugador=apellido_jugador)
        lesionados.save()

    return render(request, "appmundial/form_lesionados.html")
