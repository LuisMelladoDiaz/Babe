from django.db import models

class Audiovisual(models.Model):
    titulo = models.CharField(max_length=255)
    puntuacionM = models.DecimalField(max_digits=3, decimal_places=1, default=0)  # Puntuación masculina (0-10)
    puntuacionF = models.DecimalField(max_digits=3, decimal_places=1, default=0)  # Puntuación femenina (0-10)
    galardonado = models.BooleanField(default=False)
    foto = models.ImageField(upload_to='audiovisuals/%Y/%m/%d/', blank=True, null=True, default='audiovisuals/imagen_generica.jpg')
    fecha = models.DateField(blank=True, null=True)

    def media(self):
        """Calcula la media entre puntuacionM y puntuacionF."""
        return (self.puntuacionM + self.puntuacionF) / 2

    def __str__(self):
        return f'Audiovisual: {self.titulo} | Puntuación Media: {self.media()}'

class Pelicula(Audiovisual):
    class Genero(models.TextChoices):
        ACCION = 'Acción'
        DRAMA = 'Drama'
        COMEDIA = 'Comedia'
        ROMCOM = 'Comedia Romántica'
        CIENCIA_FICCION = 'Ciencia Ficción'
        AVENTURA = 'Aventura'
        MISTERIO = 'Misterio'
        ANIMACION = 'Animación'
        MUSICAL = 'Musical'
        HISTORICO = 'Histórico'

    genero = models.CharField(max_length=20, choices=Genero.choices)  # Género de la película
    cine = models.BooleanField(default=False)  # Vista en el cine

    def __str__(self):
        return f'Pelicula: {self.titulo} | Género: {self.genero} | En cine: {self.cine}'

class Videojuego(Audiovisual):
    class Genero(models.TextChoices):
        ACCION = 'Acción'
        AVENTURA = 'Aventura'
        DEPORTE = 'Deporte'
        SIMULACION = 'Simulación'
        RPG = 'RPG'
        ESTRATEGIA = 'Estrategia'
        FANTASIA = 'Fantasía'
        CARRERAS = 'Carreras'
        PUZZLE = 'Puzzle'
        TERROR = 'Terror'
        MUSICAL = 'Musical'
        PLATAFORMAS = 'Plataformas'
        SHOOTER = 'Shooter'


    class Dificultad(models.TextChoices):
        FACIL = 'Fácil'
        MEDIO = 'Medio'
        DIFICIL = 'Difícil'
        MUY_DIFICIL = 'Muy Difícil'

    genero = models.CharField(max_length=20, choices=Genero.choices)  # Género del videojuego
    dificultad = models.CharField(max_length=20, choices=Dificultad.choices)  # Dificultad del videojuego
    horas = models.PositiveIntegerField(default=0)  # Horas jugadas

    def __str__(self):
        return f'Videojuego: {self.titulo} | Género: {self.genero} | Dificultad: {self.dificultad} | Horas jugadas: {self.horas}'