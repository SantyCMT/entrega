from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"appmundial/base.html")


def Jugadores(request):

    return render(request, "appmundial/jugadores.html")

def Directores_tecnicos(request):

    return render(request, "appmundial/directores_tec.html")

def Selecciones(request):

    return render(request, "appmundial/selecciones.html")
