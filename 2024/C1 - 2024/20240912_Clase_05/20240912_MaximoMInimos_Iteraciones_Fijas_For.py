vi_cantidad_numeros= int(input("Ingrese la cantidad de numeros a ingresar: "))
for i in range(1,vi_cantidad_numeros+1):
    while True:
        vi_mi_numero= int(input(f"Ingrese un numero #{i}"))
        if vi_mi_numero>=0:
            break
        else:
            print("Error, debe ingresar un numero positivo")
    if i==1:
        vi_maximo=vi_mi_numero
        vi_posicion_minimo=i
        vi_minimo=vi_mi_numero
        vi_posicion_maximo=i
    else:
        if vi_mi_numero>vi_maximo:
            vi_maximo=vi_mi_numero
            vi_posicion_maximo=i
        elif vi_mi_numero<vi_minimo:
            vi_minimo=vi_mi_numero
            vi_posicion_minimo=i

print(f"El numero maximo es: {vi_maximo} y lo encontre en la posicion: {vi_posicion_maximo}")
print(f"El numero minimo es: {vi_minimo} y lo encontre en la posicion: {vi_posicion_minimo}")