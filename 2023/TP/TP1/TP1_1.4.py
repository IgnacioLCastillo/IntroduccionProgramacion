# -*- coding: utf-8 -*-
# Inicializamos las variables para la palabra más larga, su longitud, y la palabra más corta y su longitud
palabra_mas_larga = None
longitud_mas_larga = None
palabra_mas_corta = None
longitud_mas_corta = None
PrimeraPalabra = True ## Banderita para saber si es la primera palabra ingresada

while True:
    palabra = input("Ingresa una palabra o escribe 'FIN' para finalizar: ")

    if palabra.upper() == 'FIN':
        break
    # Verificamos si es la primera palabra ingresada
    if PrimeraPalabra==True:
        palabra_mas_corta = palabra
        longitud_mas_corta = len(palabra)
        palabra_mas_larga = palabra
        longitud_mas_larga = len(palabra)
        PrimeraPalabra = False
    else:
        # Comparamos la longitud de la palabra con la palabra más larga y más corta
        if len(palabra) > longitud_mas_larga:
            palabra_mas_larga = palabra
            longitud_mas_larga = len(palabra)
        else:
            if len(palabra) < longitud_mas_corta:
                palabra_mas_corta = palabra
                longitud_mas_corta = len(palabra)

# Mostramos la palabra más larga y la palabra más corta junto con sus longitudes
if palabra_mas_larga is not None:
    print(f"La palabra más larga es '{palabra_mas_larga}' con {longitud_mas_larga} letras.")

if palabra_mas_corta  is not None:
    print(f"La palabra más corta es '{palabra_mas_corta}' con {longitud_mas_corta} letras.")
