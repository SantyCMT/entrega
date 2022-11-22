from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="mundial-inicio"),
    path("jugadores/",views.Jugadores_mundial, name="mundial-jugadores"),
    path("jugadores/buscar/", views.buscar, name="mundial-buscar"),
    path("jugadores/agregar/", views.form_Jugadores, name="mundial-jugadores-agregar"),
    path("directores_Tecn/",views.Directores_tecnicos, name="mundial-directores_Tecn"),
    path("directores_Tecn/agregar/", views.form_director_tecnico, name="mundial-directores_Tecn-agregar"),
    path("directores_Tecn/buscar",views.buscar_director_tecnico, name="mundial-directores_Tecn-buscar"),
    path("selecciones/",views.Selecciones, name="mundial-selecciones"),
    path("selecciones/agregar/", views.form_Seleccion, name="mundial-selecciones-agregar"),
    path("lesionados/",views.Lesionados, name="mundial-lesionados"),
    path("subir_lesionado/", views.form_Lesionados, name="mundial-subir-lesionados"),
]