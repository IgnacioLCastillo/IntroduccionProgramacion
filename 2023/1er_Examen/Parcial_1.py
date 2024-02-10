def calcular_porcentaje_vocales(ppalabra):
    # Inicializamos contadores para vocales y consonantes
    num_vocales = 0

    # Iteramos a través de cada letra en la palabra
    for letra in ppalabra:
        # Si la letra es una vocal (A, E, I, O, U), aumentamos el contador de vocales
        if letra.upper() in 'AEIOU':
            num_vocales += 1
    # Calculamos el porcentaje de vocales sobre consonantes
    porcentaje = (num_vocales / len(ppalabra)) * 100
    return porcentaje


def mimain():
    # Solicita al usuario cuántas palabras desea ingresar
    num_palabras = int(input("Ingrese cuántas palabras desea ingresar: "))
    # Inicializamos variables
    mejor_palabra = None
    mejor_porcentaje = 0


    menos50=0
    # Ingresa el número especificado de palabras
    for i in range(num_palabras):
        palabra = input("Ingrese una palabra: ")
        # Calcula el porcentaje de vocales sobre consonantes
        porcentaje_vocal = calcular_porcentaje_vocales(palabra)
        print(f"Porcentaje de Vocales en '{palabra}': {porcentaje_vocal}%")

        #Calculamos la palabra de menor porcentaje de vocales
        if porcentaje_vocal < menor_porcentaje:
            menor_porcentaje = porcentaje_vocal
        else:
            if porcentaje_vocal > mejor_porcentaje:
                mejor_palabra = palabra
                mejor_porcentaje = porcentaje_vocal

        if porcentaje_vocal < 50:
            menos50+=1
    # Muestra la palabra con el mayor porcentaje de vocales
    if mejor_palabra is not None:
        print(f"La palabra con mayor porcentaje de vocales es '{mejor_palabra}' con {mejor_porcentaje}% de vocales.")
        print(f"Palabras con menos de 50% de vocales: {menos50}")





mimain()