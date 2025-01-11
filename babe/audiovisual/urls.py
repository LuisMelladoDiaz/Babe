from django.urls import path
from . import views

urlpatterns = [
    path('peliculas/', views.lista_peliculas, name='lista_peliculas'),
    path('videojuegos/', views.lista_videojuegos, name='lista_videojuegos'),
    path('agregar_pelicula/', views.agregar_pelicula, name='agregar_pelicula'),
    path('agregar_videojuego/', views.agregar_videojuego, name='agregar_videojuego'),
    path('editar_pelicula/<int:pelicula_id>/', views.editar_pelicula, name='editar_pelicula'),
    path('editar_videojuego/<int:videojuego_id>/', views.editar_videojuego, name='editar_videojuego'), 
]
