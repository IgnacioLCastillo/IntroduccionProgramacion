'''Ingrsar un numero 10
Para (for 10)
	minumero=input()(akjsdnakjsdhja()
	Si minumero>=1 AND minumero<=20:
		Si minero %3==0
			cuento
		Si minero%4==0
cuenta
suema
ELSE:
	ERROR
	cuentamalos
'''

def udfcalculopromedio(pacumulado,pcantidad):
    if pcantidad>0:
        promedio=pacumulado/pcantidad
    else:
        promedio=0
    return promedio

def main():
    minumero=int(input("Coloque la cantidad de numeros a ingresar"))
    cuentamalos=0
    cuentaM3=0
    cuentaM4=0
    sumaM4=0
    for i in range(1,minumero+1,1):
        numero=int(input("Ingrese el numero"))
        if numero>=1 and numero<=20:
            if numero%3==0:
                cuentaM3=cuentaM3+1

            if numero%4==0:
                cuentaM4=cuentaM4+1
                sumaM4=sumaM4+numero
        else:
            cuentamalos=cuentamalos+1
            print(f"{numero}<<<---Numero fuera de rango")

    if cuentaM4>0:
        print(f"El promedio de los multiplos de 4 es {udfcalculopromedio(sumaM4,cuentaM4)}")

    if cuentaM3>0:
        print(f"La cantidad de multiplos de 3 es {cuentaM3}")

    if cuentamalos>0:
        print(f"La cantidad de numeros fuera de rango es {cuentamalos}")




