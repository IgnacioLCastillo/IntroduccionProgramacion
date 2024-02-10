#ingrese 5 numeros y muestre el minimo de los valores pares y la posicion de cada uno
#El maximo de los impares y la posicion de cada uno

cantNum=1
cantPar=0
cantImp=0

for cantNum in range(1,6,1):
    minro=int(input("Ingrese un numero: "))
    if minro<=0:
        print("Error")
        #continue
    else:
        if minro%2==0:
            cantPar+=1
            if cantPar==1:
                min=minro
                posMin=cantNum
            else:
                if minro<min:
                    min=minro
                    posMin=cantNum
        else:
            cantImp += 1
            if cantImp == 1:
                max = minro
                posMax = cantNum
            else:
                if minro > max:
                    max = minro
                    posMax = cantNum

if cantPar==0:
   print("No hay un minimo establecido porque no se ingresaron numeros pares")
else:
    print(f"El minimo es {min} y esta en la posicion {posMin}")
    #print("El minimo es", min,"y esta en la posicion",posMin)
    #print("El minimo es "+str(min)+" y esta en la posicion "+str(posMin))


if cantImp==0:
   print("No hay un maximo  establecido porque no se ingresaron numeros Impares")
else:
    print(f"El Maximo Impar es {max} y esta en la posicion {posMax}")

