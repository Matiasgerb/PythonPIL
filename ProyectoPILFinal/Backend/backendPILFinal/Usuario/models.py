from django.db import models



# Create your models here.
class Usuario(models.Model):

    
    #Atributos
        idUser = models.IntegerField(
            primary_key=True,
            unique=True
        )
        email = models.CharField(
            max_length=60
            
        )
        password = models.CharField(
            max_length=10
        )
        userName = models.CharField(
            max_length=20
        )
        nombre = models.CharField(
            max_length=20
        )
        apellido =models.CharField(
            max_length=20
        )
        token= models.CharField(
            max_length=30,
            unique=True
        )



