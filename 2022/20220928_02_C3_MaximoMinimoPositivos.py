#Ingresa 5 Edades identificando el maximo y el minimo
#informar ademas la posicion en la que se los encontro.
#El algoritmo termina al llegar a 5 ingresos o cuando ingresa una edad negativa o 0

i=1
noSeEquivoca=True
#while i<5: Interrupiria solo si uso break
while i<5 and noSeEquivoca==True :
    miEdad=int(input('Ingrese Edad #'+str(i)+':'))
    if miEdad <=0:
        noSeEquivoca=False
        #break
    else:
        if i==1: #Si sos el primero sos maximo y minimo.
            miMaxEdad=miEdad
            miMaxSilla=i
            miMinEdad = miEdad
            miMinSilla = i
        else: #Para todos los demas que son los primeros voy evaluando si alguno le gana al maximo o al minimo
            if miEdad>miMaxEdad:
                miMaxEdad = miEdad
                miMaxSilla = i
            else:
                if miEdad<miMinEdad:
                    miMinEdad=miEdad
                    miMinSilla=i
    i+=1
print ('La edad maxima fue',miMaxEdad,'y se encontro en el banco',miMaxSilla)
print ('La edad minina fue',miMinEdad,'y se encontro en el banco',miMinSilla)


