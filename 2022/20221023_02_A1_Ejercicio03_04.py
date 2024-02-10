import array as arr
#Definicion y dimensionamiento
miArreglo = arr.array('i',range(10))
#miArreglo = arr.array('i',[0,0,0,0,0])
viCantElem=len(miArreglo)
sum=0

##Carga Tradicional Arreglo
for i in range (0,viCantElem,1):
    miArreglo[i]=int(input("Ingrese Valor en miarreglo["+str(i)+']:'))

#Promedio de los valores pares del arreglo
contPar=0
for i in range (0,viCantElem,1):
    if miArreglo[i]%2==0:
        sum=sum+miArreglo[i]
        contPar+=1


print (f"Lo acumulado fue{sum} y dividi por {contPar}. Promedio fue {sum/contPar}")

