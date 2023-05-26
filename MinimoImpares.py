i=1
sosPrimero=True
while i<=5:
   numero=int(input("Ingrese Numeros #"+str(i)+":"))
   i = i + 1
   if numero%2!=0:
       if sosPrimero:
           minimo=numero
           sosPrimero=False
       else:
           if numero<minimo:
               minimo=numero

if not sosPrimero: ##Al menos hubo un impar
    print("El minimo IMPAR es",minimo)
else:
    print ("Nunca ingreso impares")