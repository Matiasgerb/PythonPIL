#Solicitar al usuario 2 numeros, y determinar los numeros pares que se encuentren dentro del rango

pares=[]
try:
    numIni= int(input("Ingrese el número inicial: "))
    numFin= int(input("Ingrese el número final: "))
    if (numIni <=numFin):
        for par in range(numIni,numFin+1):
            if(par%2 == 0):
                pares.append(par)
        print("Los números pares dentro de ese rango son: ",pares)
    else:
        print("El primer valor tiene que ser menor o igual al segundo valor ingresado")
except:
    print("Por favor, ingresa solo numeros.")
    


    