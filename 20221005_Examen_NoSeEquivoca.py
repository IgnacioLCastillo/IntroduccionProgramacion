print("PARCIAL DE MATIAS DONADON")

i = 1
noSeEquivoca = True
contmult3 = 0
suma3=0
while i <= 10 and noSeEquivoca == True:
    miNum = int(input('Ingrese un Numero #' + str(i) + ':'))
    if miNum <= 0:
        noSeEquivoca = False
    else:
        if miNum % 3 == 0:
            print("Es multiplo de 3: ", i)
            contmult3 = contmult3 + 1
            suma3=suma3+miNum

        if i == 1:
            miMaxNum = miNum
            Lugar = i
        else:
            if miNum > miMaxNum:
                miMaxNum = miNum
                Lugar = i



    i += 1
print('Mi Numero maximo fue', miMaxNum, 'y se encontro en el Lugar', Lugar)

if contmult3>0:
    print("El promedio de Multiplos es de 3: ", suma3 / contmult3)