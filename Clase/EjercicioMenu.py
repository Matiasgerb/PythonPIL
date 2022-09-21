#Realizar un menu de un cajero automatico, donde el usuario pueda
#escoger entre alguna de las siguientes opciones, deposito, extracción
#transferencia, y salir.
operacion=0
while operacion<5:
    print("1 - Depositos")
    print("2 - Extracción")
    print("3 - Transferencia")
    print("4 - Salir")
    try:
        operacion= int (input("Seleccione la operación a realizar: "))
        if(operacion>0 and operacion<=4):
            if(operacion==1):
                depoInsert=float(input("Ingrese la cantidad a depositar: "))
                print("Usted ingreso: ", depoInsert)
            if(operacion==2):
                extra=float(input("Indique cuanto desea extraer: "))
                print("Usted extrajo: ",extra)
            if(operacion==3):
                transf=float(input("Ingrese el monto a transferir: "))
                print("Usted transfirio: ",transf)
            if(operacion==4):
                print("Saliste del programa")
                break
        else:
            print("Por favor, ingresa una operación del 1 al 4")
    except:
        print("Fuera de Rango, por favor ingresar una operación valida.")
        break
