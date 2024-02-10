import array as arr
#----------Funciones UDF-------------------
def udfCargaVector(mipArreglo, pTam):
    #Carga Tradicional Arreglo
    for i in range(0, pTam, 1):
        mipArreglo[i] = int(input("Ingrese Valor en miarreglo[" + str(i) + ']:'))

def udfMuestraModifica(mipArreglo, pPosic,pValor):
    #Carga Tradicional Arreglo
    mipArreglo[pPosic] = pValor

def udfMuestraVector(mipArreglo, pTam):
    for i in range (0,pTam,1):
        print(f'Arreglo[{i}]:{mipArreglo[i]}')

def udfMaximoVector(mipArreglo, pTam):
    for i in range (0,pTam,1):
        if i==0:
           miMax=mipArreglo[i]
           posicMax=i
        else:
            if mipArreglo[i]>miMax:
                miMax = mipArreglo[i]
                posicMax = i

    return miMax,posicMax


#----------Programa Principal-------------------
#Definicion y dimensionamiento
miArreglo = arr.array('i',range(5))
viCantElem=len(miArreglo)
viOpcion=-1 #Global
while viOpcion!=5:
    print('1-Carga')
    print('2-Modifica')
    print('3-Muestra')
    print('4-Maximo')
    print('5-Salir')
    viOpcion=int(input("Seleccione:"))

    if viOpcion==1:
        udfMuestraVector(miArreglo,viCantElem)
        udfCargaVector(miArreglo,viCantElem)
    elif viOpcion == 2:
        udfMuestraModifica(miArreglo, 2,999)
    elif viOpcion == 3:
        udfMuestraVector(miArreglo, viCantElem)
    elif viOpcion == 4:
        Valor1,Valor2=udfMaximoVector(miArreglo, viCantElem)
        print('Maximo',Valor1,Valor2)
    elif viOpcion == 5:
        print('Salir')
    else:
        print('Incorrecto')





