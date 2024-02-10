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

miEdad = int(input("Ingrese la Edad:"))
miNacionalidad = input("Ingrese la Nacionalidad:")
if miEdad >= 16 or miNacionalidad.upper() == 'AR':
    if miEdad >= 16:
        if miNacionalidad.upper() == 'AR':
            print("Podes Votar por cumplir Ambos Requisitos")
        else:
            print("No Podes Votar. Sos mayor, pero no Argentino")
    else:
        print("No Podes Votar porque sos Menor")
else:
    print("No cumple ningun requisito")
