#Iteracion simple
for i in range(1,5,1):
    print (i)
#Emular for con while
i=1
while i<5:
    print (i)
    i+=1

#Anidamiento de iteraciones con for
for i in range (1,5,1):
    for j in range (1,3,1):
        for w in range (1,3,1):
            print('I=',i,'J=',j,'W=',w)
#Anidamiento de iteraciones con while (todo a mano controlar)
i=1
while i<5:
    j=1
    while j<3:
        w=1
        while w<3:
            print('I=',i,'J=',j,'W=',w)
            w+=1
        j+=1
    i+=1
