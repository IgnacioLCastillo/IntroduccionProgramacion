# -*- coding: utf-8 -*-
'''Tuplas en Python: Una tupla es una secuencia inmutable de elementos. Una vez que creas una tupla, no puedes modificar sus elementos. Por ejemplo:

Inmutables: A diferencia de las listas, las tuplas son inmutables, lo que significa que no se pueden modificar después de su creación.
Ordenadas: Los elementos de una tupla están ordenados y se acceden mediante un índice.
Permite elementos duplicados: Puede contener elementos duplicados.
Sintaxis: Se definen mediante paréntesis, por ejemplo, mi_tupla = (1, 2, 3).
'''
'''
mi_tupla = (1, 2, 3)
# No se pueden modificar los elementos existentes de la tupla, tendrías que crear una nueva tupla si deseas cambios.
#Cadenas de caracteres en la mayoría de los lenguajes: Las cadenas de caracteres suelen ser inmutables. Puedes crear nuevas cadenas a partir de las originales, pero no puedes cambiar los caracteres en una cadena existente. Por ejemplo:

print('Aca lo muestro solito',mi_tupla[0])#Son ordenadas
#mi_tupla[0]=2 #No se pueden modificar los elementos existentes de la tupla, tendrías que crear una nueva tupla si deseas cambios.

for elemento in mi_tupla:
    print(elemento)

for i in range(len(mi_tupla)):
    print(mi_tupla[i])

'''
print (int('1'))
mi_cadena = "Hola"
# No puedes cambiar un carácter en mi_cadena, pero puedes crear una nueva cadena.
print(mi_cadena[0]) #ven que puedo mosrtar una posic del string porque es ordenado?
#mi_cadena[0] = "h" #ven que no puedes cambiar un carácter en mi_cadena, porque no es mutable
#Y si quisiese cambiarlo y transformalo en mutable que puedo hacer??
#Ya se.... lo paso a lista que si es lo puedo cambiar a lista y luego lo vuelvo a pasar a string
#Y como lo paso a lista??
micadenaenformatolista=list(mi_cadena)
print('Muestro la lista cruda:', micadenaenformatolista)
for letra in micadenaenformatolista:
    print('Letra x letra:', letra)
for i in range(len(micadenaenformatolista)):
    print('Letra x letra usando posicion:',micadenaenformatolista[i])

micadenaenformatolista[0] = "h" #No puedes cambiar un carácter en mi_cadena, pero puedes crear una nueva cadena.

for letra in micadenaenformatolista:
    print('Letra x letra:', letra)

#Como hago para que esto se vuelva un string nuevamente??
#Ya se... le paso la lista a el join y vinculo cada elemento con su vecino con el join
mi_cadena = "".join(micadenaenformatolista)
print('Corregimos la majuscula x minuscula y aca tenemos el string mutado',mi_cadena)

import random
lista = ["Hola", "mundo", "en", 'ff','dsasa']
elemnto=random.randint(1, len(lista))
print(lista[elemnto])

mi_cadena = "|".join(lista)
print(mi_cadena)
