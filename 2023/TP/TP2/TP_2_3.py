# -*- coding: utf-8 -*-
import array

def udf_cargar_valores(parreglovalores,tamano):
    for i in range(tamano):
        parreglovalores[i] = int(input(f"Ingrese un valo para la posición {i + 1}: "))

def udf_esCapicua(pvector_original,ptam):
    for i in range(0,ptam,1):
        if pvector_original[i] != pvector_original[ptam - i-1]:
            return False

    return True


def udf_esCapicua1(pvector_original,ptam):
    j=ptam-1
    for i in range(0,ptam,1):
        if pvector_original[i] != pvector_original[j]:
            return False
        j=j-1
    return True

def udf_esCapicua2(pvector_original,ptam):
    j=ptam-1
    i=0
    while i<ptam:
        if pvector_original[i] != pvector_original[j]:
            return False
        i = i + 1
        j=j-1

    return True

def palindromo(arreglo):
    if len(arreglo) != 4:
        return False
    return arreglo == arreglo[::-1]

def mimain():
    tamano = 4
    vector_original = array.array('i', [0] * tamano)
    udf_cargar_valores(vector_original,tamano)
    if udf_esCapicua(vector_original,tamano)==True:
        print("Es capicua")
    else:
        print("No es capicua")

    if palindromo(vector_original):
        print("Es capicua")
    else:
        print("No es capicua")




mimain()
