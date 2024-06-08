import array as arr
#Definicion y dimensionamiento
                           #[0,1,2,3,4]
#miArreglo = arr.array('i',range(5))
#miArreglo = arr.array('i',[0,0,0,0,0])
miArreglo = arr.array('i',[0]*6)

#Carga
for i in range (0,6,1):
    miArreglo[i]=int(input(f'Ingrese Valor en miarreglo[{i}]:'))


#Miestra
for i in range (0,6,1):
    print(f'Mi Arreglo[{i}]:{miArreglo[i]}')




#Sacar el promedio
sumaElementos=0
cantElementos=0
for i in range (0,6,1):
    sumaElementos=sumaElementos+miArreglo[i]
    cantElementos=cantElementos+1
promedio=sumaElementos/cantElementos
print(f'El promedio es {promedio}')

