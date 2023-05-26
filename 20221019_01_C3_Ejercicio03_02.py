import array as arr

#Definicion y dimensionamiento
miArregloOriginal = arr.array('i',range(5))
miArregloInverso = arr.array('i',[0,0,0,0,0])

viCantElem=len(miArregloOriginal)

##Carga Tradicional Arreglo
for h in range (0,viCantElem,1):
    miArregloOriginal[h]=int(input("Ingrese Valor en miarreglo["+str(h)+']:'))

'''
# Otra forma de cargar el arreglo pero utilizando un while
t=0
while t<viCantElem:
    miArregloOriginal[t]=int(input("Ingrese Valor en miarreglo[t="+str(t)+']:'))
    t=t+1
'''

j=viCantElem-1
for i in range (0,viCantElem,1):
    miArregloInverso[j-i]=miArregloOriginal[i]
    ##print(i,j-i)


for i in range (0,viCantElem,1):
    print(f'Arreglo[{i}]:{miArregloInverso[i]}')

'''
##No es lo que pide el 03-02 pero
##Si solo necesitaria mostrarlo inversamente este sería el camino
for i in range (viCantElem-1,-1,-1):
    print(f'Arreglo[{i}]:{miArregloOriginal[i]}')
'''

