'''Algoritmo EjMiVector
	Dimension miVector(3)
	Para i <- 1 hasta 3 hacer
		Leer miVector(i)
	FinPara
	para i <- 1 hasta 3 hacer
		Escribir "Ver",miVector(i)
	FinPara
FinAlgoritmo
'''
import array as arr

#Definicion y dimensionamiento
miArreglo = arr.array('i',range(5))

# otra forma de inicializar
# miArreglo = arr.array('i', range(10))
# Otra forma mas
# miArreglo = arr.array('i', [0]*10)
'''

#miArreglo = arr.array('i',[0,0,0,0,0])
viCantElem=len(miArreglo)

miArreglo[2]=999
##Mostrar por pantalla los valores con los que se inicializo
for i in range (0,viCantElem,1):
    print(f'Arreglo[{i}]:{miArreglo[i]}')

##Carga Tradicional Arreglo
for i in range (0,viCantElem,1):
    miArreglo[i]=int(input("Ingrese Valor en miarreglo["+str(i)+']:'))

#print(miArreglo[2:4])


##Mostrar por pantalla
for i in range (0,viCantElem,1):
    print(f'Arreglo[{i}]:{miArreglo[i]}')

#Otra forma pero se me olvidan de esto o
#me lo usan con criterio
'''
for valor in miArreglo:
    print(valor)

for letra in 'Hola':
    print(letra)
acum=0
for numero in '1234':
    acum=acum+int(numero)
    print(acum)
'''