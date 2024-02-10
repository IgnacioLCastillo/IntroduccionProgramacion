def udfDobleTriple(p1,p2):
     #Alcance local.
    return p1*2,p2*3


def udfEmulaReferenciua(p1):
    # Alcance local.
    return p1 + 10

def udfMain():
    localA=5
    localA = udfEmulaReferenciua(localA)
    print(f"Emulando referenecia localA ahora vale {localA}")
    doble,triple=udfDobleTriple(localA,localA)
    print(f"El doble es {doble}, y el trple es {triple}")


#--------------------------AREA GLOBAL--------------------------
udfMain()