import array as arr

#Definicion y dimensionamiento
miArreglo = arr.array('i',range(10))
#miArreglo = arr.array('i',[0,0,0])
viCantElem=len(miArreglo)

##Carga Tradicional Arreglo
for i in range (0,viCantElem,1):
    miArreglo[i]=int(input("Ingrese Valor en miarreglo["+str(i)+']:'))
contPar=0
sumoPar=0
for i in range (0,viCantElem,1):
    if miArreglo[i]%2==0:
        sumoPar=sumoPar+miArreglo[i]
        contPar+=1

print ("El promedio de los pares es",sumoPar/contPar)