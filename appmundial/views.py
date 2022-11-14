from django.shortcuts import render
from django.http import HttpResponse
from appmundial.models import lesionados
from appmundial.forms import JugadoresLesionados
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

        formulario = JugadoresLesionados

        if formulario.is_valid:

            info=formulario.cleaned_data

            lesion = lesionados(nombres_jugador=info["nombres_jugador"],apellidos_jugador=info["apellidos_jugador"])
        
            lesion.save()
        
            return render(request,"appmundial/base.html")
    else:
        formulario = JugadoresLesionados()

    
    return render(request, "appmundial/form_lesionados.html", {"formulario": formulario})
