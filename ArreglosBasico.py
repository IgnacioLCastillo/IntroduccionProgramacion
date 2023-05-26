import array as arr

#Definicion y dimensionamiento
miArreglo = arr.array('i',range(6))

##print(list(range(10)))

viCantElem=len(miArreglo)
##Carga Tradicional Arreglo
for i in range (0,viCantElem,1):
    miArreglo[i]=int(input("Ingrese Valor en miarreglo["+str(i)+']:'))

##Update o Inser
#miArreglo.insert(1,104)
#miArreglo.insert(6,103)

viCantElem=len(miArreglo)
##Mostrar por pantalla
for i in range (0,viCantElem,1):
    print(f'Arreglo[{i}]:{miArreglo[i]}')

#Otra forma
for valor in miArreglo:
    print(valor)

for letra in 'Hola':
    print(letra)

