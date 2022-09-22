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
                     print("Volviendo al menú principal")
                     sleep(1)
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
                print("Volviendo al menú principal")
                sleep(3)
                break
        except:
            print("Error, Porfavor, ingrese 1 para continuar o 0 para ir al menú principal.")
    return resul
   