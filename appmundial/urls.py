from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="mundial-inicio"),
    path("jugadores/",views.Jugadores, name="mundial-jugadores"),
    path("directores_Tecn/",views.Directores_tecnicos, name="mundial-directores_Tecn"),
    path("selecciones/",views.Selecciones, name="mundial-selecciones"),
    path("lesionados/",views.Lesionados, name="mundial-lesionados"),
    path("subir_lesionado/", views.form_Lesionados, name="mundial-subir-lesionados")
]