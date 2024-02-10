'''
         # {1,3,5,7,9}
for i in range(1,10,2):
    print(i)
'''

#Ingresar palabras. Realizar el conteo de sus vocales y consonantes.

miPalabra=input("Ingrese una palabra:")
miPalabra=miPalabra.lower()
contA=0
contE=0
contI=0
contO=0
contU=0
contConsonantes=0
                  #{N,E,U,Q,U,E,N}
for cadaLetra in miPalabra:
    '''
        if cadaLetra == 'a':
            contA+=1
        elif cadaLetra == 'e':
            contE+=1
        elif cadaLetra == 'i':
            contI+=1
        elif cadaLetra == 'o':
            contO+=1
        elif cadaLetra == 'u':
            contU+=1
        else:
            contConsonantes+=1
    '''
    match cadaLetra:
        case 'a':
            contA+=1
        case 'e':
            contE+=1
        case 'i':
            contI+=1
        case 'o':
            contO+=1
        case 'u':
            contU+=1
        case _:
            contConsonantes+=1

'''            
        if cadaLetra == 'a':
            contA+=1
        else:
            if cadaLetra == 'e':
                contE+=1
            else:
                if cadaLetra == 'i':
                    contI+=1
                else:    
                    if cadaLetra == 'o':
                        contO+=1
                    else:
                        if cadaLetra == 'u':
                            contU+=1
                        else:
                            contConsonantes+=1
        '''

print(f"La palabra '{miPalabra}' tiene:")
print(f"- {contA} letras 'a'")
print(f"- {contE} letras 'e'")
print(f"- {contI} letras 'i'")
print(f"- {contO} letras 'o'")
print(f"- {contU} letras 'u'")
print(f"- {contConsonantes} letras consonantes")




