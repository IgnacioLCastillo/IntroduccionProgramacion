import time
limH = int(input("Ingrese la cantidad de horas: "))
limM = int(input("Ingrese la cantidad de minutos: "))
limS = int(input("Ingrese la cantidad de segundos: "))
for h in range(24):
    for m in range(60):
        for s in range(60):
            print(f"{h}:{m}:{s}")
            time.sleep(1)
            if h==limH and m==limM and s==limS:
                print("Interruptor de ciclo")
                break
                ##exit(1)