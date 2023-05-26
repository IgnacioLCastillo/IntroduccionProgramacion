"""Este ejemplose utilizo para mostrar la sangria"""


for alumnos in range(1,4,1):
    edad=int(input("ingrese la edad"))
    nacionalidad=input("ingrese la Nacionalidad")
    if edad>=16 and nacionalidad == "AR":
        print("Voto OK")
    else:
        print("No Vota")