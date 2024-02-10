
def calcula_vocales(ppalabra):
    # Calcula el porcentaje de vocales sobre consonantes
    lvocales = 0
    for letra in ppalabra:
        if letra.upper() in 'AEIOU':
            lvocales += 1
    return lvocales


def mimain():
    contar_error = 0
    sumtam=0
    cuentatotal=0
    maximo_vocales = 0
    palabra_maximo_vocales = None
    Total_intentos=3

    while True:
        palabra = input("Ingresa una palabra: ")
        print(f"Tamaño:{len(palabra)}")

        # Verificar si la palabra es demasiado
        if len(palabra) < 3:
            contar_error+=1
            print (f'Error en Ingreso, quedan {Total_intentos-contar_error} intentos')
        else:
            sumtam = sumtam + len(palabra)
            cuentatotal= cuentatotal + 1
            cant_vocales_calculadas = calcula_vocales(palabra)
            if cant_vocales_calculadas> maximo_vocales:
                maximo_vocales = cant_vocales_calculadas
                palabra_maximo_vocales = palabra


        if contar_error == 3:
            print("Has ingresado demasiadas palabras cortas. Finalizando.")
            break

    if cuentatotal > 0:
        print(f"Promedio de longitud de palabras ingresadas: {sumtam/cuentatotal:.2f}")
        print(f"Palabra con más vocales: {palabra_maximo_vocales} y tiene {cant_vocales_calculadas} vocales")



#----
mimain()