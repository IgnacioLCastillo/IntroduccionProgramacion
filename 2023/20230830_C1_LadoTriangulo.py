# -*- coding: utf-8 -*-
'''
Algoritmo TipoTriangulo
	Para evaluarTriang = 1 Hasta 4
		Leer LadoA
		Leer LadoB
		Leer LadoC
		Si LadoA=LadoB Y LadoB=LadoC Entonces
			Escribir 'Equilatero'
		SiNo
			Si LadoA=LadoB O LadoB=LadoC O LadoC=LadoA Entonces
				Escribir 'Isosceles'
			SiNo
				Escribir 'Escaleno'
			FinSi
		FinSi
	finPara
FinAlgoritmo

if ladoA==ladoB and ladoB==ladoC:
    print("Es un triangulo equilatero")
elif ladoA==ladoB or ladoB==ladoC or ladoA==ladoC:
    print("Es un triangulo isosceles")
else:
    print("Es un triangulo escaleno")


'''

#Dada la longitud de los lados de un triángulo, determinar si es equilátero, isósceles o escaleno.
contEquilatero=0
contIsosceles=0
contEscaleno=0
cantidadTriangulos=int(input("Ingrese la cantidad de triangulos a evaluar:"))
for evaluarTriang in range(1,cantidadTriangulos+1,1):
    ladoA=int(input("Ingrese el lado A del triangulo "+str(evaluarTriang)+":"))
    ladoB=int(input("Ingrese el lado B del triangulo "+str(evaluarTriang)+":"))
    ladoC=int(input("Ingrese el lado C del triangulo "+str(evaluarTriang)+":"))
    if ladoA==ladoB and ladoB==ladoC:
        print("Es un triangulo equilatero")
        contEquilatero=contEquilatero+1
        #contEquilatero+=1
    else:
        if ladoA==ladoB or ladoB==ladoC or ladoA==ladoC:
            print("Es un triangulo isosceles")
            contIsosceles = contIsosceles + 1
        else:
            print("Es un triangulo escaleno")
            contEscaleno = contEscaleno + 1


print("Cantidad de triangulos equilateros: ",contEquilatero)
print("Cantidad de triangulos isosceles: ",contIsosceles)
print("Cantidad de triangulos escalenos: ",contEscaleno)
