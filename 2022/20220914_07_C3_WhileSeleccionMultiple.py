'''
Algoritmo Ejericio_MenuOpciones_Mientras
	viOpcion <- 1
	Mientras viOpcion < 4 Hacer
		Escribir '1- Opcion 1'
		Escribir '2- Opcion 2'
		Escribir '3- Opcion 3'
		Escribir '4- Opcion 4'
		Escribir 'Ingrese un Opcion 1-4'
		Leer viOpcion
		Segun viOpcion Hacer
			1:Escribir "Eligió 1"
			2:Escribir "Eligió 2"
			3:Escribir "Eligió 3"
			4:Escribir "Eligió 4"
			De Otro Modo: Escribir "Error en la Eleccion"
		Fin Segun
	FinMientras
FinAlgoritmo
'''
# Inicializo para que ingrese al ciclo. Luego veo como salgo...
viOpcion=1
#...pero no lo interrumpo con break. Se interrumpe cuando verifica que la condicion
# logica viOpcion < 4 no se cumple y corta.
while viOpcion<4:
    print ('1 .- Opcion 1')
    print ('2 .- Opcion 2')
    print ('3 .- Opcion 3')
    print ('4 .- Opcion 4')
    viOpcion=int(input('Ingrese la Opcion:'))
    if viOpcion == 1:
        print ('Selecciono 1')
    elif viOpcion == 2:
        print ('Selecciono 2')
    elif viOpcion == 3:
        print ('Selecciono 3')
    elif viOpcion == 4:
        print('Selecciono 4')
    else:
        print('Error')

'''
match viOpcion:
    case 1:
        print ('Selecciono 1')
    case 2:
       print ('Selecciono 2')
    case 3:
       print ('Selecciono 3')
    case 4:
       print('Selecciono 4')
    case _:
       print('Errors')
'''
