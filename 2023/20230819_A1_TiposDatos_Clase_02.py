'''
Este codigo muestra algunos ejempo de variables y constantes
Ademas mostramos el uso de la sangria y vemos algunos tipos de datos
'''

#Este codigo muestra algunos ejempo de variables y constantes
#Ademas mostramos el uso de la sangria y vemos algunos tipos de datos

import misConstantes

numero= 10 #mensaje ayuda <class int>
numero = 11.3 #mensaje ayuda <class float>
numero = "Hola" #mensaje ayuda <class str>
numero = True #mensaje ayuda  <class bool>

print ("vamos a ver que vale numero y con que tipo de dato es:",numero,type(numero))

y=4
print("Muestro antes de pisar",y)
y=8+7+\
  6+5+\
  4+3+\
  2+1

y=(8+7+
  6+5+
  4+3+
  2+1)
x=4;
x=5
a=1;b=2;c=3
X=5 #Esta X mayuscula no es lo mismo que la x minuscula
xglobal=6
miNombre="Juan"
print("Salida de x",y,X)
print("Mi nombre es:",miNombre)
print("Salida abc",a,b,c)

j=i=h=1

print("Salida jih",i,j,h)

PI = 3.14

if a==99:
    print("es uno")

print(True==1)
print(True==0)
print(False==0)
print(False==1)

probCasteo='1.5'
print(probCasteo+'999') #Concatenacion Solo texto

probCasteo='1.5'
print(probCasteo+str(999)) #Concatenacion Solo texto porque pude castear el 999 antes

probCasteo=float('1.5') #Casteo implica la conversion de un tipo de dato a otro
print(probCasteo+999)



