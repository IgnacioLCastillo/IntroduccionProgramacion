# -*- coding: utf-8 -*-
import array
def mimain():
    valores_arreglo = array.array('i', [1,3,4,5,6,7,-1,-5])
    while True:
        print("\nMenú de Opciones:")
        print("1 - Corregir el vector")
        print("2 - Promedio vector entre limites")
        print("3 - Salir")
        opcion = input("Elija una opción: ")
        if opcion == "1":
            print(f"Opcion Corregir el vector{valores_arreglo}")
            for i in range(len(valores_arreglo)):
                if valores_arreglo[i] < 0:
                    valores_arreglo[i] = abs(valores_arreglo[i])
            print(f"Vector corregido: {valores_arreglo}")
        elif opcion == "2":
            print("Opcion Promedio entre limites")

            if any(valor < 0 for valor in valores_arreglo):
                print("El vector debe estar corregido antes de calcular el promedio ")
            else:
                try:
                    x = int(input("Ingrese la posición X (índice): "))
                    y = int(input("Ingrese la posición Y (índice): "))

                    if x < 0 or y >= len(valores_arreglo) or y <= x:
                        print("¡Error! Posiciones inválidas.")
                    else:
                        promedio = sum(valores_arreglo[x:y + 1]) / (y - x + 1)
                        print(f"Promedio entre posiciones {x} y {y}: {promedio}")
                except ValueError:
                    print("¡Error! Ingrese números enteros para las posiciones.")
                if opcion == "2":
                    if any(valor < 0 for valor in valores_arreglo):
                        print("¡Error! El vector debe estar corregido antes de calcular el promedio entre límites.")
                    else:
                        try:
                            x = int(input("Ingrese la posición X (índice): "))
                            y = int(input("Ingrese la posición Y (índice): "))

                            if x < 0 or y >= len(valores_arreglo) or y <= x:
                                print("¡Error! Posiciones inválidas.")
                            else:
                                total = 0
                                elementos = 0
                                for i in range(x, y + 1):
                                    total += valores_arreglo[i]
                                    elementos += 1
                                promedio = total / elementos
                                print(f"Promedio entre posiciones {x} y {y}: {promedio}")
                        except ValueError:
                            print("¡Error! Ingrese números enteros para las posiciones.")

        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")
mimain()
