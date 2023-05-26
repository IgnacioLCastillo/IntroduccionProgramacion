import array as arr
#Definicion y dimensionamiento
miArreglo = arr.array('i',range(5))
miArregloDoble = arr.array('i',range(5))
viCantElem=len(miArreglo)

##Carga Tradicional Arreglo
for i in range (0,viCantElem,1):
    miArreglo[i]=int(input("Ingrese Valor en miarreglo["+str(i)+']:'))

#Paso doble valor la posicion impar

for i in range (0,viCantElem,1):
    if i%2!=0:
        miArregloDoble[i]=miArreglo[i]*2
    else:
        miArregloDoble[i] = miArreglo[i]

for i in range (0,viCantElem,1):
    print(f'Arreglo Original[{i}]:{miArreglo[i]}')

for i in range (0,viCantElem,1):
    print(f'Arreglo doble[{i}]:{miArregloDoble[i]}')