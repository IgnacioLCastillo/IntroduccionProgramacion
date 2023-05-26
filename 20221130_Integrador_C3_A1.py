import array as arr
'''-----------------------------Area de definicion de Funciones-------------------'''
def UDFDibujaMenu():
    print('1-Carga')
    print('2-Mi Numero Vs Maximo:')
    print('3-Muestra hasta Numero')
    print('4-Salimos')
    opcion=int(input("Ingrese Opcion:"))
    return opcion

def udfCargaVector(mipArreglo, pTam):
    for i in range(0, pTam, 1):
        miValor = int(input("Ingrese Valor en miarreglo[" + str(i) + ']:'))
        if miValor>0:
            mipArreglo[i] = miValor
        else:
            print ('Error en el ingreso. Numero guardado:',miValor *-1)
            mipArreglo[i] = miValor *-1

def udfMaximo(mipArreglo,pTam):
    miMax = 0
    for i in range(0, pTam, 1):
        if mipArreglo[i]>miMax:
            miMax=mipArreglo[i]
    return miMax

def muestraResulMax(mipValor,pMax):
    if mipValor>pMax:
        print(f"{mipValor} es mayor al Maximo {pMax}")
    else:
        print(f"{mipValor} es menor al Maximo {pMax}")

def Muestra_Hasta_Valor(mipArreglo,pmiValor,pTam):
    i=0
    encontro=False
    while  i<pTam and encontro==False:
          if mipArreglo[i]== pmiValor:
              encontro=True
          print (mipArreglo[i],i)
          i=i+1
    '''
    for i in range(0,pTam):
        if mipArreglo[i]!= pmiValor:
              print (mipArreglo[i],i)
        elif:
            break
'''
miopcion=-1
#miVector = arr.array('i',range(5))
miVector = arr.array('i',[0,0,0,0,0])
cantElem=len(miVector)
while miopcion!=4:
    miopcion=UDFDibujaMenu()
    if miopcion==1:
        udfCargaVector(miVector,cantElem)
    elif  miopcion==2:
        miMaximo = udfMaximo(miVector, cantElem)
        miValor=int(input("Ingrese un Valor a buscar"))
        muestraResulMax(miValor,miMaximo)
    elif miopcion == 3:
        miValor=int(input("Ingrese un Valor a buscar"))
        Muestra_Hasta_Valor(miVector,miValor,cantElem)
    elif miopcion == 4:
        print("Sale")
    else:
        print("Error Opcion 1 - 4 Validas")