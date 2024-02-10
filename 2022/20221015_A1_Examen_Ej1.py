mes=1
viPasajeros=1
cont1S=0
cont2S=0
suma1S=0
suma2S=0
while mes<=12 and viPasajeros >0 :
    viPasajeros=int(input("Ingrese Pasajeros mes"+str(mes)+":"))
    if viPasajeros>0:
        if mes>=1 and mes<=6:
            suma1S=suma1S+viPasajeros
            cont1S+=1
        else:
            suma2S = suma2S + viPasajeros
            cont2S += 1

        if mes==1:
            minimo=viPasajeros
            mesMenor=mes
        else:
            if viPasajeros<minimo:
                minimo = viPasajeros
                mesMenor = mes
        mes+=1

if mes>0:
    print(f"El mes de menos pasajeros fue {mesMenor} con {minimo} ")
    print("El mes de menos pasajeros fue",mesMenor,"con ",minimo)
    print("El mes de menos pasajeros fue"+str(mesMenor)+" con "+str(minimo))
if cont1S>0:
    print("El promedio del primer semestre es",suma1S /cont1S)

if cont2S>0:
    print("El promedio del segundo semestre es", suma2S / cont2S)