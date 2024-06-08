

def udfContarVocales(palabra):
    contador = 0
    for i in range(0,len(palabra),1):
        if palabra[i].upper() in 'AEIOU':
            contador += 1
    return contador


def mimain():
    miPalabra= input("Ingrese una palabra: ")
    lrecibidasvocales = udfContarVocales(miPalabra)
    print(f'La palabra {miPalabra} tiene {lrecibidasvocales} vocales')
    porcentajeVocales=100-(lrecibidasvocales/len(miPalabra)*100)
    print(f'Las vocales representan %{porcentajeVocales} sobre las conosonantes')
    print('las vocales representan %{:.2f} sobre las conosonantes'.format(porcentajeVocales))
    print('las vocales representan %{3.4f} sobre las conosonantes'.format(porcentajeVocales))



#*-*-*-*-AREA PUBLICA*-*-*-*--*-
mimain()