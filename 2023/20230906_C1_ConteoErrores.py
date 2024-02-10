#Ingresar numero enteros positivos.
# El programa finaliza cuando comete 3 errores o cuando se ingresan 10 numeros.
#considermos error al ingreso de un numero negativo o cero.
#El programa debe informar: la cantidad de numeros ingresados,
# la suma de los numeros ingresados,
# el promedio de los numeros ingresados.
# la cantidada de impares
cantVidas=3
cantErrores=0
contImpar=0
suming=0
conting=0
while cantErrores<cantVidas and conting<10:
    miNro=int(input("Ingrese un numero: "))
    if miNro>0:
        suming = suming + miNro
        conting = conting + 1
        if miNro%2!=0:
            contImpar+=1
    else:
        cantErrores = cantErrores + 1
        print(f"Error {cantErrores}/{cantVidas}")

print(f"Suma: {suming}")
print(f"Promedio: {suming/conting}")
print(f"Cantidad de impares: {contImpar}")
print(f"Cantidad de numeros ingresados: {conting}")

