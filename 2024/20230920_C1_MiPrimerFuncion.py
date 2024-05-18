#----------------------
def udfDuplicaTriplica(p1,p2):
    factor2=2 #Variable Local
    factor3=3
    if p2==1:
        return p1*factor2
    elif p2==2:
        return (p1*factor3)


def udfConDefault(p1,p2=2):
    return p1*p2

def udfReferencia(p1):
    return p1+5

#---Programa principal
def udfmain():
    numero=int(input("Ingrese un numero"))
    accion=int(input("1-Duplica / 2-Triplica"))
    #resul=udfDuplicaTriplica(numero,accion)
    print(udfDuplicaTriplica(numero,accion))
    print("Numero no cambia",numero)
    numero=udfReferencia(numero)
    print("Numero cambia (emulamos la referencia)",numero)
    print("Esto esta para evidenciar que los param fueron x valor", numero, accion)
    print("Aqui imprimo un resutado omitiendo el default",udfConDefault(numero,5))
    print("Aqui imprimo un resutado usando el default",udfConDefault(numero))


print("Bienvenido fuera")
#----------------------------------------------
a=5 #Global
udfmain()
#print(factor3) no funcionaria porque factor3 es local a la funcion udfDuplicaTriplica
