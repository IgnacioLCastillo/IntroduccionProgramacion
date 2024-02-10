# -*- coding: utf-8 -*-

'''Diccionarios:
Mutables: Los diccionarios son estructuras de datos mutables que almacenan clave-valor.
No ordenados: Los elementos de un diccionario no están ordenados y se acceden mediante una clave en lugar de un índice.
Claves únicas: Las claves en un diccionario son únicas; no puede haber claves duplicadas.
Sintaxis: Se definen mediante llaves y pares clave-valor, por ejemplo, mi_diccionario = {"clave1": "valor1", "clave2": "valor2"}.
'''

def mostrarTempSinSaberDiccionarios(ptemperaturas,pcantDias):
    diadesc=''
    for i in range(1,pcantDias,1):
        if i == 1:
            diadesc='Lunes'
        if i == 2:
            diadesc='Martes'
        if i == 3:
            diadesc='Miercoles'
        if i == 4:
            diadesc='Jueves'
        if i == 5:
            diadesc='Viernes'

    print(f"Temperatura del dia {diadesc} es {ptemperaturas[i]}")


def cargarTemp(ptemperaturas,pcantDias,pdiccDiaSemana):
    for i in range(0,pcantDias,1):
        diadesc=pdiccDiaSemana[i+1]
        ptemperaturas[i] = int(input(f"Ingrese la temperatura del dia {diadesc}"))


def cargarTempValidadas(ptemperaturas,pcantDias,pdiccDiaSemana):
    i=0
    while i< pcantDias:
        diadesc=pdiccDiaSemana[i+1]
        tempavalidar= int(input(f"Ingrese la temperatura del dia {diadesc}"))
        if tempavalidar < -10 or tempavalidar > 50:
            print("La temperatura debe estar entre -10 y 50")
        else:
            ptemperaturas[i] = tempavalidar
            i+=1


def mostrarTemp(ptemperaturas,pcantDias,pdiccDiaSemana,pdiasenIngles):
    pdiasenIngles['Lunes'] = 'Monday' #Mutables corrijo y puedo porque es mutable el diccionario
    for i in range(0,pcantDias,1):
        diadesc = pdiccDiaSemana[i + 1]
        print(f"Temperatura del dia {diadesc} es {ptemperaturas[i]}")
        print(f"The temperature of the day  {pdiasenIngles[diadesc]} is {ptemperaturas[i]}")


def mimain():
    import array as arr
    diccDiaSemana = {1: 'Lunes', 2: 'Martes', 3: 'Miercoles', 4: 'Jueves', 5: 'Viernes', 6: 'Sabado', 7: 'Domingo'}
    diasenIngles = {'Lunes': 'Mondai', 'Martes': 'Tuesday', 'Miercoles': 'Wednesday', 'Jueves': 'Thursday',
                    'Viernes': 'Friday', 'Sabado': 'Saturday', 'Domingo': 'Sunday'}
    while True:
        tamano = int(input("Ingrese la cantidad de dias a procesar"))
        if tamano < 0 or tamano > 7:
            print("Cantidad de dias incorrecta")
            continue
        else:
            break

    miTemperaturas = arr.array('d', range(tamano))
    #miTemperaturas = arr.array('d', [0.0, 0.0, 0.0,0.0,0.0])
    cargarTempValidadas(miTemperaturas,tamano,diccDiaSemana)
    mostrarTemp(miTemperaturas,tamano,diccDiaSemana,diasenIngles)

#----- Area Global -------
mimain()

