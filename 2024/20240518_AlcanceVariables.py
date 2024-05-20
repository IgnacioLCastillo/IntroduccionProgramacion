def udfMinumeroMas(p1):
    localX=99 #Alcance local. Vive dentro de mi udf
    print(globalA)
    '''Esto no me gusta porque la variable gobalA se mete en la funcion sin pedir permiso
    deberia en todo caso haber entrado como parametro'''
    print(localX)
    return p1+5

#--------------------------AREA GLOBAL--------------------------
globalA=5
print(udfMinumeroMas(globalA))
#print(localX) no la puedo invocar desde

