'''Algoritmo VotaNoVota
	Escribir "Ingrese Edad:"
	Leer laEdad
	Escribir "Ingrese Nacionalidad"
	Leer laNacionalidad
	Si laEdad >= 16 Entonces
		Si laNacionalidad = 'AR' Entonces
			Escribir "Puede Votar"
		SiNo
			Escribir "No puede por Nacionalidad"
		FinSi
	SiNo
		Escribir "No vota por tema de Edad"
	FinSi
FinAlgoritmo
'''

edad = int(input("Ingrese Edad:"))
nacion = input("Ingrese Nacion:")

if edad < 16 and nacion.upper() != 'AR' :
    print ("No vota porque no cumlpe ningun requisito")
else:
    if edad >= 16:
        if nacion.upper() == 'AR':
            print('Vota ')
        else:
            print("No vota no es Argentino")
    else:
        print("No vota no cumple requisito Edad")
