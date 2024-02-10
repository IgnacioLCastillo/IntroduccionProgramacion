# -*- coding: utf-8 -*-
palabra = input("Ingrese la palabra")
palabra = palabra.lower()

# Inicializar contadores para cada letra
contador_a = 0
contador_e = 0
contador_i = 0
contador_u = 0
contador_o = 0

# Iterar sobre cada letra en la palabra
for letra in palabra:
    # Verificar qué letra es y aumentar el contador correspondiente
    if letra == 'a':
        contador_a += 1
    elif letra == 'e':
        contador_e += 1
    elif letra == 'i':
        contador_i += 1
    elif letra == 'o':
        contador_o += 1
    elif letra == 'u':
        contador_u += 1


# Mostrar el resultado
print(f"La palabra '{palabra}' tiene:")
print(f"- {contador_a} letras 'a'")
print(f"- {contador_e} letras 'e'")
print(f"- {contador_i} letras 'i'")
print(f"- {contador_o} letras 'u'")
print(f"- {contador_u} letras 'u'")