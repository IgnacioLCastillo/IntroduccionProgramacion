# -*- coding: utf-8 -*-
# Ahora vamos a definir un set
# Un set es una colección desordenada de elementos únicos
# No se puede acceder a un elemento por su índice
# No se puede modificar un elemento por su índice
# No se puede agregar un elemento por su índice
# No se puede eliminar un elemento por su índice

'''
Mutables: Los conjuntos son mutables, lo que significa que los elementos pueden agregarse o eliminarse.
No ordenados: Los elementos de un conjunto no están ordenados y no se pueden acceder mediante un índice.
No permite elementos duplicados: Un conjunto no puede contener elementos duplicados.
Sintaxis: Se definen mediante llaves o la función set(), por ejemplo, mi_conjunto = {1, 2, 3}.
'''

conjunto= {"rojo", "azul", "amarillo","rojo"}
print(conjunto)


import array as arr

miArreglo = arr.array('i', [2, 3, 4, 3, 2, 2, 3, 7, 8, 9])

print(miArreglo[0])
for elemento in miArreglo:
    print ("Del Arreglo",elemento)


miconjunto=set(miArreglo)
#print(miconjunto[0])
for elemento in miconjunto:
    print ('Del conjunto:',elemento)


