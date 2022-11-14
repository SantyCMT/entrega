from django import forms


class JugadoresLesionados(forms.Form):
    
    nombres_jugador = forms.CharField()

    pellidos_jugador = forms.CharField()