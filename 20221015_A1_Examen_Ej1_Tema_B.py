
continua='S'
contDias=1
sumaTem=0

#dicDiasSemana = {1:"Lunes", 2:"Martes", 3:"Miercoles", 4:"Jueves",5:"Viernes",6:"Sabado",7:"Domingo"}

while contDias<=7 and continua.upper()=='S':
    viTempe=int(input("Ingrese Temperatura dia("+str(contDias)+"):"))
    sumaTem=sumaTem+viTempe
    if contDias==1:
       maximo=viTempe
       DiaMayor=contDias
    else:
            if viTempe>maximo:
                maximo = viTempe
                DiaMayor = contDias
    continua=input("Continua S/N ?")
    if continua.upper()=='S':
        contDias+=1

if DiaMayor>0:
    if contDias == 1:
        diaTexto = 'Lunes'
    elif contDias == 2:
        diaTexto = 'Martes'
    elif contDias == 3:
        diaTexto = 'Miercoles'
    elif contDias == 4:
        diaTexto = 'Jueves'
    elif contDias == 5:
        diaTexto = 'Viernes'
    elif contDias == 6:
        diaTexto = 'Sabado'
    elif contDias == 7:
        diaTexto = 'Domingo'

    print("El promedio DE TEMPERATURA es",sumaTem /contDias)
    #print(f"La maxima temperatura fue {maximo} el dia {dicDiasSemana[contDias]}")
    print(f"La maxima temperatura fue {maximo} el dia {diaTexto}")
