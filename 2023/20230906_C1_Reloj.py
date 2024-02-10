import time
import os
minutos = 0
horas = 0
segundos = 0

for horas in range(0, 24, 1):
    for minutos in range(0, 60, 1):
        for segundos in range(0, 60, 1):
            ##os.system("cls")
            print(horas, ':', minutos, ':', segundos)
            time.sleep(1)
            '''
            if horas==0 and m
            inutos==0 and segundos==15:
                print('Fin de segundos - Ciclo interrumpido')
                break
            '''