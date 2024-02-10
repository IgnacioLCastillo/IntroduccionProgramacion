
palabra_mas_larga = None
longitud_mas_larga = None
palabra_mas_corta = None
longitud_mas_corta = None
PrimeraPalabra = True ## Banderita para saber si es la primera palabra ingresada

while True:
    mipalabra = input("Ingrese una palabra: ")
    if mipalabra.upper() == 'FIN':
        break

    ancho = len(mipalabra)
    if PrimeraPalabra==True:
        max = ancho
        palabra_mas_larga = mipalabra
        min = ancho
        palabra_mas_corta = mipalabra
        PrimeraPalabra = False
    else:
        if ancho>max:
            max=ancho
            palabra_mas_larga=mipalabra
        else:
            if ancho<min:
                min=ancho
                palabra_mas_corta=mipalabra

if PrimeraPalabra==True:
    print("No se ingresaron palabras")
else:
    print(f"La palabra mas larga es {palabra_mas_larga} con {max} letras")
    print(f"La palabra mas corta es {palabra_mas_corta} con {min} letras")

