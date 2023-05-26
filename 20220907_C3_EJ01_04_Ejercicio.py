'''Algoritmo Ejericio1_4
	Leer numA
	Leer numB

	Si numB = 0 Entonces
		Escribir "No voy a poder dividir"
	SiNo
		Escribir "Division es:",numA/numB
	FinSi
	Escribir "Suma es:",numA+numB
	Escribir "Resta es:",numA-numB

FinAlgoritmo'''

numA = int(input('Ingrese un Numero A:'))
numB = int(input('Ingrese un Numero B:'))

if numB == 0:
    print('No voy a poder dividir')
else:
    print('La division es:', numA / numB)
    ##print('La division es: %2.2f' %(numA/numB))
print('La Suma es:', numA + numB)
print('La Resta es:', numA - numB)
print('La Multiplicación es:', numA * numB)

