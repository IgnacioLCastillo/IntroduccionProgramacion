'''
Hacer un algoritmo que se ingresan 10 números enteros mayores a cero, mostrar por pantalla la
cantidad de números pares que se ingresaron.

Algoritmo DiezNumeros
	para CadaNumero=1 Hasta 10
		Leer miNro

		Si miNro%2=0 Entonces
			Escribir "Es par"
			contPar=conPar+1
		FinSi

	FinPara

		Escribir "La cantidad de Pares fueron",conPar
FinAlgoritmo
'''
contPar=0
for CadaNumero in range(1,11,1):
    miNro=int(input("Ingrese el numero #"+str(CadaNumero)+" :"))
    if miNro<=0:
        print("Es cero o Negativo")
    else:
        if miNro%2==0:
            print("Es par")
            contPar=contPar+1
            print("La cantidad de Pares son", contPar)


