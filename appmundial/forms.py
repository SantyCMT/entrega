from django import forms


class JugadoresLesionados(forms.Form):
    
    nombres = forms.CharField(max_length=30)
    apellidos = forms.CharField(max_length=30)