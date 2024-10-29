
def udf_funcion1(pmivar2):
    print("Hola mundo",pmivar2)

def udf_funcion2(pmiVar):
    print(f"Hola mundo 2 {pmiVar}")

def mi_len(ppalabra):
    cantidad=0
    for letra in ppalabra:
        #print(letra)
        cantidad+=1
    return cantidad

def mimain():
    cantidad=99
    mivar2 = '2'  # Ambito Global
    mivar='1' #Ambito Local
    mitexto="Hola Mundo"
    mitexto2="Mundo"
    mivarint=int(mivar)
    print(mivarint)
    udf_funcion1(mivar)
    udf_funcion2(mivar2)
    resul=mi_len(mitexto)
    result2=mi_len(mitexto2)
    print(len(mitexto),cantidad,'Aca aparece milen:',resul,'Aca aparece milen:',result2)


#Programa Principal
mimain()
