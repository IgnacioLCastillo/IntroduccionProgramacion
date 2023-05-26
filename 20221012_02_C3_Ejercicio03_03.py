import array as arr

#Definicion y dimensionamiento
miArreglo = arr.array('i',range(10))
#miArreglo = arr.array('i',[0,0,0])
viCantElem=len(miArreglo)

##Carga Tradicional Arreglo
for i in range (0,viCantElem,1):
    miArreglo[i]=int(input("Ingrese Valor en miarreglo["+str(i)+']:'))

haymult3 = False
#cont3=0
for i in range (0,viCantElem,1):
    if miArreglo[i]%3==0:
        haymult3=True
       #cont3+=1

if haymult3==0:
    print (" Hay")
else:
    print('No Hay')


'''
if cont3==0:
    print ("No Hay")
else:
    print(f'Hay {cont3} multiplos de tres')
'''