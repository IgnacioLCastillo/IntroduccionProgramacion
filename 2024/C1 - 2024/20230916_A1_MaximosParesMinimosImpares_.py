#Ingresar numero enteros.
#el programa finaliza cuando se ingresan 10 numeros. o se coloca 0
#El programa debe informa el menor numero ingresado Impar y posicion y el maximo ingresardo Par y posiciion.
canNume=5
i=1
miNro=-1
cantPar=0
cantImp=0
min=0
max=0
minPos=0
maxPos=0
while i<=canNume and miNro!=0:
    miNro=int(input("Ingrese un numero# "+str(i)+": "))
    if miNro>=0:
        if miNro%2==0:
            cantPar=cantPar+1
            if cantPar==1:
                max = miNro
                maxPos = i
            else:
                if miNro > max:
                    max = miNro
                    maxPos = i
        else:
            cantImp=cantImp+1
            if cantImp==1:
                min = miNro
                minPos = i
            else:
                if miNro<min:
                    min=miNro
                    minPos = i
    i+=1

if cantImp!=0:
    print("El minimo Impar es",min,"y esta en la posicion",minPos)

if cantPar!=0:
    print("El maximo Par es",max,"y esta en la posicion",maxPos)
