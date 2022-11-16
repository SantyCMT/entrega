from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="mundial-inicio"),
    path("jugadores/",views.Jugadores_mundial, name="mundial-jugadores"),
    path("Buscar_jugador/resultados/", views.busqueda_jugador, name="mundial-busqueda-jugador"),
    path("buscar/", views.buscar, name="mundial-buscar"),
    path("directores_Tecn/",views.Directores_tecnicos, name="mundial-directores_Tecn"),
    path("selecciones/",views.Selecciones, name="mundial-selecciones"),
    path("lesionados/",views.Lesionados, name="mundial-lesionados"),
    path("subir_lesionado/", views.form_Lesionados, name="mundial-subir-lesionados"),
]