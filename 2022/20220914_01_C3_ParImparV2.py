viAcumPar=0
viContPar=0
viAcumImPar=0
viContImPar=0

viCantNum=int(input("Ingrese la cantidad de numeros a ingresar:"))
for i in range(1,viCantNum+1,1):
    viMiNro=int(input("Ingrese Un Nro:"))
    if viMiNro !=0:
        if viMiNro%2==0:
            print ("Es par el numero:", viMiNro)
            viAcumPar=viAcumPar+viMiNro #Acumulador de Pares
            viContPar=viContPar+1 #Contador de Pares
        else:
            print("Es Impar el numero:", viMiNro)
            viAcumImPar = viAcumImPar + viMiNro  # Acumulador de ImPares
            viContImPar = viContImPar + 1  # Contador de ImPares
    else:
        break

if viContPar>0:
    print("El promedio Pares es ",viAcumPar/viContPar)
else:
    print("No Hubo Valores Pares en los ingresos")

if viContImPar>0:
    print("El promedio Impares es ",viAcumPar/viContImPar)
else:
    print("No Hubo Valores Impares en los ingresos")