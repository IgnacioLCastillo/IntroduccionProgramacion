'''OpcionDecision = -1
while OpcionDecision != 5:
    print("1-Sumarlos")
    print("2-Restarlos")
    print("3-Multiplicarlos")
    print("4-Dividirlos")
    print("5-Salir")
    OpcionDecision = int(input("Ingrese la opcion: "))

'''
numA= int(input("Ingrese el numero A: "))
numB= int(input("Ingrese el numero B: "))
while True:
    print("1-Sumarlos")
    print("2-Restarlos")
    print("3-Multiplicarlos")
    print("4-Dividirlos")
    print("5-Salir")
    OpcionDecision = int(input("Ingrese la opcion: "))
    '''if OpcionDecision == 1:
        print("Suma", numA + numB)
    elif OpcionDecision == 2:
        print("Resta", numA - numB)
    elif OpcionDecision == 3:
        print("Multiplicacion", numA * numB)
    elif OpcionDecision == 4:
        if numB == 0:
            print("No se puede dividir por 0")
        else:
            print("Division", numA / numB)
    elif OpcionDecision == 5:
        break
    else:
        print("Opcion incorrecta")
    '''
    match OpcionDecision:
        case 1:
            print("Suma", numA + numB)
        case 2:
            print("Resta", numA - numB)
        case 3:
            print("Multiplicacion", numA * numB)
        case 4:
            if numB == 0:
                print("No se puede dividir por 0")
            else:
                print("Division", numA / numB)
        case _:
            print('Errors')
    '''

    
    #en c lo van a encontar como
    #do
    #   bloque de codigo
    #while (condicion)
    #En pascal
    #repeat
    #   bloque de codigo
    #until (condicion)'''

