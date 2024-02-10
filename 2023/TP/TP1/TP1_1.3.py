# -*- coding: utf-8 -*-
#Generar un algoritmo que genere un número aleatorio entre 1 y 10. Ese número secreto podrá generarlo mediante la utilización de la librería y función que a continuación se pone como ejemplo
import random # Genera un número aleatorio entre 1 y 10 numero_secreto = random.randint(1, 10)
#Una vez generado este número, tendremos 3 oportunidades para adivinar el número secreto. En caso que no acierte deberá indicar cuántas oportunidades quedan e informará si el número es mayor o menor del número secreto.
#El algoritmo finaliza cuando falla 3 veces o cuando acierta el número.

import random

# Genera un número aleatorio entre 1 y 10
numero_secreto = random.randint(1, 10)

# Inicializa el contador de intentos
intentos = 0
max_intentos = 3

print("Adivina el número secreto entre 1 y 10.",numero_secreto)
# Comienza el bucle para adivinar el número
#encontro=False
#while not encontro and intentos < max_intentos: #si hubiese usado la bandera corto asi....
while intentos < max_intentos:
    # Solicita al usuario que ingrese su suposición
    intentos += 1
    suposicion = int(input(f"Intento {intentos}/{max_intentos}: Ingresa tu suposición: "))

    # Incrementa el contador de intentos

    # Comprueba si la suposición es correcta
    if suposicion == numero_secreto:
        print(f"¡Felicidades! Adivinaste el número secreto ({numero_secreto}")
        #intentos=max_intentos
        break
        #encontro=True

    else:
        # Comprueba si la suposición es mayor o menor
        if suposicion < numero_secreto:
            print("El número secreto es mayor.")
        else:
            print("El número secreto es menor.")

# Si el bucle termina sin adivinar el número, muestra un mensaje de fallo
if intentos == max_intentos:
    print("Agotaste todas tus oportunidades. El número secreto era: {}.".format(numero_secreto))

