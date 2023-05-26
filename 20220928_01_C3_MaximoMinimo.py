#Ingresa 5 Edades identificando el maximo y el minimo
#informar ademas la posicion en la que se los encontro.
#  5 6 2 4 5 6 3 2 5 7
for i in range (1,5,1):
    miEdad=int(input('Ingrese Edad #'+str(i)+':'))
    if i==1:
        miMaxEdad=miEdad
        miMaxSilla=i
        miMinEdad = miEdad
        miMinSilla = i
    else:
        if miEdad>miMaxEdad:
            miMaxEdad = miEdad
            miMaxSilla = i
        else:
            if miEdad<miMinEdad:
                miMinEdad=miEdad
                miMinSilla=i

print ('La edad maxima fue',miMaxEdad,'y se encontro en el banco',miMaxSilla)
print ('La edad mimina fue',miMinEdad,'y se encontro en el banco',miMinSilla)


