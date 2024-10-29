# -*- coding: utf-8 -*-
def udf_agregar_pelicula(plistitulos, plisgeneros, pliscalificaciones):
    unTitulo = input("Ingrese el titulo de la pelicula: ")
    unGenero = input("Ingrese el genero de la pelicula: ")
    unaCalificacion = float(input("Ingrese la calificacion de la pelicula del 1 al 5): "))
    plistitulos.append(unTitulo)
    plisgeneros.append(unGenero)
    pliscalificaciones.append(unaCalificacion)
    return plistitulos, plisgeneros, pliscalificaciones

def udf_mostrar_peliculas(plistitulos, plisgeneros, pliscalificaciones):
    if len(plistitulos)>0:
        print("\nLista de peliculas:")
        for i in range(len(plistitulos)):
            print(f"Titulo: {plistitulos[i]}, Genero: {plisgeneros[i]}, Calificacion: {pliscalificaciones[i]}")
    else:
        print("No hay peliculas en la lista.")


def udf_mostrar_peliculas_por_genero(plistitulos, plisgeneros, pliscalificaciones, pungenero):
    hayunagenero = False
    for i in range(len(plisgeneros)):
        if plisgeneros[i].lower() == pungenero.lower():
            hayunagenero = True
            print(f"Título: {plistitulos[i]}, Calificación: {pliscalificaciones[i]}")

    if not hayunagenero:
        print(f"No hay peliculas del genero {pungenero} en la lista.")


def udf_promedio_calificaciones(calificaciones):
    if len(calificaciones)>0:
        for i in range(len(calificaciones)):
            acumCalif=acumCalif+calificaciones[i]

        totalpromedio = acumCalif / len(calificaciones)
        print(f"\nEl promedio de calificaciones es: {totalpromedio:.2f}")
    else:
        print("No hay películas en la lista para calcular el promedio.")


def udf_peor_calificacion(titulos, calificaciones):
    if len(titulos)>0:
        peor_index = 0
        for i in range(1, len(calificaciones)):
            if calificaciones[i] < calificaciones[peor_index]:
                peor_index = i
        print(
            f"\nLa película peor calificada es: {titulos[peor_index]} con una calificación de {calificaciones[peor_index]}")
    else:
        print("No hay peliculas en la lista.")


def udf_mejormejor_calificada_genero(plisgeneros, pliscalificaciones, pungenero):
    maxindex=-1
    for i in range(0,len(plisgeneros),1):
        if plisgeneros[i].lower() == pungenero.lower():
            if maxindex==-1:
                maximacalif = pliscalificaciones[i]
                maxindex= i
            else:
                if pliscalificaciones[i]>maximacalif:
                    maximacalif=pliscalificaciones[i]
                    maxindex=i
    return i

def mimenu():
    print("\nMenu:")
    print("1. Agregar una nueva película")
    print("2. Mostrar la lista de películas")
    print("3. Mostrar películas por género")
    print("4. Calcular el promedio de calificaciones")
    print("5. Encontrar la película peor calificada")
    print("6. Encontrar la película mejor calificada de un género específico")
    print("7. Salir")
    opcion = int(input("Seleccione una opción: "))
    return opcion


def mimain():
    titulos = []
    generos = []
    calificaciones = []

    while True:
        opcionrecibida = mimenu()

        if opcionrecibida == '1':
            udf_agregar_pelicula(titulos, generos, calificaciones)
        elif opcionrecibida == '2':
            udf_mostrar_peliculas(titulos, generos, calificaciones)
        elif opcionrecibida == '3':
            genero = input("Ingrese el genero: ")
            udf_mostrar_peliculas_por_genero(titulos, generos, calificaciones, genero)
        elif opcionrecibida == '4':
            udf_promedio_calificaciones(calificaciones)
        elif opcionrecibida == '5':
            udf_peor_calificacion(titulos, calificaciones)
        elif opcionrecibida == '6':
            genero = input("Ingrese el genero: ")
            indiceMejor=udf_mejormejor_calificada_genero(generos, calificaciones, genero)
            if indiceMejor==-1:
                print(f"No hay películas del género {genero} en la lista.")
            else:
                print(f"La pelIcula mejor calificada del gEnero {genero} es: {titulos[indiceMejor]} con una calificaciOn de {calificaciones[indiceMejor]}")
        elif opcionrecibida == '7':
            print("Terminamos.")
            break
        else:
            print("Opcion no valida. Intente de nuevo.")

#AreaPrincipal
mimain()
