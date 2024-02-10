
def porc_calcula_vocales(ppalabra):
    # Calcula el porcentaje de vocales sobre consonantes
    ltamaño = len(ppalabra)
    lvocales = 0
    for letra in ppalabra:
        if letra.upper() in 'AEIOU':
            lvocales += 1
    return ((lvocales/ltamaño)*100, ltamaño, lvocales)


def mimain():
    num_palabras = int(input("Ingrese cuántas palabras desea ingresar: "))
    cuentomenores=0
    prorcentaje_mayor = 0
    palabra_mayor = None

    for i in range(num_palabras):
        palabra = input("Ingrese una palabra: ")
        porcentaje,tamaño,vocales = porc_calcula_vocales(palabra)

        if porcentaje > prorcentaje_mayor:
            prorcentaje_mayor = porcentaje
            palabra_mayor = palabra


        if porcentaje< 50:
            cuentomenores+=1

        print(f"Porcentaje de Vocales en '{palabra} ---> {vocales} /{tamaño} ---> {porcentaje}%")

    print(f"La palabra con mayor porcentaje de vocales es '{palabra_mayor}' con {prorcentaje_mayor}% de vocales.")
    print(f"Palabras con menos de 50% de vocales: {cuentomenores}")


#----------------------------------
mimain()
