# -*- coding: utf-8 -*-
'''
Algoritmo EntradasYSalidas
	Escribir "Ingrese La edad:"
	Leer edad
	Escribir "Cuantos años a futuro:"
	Leer edadIntervalo
	Escribir "Ingrese el Peso:"
	Leer peso
	result=edad+edadIntervalo
	Escribir 'En ', edadIntervalo," años voy a a tener ",result, "El peso es: ",peso
FinAlgoritmo
'''

edad=int(input("Ingrese La edad:"))
edadIntervalo=int(input("Cuantos años a futuro:"))
peso=float(input("Ingrese el Peso:"))
result=edad+edadIntervalo
#Diferentes formas de usar la salida print
print('En ', edadIntervalo," años voy a tener ",result, "El peso es: ",peso*1.40)
print(f'En {edadIntervalo} años voy a tener {result} El peso es: {peso*1.40}')
print("En {} años voy a tener {} El peso es: {}".format(edadIntervalo,result,peso*1.40))
print("En %d años voy a tener %d El peso es: %2.2f" % (edadIntervalo,result,peso*1.409876))



#Print con delimitadores
print(2,3,4,5,sep="|",end="*")
print(2,"|",3,"|",4,"|",5)