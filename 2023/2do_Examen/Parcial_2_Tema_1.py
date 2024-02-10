# -*- coding: utf-8 -*-
import array
import random

def cargar_valores_manual(pvalores_manual,tamano):
    for i in range(tamano):
        valor_manual = 0
        while valor_manual <= 0:
            valor_manual = int(input(f"Ingrese un valor mayor a cero para la posición {i + 1} del vector manual: "))

        pvalores_manual[i] = valor_manual


def cargar_valores_aleatorios(pvalores_aleatorios,tamano):
    for i in range(tamano):
        pvalores_aleatorios[i] = random.randint(1, 100)


def clonar_vectores(pvalores_manual, ppvalores_aleatorios,pvalores_clonados, tamano):
    for i in range(tamano):
        if i % 2 == 0: # Posiciones pares, sumar
            pvalores_clonados[i] = pvalores_manual[i] + ppvalores_aleatorios[i]
        else:   # Posiciones impares, multiplicar
            pvalores_clonados[i] = pvalores_manual[i] * ppvalores_aleatorios[i]



def calcular_promedio(pvalores_clonados,ptam):
    suma=0
    for i in range(0,ptam,1):
        suma = suma + pvalores_clonados[i]

    return suma / ptam

def encontrar_valores_sobre_promedio(pvalores_clonados,ppromedio):
    for valor in pvalores_clonados:
        if valor > ppromedio:
            print(f"El valor {valor} es mayor al promedio {ppromedio}")

def mimain():
    tamano = 5
    valores_manual = array.array('i', [0] * tamano)
    valores_aleatorios = array.array('i', [0] * tamano)
    cargado = False
    clonado = False

    while True:
        print("\nMenú de Opciones:")
        print("1 - Cargar Valores Manual y Aleatoriamente")
        print("2 - Clonar Vectores y ver")
        print("3 - Informar Mínimo por Encima del Promedio")
        print("4 - Salir")
        opcion = input("Elija una opción: ")
        if opcion == "1":
            cargar_valores_manual(valores_manual,tamano)
            cargar_valores_aleatorios(valores_aleatorios,tamano)
            clonado = False
            valores_clonados = array.array('i', [0] * tamano)
            cargado = True
            print("Valores cargados exitosamente.")
            print("Tercer Manual:", valores_manual)
            print("Tercer Aleatorio:", valores_aleatorios)
        elif opcion == "2":
            if cargado == True:
                clonar_vectores(valores_manual, valores_aleatorios,valores_clonados,tamano)
                print("Tercer Manual:", valores_manual)
                print("Tercer Aleatorio:", valores_aleatorios)
                print("Tercer Arreglo:", valores_clonados)
                clonado = True
            else:
                print("hay que cargar primero los valores")
        elif opcion == "3":
            if clonado == True:
                promedioobtenido = calcular_promedio(valores_clonados,tamano)
                print("El promedio es:", promedioobtenido)
                encontrar_valores_sobre_promedio(valores_clonados,promedioobtenido)
            else:
                print("hay que Clonar primero los valores")
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")

mimain()
