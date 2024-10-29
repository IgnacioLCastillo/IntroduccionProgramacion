vi_cantidad_vueltas = 6
valor_total = 1

for i in range (1,vi_cantidad_vueltas,1):

    while True:
        vi_tiempo_vuelta = int (input(f"Ingrese tiempo de vuelta {i} en segundos:"))
        if vi_tiempo_vuelta >0:
            break
        else:
            print("Error, un nùmero negativo no es posible")

    if i == 1:
       vi_mejor_tiempo_vuelta = vi_tiempo_vuelta
       vi_peor_tiempo_vuelta = vi_tiempo_vuelta
    else:
        if vi_tiempo_vuelta < vi_mejor_tiempo_vuelta:
            vi_mejor_tiempo_vuelta = vi_tiempo_vuelta
        elif vi_tiempo_vuelta > vi_peor_tiempo_vuelta:
            vi_peor_tiempo_vuelta = vi_tiempo_vuelta

    valor_total += vi_tiempo_vuelta

print(f"EL mejor tiempo fue: {vi_mejor_tiempo_vuelta}")
print(f"EL peor tiempo fue: {vi_peor_tiempo_vuelta}")
print(f"EL promedio de tiempo total fue: {valor_total/i}")