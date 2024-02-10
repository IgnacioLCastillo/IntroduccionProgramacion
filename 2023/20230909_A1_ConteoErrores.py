#Ingresar numero enteros positivos.
# El programa finaliza cuando comete 3 errores
#considermos error al ingreso de un numero negativo o cero.
cantOpciones=3
contErrores=0
while contErrores<cantOpciones:
    numero=int(input("Ingrese un numero: "))
    if numero<=0:
        #continue me manda al while e ignora el resto del codigo
        contErrores+=1
        print(f"Error de {cantOpciones} intentos hay {contErrores} errores")
    if numero == 999: #Este break es para salir del while y no ejecuta el else
        break

else:
    print("Fin del programa")


