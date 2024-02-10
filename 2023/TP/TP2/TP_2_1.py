# -*- coding: utf-8 -*-
'''Desarrollar un algoritmo que permita la carga de un vector de 10 posiciones.
Generar una rutina que transcriba el contenido del vector a otro vector en orden inverso.'''
import array

def udf_cargar_valores(parreglovalores,tamano):
    for i in range(tamano):
        parreglovalores[i] = int(input(f"Ingrese un valo para la posición {i + 1}: "))


def udf_mostrar_vector(pvector,ptam):
    for i in range(0,ptam,1):
        print(f"{pvector[i]}",end='|')

def udf_Copia_inverso(pvector_original,pvector_copia,ptam):

    for i in range(ptam):
        pvector_copia[i] = pvector_original[ptam - i - 1]
    #Forma 2
    '''
    j=ptam-1 #j=9
    for i in range(ptam):
        pvector_copia[i] = pvector_original[j]
        j=j-1
    '''
    #Forma 3
    '''
    j = ptam - 1
    while i <ptam:
        pvector_copia[i] = pvector_original[j]
        i=i+1
        j = j - 1
    '''

def mimain():
    tamano = 10
    valores_original = array.array('i', [0] * tamano)
    valores_copias = array.array('i', [0] * tamano)
    udf_cargar_valores(valores_original,tamano)
    udf_mostrar_vector(valores_original, tamano)
    udf_Copia_inverso(valores_original,valores_copias,tamano)
    udf_mostrar_vector(valores_copias, tamano)


'''Area Publica'''

mimain()


