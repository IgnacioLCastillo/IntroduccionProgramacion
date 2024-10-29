def udfMinumeroMas(p1=0):
    x=99 #Alcance local. Vive dentro de mi udf
    print("Print 1",x)
    print("Print 2",p1)

#--------------------------AREA GLOBAL--------------------------
x=5
print("Print 0",x)
udfMinumeroMas(6)

#print(localX) no la puedo invocar desde

