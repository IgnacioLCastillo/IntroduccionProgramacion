import array as arr
#Definicion y dimensionamiento
miArreglo = arr.array('i',range(5))
viCantElem=len(miArreglo)

##Carga Tradicional Arreglo
for i in range (0,viCantElem,1):
    miArreglo[i]=int(input("Ingrese Valor en miarreglo["+str(i)+']:'))

'''
#Busqueda de la primer posic mult de tres
posicM3=-1
for i in range (0,viCantElem,1):
    if miArreglo[i]%3==0:
        posicM3=i
        break
'''
posicM3=-1
i=0
while i< viCantElem and posicM3==-1:
    if miArreglo[i]%3==0:
        posicM3=i
    i=i+1

if posicM3==-1:
    print("NO EXISTE M3")
else:
    print ("La primer posicion M3 es:",posicM3)