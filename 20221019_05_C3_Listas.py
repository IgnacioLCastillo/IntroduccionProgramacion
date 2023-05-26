# Teoría: listas y matrices

"""# Crear una lista
lista = [1, 2, 3, 4, "Hola", 2.4, True, False]
tamanio = len(lista)
print("Tamaño de la lista:", tamanio)

# Posiciones
print("Primer elemento de la lista:", lista[0])

ultima_posicion = tamanio - 1
print("El último elemento de la lista es:", lista[ultima_posicion])

# Slicing
print("Slicing, ultimo elemento:", lista[-1])
print("Slicing, primer elemento:", lista[-8])
print("Slicing, ver todos los elementos:", lista[:])
print("Slicing, ver todos los elementos:", lista[0:])
print("Slicing, ver todos los elementos:", lista[0:8])

# Dar vuelta una lista
print("Slicing, dada vuelta:", lista[::-1])

# Propiedades
# Iteración
texto = ["Hola","mi nombre", "es", "Facundo"]
for palabra in texto:
    print(palabra + " ", end="")

print("-----------")
for palabra in range(len(texto)):
    print(f"Posicion {palabra} - Palabra {texto[palabra]}")

# Ordenar una lista
lista_desordenada = [2,6,21,8,25,3,8,-123]
print("Lista desordenada:", lista_desordenada)
lista_ordenada = sorted(lista_desordenada, reverse=True)
print("Lista ordenada:", lista_ordenada)"""

# Añadir elemtos
# Usando append
lista_vacia = []
print("Lista vacia:", lista_vacia)
lista_vacia.append(1)
lista_vacia.append(2)
lista_vacia.append(3)
print("Lista con datos:", lista_vacia)

# Usando insert
lista_vacia.insert(1, 4)
print("Lista con insert:", lista_vacia)

# Usando extend
lista_vacia.extend([5, 6, 7])
print("Lista con extend:", lista_vacia)

# Eliminar datos con pop
capturar = lista_vacia.pop(0)
print("Lista nueva con pop:", lista_vacia)
print("Y lo capturé aquí:", capturar)

# Eliminar con del
del lista_vacia[0]
print("Eliminado con del:", lista_vacia)

# Modificar
lista_vacia[-1] = 999
print("Lista modificada:", lista_vacia)

# Buscar
posicion = lista_vacia.index(999)
print("La posición de 999 es:", posicion)