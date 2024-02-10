

def udfcargar(pvalores_destino,ptam):
    for i in range(ptam):
        pvalores_destino[i] = int(input("Ingrese un valor: "))

def promediovector(pvalores_destino,ptam):
    acumulador=0
    for i in range(ptam):
        acumulador=acumulador+pvalores_destino[i]
    promedio=acumulador/ptam
    return promedio


def mimain():
    import array as arr
    valores_origen = arr.array('i' , [0]*3)
    valores_origen2 = arr.array('i', [0] *3)
    valores_origen3 = arr.array('i', [0] *3)
    tam=len(valores_origen)
    udfCargar(valores_origen, tam)
    udfCargar(valores_origen2, tam)
    udfCargar(valores_origen3, tam)



    print (valores_origen,promediovector(valores_origen,tam))
    print(valores_origen2,promediovector(valores_origen2,tam))
    print(valores_origen3,promediovector(valores_origen3,tam))


ladoa= int(input("ingrese el lado a: "))
ladob= int(input("ingrese el lado b: "))
ladoc= int(input("ingrese el lado c: "))
if ladoa==ladob or ladoa==ladoc or ladob==ladoc:
    print("es isoceles")
else:
    print("no es isoceles")


mimain()