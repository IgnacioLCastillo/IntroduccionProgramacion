i=1
conError=0
hayunmuliplo=False
while conError<3:
    num=int(input("Ingrese un numero: "))
    if num%5==0:
        hayunmuliplo=True

    if num<=0:
        conError=conError+1

        print("Hay otra chance: ", 3-conError)
    else:
        if i==1:
            miMinimo=num
            posiMin=i
        else:
            if num<miMinimo:
                miMinimo=num
                posiMin=i

    i=i+1

print ("El minimo es ",miMinimo, 'en la iteracion',posiMin)
print (f"El minimo es {miMinimo} en la iteracion {posiMin}")

if hayunmuliplo:
    print("Hay por lo menos un multiplo de 5")
else:
    print("No hubo múltiplos de 5 en la secuencia ingresada")