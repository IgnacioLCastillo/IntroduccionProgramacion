import array as arr
import random
vector1 = arr.array('i', range(5))
vector2 = arr.array('i', range(5))
vector3 = arr.array('i', range(5))

def Main():
    Menu()

def Menu():

    flag=True
    flag2=False
    flag3=False
    while flag:
        print(f"Ingrese la opcion a elegir")
        print(f"1-Cargar el vector")
        print(f"2-Clonar el vector y mostrarlo")
        print(f"3-Mostrar valores por encima del promedio")
        opcion= int (input(f"4-Salir "))
        match opcion:
            case 1:
                Carga(vector1,vector2)
                flag2=True
            case 2:
                if flag2==True:
                    Clonar(vector1,vector2,vector3)
                    Mostrar(vector1,vector2,vector3)
                    flag3=True
                else:
                    print(f"Primero debe cargar el vector")
            case 3:
                if flag3==True:
                    Promedio(vector3)
                    print(f"El valor promedio es: {Promedio(vector3)}")
                else:
                    print(f"primero debe clonar el vector")
            case 4:
               flag=False

def Carga(vector1,vector2):
    a=0

    while a<5:
        b = random.randint(1, 100)
        valor = int(input(f"Ingrese el valor para la posicion {a} "))
        if valor>0:
            vector1[a]=valor
            vector2[a]=b
            a=a+1
        else:
            print(f"Valor no valido")
    return

def Mostrar(vector1,vector2,vector3):

    for i in range (0,5,1):
        print(f"Valor en la posicion {i}  del vector manual {vector1[i]}")
    for i in range(0, 5, 1):
        print(f"Valor en la posicion {i} del vector aleatorio {vector2[i]}")
    for i in range(0, 5, 1):
        print(f"Valor en la posicion {i} del vector clonado {vector3[i]}")

def Clonar(vector1,vector2,vector3):

    for i in range(0,5,2):
        vector3[i]=vector1[i]*vector2[i]
    for i in range(1,5,2):
        vector3[i]=vector1[i]+vector2[i]
    return

def Promedio(vector3):
    acumulador=0
    for i in range(0,5,1):
        acumulador=acumulador+vector3[i]
        promedio = acumulador / 5

    for i in range(0,5,1):
        if vector3[i]>promedio:
            print(f"Los valores mayores al promedio son {vector3[i]}")

    return promedio

Main()
