def Alcancefuncion(pp):
    x=10 # Variable Local
    print(f'x:{x} {pp}')

def Alcancefuncion2():
    x=99
    print(f'x:{x}')
    return 1,2

def mimain():
    x=20 # Variable Local
    y=5
    Alcancefuncion(y)
    a,b=Alcancefuncion2()
    print(f'x:{x} {a} {b}')

x=-1
mimain()


