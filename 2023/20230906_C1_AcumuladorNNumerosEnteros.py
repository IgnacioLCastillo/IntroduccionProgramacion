#Ejemplo Original con Break --------------------------------------------------
n=5
suma=0
i=1
while i<=n:
    suma=suma+i
    #i=i+1
    i+=1
    '''if i==3:
        break''' #break si lo pongo no ejecuta el else porque interrumpe
                 # y quita la naturalidad de corte de la estructura
else:
    print('La suma con While es',suma)

#Ejemplo bugueado con continue-----------------------------------
n=5
suma=0
i=1
while i<=n:
    if i==3:
        print(i)
        continue
    suma=suma+i
    #i=i+1
    i+=1
    print(i)
else:
    print('La suma con While es',suma)

#Sumatoria 5 primeros numeros con for-----------------------------------
suma=0
for i in range(1,6,1):
    suma=suma+i
    print('La suma con for es',suma)