miPalabraClave='ELEFANTE'
miPalabraAcierto=''
misVidas=6
miIntento=''
misErrores=0

miLetra=input("Letra:")
print(miPalabraClave.index(miLetra))
miPalabraAcierto.insert(miPalabraClave.index(miLetra),miLetra)

print(miPalabraAcierto)