'''
resultado=0
def UdfSumaEmulandoRef(paramA,paramB):
    global resultado
    resultado = (paramA+paramB)
'''
#--------------Area de Definicion de Funciones---------------
def USPDibuijaMenu():
    print('1-SUMA')
    print('2-RESTA')
    print('3-MULTI')
    print('4-DIVI')
    print('5-Salir')
    viOpcion=int(input("Seleccione:"))
    return viOpcion

def UDFSuma(paramA,paramB):
    paramA=9
    return (paramA + paramB)
    #coeficiente=1.20#Variable Local
   # return (paramA+paramB)*coeficiente
def UDFResta(pNumA,pNumB):
    return (pNumA - pNumB)

def UDFMulti(pNumA,pNumB):
    return (pNumA * pNumB)

def UDFDivi(pNumA,pNumB):
    if pNumB==0:
        return -1 #-1 implica un error
    else:
        return (pNumA / pNumB)
#------------Programa Principal-------------
viOpcionElegida=-1 #Global
miValorA=5
miValorB=0

while viOpcionElegida!=5:
    viOpcionElegida=USPDibuijaMenu()
    ##viOpcion=int(input("Seleccione:"))
    if viOpcionElegida==1:
        print (f"La suma de {miValorA} + {miValorB} es {UDFSuma(miValorA,miValorB)}")
    elif viOpcionElegida == 2:
        resultado=UDFResta(miValorA, miValorB)
        print(f"La Resta de {miValorA} - {miValorB} es {resultado}")
    elif viOpcionElegida == 3:
        print(f"La Multi de {miValorA} * {miValorB} es {UDFMulti(miValorA, miValorB)}")
    elif viOpcionElegida == 4:
        resultado = UDFDivi(miValorA, miValorB)
        if resultado!=-1:
            print(f"La Divi de {miValorA} / {miValorB} es {UDFDivi(miValorA, miValorB)}")
        else:
            print("Error en Division")
    elif viOpcionElegida == 5:
        print('Salir')
    else:
        print('Incorrecto')



