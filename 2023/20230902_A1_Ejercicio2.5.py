iteraciones = int(input("Ingrese el tope: "))

for i in range(1,iteraciones+1,2):
    ## Esta logica la hice para que el ultimo no imprima la coma
    ## Si fuese los 20 los numeros, el ultimo seria el 19.
    ## Cuando llegue a 19 (interaciones-1) no imprimo la coma
    if i==iteraciones-1: ## Esta logica la hice para que el ultimo no imprima la coma
        print(i,end='')
    else:
        print(i,end=',')

'''
print('------------------')
for i in range(1,iteraciones+1,1):
    if i%2!=0:
        print(i,end=',')
'''