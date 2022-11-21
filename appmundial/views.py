from django.shortcuts import render
from django.http import HttpResponse
from .models import lesionados, Jugadores, DT, selecciones
from .forms import JugadoresLesionados
# Create your views here.
def index(request):
    return render(request,"appmundial/index.html")


def Jugadores_mundial(request):

    jugadores1 = Jugadores.objects.all()

    datos = {"listajugadores" : jugadores1}

    return render(request, "appmundial/jugadores.html",datos)


def busqueda_jugador(request):

    return render(request, "appmundial/busqueda_jugador.html")


def buscar(request):    
    
    if request.GET:
        jugador = request.GET.get("respuesta", "")
        if jugador == "":
            lisjugador = []

        else:
            lisjugador = Jugadores.objects.filter(nombres_jugador=jugador)
        return render( request, "appmundial/busqueda_jugador.html", {"listajugadores": lisjugador} )

    return render( request, "appmundial/busqueda_jugador.html", { "listajugadores": []})

def Directores_tecnicos(request):
    director = DT.objects.all()

    datos = { "listasdirectores" : director }

    return render(request, "appmundial/directores_tec.html", datos)

def Selecciones(request):
    seleccion = selecciones.objects.all()

    datos =  { "listasselecciones" : seleccion }

    return render(request, "appmundial/selecciones.html", datos)
    
def Lesionados(request):

    lesion = lesionados.objects.all()

    datos =  { "listaslesionados" : lesion }

    return render(request, "appmundial/lesionados.html",datos)

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
