import array as arr
#Area de Definicion de Funciones Necesarias
def UDFDibujaMenu():
    print('1-Muestra')
    print('2-Promedio de Impares dentro del Rango')
    print('3-Maximo dentro del Rango')
    print('4-Salir')
    viOpcion = int(input("Seleccione:"))
    return viOpcion

def udfMuestraVector(mipArreglo, pTam):
    for i in range (0,pTam,1):
        print(f'Arreglo[{i}]:{mipArreglo[i]}')

#***********************Area Programa Principal********************************
miOpcion=-1 #Variable Global inicializada en -1 para que entre al menos 1 vez
miArreglo = arr.array('i',[3,4,6,7,9,2,1,5,8,4]) #Global
viCantElem=len(miArreglo) #Global
udfMuestraVector(miArreglo, viCantElem)

viRangoDesde=int(input("Posicion Rango desde:"))
viRangoHasta=int(input("Posicion Rango Hasta:"))

while miOpcion!=4:
    miOpcion=UDFDibujaMenu()
    if miOpcion==1:
         udfMuestraVector(miArreglo,viCantElem)
    elif miOpcion == 2:
        print('a desarrollar')
    elif miOpcion == 3:
        print('a desarrollar')
 #        break # Solo si usan un While True
    elif miOpcion == 4:
         print("---Fin Algoritmo----")
    else:
        print("Opcion Invalida")

