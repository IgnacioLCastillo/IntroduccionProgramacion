import array as arr
#Definicion y dimensionamiento
miArreglo = arr.array('i',range(5))
viCantElem=len(miArreglo)

##Carga Tradicional Arreglo
for i in range (0,viCantElem,1):
    miArreglo[i]=int(input("Ingrese Valor en miarreglo["+str(i)+']:'))

#Busqueda del Maximo y Minimo
for i in range (0,viCantElem,1):
    if i==0:
       miMax=miArreglo[i]
       posicMax=i
       miMin = miArreglo[i]
       posicMIn = i
    else:
        if miArreglo[i]>miMax:
            miMax = miArreglo[i]
            posicMax = i
        else:
            if miArreglo[i]<miMin:
                miMin = miArreglo[i]
                posicMin = i


print (f"El maximo es {miMax} y esta en la posicion {posicMax} y el minimo es {miMin} y esta en la posicion {posicMin}")