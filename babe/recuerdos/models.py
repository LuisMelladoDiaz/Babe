from django.db import models

class Recuerdo(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    fecha = models.DateField()
    
    def __str__(self):
        return self.titulo

class ArchivoRecuerdo(models.Model):
    recuerdo = models.ForeignKey(Recuerdo, related_name="archivos", on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='recuerdos/')
    tipo = models.CharField(max_length=10, choices=[('foto', 'Foto'), ('video', 'Video')])

    def __str__(self):
        return f"{self.recuerdo.titulo} - {self.tipo}"
