from django.db import models

# Create your models here.

class Trabajo(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombreTrabajo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombreTrabajo, self.descripcion)