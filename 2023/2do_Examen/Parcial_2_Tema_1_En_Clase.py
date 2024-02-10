# -*- coding: utf-8 -*-
import array
import random

def udf_cargar_valores_manual(parreglo_manual,ptamano):
    for i in range(ptamano):
        valor_manual = 0
        while valor_manual <= 0:
            valor_manual = int(input(f"Ingrese un valor mayor a cero para la posición {i + 1} del vector manual: "))

        parreglo_manual[i] = valor_manual

def udf_miPromedio(pvalores_clonados,ptam):
    suma=0
    for i in range(0,ptam,1):
        suma = suma + pvalores_clonados[i]

    return suma / ptam

def udf_informar_encima_promedio(pvalores_clonados,ptam):
    mipromedio = udf_miPromedio(pvalores_clonados,len(pvalores_clonados))
    for i in range(0,ptam,1):
        if pvalores_clonados[i] > mipromedio:
            print(f"El valor {pvalores_clonados[i]} es mayor al promedio {mipromedio}")

def udf_cargar_valores_aleatorios(pvalores_aleatorios,ptamano):
    for i in range(ptamano):
        pvalores_aleatorios[i] = random.randint(1, 100)

    print("Valores cargados exitosamente.")

def udf_mostrar_vector(pvector,ptam):
    for i in range(0,ptam,1):
        print(f"Posición [{i}] = {pvector[i]}")

def udf_Clonar_Vector(pvalores_manual, pvalores_aleatorios,pvalores_clonado,ptam):
    for i in range(ptam):
        if i % 2 == 0: # Posiciones pares, sumar
            pvalores_clonado[i] = pvalores_manual[i] + pvalores_aleatorios[i]
        else:   # Posiciones impares, multiplicar
            pvalores_clonado[i] = pvalores_manual[i] * pvalores_aleatorios[i]

    print("Valores Clonados exitosamente.")

def mimain():
    tamano = 5
    valores_manual = array.array('i', [1] * tamano)
    valores_aleatorios = array.array('i', [0] * tamano)
    valores_clonado = array.array('i', [0] * tamano)
    bandcargado = False
    bandclonado = False

    while True:
        print("\nMenú de Opciones:")
        print("1 - Cargar Valores Manual y Aleatoriamente")
        print("2 - Clonar Vectores y ver")
        print("3 - Informar valores Encima del Promedio")
        print("4 - Salir")
        opcion = input("Elija una opción: ")
        if opcion == "1":
            udf_cargar_valores_manual (valores_manual, tamano)
            udf_cargar_valores_aleatorios(valores_aleatorios,tamano)
            bandcargado= True
            print("*******Verificacion Vector Manual*******")
            udf_mostrar_vector(valores_manual,tamano)
            print("*******Verificacion Vector Aleatoria*******")
            udf_mostrar_vector(valores_aleatorios,tamano)
        elif opcion == "2":
           if bandcargado == True:
               udf_Clonar_Vector(valores_manual, valores_aleatorios, valores_clonado, tamano)
               udf_mostrar_vector(valores_clonado, tamano)
               bandclonado = True
           else:
                print("hay que cargar primero los valores")
        elif opcion == "3":
            if bandclonado == True:
                udf_informar_encima_promedio(valores_clonado,tamano)
            else:
                print("hay que Clonar primero los valores")
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")

mimain()