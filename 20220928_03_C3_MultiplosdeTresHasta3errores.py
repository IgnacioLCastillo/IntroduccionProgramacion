#Ingresar numeros enteros positivos. En caso de ingresar
#un numero negativo interpretarlo como un error. El algoritmo finaliza cuando
#completa 10 numero o se equivoca 3 veces.
#Al finalizar informar el el maximo de los multiplos de 3

i=1
conError=0
cantMultiplos=0
sosPrimero=True #hipotesis multiplos de tres al menos 1 que si pasa a falso es porque encontro uno al menos

while i<=11 and conError<3:
    miNumero=int(input('Mi Numero '+str(i)+':'))
    if miNumero<0:
        conError=conError+1
        print ("Quedan Chances#",3-conError)
    else:
        if miNumero%3==0:
            cantMultiplos += 1
            #if sosPrimero==True:
            if cantMultiplos == 1:
                maxTres=miNumero
            #    sosPrimero=False
            else:
                if miNumero>maxTres:
                    maxTres=miNumero
    i+=1  #i=i+1

if cantMultiplos!=0:
#if sosPrimero == False
    print ("El maximo de los multiplos de tres es:",maxTres)
else:
    print("No hay ni uno:")
