palabras_validas = []
intentos_invalidos = 0


while intentos_invalidos < 3:
palabra = input("Ingresa una palabra (más de 2 letras): ")


if len(palabra) > 2:
palabras_validas.append(palabra)
else:
print("Palabras de una o dos letras no están permitidas.")
intentos_invalidos += 1


if len(palabras_validas) > 0:
total_longitud = 0
for palabra in palabras_validas:
total_longitud += len(palabra)

promedio = total_longitud / len(palabras_validas)


vocales = "aeiou"
palabra_mas_vocales = ""
max_vocales = 0

for palabra in palabras_validas:
contador_vocales = 0
for letra in palabra:
if letra.lower() in vocales:
contador_vocales += 1
if contador_vocales > max_vocales:
max_vocales = contador_vocales
palabra_mas_vocales = palabra

print(f"Promedio de longitud de palabras: {promedio:.2f}")
print(f"La palabra con más vocales es: {palabra_mas_vocales}")
else:
print("No se ingresaron palabras válidas.")