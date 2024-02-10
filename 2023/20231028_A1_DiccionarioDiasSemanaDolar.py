# -*- coding: utf-8 -*-

'''Diccionarios:
Mutables: Los diccionarios son estructuras de datos mutables que almacenan pares clave-valor.
No ordenados: Los elementos de un diccionario no están ordenados y se acceden mediante una clave en lugar de un índice.
Claves únicas: Las claves en un diccionario son únicas; no puede haber claves duplicadas.
Sintaxis: Se definen mediante llaves y pares clave-valor, por ejemplo, mi_diccionario = {"clave1": "valor1", "clave2": "valor2"}.
'''

DiasSemana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"] #Aca hay una lista
PrecioDolar = {"Lunes":0, "Martes":0, "Miercoles":0, "Jueves":0, "Viernes":0, "Sabado":0, "Domingo":0}
#cargar el precio del dolar para cada dia
for dia in DiasSemana:
    PrecioDolar[dia] = float(input("Ingrese el precio del dolar para el día " + dia + ": "))

#mostrar el precio del dolar para cada dia
for elemento in PrecioDolar:
    print ("El precio del dolar para el día", elemento, "es:", PrecioDolar[elemento])



