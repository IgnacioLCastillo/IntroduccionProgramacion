# -*- coding: utf-8 -*-
#Caractreristicas de las cadenas de caracteres
#Las cadenas de caracteres suelen ser inmutables. Puedes crear nuevas cadenas a partir de las originales, pero no puedes cambiar los caracteres en una cadena existente. Por ejemplo:
#Ordenadas: Los elementos de una cadena están ordenados y se acceden mediante un índice.
#Sintaxis: Se definen mediante comillas simples o dobles, por ejemplo, mi_cadena = "Hola".
#Agregar un carácter: No puedes agregar un carácter a una cadena existente, pero puedes crear una nueva cadena.
#Eliminar un carácter: No puedes eliminar un carácter de una cadena existente, pero puedes crear una nueva cadena.


mi_cadena = "Hola"
# No puedo cambiar un carácter en mi_cadena, pero puedo crear una nueva cadena.
print(mi_cadena[0]) #ven que puedo mosrtar una posic del string porque es ordenado?
#mi_cadena[0] = "h" #ven que no puedes cambiar un carácter en mi_cadena, porque no es mutable
#Y si quisiese cambiarlo y transformalo en mutable que puedo hacer??
#Ya se.... lo paso a lista que si es lo puedo cambiar a lista y luego lo vuelvo a pasar a string
#Y como lo paso a lista??
micadena=input('Ingrese una cadena:')
#micadenaenformatolista= list(mi_cadena)
print('Muestro la lista cruda:', micadena)

#Itero haciendo honor a el concepto de que las cadenas son ordenadas
for i in range(0,len(micadena),1):
    print('Letra x letra usando posicion:',micadena[i])
#Itero haciendo valer la capacidad del for que itera sobre listas o colecciones de valores
for letra in micadena:
    print('Letra x letra:', letra)

#micadena[0] = "h" #No puedes cambiar un carácter en mi_cadena, pero puedes crear una nueva cadena.
