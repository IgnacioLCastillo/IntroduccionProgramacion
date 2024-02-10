# -*- coding: utf-8 -*-

def udf_encontro_asterisco(ppalabra):
    print(total_longitud)
    for letra in ppalabra:
        if letra == '*':
            return True
    return False



def mimain():
    # Inicializamos las variables
    total_longitud = 0
    contador_palabras = 0
    palabra_mas_logitud = None
    tamaño_palabra_mas_larga = 0
    

    # Solicitar al usuario que ingrese palabras (hasta un máximo de 10)
    for i in range(10):
        palabra = input("Ingrese una palabra (o una palabra con * para finalizar): ")

        # Comprobar si la palabra contiene un asterisco (*)
        if udf_encontro_asterisco(palabra)==True:
            break

        # Calcular la longitud de la palabra y agregarla al total
        print(f"La longitud de la palabra '{palabra}' es: {len(palabra)}")
        longitud = len(palabra)
        #total_longitud += longitud
        total_longitud=total_longitud+longitud
        contador_palabras += 1

        if longitud > tamaño_palabra_mas_larga:
            palabra_mas_logitud = palabra
            tamaño_palabra_mas_larga = longitud

    # Calcular el promedio de longitud
    if contador_palabras > 0:
        promedio_longitud = total_longitud / contador_palabras
        print(f"El promedio de longitud de las palabras ingresadas es: {promedio_longitud}")
        print(f"La palabra más larga es '{palabra_mas_logitud}' con {tamaño_palabra_mas_larga} letras.")
    else:
        print("No se ingresaron palabras válidas.")
