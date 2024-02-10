# -*- coding: utf-8 -*-
# Teoria - Diccionarios

# Ahora vamos a definir un diccionario
# Un diccionario es una colección desordenada de elementos que están indexados por claves
# No se puede acceder a un elemento por su índice
# No se puede modificar un elemento por su índice
# Los elementos no están ordenados
# Los elementos no son únicos
# Los elementos son inmutables
# Los elementos son de cualquier tipo de dato

diccionario = {"rojo":"red", "azul":"blue", "amarillo":"yellow"}

# Mostramos
print("El color rojo en inglés es:", diccionario["rojo"])
print("El color azul en inglés es:", diccionario["azul"])
print("El color amarillo en inglés es:", diccionario["amarillo"])

semana = {1:"Lunes", 2:"Martes", 3:"Miércoles", 4:"Jueves", 5:"Viernes", 6:"Sábado", 7:"Domingo"}
print (semana[1])
print (semana[2])

# Agregar un elemento al diccionario. Puedo modificarlos
semana[1] = "Monday"
print (semana[1])

# Ahora vamos a definir un set
# Un set es una colección desordenada de elementos únicos
# No se puede acceder a un elemento por su índice
# No se puede modificar un elemento por su índice
# No se puede agregar un elemento por su índice
# No se puede eliminar un elemento por su índice
conjunto= {"rojo", "azul", "amarillo"}
print(conjunto)
mi_conjunto = {3, 1, 2, 4, 5}  # Los elementos están ordenados y no hay duplicados.
print('Conjunto',mi_conjunto)
palabra={'h','o','l','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a'}
print(palabra)


lista = [5, 1, 1, 3, 4, 4, 5]
conjunto = set(lista)
# conjunto ahora contiene {1, 2, 3, 4, 5}, sin duplicados
print(conjunto)

# Ahora vamos a definir una tupla
# Una tupla es una colección ordenada e inmutable de elementos
# No se puede acceder a un elemento por su índice
# No se puede modificar un elemento por su índice
# No se puede agregar un elemento por su índice
# No se puede eliminar un elemento por su índice
# Los elementos pueden ser de cualquier tipo de dato
# Los elementos pueden ser duplicados
# Los elementos son inmutables
tupla = ("rojo", "azul", "amarillo")
print(tupla)


# Ahora vamos a definir una lista
# Una lista es una colección ordenada de elementos
# Se puede acceder a un elemento por su índice
# Se puede modificar un elemento por su índice
# Se puede agregar un elemento por su índice
# Se puede eliminar un elemento por su índice
# Los elementos pueden ser de cualquier tipo de dato
# Los elementos pueden ser duplicados
# Los elementos son mutables
lista = ["rojo", "azul", "amarillo"]
print(lista)


