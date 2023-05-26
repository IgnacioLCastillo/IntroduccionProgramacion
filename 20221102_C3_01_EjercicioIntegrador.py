import array as arr
#import os as cmd
import random
#Area de Definicion de Funciones Necesarias
def UDFDibujaMenu():
    print('1-Carga')
    print('2-Muestra')
    print('3-Muestra')
    print('4-Maximo')
    print('5-Reemplazo -1 Mult. 5')
    print('6-Busca un elemento')
    print('7-Promedio Valores Impares')
    print('8-Salir')
    viOpcion = int(input("Seleccione:"))
    return viOpcion

def udfMuestraModifica(mipArreglo, pPosic,pValor,pTam):
    #Carga Tradicional Arreglo
    if pPosic>=0 and pPosic<pTam:
        mipArreglo[pPosic] = pValor
        return 1 # Mensaje que le mando al principal para que sepa que esta OK
    else:
        return -1 # Mensaje que le mando al principal para que sepa que esta MAL

def udfCargaVectorManual(mipArreglo, pTam):
    #Carga Tradicional Arreglo
    # print (random.randint(0, 5))
    for i in range(0, pTam, 1):
        mipArreglo[i] = int(input("Ingrese Valor en miarr1eglo[" + str(i) + ']:'))

def udfCargaVectorAutomatica(mipArreglo, pTam):
    #Carga Aleatoria de Valores
    for i in range(0, pTam, 1):
        mipArreglo[i] = random.randint(1, 10)
    print ("--------Carga Finalizada Automaticamente con Exito------------")


def udfReemplazaCeroM5(mipArreglo, pTam):
    #Carga Aleatoria de Valores
    hayMul5=False
    for i in range(0, pTam, 1):
        if mipArreglo[i]%5==0:
            mipArreglo[i] = -1
            hayMul5=True

    return hayMul5



def udfMuestraVector(mipArreglo, pTam):
    for i in range (0,pTam,1):
        print(f'Arreglo[{i}]:{mipArreglo[i]}')

def udfBusquedaenVector(mipArreglo,pValorBuscado, pTam):
    for i in range (0,pTam,1):
        if mipArreglo[i]==pValorBuscado:
            return i

    return -1


def udfPromedioPosicImpar(mipArreglo, pTam):
    viContImp=0
    viSumaImp=0
    for i in range (0,pTam,1):
        if mipArreglo[i]%2!=0:
            viSumaImp=viSumaImp+mipArreglo[i]
            viContImp+=1
    if viContImp>0:
        return viSumaImp/viContImp
    else:
        return 0

def udfMaximoVector(mipArreglo, pTam):
    for i in range (0,pTam,1):
        if i==0:
           miMax=mipArreglo[i]
           posicMax=i
        else:
            if mipArreglo[i]>miMax:
                miMax = mipArreglo[i]
                posicMax = i

    return posicMax

#***********************Area Programa Principal********************************

miOpcion=-1 #Variable Global inicializada en -1 para que entre al menos 1 vez
miArreglo = arr.array('i',range(5)) #Global
viCantElem=len(miArreglo) #Global
#Mientras
while miOpcion!=8:
#Repetir / Hasta
#while True:

    miOpcion=UDFDibujaMenu()
    if miOpcion==1:
        miModo=int(input("Ingrese Modo 1 - Manual / 2- Automatico"))
        if miModo==1:
            udfCargaVectorManual(miArreglo,viCantElem)
        elif miModo==2:
            udfCargaVectorAutomatica(miArreglo,viCantElem)
        else:
            print ('Error en la selecion del Modo. 1 o 2 como Valido')
    elif miOpcion == 2:
            miPosicaModif = int(input("Posicion a Modificar:"))
            miNuevoValor=int(input("Ingrese Nuevo Valor:"))
            retorno=udfMuestraModifica(miArreglo,miPosicaModif,miNuevoValor,viCantElem)
            if retorno == 1:
                print('Actualización Exitosa')
            else:
                print('Error en actualizacion - Rango Invalido')
    elif miOpcion == 3:
         udfMuestraVector(miArreglo,viCantElem)
    elif miOpcion == 4:
         maxPosicRecibido=udfMaximoVector(miArreglo,viCantElem)
         print (f'El maximo es {miArreglo[maxPosicRecibido]} que esta en la posicion {maxPosicRecibido}')
    elif miOpcion == 5:
         if udfReemplazaCeroM5(miArreglo,viCantElem) == True:
             print('*************Reemplazos Realizados**********')
         else:
             print('*************No Hubo Reemplazos**********')
    elif miOpcion == 6:
        miValoraBuscar = int(input("Valor a Buscar:"))
        posicEncontrada=udfBusquedaenVector(miArreglo,miValoraBuscar, viCantElem)
        if posicEncontrada == -1:
            print('Valor No Encontrado')
        else:
            print(f'Encontrado en la posicion {posicEncontrada}')

    elif miOpcion == 7:
        miPromRecibido=udfPromedioPosicImpar(miArreglo,viCantElem)
        print(f'El promedio es {miPromRecibido}')
    elif miOpcion == 8:
 #        break # Solo si usan un While True
         print("---Fin Algoritmo----")
    else:
        print("Opcion Invalida")

