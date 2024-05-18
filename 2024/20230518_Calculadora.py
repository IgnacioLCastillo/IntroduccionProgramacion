





def miMenu(pmiValor):
    mivalor=99
    print("Estoy en miMenu y quiero ser evidente y mostrar el resultado de lo recibido desde miMain",pmiValor)
    print(mivalor)
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")
    opcion = int(input("Ingrese una opcion: "))
    return opcion



def miMain():
    mivalor=10
    #print("Quiero ser evidente y mostrar la global sin pedir permiso",mivalor)
    opcion=44
    opcionrecibida=miMenu(mivalor)
    print("Opcion recibida: ",opcionrecibida)
    if opcionrecibida==1:
        print("Suma")
    elif opcionrecibida==2:
        print("Resta")
    elif opcionrecibida==3:
        print("Multiplicacion")
    elif opcionrecibida==4:
        print("Division")
    elif opcionrecibida==5:
        print("Salir")
    else:
        print("Opcion incorrecta")




#***********************Area Publica o Global del Programa***************
miMain()

