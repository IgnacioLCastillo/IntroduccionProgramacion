x = int(input("Ingrese un numero entero: "))
contMultiDe4 = 0
acumMultiDe4 = 0
suma = 0
if x > 0:
    print("Algoritmo sin actividad")
else:
    for i in range(x,0 , -1):
        suma += i
        print("Los valores comprendidos entre 1 y su numero son: ", i)
        if i %4==0:
            contMultiDe4 = contMultiDe4 + 1

    print("La cantidad de multiplos de 4 en ese rango es de: ",contMultiDe4)
    print("El promedio de todos los valores del rango es de: ",suma/x)

