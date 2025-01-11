from django.shortcuts import render, redirect, get_object_or_404
from .models import Pelicula, Videojuego
from .forms import *

def lista_peliculas(request):
    peliculas = Pelicula.objects.all()  # Obtener todas las películas
    return render(request, 'peliculas.html', {'peliculas': peliculas})

def lista_videojuegos(request):
    videojuegos = Videojuego.objects.all()  # Obtener todos los videojuegos
    return render(request, 'videojuegos.html', {'videojuegos': videojuegos})

def agregar_pelicula(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_peliculas')
    else:
        form = PeliculaForm()
    return render(request, 'agregar_pelicula.html', {'form': form})

def agregar_videojuego(request):
    if request.method == 'POST':
        form = VideojuegoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_videojuegos')
    else:
        form = VideojuegoForm()
    return render(request, 'agregar_videojuego.html', {'form': form})

def editar_pelicula(request, pelicula_id):
    pelicula = get_object_or_404(Pelicula, id=pelicula_id)  # Obtener la película por ID
    if request.method == 'POST':
        form = PeliculaForm(request.POST, request.FILES, instance=pelicula)
        if form.is_valid():
            form.save()  # Guardar los cambios en la película
            return redirect('lista_peliculas')  # Redirigir a la lista de películas
    else:
        form = PeliculaForm(instance=pelicula)  # Pre-cargar el formulario con los datos de la película
    
    return render(request, 'editar_pelicula.html', {'form': form, 'pelicula': pelicula})

def editar_videojuego(request, videojuego_id):
    videojuego = get_object_or_404(Videojuego, id=videojuego_id)  # Obtener el videojuego por ID
    if request.method == 'POST':
        form = VideojuegoForm(request.POST, request.FILES, instance=videojuego)
        if form.is_valid():
            form.save()  # Guardar los cambios en el videojuego
            return redirect('lista_videojuegos')  # Redirigir a la lista de videojuegos
    else:
        form = VideojuegoForm(instance=videojuego)  # Pre-cargar el formulario con los datos del videojuego
    
    return render(request, 'editar_videojuego.html', {'form': form, 'videojuego': videojuego})
