'''Algoritmo Ejericio1_17
	Leer LetraA
	Leer LetraB
	Si LetraA = LetraB
		Escribir "Son Iguales",LetraB,LetraA
	SiNo
    	Si LetraA > LetraB Entonces
    		Escribir "Orden",LetraB,LetraA
    	SiNo
    		Escribir "Orden:",LetraA,LetraB
    	FinSi
	FinSi
FinAlgoritmo
'''

letra1 = input('Ingrese primer Letra :')
letra2 = input('Ingrese segunda Letra :')

if letra1 == letra2:
    print('Son iguales',letra2,letra1)
else: 
    if letra1>letra2:
        print('Orden',letra2,letra1)
    else:
        print('Orden:',letra1,letra2)