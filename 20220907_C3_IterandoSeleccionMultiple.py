viOpcion = 0
while viOpcion!=4:
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
    else:
        print('Error')

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

'''
for i in range(0,10,2):
    print (i)
'''