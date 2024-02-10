miNumeroDesde=int(input("Ingrese dato X:"))
cantImp=1
acum=0
while cantImp <= 5:
    if miNumeroDesde%2!=0:
        print(f"Muestra Impar #{cantImp},{miNumeroDesde}")
        cantImp += 1
    else:
        acum=acum+miNumeroDesde

    miNumeroDesde+=1

print (f"La suma de los pares es {acum}")

'''
contpar=0
contimpar=0
sumtotal=0
prom=0
cont=int(input("digite numero:"))
for i in range(cont,cont+9,1):
        if i%2==0:
            print(i)
            contpar=contpar+i
            prom+=i

        else:
            print(f"{i} es impar")
print(f"la suma de pares {contpar}")

'''

