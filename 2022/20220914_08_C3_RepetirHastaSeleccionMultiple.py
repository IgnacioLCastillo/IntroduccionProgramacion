# Como el python no tiene una estrcutura repetir hasta, que nos deje entrar al ciclar y luego evalue salor
# lo que tenemos como herramoienta es colocar un while True: y luego romperlo con un break
# El while true asegura que entramos y luego salimos rompiendo el ciclo.
# Es lo mas parecido a un do while del lenguaje c, Repeat Until de Pascal o Repetir Hasta en Pseudocodigo.
while True:
#viOpcion=1             #Si lo hiciera con un while tradicional seria con estas
#while viOpcion!=4:     #dos lineas de codigo y sin interrumpir x break
    print ('1 .- Opcion 1')
    print ('2 .- Opcion 2')
    print ('3 .- Opcion 3')
    print ('4 .- Opcion 4')
    viOpcion=int(input('Ingrese la Opcion:'))
    if viOpcion == 1:
        print ('Selecciono 1')
    elif viOpcion == 2:
        print ('Selecciono 2')
    elif viOpcion == 3:
        print ('Selecciono 3')
    elif viOpcion == 4:
        print('Selecciono 4')
        break #Cortamos y rompemos el while
    else:
        print('Error Valido 1-4')


'''
match viOpcion:
    case 1:
        print ('Selecciono 1')
    case 2:
       print ('Selecciono 2')
    case 3:
       print ('Selecciono 3')
    case 4:
       print('Selecciono 4')
    case _:
       print('Errors')
'''
