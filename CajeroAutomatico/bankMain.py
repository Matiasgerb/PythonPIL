
from time import sleep
from bankFunc import deposito,extraccion

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
                dineroActual += extraccion(dineroActual)
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