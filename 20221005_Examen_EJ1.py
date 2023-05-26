numeroX = int(input("Ingrese un número: "))
numeroY = int(input("Ingrese un número mayor: "))
contMult = 0
sumTotal = 0
cantVueltas = 0
if numeroX < numeroY:
    for i in range(4, 11 ,1):
        print(i)
        sumTotal += i
        cantVueltas += 1

        if i % 2 == 0:
            contMult = contMult + 1

    print("Cantidad de múltiplos de 2: ", contMult)
    print("Promedio: ", sumTotal / cantVueltas)

else:
    print("Algoritmo sin actividad")


