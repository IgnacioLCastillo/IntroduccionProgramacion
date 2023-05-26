cuenta=0
acumula=0
for i in range(1,6,1): #inicio en 1 hasta 5 (6 no cuenta) Paso en 1
    miNumero = int (input("Numero:"))
    if miNumero%2 == 0:
        cuenta=cuenta+1
    else:
        acumula=acumula+miNumero

print (acumula)
print (cuenta)



