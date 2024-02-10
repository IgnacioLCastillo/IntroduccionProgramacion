# -*- coding: utf-8 -*-
import random
'''match opcion:
            case 1:
                cargarArreglo(miArreglo)
            case 2:
                mostrarArreglo(miArreglo)
            case 5:
                print("Adios")
            case _:
                print("Opcion Incorrecta")
'''

def mimenu():
    print("1. Cargar Arreglo Manual")
    print("2. Cargar Arreglo Aleartoria")
    print("3. Mostrar Arreglo")
    print("4. Sumar Arreglo")
    print("5. Promediar Arreglo")
    print("6. Calcular Maximo de todo el Arreglo")
    print("7. Calcular Minimo de las posiciones Impares")
    print("8. Copia de Un Vector Duplicando los Valores")
    print("9. Maximo de los imPares")
    print("10. Salir")
    opcion=int(input("Ingrese Opcion:"))
    return opcion


def cargarArreglo(pArreglo,pTam):
    i=0
    while i<pTam:
        numerosimple = int(input(f"Ingrese Valor en miarreglo[{i}]:"))
        if numerosimple<0:
            print("Error - Solo se aceptan Positivos")
        else:
            pArreglo[i]=numerosimple
            i+=1

'''def cargarArreglo(pArreglo,pTam):
    for i in range (0,pTam,1):
        pArreglo[i]=int(input(f"Ingrese Valor en miarreglo[{i}]:"))
'''

#funcion para carga aleatoria
def cargaVectorRandom(parreglo,ptam):
    for i in (range(0,ptam,1)):
        parreglo[i]=random.randint(1, 100)

def mostrarArreglo(pArreglo,pTam):
    for i in range (0,pTam,1):
        print(f'mi arreglo en la posicion[{i}] contiene:  {pArreglo[i]}')


def sumarArreglo(pArreglo,pTam):
    suma=0
    for i in range (0,pTam,1):
        suma=suma+pArreglo[i]
    return suma


def maximoValoresImpares(pArreglo,pTam):
    primerImpar=0 #bandera
    mimaximo=None
    posicMaxima = None
    for i in range (0,pTam,1):
        if pArreglo[i]%2!=0:
            if primerImpar==0:
                mimaximo=pArreglo[i]
                posicMaxima=i
                primerImpar=1
            else:
                if pArreglo[i]>mimaximo:
                    mimaximo=pArreglo[i]
                    posicMaxima = i

    return mimaximo,posicMaxima,primerImpar



def maximoArreglo(pArreglo,pTam):

    mimaximo=pArreglo[0]
    mimaxposic=0
    for i in range (1,pTam,1):
        if pArreglo[i]>mimaximo:
            mimaximo=pArreglo[i]
            mimaxposic=i
    return mimaximo,mimaxposic

def minimodePosicionesImpares(pArreglo,pTam):
    miminimo=pArreglo[1]
    miminposic=1
    for i in range (3,pTam,2):
        if pArreglo[i]<miminimo:
            miminimo=pArreglo[i]
            miminposic=i
    return miminimo,miminposic


def copiavectorDuplicando(pArreglo,pArregloCopia,pTam):
    for i in range (0,pTam,1):
        pArregloCopia[i]=pArreglo[i]*2


def mimain():
    import array as arr #Importar libreria de arreglos
    tamDef = int(input("Ingrese Tamaño del Arreglo:"))
    miArreglo = arr.array('i', range(tamDef)) #Dimensionar el arreglo
    #Inicializo una lista
    milista= [0]*tamDef

    #miArreglo = arr.array('i', [0,0,0,0,0])  # Dimensionar el arreglo
    miArreglocopia = arr.array('i', range(tamDef))  # Dimensionar el arreglo
    opcion=0
    arreglocargado =False
    while opcion!=10:
        opcion=mimenu()

        if opcion==1:
            cargarArreglo(miArreglo,tamDef)
            arreglocargado=True #Unica opcion habilitada a cambiar el estado del flag
        elif opcion==2:
             cargaVectorRandom(miArreglo,tamDef)
             arreglocargado=True #Unica opcion habilitada a cambiar el estado del flag
        elif opcion==3:
            if arreglocargado==True:
               mostrarArreglo(miArreglo,tamDef)
            else:
                print("Debe cargar el arreglo primero")
        elif opcion==4:
            if arreglocargado == True:
                resultadosuma=sumarArreglo(miArreglo,tamDef)
                print('La suma conseguida es:',resultadosuma)
            else:
                print("Debe cargar el arreglo primero")
            #print('La suma conseguida es:',sumarArreglo(miArreglo,tamDef))
        elif opcion==5:
            if arreglocargado == True:
                print('El promedio es:',sumarArreglo(miArreglo,tamDef)/tamDef)
            else:
                print("Debe cargar el arreglo primero")
        elif opcion==6:
            if arreglocargado == True:
                mimaximoencontrado,mimaxposicencontrado=maximoArreglo(miArreglo,tamDef)
                print('El maximo es:',mimaximoencontrado,'y esta en la posicion',mimaxposicencontrado)
            else:
                print("Debe cargar el arreglo primero")
        elif opcion==7:
            if arreglocargado == True:
                miminimoencontrado,miminposicencontrado=minimodePosicionesImpares(miArreglo,tamDef)
                print('El minimo es:',miminimoencontrado,'y esta en la posicion',miminposicencontrado)
            else:
                print("Debe cargar el arreglo primero")
        elif opcion==8:
            if arreglocargado == True:
                copiavectorDuplicando(miArreglo,miArreglocopia,tamDef)
                mostrarArreglo(miArreglocopia,tamDef)
        elif opcion==9:
            if arreglocargado == True:
                mimaximoencontrado,mimaxposicencontrado,primerImpar=maximoValoresImpares(miArreglo,tamDef)
                if primerImpar==1:
                    print('El maximo de los impares es:',mimaximoencontrado,'y esta en la posicion',mimaxposicencontrado)
                else:
                    print('No hay impares')


        elif opcion==10:
            print("Adios")
        else:
            print("Opcion Incorrecta")

#------- Area global
mimain()

