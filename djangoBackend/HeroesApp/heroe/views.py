#REST IMPORT
from email.policy import HTTP
from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#Models import
from heroe.models import Hero

#serializers imports
from heroe.serializer import HeroSerial

#Helpers
from heroe.helpers.heroErrors import hayHero

# Create your views here.
class HeroAPIView(APIView):
    
    def get(self,request):
        #Retorna lista con todos los heroes almacenados en nuestra base
        #print(f'REQUEST --->{request}')

        #Base de datos 
        heroes= Hero.objects.all() # Recibe todos los Heroes de la base de datos

        heroesSerial= HeroSerial(heroes, many=True) #hace la conversion de un objeto a un JSon.

        return Response(
            data = heroesSerial.data,
            status = status.HTTP_200_OK
        )

class CreateAPIView(APIView):
        
        
    def post(self,request):
        #Crea un nuevo registro /heroe
        print("ESTAMOS EN UN METODO POST")

        serialazer = HeroSerial(data=request.data, many =True) #Many permite crear varios heroes al mismo tiempo

        if(serialazer.is_valid()):
            serialazer.save()

            data = {
                    'menssage' : 'el heroe fue creado con exito'
                }
            return Response(
                data=data,
                status = status.HTTP_201_CREATED
            )
            
        return Response(
            data = serialazer.errors,
            status = status.HTTP_400_BAD_REQUEST
        )

class HeroDetailsAPIView(APIView):
    
    def get(self,request,pk):


        try:
            heroe= Hero.objects.get(pk=pk)

            heroeSerial= HeroSerial(heroe) 

            return Response(
                data = heroeSerial.data,
                status = status.HTTP_200_OK
            )
        except:
           data = {
                'menssage' : 'Heroe no encontrado'
            } 

        return Response(
            data = data,
            status = status.HTTP_400_BAD_REQUEST
        )

    def put(self,request,pk):
        heroe= hayHero(pk)
        if(heroe[0]):
            heroeSerial= HeroSerial(heroe[1], data=request.data) 

            if(heroeSerial.is_valid()):
                heroeSerial.save()
            
            data = {
                    'menssage' : 'el heroe fue modificado con exito'
                } 

            return Response(
                data = heroeSerial.data,
                status = status.HTTP_200_OK
            )
        return Response(
            data = heroeSerial.errors,
            status = status.HTTP_400_BAD_REQUEST
        ) 

    def delete(self,request,pk):
        heroe= Hero.objects.get(pk=pk)
        
        heroe.delete()

        data = {
                'menssage' : 'el heroe fue eliminado de forma'
            } 
        
        return Response(
            data = data,
            status = status.HTTP_200_OK
        )