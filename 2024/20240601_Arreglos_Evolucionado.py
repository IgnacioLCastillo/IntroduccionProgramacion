# -*- coding: utf-8 -*-
import array as arr
def miMenu():
    print("1. Cargar Datos Arrglo")
    print("2. Carga condicionada de Datos Arrglo")
    print("3. Mostrar Datos del Arreglo")
    print("4. Promedio de Datos del Arreglo")
    print("5. Minimo del Arreglo")
    print("6. Maximo de los pares del Arreglo")
    print("7. Salir")
    opc = int(input("Ingrese Opcion:"))
    return opc

def udfCargaArreglo(parreglo,ptam):
    for i in range(0,ptam,1):
        parreglo[i]=int(input(f'Ingrese Valor en miarreglo[{i}]:'))
    return parreglo


def udfCargaArregloCondicionada(parreglo,ptam):
    contbuenos=0
    for i in range(0,ptam,1):
        miElemento=int(input(f'Ingrese Valor en miarreglo[{i}]:'))
        if miElemento>0:
            parreglo[i]=miElemento
            contbuenos=contbuenos+1
        else:
            break
    return parreglo,contbuenos

def udfMuestraArreglo(parreglo,ptam):
    for i in range(0,ptam,1):
        print(f'Mi Arreglo[{i}]:{parreglo[i]}')

def udfMuestraArreglo(parreglo,ptam):
    for i in range(0,ptam,1):
        print(f'Mi Arreglo[{i}]:{parreglo[i]}')

def udfPromedioArreglo(parreglo,ptam):
    sumaElementos=0
    cantElementos=0
    for i in range (0,ptam,1):
        sumaElementos=sumaElementos+parreglo[i]
        cantElementos=cantElementos+1
    promedio=sumaElementos/cantElementos
    return promedio

def udfMinimoArreglo(parreglo,ptam):
    minvalor=parreglo[0]
    for i in range(1,ptam,1):
        if parreglo[i]<minvalor:
            minvalor=parreglo[i]
    return minvalor


def udfMaximodelosPares(parreglo,ptam):
    esPrimero=False
    maxvalor=0
    for i in range(0,ptam,1):
        if parreglo[i]%2==0:
            if esPrimero==False:
                maxvalor=parreglo[i]
                esPrimero=True
            else:
                if parreglo[i]>maxvalor:
                    maxvalor=parreglo[i]

    return maxvalor,esPrimero

def miMain():
    #Definicion y dimensionamiento
    tamaño=int(input("Ingrese el tamaño del arreglo:"))
    miArreglo = arr.array('i',[0]*tamaño)
    miopc=0
    while miopc!=7:
        miopc=miMenu()
        if miopc==1:
            miArreglo=udfCargaArreglo(miArreglo,tamaño)
        elif miopc==2:
            #El vector se retorna cargado y el tamaño se redefine segun los valores
            #buenos
            miArreglo,tamaño = udfCargaArregloCondicionada(miArreglo, tamaño)
        elif miopc==3:
            udfMuestraArreglo(miArreglo,tamaño)
        elif miopc==4:
            print(f'El promedio es {udfPromedioArreglo(miArreglo,tamaño)}')
        elif miopc==5:
            miminimorecibido=udfMinimoArreglo(miArreglo,tamaño)
            print(f'El minimo es {miminimorecibido}')
        elif miopc==6:
            mimaximo,esprimero=udfMaximodelosPares(miArreglo,tamaño)
            if esprimero==True:
                print(f'El maximo de los pares es {mimaximo}')
            else:
                print('No hay pares en el arreglo y no puedo mostrar un maximo')

        elif miopc==7:
            print("Adios")
        else:
            print("Opcion no valida")


### Area Global
#Llamada al main para dar inicio al programa
miMain()