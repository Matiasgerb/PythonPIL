from enum import unique
from random import choices
from secrets import choice
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Hero(models.Model):
    #Opciones
    universo_choice = (
        ('1','Marvel'),
        ('2','DC')
    )
    #Atributos
    name = models.CharField (
        max_length= 12, 
        unique=True,
        verbose_name='Nombre'
    )
    edad = models.IntegerField(

    )
    universo= models.CharField(
        max_length=1,
        choices=universo_choice,
        verbose_name='Universo'

    )

    def __str__(self):
        return self.name