#ingrese 5 numeros y muestre el maximo y el minimo y la posicion de cada uno
cantNum=1
#while cantNum<=5:
for cantNum in range(1,6,1):
    minro=int(input("Ingrese un numero: "))
    if cantNum==1:
        max=minro
        posiMax=cantNum
        min=minro
        posMin=cantNum
    else:
        if minro>max:
            max=minro
            posiMax=cantNum
        else:
            if minro<min:
                min=minro
                posMin=cantNum

    #cantNum+=1

print(f"El maximo es {max} y esta en la posicion {posiMax}")
print(f"El minimo es {min} y esta en la posicion {posMin}")


