#2.3. Hacer un algoritmo que se
# ingresan X números enteros, mostrar por pantalla la
# cantidad de números pares que se ingresaron.
# la sumatoria de ellos
#Este ejercicios es el 2.3 pero le agregamos mas cosas. Control de cantidad de ceros y
#Suma y cantidad de impares

#Pares
contPar=0
acumPar=0
contImPar=0
acumImPar=0
misCeros=0
cantNum=int(input("Cuantos numeros van a ingresar?:"))
for i in range(1,cantNum+1,1): #ini, tope, paso
    vmiNro=int(input("Ingreso mi Nro #"+str(i)+":"))
    if vmiNro!=0:
        if vmiNro%2==0:
            contPar=contPar+1
            acumPar=acumPar+vmiNro
        else:
            contImPar = contImPar + 1
            acumImPar = acumImPar + vmiNro
    else:
        misCeros+=1 #misCeros=misCeros+1

print ("La cantidad de pares es:",contPar)
print ("Lo Acumulado Par es:",acumPar)
print ("La cantidad de Impares es:",contImPar)
print ("Lo Acumulado Impar es:",acumImPar)
print ("Ceros ingresados",misCeros)
