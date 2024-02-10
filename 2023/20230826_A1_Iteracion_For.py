'''para i=1 hasta 11 hacer
    imprimir i
'''


for i in range(1,10,1):
    print('Incremental',i)

for i in range(10,0,-1):
    print('Decreciente',i)


tope=int(input('Ingrese el tope: '))
for i in range(0,tope,2):
    print(i)

for i in range(1,tope):
    if i%2==0:
        print(i)
