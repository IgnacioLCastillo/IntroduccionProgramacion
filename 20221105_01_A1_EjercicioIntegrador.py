import array as arr
'''-----------------------------Area de definicion de Funciones-------------------'''
def UDFDibujaMenu():
    print('1-Carga')
    print('2-Modifica')
    print('3-Muestra')
    print('4-Suma Elementos indicados por posicion')
    print('5-Salimos')
    opcion=int(input("Ingrese Opcion:"))
    return opcion

def udfCargaVector(mipArreglo, pTam):
    #Carga Tradicional Arreglo
    for i in range(0, pTam, 1):
        mipArreglo[i] = int(input("Ingrese Valor en miarreglo[" + str(i) + ']:'))


def udfMuestraVector(mipArreglo, pTam):
    for i in range (0,pTam,1):
        print(f'Arreglo[{i}]:{mipArreglo[i]}')


def udfSumaTodo(mipArreglo, pTam):
    for i in range (0,pTam,1):
        suma=suma+mipArreglo[i]

    return suma


def udfMuestraModifica(mipArreglo, pPosic,pValor,pTam):
    #Carga Tradicional Arreglo
    if pPosic>=0 and pPosic<pTam:
        mipArreglo[pPosic] = pValor
        return 1 # Mensaje que le mando al principal para que sepa que esta OK
    else:
        return -1 # Mensaje que le mando al principal para que sepa que esta MAL

def udfSumaPosic(mipArreglo, pPosicA,pPosicB,pTam):
    #Carga Tradicional Arreglo
    if pPosicA>=0 and pPosicA<pTam:
        if pPosicB>=0 and pPosicB<pTam:
            return (mipArreglo[pPosicA]+mipArreglo[pPosicB])
            # Mensaje que le mando al principal para que sepa que esta OK
    else:
        return -1 # Mensaje que le mando al principal para que sepa que esta MAL

'''-----------------------------PROGRAMA PRINCIPAL-------------------'''

miopcion=-1
miVector = arr.array('i',range(5))
cantElem=len(miVector)
while miopcion!=5:
    miopcion=UDFDibujaMenu()
    if miopcion==1:
        udfCargaVector(miVector,cantElem)
    elif  miopcion==2:
        miPosic=int(input("Ingrese valor a modifiicar:"))
        miNuevoValor=int(input("Ingrese Nuevo Valor:"))
        ##result=udfMuestraModifica(miVector,miPosic,miNuevoValor,cantElem)
        if (udfMuestraModifica(miVector,miPosic,miNuevoValor,cantElem))==-1:
            print("Error en Rango")
        else:
            print("Modificacion Exitosa")
    elif miopcion == 3:
        udfMuestraVector(miVector,cantElem)

    elif miopcion == 4:
        miPosicA = int(input("Ingrese posicion A:"))
        miPosicB = int(input("Ingrese posicion B:"))
        result=udfSumaPosic(miVector, miPosicA, miPosicB, cantElem)
        if (result == -1):
            print("Error en Rango")
        else:
            print("Suma",result)


    elif miopcion == 5:
        print("Sale")
    else:
        print("Error Opcion 1 - 4 Validas")