import array as arr
'''-----------------------------Area de definicion de Funciones-------------------'''
def UDFDibujaMenu():
    print('1-Carga')
    print('2-Mostrar Valores Promedio')
    print('3-Muestra')
    print('4-Salimos')
    opcion=int(input("Ingrese Opcion:"))
    return opcion

def udfCargaVector(mipArreglo, pTam):
    #Carga Tradicional Arreglo
    for i in range(0, pTam, 1):
        miValor = int(input("Ingrese Valor en miarreglo[" + str(i) + ']:'))
        if miValor > 0:
            mipArreglo[i] = miValor
        else:
            mipArreglo[i] = 0

def udfMuestraVector(mipArreglo,pValor ,pTam):
    for i in range (0,pTam,1):
        if  mipArreglo[i]>=pValor:
            print(f'Arreglo[{i}]:{mipArreglo[i]}')


def udfCalculaPromedio(mipArreglo, pTam):
    locSuma=0
    for i in range (0,pTam,1):
        locSuma=locSuma+mipArreglo[i]

    return locSuma/pTam

'''-----------------------------PROGRAMA PRINCIPAL-------------------'''
miopcion=-1
miVector = arr.array('i',range(5))
cantElem=len(miVector)
while miopcion!=4:
    miopcion=UDFDibujaMenu()
    if miopcion==1:
        udfCargaVector(miVector,cantElem)
    elif  miopcion==2:
        miProm=udfCalculaPromedio(miVector,cantElem)
        print ("El promedio es:",miProm)
        udfMuestraVector(miVector,miProm,cantElem)
    elif miopcion == 3:
        udfMuestraVector(miVector,0,cantElem)
    elif miopcion == 4:
        print("Sale")
    else:
        print("Error Opcion 1 - 4 Validas")