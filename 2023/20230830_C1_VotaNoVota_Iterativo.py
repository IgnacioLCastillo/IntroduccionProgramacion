'''Algoritmo Decision
	contVotSi=0
	conVotoNo=0
	Para cadaVotante=1 Hasta 5 Hacer
		Escribir "Ingrese la Edad:"
		Leer Edad
		Escribir "Ingrese la Nacionalidad"
		Leer Nacionalidad
		Si Edad>16 Entonces
			Si Nacionalidad = 'AR' Entonces
				Escribir "Puede VOTAR"
				contVotSi=contVotSi+1
			SiNo
				Escribir "No Puede VOTAR por Nacionalidad"
				conVotoNo=conVotoNo+1
			FinSi
		SiNo
			Escribir "No vota porque es Menor"
			conVotoNo=conVotoNo+1
		FinSi
	FinPara
FinAlgoritmo'''
conVotSi=0
conVotNo=0
promedioVotanteSI=0
acumuladorEdadesSI=0
for cadaVotante in range(1,6,1):
    print('Votante Nro:',cadaVotante)
    miEdad = int(input("Ingrese la Edad:"))
    miNacionalidad = input("Ingrese la Nacionalidad:")

    if miEdad >= 16:
        if miNacionalidad.upper() == 'AR':
            print("Podes Votar por cumplir Ambos Requisitos")
            conVotSi=conVotSi+1
            acumuladorEdadesSI=acumuladorEdadesSI+miEdad
        else:
            print("No Podes Votar. Sos mayor, pero no Argentino")
            conVotNo = conVotNo + 1
    else:
        print("No Podes Votar porque sos Menor")
        conVotNo = conVotNo + 1

print(f"Votan {conVotSi} personas y el promedio de edad fue {acumuladorEdadesSI/conVotSi}", )
print("No Votan",conVotNo,"personas")
