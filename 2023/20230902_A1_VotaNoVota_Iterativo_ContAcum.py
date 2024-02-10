'''Algoritmo Algoritmo_Vota_NoVota
	Escribir "Ingrese la Edad:"
	Leer Edad
	Escribir "Ingrese la Nacionalidad"
	Leer Nacionalidad
	Si Edad>=16 o Nacionalidad = 'AR'
		Si Edad >= 16 Entonces
			Si Nacionalidad = 'AR' Entonces
				Escribir "Podes Votar por cumplir Ambos Requisitos"
			SiNo
				Escribir "No Podes Votar. Sos mayor, pero no Argentino"
			FinSi
		SiNo
			Escribir "No Podes Votar porque sos Menor"
		FinSi
	SiNo
		Escribir "No cumple ningun requisito"
	FinSi
FinAlgoritmo'''
novota=0
sivota=0
edadAcum=0
cantidadVotantes=int(input("Ingrese la cantidad de Votantes:"))
#cantidadVotantes=cantidadVotantes+1
for cadaVotante in range(1,cantidadVotantes+1,1):
    miEdad = int(input("Ingrese la Edad del votante "+str(cadaVotante)+':'))
    miNacionalidad = input("Ingrese la Nacionalidad "+str(cadaVotante)+':')
    if miEdad >= 16 or miNacionalidad.upper() == 'AR':
        if miEdad >= 16:
            if miNacionalidad.upper() == 'AR':
                print("Podes Votar por cumplir Ambos Requisitos")
                edadAcum=edadAcum+miEdad
                sivota=sivota+1
                #sivota+=1
            else:
                print("No Podes Votar. Sos mayor, pero no Argentino")
                novota=novota+1
        else:
            print("No Podes Votar porque sos Menor")
            novota = novota + 1
    else:
        print("No cumple ningun requisito")
        novota = novota + 1

edadProm=edadAcum/sivota
print("No votan",novota,"personas")
print("Si votan",sivota,"personas y la edad promedio de los votantes es",edadProm)
