# -*- coding: utf-8 -*-
# Inicializamos variables para contar los múltiplos de 3 y los números fuera de rango
suma_multiplos_4 = 0
cantidad_multiplos_3 = 0
cantidad_multiplos_4 = 0
numeros_fuera_de_rango = 0

# Solicitamos al usuario la cantidad de números a evaluar
cantidad_numeros = int(input("Ingrese la cantidad de números a evaluar: "))

# Iteramos la cantidad de veces especificada
for i in range(cantidad_numeros):
    numero = int(input(f"Ingrese el número {i + 1} (entre 1 y 20): "))

    # Verificamos si el número está dentro del rango
    if numero >= 1 and numero <= 20:
        # Calculamos si es múltiplo de 4
        if numero % 4 == 0:
            cantidad_multiplos_4 += 1
            suma_multiplos_4 += numero
        # Calculamos si es múltiplo de 3
        if numero % 3 == 0:
            cantidad_multiplos_3 += 1
    else:
        # Si el número está fuera de rango, lo contamos
        numeros_fuera_de_rango += 1
        print(f"Número {numero} fuera de rango")

# Calculamos el promedio de los múltiplos de 4 (si hay múltiplos de 4)
if cantidad_multiplos_4 > 0:
    promedio_multiplos_4 = suma_multiplos_4 / cantidad_multiplos_4
else:
    promedio_multiplos_4 = 0

# Informamos los resultados
print(f"Promedio de múltiplos de 4: {promedio_multiplos_4}")
print(f"Cantidad de múltiplos de 3: {cantidad_multiplos_3}")
print(f"Números fuera de rango: {numeros_fuera_de_rango}")
