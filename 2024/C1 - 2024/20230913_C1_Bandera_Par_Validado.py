#Ingresar numeros positivos. En caso de ingresar un numero par el algorimto debera informarlo
#esa situacion
#Al ingresar un numero <=0 el programa informa como error ese valor y permite volver a cargarlo
#Al algoritmo finaliza cuiando se ingresan 5 numeros.
#Una forma (A) corrige i mediante la resta del indice i y en la otra forma (B) se utiliza el continue
#que nunca permite que se incremente el indice i
'''
#Forma A
topeNros = 5
i=0
huboPar=False
while i<topeNros:
    i += 1
    nro=int(input("Ingrese un numero: "+str(i)+"/"+str(topeNros)+": "))
    if nro<=0:
        print("Error")
        i-=1
    else:
        if nro%2==0:
            huboPar=True
'''

#Forma B
topeNros = 5
i=1
huboPar=False
while i<=topeNros:

    nro=int(input("Ingrese un numero: "+str(i)+"/"+str(topeNros)+": "))
    if nro<=0:
        print("Error")
        continue
    else:
        if nro%2==0:
            huboPar=True
    i += 1

if huboPar:
    print("Hubo un numero par")
else:
    print("Nunca cargo un numero par")