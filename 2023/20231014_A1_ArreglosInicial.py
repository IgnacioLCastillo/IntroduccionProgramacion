import random
import array as arr

#Realizar un ejercicio que permita la carga de un vector.
#La carga puede ser manual o Automatica.
#La carga manual debe verificar que solo se ingresen numeros pusitivos.
#En caso de colocar negativos o cero debe volver a solicitar la carga de la posicion.
#Los valores de las posiciones impares
#los valores pares

def mimenu():
    print("1. Cargar Arreglo Manual")
    print("2. Cargar Arreglo Random")
    print("3. Mostrar Arreglo")
    print("4. Mostrar Posiciones Impares")
    print("5- Maximo total")
    print("6- Minimo Impares")
    print("7. Copia de Vector Duplicado Valores")
    print("8. Salir")
    opcion=int(input("Ingrese Opcion:"))
    return opcion

def cargaVector(ptam,parreglo):
    for i in (range(0,ptam,1)):
        parreglo[i]=int(input(f"Ingrese Valor miArreglo[{i}]:"))

def cargaVectorValidada(ptam, parreglo):
    i=0
    while i<ptam:
        midato = int(input(f"Ingrese Valor miArreglo[{i}]:"))
        if midato > 0:
            parreglo[i] = midato
            i+=1
        else:
            print("No puede cargar datos negativos")

def udfMuestraVectorPares(ptam,parreglo):
    for i in (range(1, ptam, 2)):
        if parreglo[i]%2==0:
            print(f"Muestro Resultado miArreglo[{i}]={parreglo[i]}")

def udfMuestraVectorposicImpar(ptam,parreglo):
    for i in (range(1, ptam, 2)):
        #if i%2!=0:
        print(f"Muestro Resultado miArreglo[{i}]={parreglo[i]}")

def MinimodelosImpare(ptam,parreglo):
    contimp = 0
    for i in (range(0, ptam, 1)):
        if parreglo[i]%2!=0:
            if contimp==0:
                minvalorImp=parreglo[i]
                contimp+=1
            else:
                if parreglo[i]<minvalorImp:
                    minvalorImp = parreglo[i]
                    contimp += 1

    return minvalorImp

def muestravector(ptam,parreglo):
    # Rutina informa
    for i in (range(0, ptam, 1)):
        print(f"Muestro Resultado miArreglo[{i}]={parreglo[i]}")

#funcion para carga aleatoria
def cargaVectorRandom(ptam,parreglo):
    for i in (range(0,ptam,1)):
        parreglo[i]=random.randint(1, 100)

def udMaximoTotalArreglo(ptam,parreglo):
    maxval=parreglo[0]
    maxposic=0
    for i in (range(1, ptam, 1)):
        if parreglo[i]>maxval:
            maxval=parreglo[i]
            maxposic=i

    return maxval,maxposic


def udfCopiaVector(ptam,parreglooroginal,parregloCopiaDuplicado):
    for i in (range(0, ptam, 1)):
        parregloCopiaDuplicado[i]=parreglooroginal[i]*2


def mimain():

    miArreglo = arr.array('i', [0, 0, 0,0,0,0,0,0,0,0])
    miArregloDuplicado = arr.array('i', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    #miArreglo = arr.array('i', range(10))
    #Rutina de carga del Vector
    tam=len(miArreglo)

    while True:
        miopcionseleccionada=mimenu()
        if miopcionseleccionada==1:
            #cargaVector(tam,miArreglo)
            cargaVectorValidada(tam,miArreglo)
        elif miopcionseleccionada==2:
            cargaVectorRandom(tam,miArreglo)
        elif miopcionseleccionada==3:
            muestravector(tam,miArreglo)
        elif miopcionseleccionada==4:
            udfMuestraVectorposicImpar(tam,miArreglo)
        elif miopcionseleccionada == 5:
            maximoconseguido,posiconseguida=udMaximoTotalArreglo(tam, miArreglo)
            print(f"El maximo es:{maximoconseguido} y esta en la posicion {posiconseguida}")
        elif miopcionseleccionada == 6:
            minimoimparconseguido=MinimodelosImpare(tam,miArreglo)
            print(f"El minimo de los impares es {minimoimparconseguido}")
        elif miopcionseleccionada == 7:
            udfCopiaVector(tam,miArreglo,miArregloDuplicado)
            print("------Copia Satisfactoria--------------")
            input(())
            print("------Vector Resultado--------------")
            muestravector(tam, miArregloDuplicado)
        elif miopcionseleccionada==8:
            udfMuestraVectorPares(tam,miArreglo)
        elif miopcionseleccionada==9:
            print("Adios")
            break




#----------------- Area global----------
mimain()

'''
for i in range(0, 5, 1):
    num=int(input("Ingrese Valor"))
    if num%2==0:
        print(f'Par')

print (num)
'''