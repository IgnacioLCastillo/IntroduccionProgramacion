'''Algoritmo EjemploPara
	Para i<-1 hasta 5 Hacer
		Leer miNumero
		Si miNumero%2=0 Entonces
			Escribir "Es par el numero:",miNumero
		SiNo
			Escribir "Es Impar el numero:",miNumero
		FinSi
	FinPara
FinAlgoritmo'''

for i in range(1,11,1):
    ##for i in range(11): Asume el inicio en 0 y el paso en 1
    miNumero = int(input('Ingrese Numero #'+str(i)+':'))
    miotronumero=float(input('Ingreso Otro Numero'))
    if miNumero%2==0:
        print ("Es par el numero:", miNumero,miotronumero)
    else:
        print("Es Impar el numero:", miNumero)
        print("Y los impares me encantan")
