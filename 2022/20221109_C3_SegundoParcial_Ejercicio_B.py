import array as arr
'''-----------------------------Area de definicion de Funciones-------------------'''
def UDFDibujaMenu():
    print('1-Carga')
    print('2-Mostrar Minimo')
    print('3-Muestra')
    print('4-Salimos')
    opcion=int(input("Ingrese Opcion:"))
    return opcion

def udfCargaVectorMetodoB(mipArreglo, pTam):
    for i in range(0, pTam, 1):
        miValor = int(input("Ingrese Valor en miarreglo[" + str(i) + ']:'))
        indiceOk=i
        if miValor>0:
            mipArreglo[i] = miValor
        else:
            break

    for (i) in range(indiceOk, pTam, 1):
        mipArreglo[i]=0


def udfCargaVectorMetodoC(mipArreglo, pTam):
    for i in range(0, pTam, 1):
        miValor = int(input("Ingrese Valor en miarreglo[" + str(i) + ']:'))
        if miValor>0:
            mipArreglo[i] = miValor
        else:
            break




def udfCargaVector(mipArreglo, pTam):
    #Carga Tradicional Arreglo
    sinoHayNegativo=True
    for i in range(0, pTam, 1):
       if sinoHayNegativo==True:
            miValor = int(input("Ingrese Valor en miarreglo[" + str(i) + ']:'))
            if miValor>0:
                mipArreglo[i] = miValor
            else:
                sinoHayNegativo=False
                mipArreglo[i] = 0
       else:
           mipArreglo[i] = 0


def udfMuestraVector(mipArreglo,pValor ,pTam):
    for i in range (0,pTam,1):
        if  mipArreglo[i]>=pValor:
            print(f'Arreglo[{i}]:{mipArreglo[i]}')


def udfCalculaMinimo(mipArreglo, pTam):
    for i in range (0,pTam,1):
        if mipArreglo[i]>0:
            if i==0:
                minPosic=i
                minValor=mipArreglo[i]
            else:
                if mipArreglo[i]<minValor:
                    minPosic = i
                    minValor=mipArreglo[i]
    return minPosic

'''-----------------------------PROGRAMA PRINCIPAL-------------------'''
miopcion=-1
#miVector = arr.array('i',range(5))
miVector = arr.array('i',[0,0,0,0,0])
cantElem=len(miVector)
while miopcion!=4:
    miopcion=UDFDibujaMenu()
    if miopcion==1:
        #udfCargaVector(miVector,cantElem)
        #udfCargaVectorMetodoB(miVector,cantElem)
        udfCargaVectorMetodoC(miVector,cantElem)
    elif  miopcion==2:
        miMinimo=udfCalculaMinimo(miVector,cantElem)
        print(miVector[miMinimo])
    elif miopcion == 3:
        udfMuestraVector(miVector,0,cantElem)
    elif miopcion == 4:
        print("Sale")
    else:
        print("Error Opcion 1 - 4 Validas")