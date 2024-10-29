mejor_tiempo = 0
vi_suma_tiempos = 0
tiempo_promedio = 0
peor_tiempo = 0
tiempo_vuelta = 0

print("*******Bienvenido a las vueltas de Franco Colapinto ************")
print()
for i in range(1,6):
    while True:
        tiempo_vuelta = int(input(f"ingrese tiempo en segundos vuelta {i}: "))
        if tiempo_vuelta < 0:
            print("error no puede ingresar tiempo negativo")
            continue
        else:
            break

    if tiempo_vuelta == 0:
        print("el auto tuvo un problema")
        break

    vi_suma_tiempos += tiempo_vuelta
    vueltas_dadas = i + 1
    if i == 1:
        mejor_tiempo = tiempo_vuelta
        peor_tiempo = tiempo_vuelta
    else:
        if tiempo_vuelta > mejor_tiempo:
            mejor_tiempo = tiempo_vuelta
        elif tiempo_vuelta < peor_tiempo:
            peor_tiempo = tiempo_vuelta

print(f"el mejor tiempo es: {mejor_tiempo}")
print(f"el peor tiempo es: {peor_tiempo}")
print(f"el tiempo promedio de las vueltas es: {vi_suma_tiempos / vueltas_dadas}")
