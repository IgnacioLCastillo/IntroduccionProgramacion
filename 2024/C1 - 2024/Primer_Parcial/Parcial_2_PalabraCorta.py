# -*- coding: utf-8 -*-

def contar_vocales(palabra):
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in palabra:
        if letra in vocales:
            contador += 1
    return contador

# Inicializar variables
total_longitud = 0
palabra_max_vocales = ""
cont_palabras_cortas = 0
longitud_minima = 3  # Longitud mínima permitida
max_intentos_palabras_cortas = 3  # Máximo de intentos para palabras cortas
intentos_palabras_cortas = 0  # Contador de intentos para palabras cortas



# Solicitar palabras al usuario continuamente
while True:
    palabra = input("Ingresa una palabra: ")
    print(f"Tamaño:{len(palabra)}")
    # Verificar si la palabra es demasiado corta
    if len(palabra) < longitud_minima:
        intentos_palabras_cortas += 1
        print(f"Palabra demasiado corta. No está permitido. Te quedan {max_intentos_palabras_cortas-intentos_palabras_cortas} intentos")


        if intentos_palabras_cortas >= max_intentos_palabras_cortas:
            print("Has ingresado demasiadas palabras cortas. Finalizando.")
            break
    else:
        # Incrementar el contador de palabras válidas
        cont_palabras_cortas += 1

        # Calcular el total de longitud de palabras ingresadas
        total_longitud += len(palabra)

        # Encontrar la palabra con más vocales

        num_vocales = contar_vocales(palabra)

        if num_vocales > contar_vocales(palabra_max_vocales):
            palabra_max_vocales = palabra

# Calcular el promedio de longitud de palabras ingresadas
if cont_palabras_cortas > 0:
    promedio_longitud = total_longitud / cont_palabras_cortas
else:
    promedio_longitud = 0

# Mostrar resultados
print(f"Promedio de longitud de palabras ingresadas: {promedio_longitud:.2f}")
print(f"Palabra con más vocales: {palabra_max_vocales}")
