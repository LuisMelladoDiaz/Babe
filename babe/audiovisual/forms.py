from django import forms
from .models import Pelicula, Videojuego

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['titulo', 'puntuacionM', 'puntuacionF', 'galardonado', 'foto', 'fecha', 'genero', 'cine']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }

class VideojuegoForm(forms.ModelForm):
    class Meta:
        model = Videojuego
        fields = ['titulo', 'puntuacionM', 'puntuacionF', 'galardonado', 'foto', 'fecha', 'genero', 'dificultad', 'horas']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }
