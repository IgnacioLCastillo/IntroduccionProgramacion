"""
Se requiere el ingreso de la cantidad de alumnos a evaluar.
Una vez ingresada el algoritmo requiere capturar la menor/mayor edad
ingresada y la silla en la que estaba sentado.
En caso de inrgesar <=0 se interrumpe
"""
cantAlumnos=int(input("Ingrese Cantidad de Alumnos:"))
for isilla in range (1,cantAlumnos+1,1):
    viEdad=int(input("Edad de silla"+str(isilla)+':'))
    if viEdad<=0:
        break

    if isilla==1:
        viEdadMenor=viEdad
        viSillaMenor=isilla
        viEdadMayor=viEdad
        viSillaMayor=isilla
    else:
        if viEdad<=viEdadMenor:
            viEdadMenor = viEdad
            viSillaMenor = isilla
        else:
            if viEdad>=viEdadMayor:
                viEdadMayor = viEdad
                viSillaMayor = isilla

print ("La edad Minima encontrada es:",viEdadMenor,"y esta sentadx en",viSillaMenor)
print ("La edad Maxima encontrada es:",viEdadMayor,"y esta sentadx en",viSillaMayor)
