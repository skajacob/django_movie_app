"""Movies app models"""

from tkinter import CASCADE
from django.db import models


class Movie(models.Model):
    """Movie models for movies app"""
    name = models.CharField(max_length=255)
    director= models.ForeignKey("Director", on_delete=models.CASCADE)
    release_date = models.DateField(blank=True, null=True)
    created_at =  models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Director(models.Model):
    """Director of a movie"""
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    brithday = models.DateField(blank=True, null=True)


    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name




#Migraciones:
# * Crear la migracion(¿que hace? prepara la consulta de SQL)
# * Aplicar la migracion(Ejecutar la consulta de SQL)