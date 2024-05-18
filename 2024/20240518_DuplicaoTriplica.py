def udfMiMenuOpciones():
    print("****************Menu de Opciones*****************")
    print("1. Duplicar")
    print("2. Triplicar")
    print("3. Salir")
    opcion=int(input("Ingrese una opcion: "))
    return opcion


def udfMiDuplicado(pmiNumero):
    resultado=pmiNumero*2
    return resultado

def udfMiTriplicado(pmiNumero):
    resultado=pmiNumero*3
    return resultado

def udfDuplicaoTriplica(pmiNumero,pmiOpcion):
    if pmiOpcion==1:
        return pmiNumero*2
    elif pmiOpcion==2:
        return pmiNumero*3
    else:
        return -1


def udfMiDuplicadoconMensaje(pmiNumero):
    resultado=pmiNumero*2
    print("El resultado Duplicado es: ",resultado)

def udfMiTriplicadoConMensaje(pmiNumero):
    resultado=pmiNumero*3
    print("El resultado Triplicado es: ",resultado)


def miMain():
    print("****************Seccion Main*****************")
    miNumero=int(input("Ingrese un numero: "))
    opcionSeleccionada=udfMiMenuOpciones()
    print("Resultado recibido desde udfDuplicaoTriplica: ", udfDuplicaoTriplica(miNumero, opcionSeleccionada))
    if opcionSeleccionada==1:
        #Usando una variable de apoyo a la funcion
        resultadoRecibido=udfMiDuplicado(miNumero)
        print("Duplicado recibido desde udfMiDuplicado: ",resultadoRecibido)
        #Llamo al subprograma que muestra el resultado
        udfMiTriplicadoConMensaje(miNumero)

    elif opcionSeleccionada==2:
        # Directamente mostrando el resultado en el print
        print("Triplicado recibido desde udfMiTriplicado: ",udfMiTriplicado(miNumero))
        #Llamo al subprograma que muestra el resultado
        udfMiTriplicadoConMensaje(miNumero)
    elif opcionSeleccionada==3:
        print("Salir")
    else:
        print("Opcion incorrecta")


#****AreaPublica Inicio del Programa
miMain()