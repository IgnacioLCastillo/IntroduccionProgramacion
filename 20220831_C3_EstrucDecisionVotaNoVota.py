"""Algoritmo EstrucDecisionVotaNovota
	Leer edad
	Leer nacion
	Si edad > 16
		Si nacion='AR'
			Escribir "Vota porque cumple los dos requisitos"
		SiNo
			Escribir ("No vota por Incumplir Nacion")
		FinSi
	SiNo
		Si nacion<>'AR'
			Escribir "No Vota  porque es menor y x Nacion"
		Sino
			Escribir "No vota por menor aun siendo ARGENTINO"
		FinSi
	Finsi
FinAlgoritmo
"""

edad = int(input("Ingrese Edad:"))
nacion = input("Ingrese Nacion:")

if edad > 16:
    if nacion.upper() == 'AR':
        print('Vota porque cumple los dos requisitos')
    else:
        Escribir("No vota por Incumplir Nacion")
else:
    if nacion != 'AR':
        print("No vota porque es menor y x Nacion")
    else:
        print("No vota porque es menor aun siendo ARGENTINO")