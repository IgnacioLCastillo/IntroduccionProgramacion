#Ingresar numero enteros.
#el programa finaliza cuando se ingresan 10 numeros. o se coloca 0
#El programa debe informa el menor y mayor numero ingresado
canNume=5
i=1
miNro=-1
while i<=canNume and miNro!=0:
    miNro=int(input("Ingrese un numero# "+str(i)+": "))
    if i==1:
        min=miNro
        minPos=i
        max = miNro
        maxPos = i
    else:
        if miNro<min and miNro!=0:
            min=miNro
            minPos = i
        else:
            if miNro>max and miNro!=0:
                max=miNro
                maxPos=i

    i+=1


print("El minimo es",min,"y esta en la posicion",minPos)
print("El maximo es",max,"y esta en la posicion",maxPos)
