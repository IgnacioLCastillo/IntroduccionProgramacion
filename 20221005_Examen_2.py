multAcum = 0
multCont = 0

print(":Seleccione 10 numeros:")
for i in range(1, 11, 1):
    numero = int(input("Ingrese el numero #" + str(i) + ": "))

    if numero <= 0:
        print("Error: Este numero no esta permitido")
        break
    else:

        if i == 1:
            maxNum = numero
            maxUbi = i

        else:
            if numero > maxNum:
                maxNum = numero
                maxUbi = i

        if numero % 3 == 0:
            multAcum = multAcum + numero
            multCont = multCont + 1

print("El maximo valor ingresado es: ", maxNum, "y se encuentra en la posicion: ", maxUbi)
if multAcum == 0:
    print("No hay promedio para informar")
else:
    print("El promedio de multiplos de 3 es: ", multAcum / multCont)