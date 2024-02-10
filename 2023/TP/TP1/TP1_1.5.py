# -*- coding: utf-8 -*-
# Función para calcular el promedio y el máximo de números ingresados

def mimenu():
    print("Selecciona una opción:")
    print("1. Procesamiento de Números")
    print("2. Procesamiento de Palabras")
    print("3. Salir")
    opcionmenu = int(input("Ingrese una opción: "))
    return opcionmenu

def procesar_numeros():
    cantnumero = 0
    suma = 0
    mimaximo = 0
    while True:
        num = int(input("Ingresa un número entre 1 y 10 (o un número fuera de rango para finalizar): "))

        if 1 <= num <= 10:
            cantnumero += 1
            suma += num
            if num > mimaximo:
                mimaximo = num
        else:
            break

    if cantnumero > 0:
        promedio = suma / cantnumero
        print(f"Promedio de los números ingresados: {promedio}")
        print(f"Número máximo ingresado: {mimaximo}")
    else:
        print("No se ingresaron números válidos.")


# Función para contar las vocales en una palabra

def contar_vocales(palabra):
    vocales = 0
                {p,e,r,r,o}
    for letra in palabra:
        if letra.lower() in 'aeiouáéíóú':
            vocales += 1
    return vocales


# Función para contar palabras con más de 2 vocales
def procesar_palabras():
    palabras_con_mas_de_2_vocales = 0

    while True:
        palabra = input("Ingresa una palabra (o '*' para finalizar): ")

        if palabra == '*':
            break

        # Contar vocales en la palabra
        vocales = contar_vocales(palabra)

        if vocales > 2:
            palabras_con_mas_de_2_vocales += 1

    print(f"Total de palabras con más de 2 vocales: {palabras_con_mas_de_2_vocales}")


# Función principal que maneja el menú
def udfMain():
    while True:

        opcion = mimenu()

        if opcion == 1:
            procesar_numeros()
        elif opcion == 2:
            procesar_palabras()
        elif opcion == 3:
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida")


# ----------------Are global---------------
udfMain()
