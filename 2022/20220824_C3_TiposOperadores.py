## Operadores  Comparativos
print(1==1) #TRUE
print(1<=1) #TRUE
print(1<1) #FALSO
print(1>2) #FALSO
print(11>2) #VERDADERO
print(2>=2) #VERDADERO
print(2!=2) #FALSO <>
print(1!=2) #VERDADERO <>

## Operadores  Logicos
print("salida AND",1==1 and 1==1 ) #TRUE
print("salida AND",1==2 and 1==1 ) #FALSO
print("salida AND",1==1 and 2==1 ) #FALSO
print("salida AND",1==2 and 2==1 ) #FALSO

print("salida OR",1==1 or 1==1 ) #TRUE
print("salida OR",1==2 or 1==1 ) #VERDADERO
print("salida OR",1==1 or 2==1 ) #Verdadero
print("salida OR",1==2 or 2==1 ) #FALSO

print("salida OR Negado",not (1==1 or 1==1)) #Falso
print("salida OR Negado",not (1==2 or 1==1)) #Falso
print("salida OR Negado",not (1==1 or 2==1)) #Falso
print("salida OR Negado",not (1==2 or 2==1)) #Verdadero

#Operadores Asignacion
a=5 #Asignacion
a=a+5 #Asignacion y Suma Explicita
a=a+5 #Asignacion y Suma Explicita
a+=5 #Asignacion y Suma simplificada
print (a)