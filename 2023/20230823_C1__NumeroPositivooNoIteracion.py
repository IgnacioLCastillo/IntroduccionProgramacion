'''
Algoritmo EstrucDecision

	Para i<-1 hasta 5 Hacer
		Leer Num
		Si Num>0 Entonces
			Escribir "Es positivo"
		SiNo
			Escribir "No es positivo"
			Escribir "Confirmo que no es positivo"
		FinSi
	FinPara
FinAlgoritmo
'''
#Ingresar 5 numeros y decir si es positivo o no

for i in range(1,6):
    otraVariable=int(input("Ingrese un numero: "))
    if otraVariable>=0:
        print("Positivo o Cero",otraVariable)
    else:
        print("Es Negativo",otraVariable)


