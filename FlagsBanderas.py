#Una carrera los autos dan hasta 15 vueltas.
#Es de interes saber si alguno de los autos es color naranja
#En caso lo sea al finalizar indicar si hubo o no hubo
#Si hay un naranja dejo de cargar
flagHuboNaranja=False #hipotesis o estado inicial
#for ivuelta in range (1,16,1):
ivuelta =0

while ivuelta <= 15 and not flagHuboNaranja:
    ivuelta+=1
    vsColor=input ("Ingrese Color Auto "+str(ivuelta)+': ')
    if vsColor.upper() == 'NARANJA':
        flagHuboNaranja=True

#if flagHuboNaranja == True:
if flagHuboNaranja:
    print("Hubo al menos un auto Naranja")
else:
    print("No Hubo ni uno")

