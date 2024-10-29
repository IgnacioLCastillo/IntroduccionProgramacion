# -*- coding: utf-8 -*-


#Podriamos calcular "a mano" con un contador el tamaño de la palabra
#tamaño=0
def miLen(palabra):
    tam=0
    for letra in palabra:
        print(letra)
        tam+=1
    return tam


miPalabra = input("Introduce una palabra: ")
tamaño = len(miPalabra).
mitamaño = miLen(miPalabra)
print(f"La palabra '{miPalabra}' tiene {tamaño} letras")
print(f"La palabra '{miPalabra}' tiene {mitamaño} letras")
