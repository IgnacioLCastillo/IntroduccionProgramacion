#Una carrera los autos dan hasta 15 vueltas.
#Es de interes saber si alguno de los autos es color naranja
#En caso lo sea al finalizar indicar si hubo o no hubo
#Si hay un naranja dejo de cargar
'''
mivar=True
if mivar: #if mivar==True: #
    print("Es Verdadero")
else:
    print("Es Falso")
'''


flagHuboNaranja=False #hipotesis o estado inicial
ivuelta=0
while ivuelta < 5 and not flagHuboNaranja:
    ivuelta+=1
    vsColor=input ("Ingrese Color Auto "+str(ivuelta)+': ')
    if vsColor.upper() == 'NARANJA':
        flagHuboNaranja=True

#if flagHuboNaranja == True:
if flagHuboNaranja:
    print("Hubo al menos un auto Naranja")
else:
    print("No Hubo ni uno")

''' Emular una bandera usando un contador
ivuelta=0
cantNaraja=0
while ivuelta < 5 and cantNaraja==0:
    ivuelta+=1
    vsColor=input ("Ingrese Color Auto "+str(ivuelta)+': ')
    if vsColor.upper() == 'NARANJA':
        cantNaraja+=1

#if flagHuboNaranja == True:
if cantNaraja!=0:
    print("Hubo al menos un auto Naranja")
else:
    print("No Hubo ni uno")
'''