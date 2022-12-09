from django.db import models
from Usuario.models import Usuario as user

# Create your models here.

class Notas(models.Model):
    #Opciones
    estados = (
        ('1','Aprobado'),
        ('2','Desaprobado'),
        ('3','Verificando')
    )
    #Atributos
    idNotas = models.IntegerField(
        primary_key=True,
        unique=True,
    )
    Titulo = models.CharField(
        max_length=45
    )
    descrip = models.CharField(
        max_length=45
    )
    estado = models.CharField(
        max_length=1,
        choices=estados,
        verbose_name='Estado'
    )
    fechCreacion = models.DateField(

    )
    fechCierre = models.DateField(

    )
    idUser = models.ForeignKey(
        user,"idUser", on_delete=models.CASCADE
    )