from django.shortcuts import render
from django.http import HttpResponse
from .models import lesionados, Jugadores
from .forms import JugadoresLesionados
# Create your views here.
def index(request):
    return render(request,"appmundial/base.html")


def Jugadores(request):

    return render(request, "appmundial/jugadores.html")




def busqueda_jugador(request):

    return render(request, "busqueda_jugador.html")


def buscar(request):
    respusta = request.GET["nombres_jugador"]
    jugadores = Jugadores.object.filter(nombre_icontains=nombres_jugador)
    return render(request, "appmundial/resultados_busqueda_jugador.html", {"jugadores": jugadores})

def Directores_tecnicos(request):

    return render(request, "appmundial/directores_tec.html")

def Selecciones(request):

    return render(request, "appmundial/selecciones.html")
    
def Lesionados(request):

    return render(request, "appmundial/lesionados.html")

def form_Lesionados(request):

    if request.method == "POST":

        miFormulario = JugadoresLesionados(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            info = miFormulario.cleaned_data

            lesion = lesionados(nom_jug_les=info["nombres"], ape_jug_les=info["apellidos"])
        
            lesion.save()

    else:
        miFormulario = JugadoresLesionados()


    contexto = { "miFormulario" : miFormulario }
         
    return render(request, "appmundial/form_lesionados.html", contexto)
