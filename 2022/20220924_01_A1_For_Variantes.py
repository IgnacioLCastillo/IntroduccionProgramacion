#Incremental Paso en 1
for i in range(1,4,1): #ini, tope, paso
    print('i:',i)
#decremental Paso en -1
for j in range(3,0,-1): #ini, tope, paso
    print("j:",j)

#For Anidados i y j
for i in range(1,5,1): #ini, tope, paso
    for j in range(1,3,1): #ini, tope, paso
        print("i:",i,"j:",j)

#Pares
for i in range(0,22,2): #ini, tope, paso
    print('i:',i)
else:
    print("Ya no hay mas pares")

#ImPares
for i in range(1,22,2): #ini, tope, paso
    print('impar i:',i)

#Pares
for i in range(1,20,1): #ini, tope, paso
    if i%2==0:
        print('par i:',i)
        break
    else:
        print('Impar i:', i)