#Area de definicion de funciones
def UDPSuma(px,py,pMensaje): #Mas parecido a un PROC
    i=100 #local a la fucion miUDFSuma
    print(pMensaje,px+py,px,py,100)

def UDFSuma(px,py): #nMas parecido a un Funcion Pura
    i=10 #local a la fucion miUDFSuma
    return(px+py+i)
#------------------------------
#------------------------------
resultado =0 #Global
i=99 #Global
#-----------ENTRADA-------------------
miValorA=int(input("Ingrese A"))
miValorB=int(input("Ingrese B"))
miTexto='El Resultado es:'
#------------PROC(FUNCION)------------------
UDPSuma(miValorA,miValorB,miTexto)
resultado=UDPSuma(miValorA,miValorB,miTexto) ## Seria un error porque UDPSuma no tiene Retorno
print ('Creo deberia ser None:',resultado)
#------------FUNCION------------------
resultado=UDFSuma(miValorA,miValorB)
print(resultado)
#------------INVOCO LA GLOBAL------------------
print (i) #Aca va a ser la i Global que tiene 99
#print('El resultado es',UDFSuma(miValorA,miValorB))
