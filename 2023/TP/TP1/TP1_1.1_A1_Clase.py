#utf-8
#Resuelto mediante multiplicacion explicita.
def multiplica(pnumero,pi):
    return pnumero*pi

def mimain():
    miNumero=int(input("Ingrese la tabla de multiplicar que desea ver: "))
    for i in range(1,11,1):
        print(f"{miNumero} x {i} = {multiplica(miNumero,i)}")

#-------
mimain()



'''
Algoitmos
ENTRADAS> un numero. usuarios
PROCESOS> multiplicar el numero por 1,2,3,4,5,6,7,8,9,10
SALIDA > la tabla de multiplicar del numero ingresado

#Forma 1
def mimain():
    unnumero=int(input("Ingrese un numero: "))
    for i in range(1,11,1):
        print(f'Tabla del {unnumero}*{i}-->{unnumero * i}')

#Forma 2
i=1
unnumero=int(input("Ingrese un numero: "))
while i<=10:
    print(f'Tabla While del {unnumero}*{i}-->{unnumero * i}')
    i += 1


#Forma 3
#resuelto mediante sumas consecutivas
miNumero=int(input("Ingrese un numero: "))
resultado=0
i=0
while resultado<50:
    i+=1
    resultado=resultado+miNumero
    print(f"Tabla Sumatoria Consecutivas: {miNumero} x {i}  = {resultado}")
'''