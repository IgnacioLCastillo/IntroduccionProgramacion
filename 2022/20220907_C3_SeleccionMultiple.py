'''
Algoritmo Ejericio_MenuOpciones
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
FinAlgoritmo'''
##viOpcion=0
##while viOpcion!=4:
while True:
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
        break
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
