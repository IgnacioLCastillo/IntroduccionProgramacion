'''
Algoritmo EstrucDecision
	leer a
	Si a>0 Entonces
		Escribir "Es positivo"
	FinSi
	Escribir "Chau"
FinAlgoritmo
'''
'''
a=int(input("Ingrese un numero: "))
if a>0: #Decision Simple
    print("Es positivo 1")
    print("Es positivo 2")

if a>0: #Decision Doble
    print("Es positivo 1")
    print("Es positivo 2")
else: #Decision Doble
    print("No es positivo 1")
'''

#Decision anidada
edad=int(input('Ingrese la edad: '))
nacionalidad=input('Ingrese la nacionalidad: ')
if edad>=16 or nacionalidad.upper()=='AR':
    if edad>=16:
            if nacionalidad.upper()=='AR':
                print('Podes votar')
            else:
                print('No Podes votar por tu nacionalidad')
    else:
        print('No Podes votar por tu edad')
else:
    print('No Podes votar por tu edad y nacionalidad')

