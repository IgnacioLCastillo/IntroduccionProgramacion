"""
Algoritmo ParImparSioNo
	Escribir "Entras (S/N)?"
	leer resp
	Mientras resp='S' Hacer
		Leer miNUmero
		Si miNumero%2 = 0 Entonces
			cont<-cont+1
	    FinSi
		Escribir "Sigo o no (S/N)?"
		leer resp
	FinMientras
	Escribir "La cantridad de Pares es",cont
FinAlgoritmo
"""
cont=0
resp=input ("Entramos?")
while resp.upper()=='S':
    miNumero=int(input("Ingrese Nro:"))
    if miNumero%2==0:
        cont+=1
    resp = input("Seguimos (S/N?")

print("La cantidad fue:",cont)

