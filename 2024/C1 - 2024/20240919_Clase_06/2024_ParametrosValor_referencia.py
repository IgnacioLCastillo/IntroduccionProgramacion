def udf_operacio(pa,pb):
    presul=pa+pb
    return presul

def udf_mimain():
    a=1
    b=2
    result=0
    result=udf_operacio(a,b)
    print(f"El resultado de sumar {a} y {b} es: {result}")


#Programa Principal
udf_mimain()