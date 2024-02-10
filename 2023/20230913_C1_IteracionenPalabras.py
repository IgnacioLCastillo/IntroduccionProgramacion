'''
#{1,2,3,4,5,6,7,8,9}
for i in range (1,10,1):
    print (i)
'''
contA=0
contE=0
contI=0
contO=0
contU=0
contadorCons=0
palabra=input ("Ingrese una palabra: ")
for letra in palabra:
    match letra.lower():
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
            contadorCons+=1
    '''
    if letra.upper()=='A':
        contA+=1
    elif letra.upper()=='E':
        contE+=1
    elif letra.upper()=='I':
        contI+=1
    elif letra.upper()=='O':
        contO+=1
    elif letra.upper()=='U':
        contU+=1
    else:
        contadorCons+=1
'''
print(f"La palabra '{palabra}' tiene:")
print(f"- {contA} letras 'a'")
print(f"- {contE} letras 'e'")
print(f"- {contI} letras 'i'")
print(f"- {contO} letras 'o'")
print(f"- {contU} letras 'u'")
print(f"- {contadorCons} letras consonantes")
