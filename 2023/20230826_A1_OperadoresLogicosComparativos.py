# -*- coding: utf-8 -*-
#Mostramos Tipos de datos y conversiones
#implicitas y explicitas
numA=1
numB='3'
numC=1.1
resulUno=numA+numC #Autoconversion de tipos Implicita
resultadoDos=numA+int(numB) #Autoconversion de tipos Explicita (Casting)
#Autoconversion de tipos Implicita
print('Suma de Enterós',resulUno,'-->',resultadoDos)

# Teoria: Comparativos
# Mayor estricto >
print('Comparo 3 > 2 con resultado: ',3 > 2)
# Menor estricto <
print(2 < 2)
# Mayor o igual >=
print(2 >= 2)
# Menor o igual <=
print(2 <= 1)
# Es igual ==
print('Comparo si 2 == 1 con resultado: ',2 == 1)
# Diferente

print('Comparo si 2 != 2 con resultado: ',2 != 2)

# Teoria: Logicos AND OR NOT

x=False
y=False
print("Operación 1:", x and y)
print("Operación 2:", x or y)
print("Operación 3:", not x)

print("Operación 1:", 1 < 2 and 2 != 2)
print("Operación 2:", 1 < 2 and 2 == 2)
print("Operación 3:", 1 < 2 or 2 != 2)
print("Operación 4:", 4 < 2 or 2 != 2)
print("Operación 5:", not 4 < 2 and not 2 != 2)
