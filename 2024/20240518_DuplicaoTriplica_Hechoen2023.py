def ufdMimenutipoProc():
    print("1-Doble")
    print("2-Triple")

def ufdMimenutipoFunc():
    print("1-Doble")
    print("2-Triple")
    fopcion=int(input("Ingrese una opcion"))
    if fopcion<1 or fopcion>2:
        return -1 #Retorna un valor de error
    return fopcion

def miFuncionDoble(pminumero):  # pminumero es un parametro de entrada formal
    return pminumero*2

def miFuncionTriple(p1):
    return p1*3

def udfmain():
    minumero=int(input("Ingrese un numero"))
    opcion=ufdMimenutipoFunc()
    if opcion==1:
        print(f"El doble de {minumero} es {miFuncionDoble(minumero)}") #minumero es un parametro actual
    elif opcion==2:
        print(f"El triple de {minumero} es {miFuncionTriple(minumero)}")
    elif opcion==-1:
        print("Opcion incorrecta")
#------------------------------------------------------
udfmain()