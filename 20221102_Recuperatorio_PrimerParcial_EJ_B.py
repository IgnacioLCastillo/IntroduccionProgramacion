cantM4=0
cantNeg=0
cantTotal=0
sumam4 = 0
while cantNeg < 3:
    miNumero = int(input('Ingrese Nro:'))
    if miNumero>0:
        cantTotal+=1
        if miNumero%4==0:
            sumam4+=miNumero
            cantM4+= 1
    else:
        cantNeg+=1

print (f"Cantidad total de numeros validos ingresados {cantTotal}")

if cantM4>1:
    print (f"El promedio de los multiplos de 4 es {sumam4/cantM4}")





