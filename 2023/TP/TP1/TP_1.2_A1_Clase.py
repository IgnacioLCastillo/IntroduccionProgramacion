# -*- coding: utf-8 -*-
'''ENTRADA: cant Numero a Ingresar
Proceso: Recibe numeros y se fija si esta 1 y 20.(Es bueno) Si esta entre 1 y 20 pregunto si es multiplo de 4… y si esto pasa suma y cuenta y lo promedia. Si es multiplo de 3.lo cuento.
Si es malo—informar y contar
Informar……Promedios 4 ,. Cantidad de los 3 y canrtidad de errores
'''

def misSalidas(psumaM4,pcuentaM4,pcuentaM3,pcuentamalos):
    if pcuentaM4>0:
        resultado=float(psumaM4/pcuentaM4)
        print(f"El promedio de los multiplos de 4 es  {resultado}")
    else:
        print("No se ingresaron multiplos de 4")
    if pcuentaM3>0:
        print(f"La cantidad de multiplos de 3 es {pcuentaM3}")
    else:
        print("No se ingresaron multiplos de 3")

    if pcuentamalos>0:
        print(f"La cantidad de numeros fuera de rango es {pcuentamalos}")
    else:
        print("No se ingresaron numeros fuera de rango")


def mimain():
    cantNumero=int(input("Ingrese la cantidad de numeros a ingresar"))
    cuentaM4=0
    sumaM4=0
    cuentaM3=0
    cuentamalos=0
    for i in range(1,cantNumero+1,1):
        numero=int(input("Ingrese el numero"))
        if numero>=1 and numero<=20:
            if numero%4==0:
                print(f"{numero}<<<---Numero multiplo de 4")
                cuentaM4=cuentaM4+1
                sumaM4=sumaM4+numero
            if numero%3==0:
                    print(f"{numero}<<<---Numero multiplo de 3")
                    cuentaM3=cuentaM3+1
        else:
            cuentamalos=cuentamalos+1
            print(f"{numero}<<<---Numero fuera de rango")

    misSalidas(sumaM4,cuentaM4,cuentaM3,cuentamalos)

#----
mimain()