from django.shortcuts import render
from django.http import HttpResponse
from .models import lesionados, Jugadores, DT, selecciones
from .forms import JugadoresLesionados, Jugadores_Mundial, Director_tecnico_mundial, seleccion_mundial
# Create your views here.
def index(request):
    return render(request,"appmundial/index.html")


def Jugadores_mundial(request):

    jugadores1 = Jugadores.objects.all()

    datos = {"listajugadores" : jugadores1}

    return render(request, "appmundial/jugadores.html",datos)


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

def buscar_director_tecnico(request):

    if request.GET:
        director = request.GET.get("nombre_dt", "")
        if director == "":
            list_director = []

        else:
            list_director = DT.objects.filter(nombre_dt=director)
        return render(request, "appmundial/busqueda_director.html", {"listaDirector": list_director})
    
    return render(request, "appmundial/busqueda_director.html", {"listaDirector": [] })
    

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




def form_Jugadores(request):

    if request.method == "POST":

        formJugadores = Jugadores_Mundial(request.POST)
        print(formJugadores)

        if formJugadores.is_valid():

            info = formJugadores.cleaned_data

            jugador = Jugadores( nombres_jugador=info["nombre"], apellidos_jugador=info["apellido"], numero_camiseta=info["numeros_remera"], pais_jugador=info["pais_del_jugador"])

            jugador.save()

    else:
        formJugadores = Jugadores_Mundial()

    contexto = { "formJugadores" : formJugadores}
    
    return render(request, "appmundial/form_jugadores_mundial.html", contexto)


def form_director_tecnico(request):

    if request.method == "POST":

        formdirector_tecnico = Director_tecnico_mundial(request.POST)
        print(formdirector_tecnico)

        if formdirector_tecnico.is_valid():

            info = formdirector_tecnico.cleaned_data

            director = DT( nombre_dt=info["nombre_dt"], apellido_dt=info["apellido_dt"], pais_dt=info["pais_dt"], seleccion_representada=info["seleccion_representada"])

            director.save()

    else:
        formdirector_tecnico = Director_tecnico_mundial()

    contexto = { "formdirector_tecnico" : formdirector_tecnico}
    
    return render(request, "appmundial/form_director_tecnico_mundial.html", contexto)



def form_Seleccion(request):

    if request.method == "POST":

        formseleccion = seleccion_mundial(request.POST)
        print(formseleccion)

        if formseleccion.is_valid():

            info = formseleccion.cleaned_data

            seleccion = selecciones( nombre_seleccion=info["nombre_seleccion"], grupo=info["grupo"], num_jugadores_convocados=info["num_jugadores_convocados"], capitan=info["capitan"])

            seleccion.save()

    else:
        formseleccion = seleccion_mundial()

    contexto = { "formseleccion" : formseleccion}
    
    return render(request, "appmundial/form_seleccion_mundial.html", contexto)