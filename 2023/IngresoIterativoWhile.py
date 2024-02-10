'''
cantNumeros=int(input("Ingrese la cantidad de numeros: "))
for i in range(1,cantNumeros+1,1):
    print("1-Sumarlos")
    print("2-Restarlos")
    print("3-Multiplicarlos")
    print("4-Dividirlos")
    OpcionDecision=int(input("Ingrese la opcion: "))
'''

respuesta=-1
while respuesta!=5:
    print("1-Sumarlos")
    print("2-Restarlos")
    print("3-Multiplicarlos")
    print("4-Dividirlos")
    print("5-Salir")
    respuesta=int(input("Ingrese la opcion: "))
