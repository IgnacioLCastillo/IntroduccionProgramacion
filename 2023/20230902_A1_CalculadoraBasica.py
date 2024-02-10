
cantNumeros=int(input("Ingrese la cantidad de numeros: "))
numA=int(input("Ingrese el numero A: "))
numB=int(input("Ingrese el numero B: "))
for i in range(1,cantNumeros+1,1):
    print("1-Sumarlos")
    print("2-Restarlos")
    print("3-Multiplicarlos")
    print("4-Dividirlos")
    OpcionDecision=int(input("Ingrese la opcion: "))
    if OpcionDecision==1:
        print("Suma",numA+numB)
    elif OpcionDecision==2:
        print("Resta",numA-numB)
    elif OpcionDecision==3:
        print("Multiplicacion",numA*numB)
    elif OpcionDecision==4:
        if numB==0:
            print("No se puede dividir por 0")
        else:
            print("Division",numA/numB)
    else:
        print("Opcion incorrecta")


'''
    match OpcionDecision:
        case 1:
            print('Selecciono 1')
        case 2:
            print('Selecciono 2')
        case 3:
            print('Selecciono 3')
        case 4:
            print('Selecciono 4')
        case _:
            print('Errors')
'''
'''
    if OpcionDecision==1:
        print("Suma")
    else:
        if OpcionDecision==2:
            print("Resta")
        else:
            if OpcionDecision==3:
                print("Multiplicacion")
            else:
                if OpcionDecision==4:
                    print("Division")
                else:
                    print("Opcion incorrecta")
'''