# Realizar un menu de un cajero automatico, donde el usuario pueda
# escoger entre alguna de las siguientes opciones, deposito, extracción
# transferencia, y salir.
from time import sleep



def deposito():
    cont=1
    resul = 0
    while cont==1:
        try:
            opDepo=int(input("Ingrese 1 para continuar o 0 para salir: "))
            try:
                if(opDepo==1):
                    a = float(input("Ingrese la cantidad a depositar: "))
                    resul = resul + a
                if(opDepo==0):
                     print("Gracias por confiar en nosotros...")
                     print("Volviendo al menú principal")
                     sleep(3)
                     break
            except:
                print("ERROR, Utilice solo números")
        except:
            print("Error, ingrese una opción valida")
    return resul

def extraccion(dineroActual):
    cont=0
    resul = 0
    while cont==0:
        try:
            opExtra=int(input("Ingrese 1 para continuar o 0 para salir: "))
            if(opExtra==1):
                try:
                    extraccion = float(input("Ingrese el dinero a extraer: "))
                    if(dineroActual>=extraccion):
                        resul = resul - extraccion
                    elif(dineroActual<extraccion):
                        print("No cuenta con el saldo suficiente para realizar la operación")
                        print("Hay: $",dineroActual," disponible para retirar")
                except:
                    print("ERROR, solo utilice números.")
            if(opExtra==0):
                print("Gracias por confiar en nosotros...")
                print("Volviendo al menú principal")
                sleep(3)
                break
        except:
            print("Error, Porfavor, ingrese 1 para continuar o 0 para ir al menú principal.")
    return resul
   
dineroActual = 0
cont=0
while cont==0:
    print("1 - Deposito")
    print("2 - Extracción")
    print("3 - Consultar saldo")
    print("4 - Salir")
    try:
        operacion=int(input("Ingrese una opción: "))
        if(operacion<=5):
            if(operacion==1):
                dineroActual += deposito()
            if(operacion==2):
                dineroActual+=extraccion(dineroActual)
            if(operacion==3):
                print("Hay disponible en la cuenta: ",dineroActual)
            if(operacion==4):
                print("Gracias por confiar en nosotros ")
                print("Finalizando programa...")
                sleep(3)
                break
        else:
            print("No existe dicha operación")
    except:
        print("ERROR, operación no valida")