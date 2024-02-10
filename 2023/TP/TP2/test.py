vector = []
def cargar_vector_manual():
    for i in range(10):
        while True:
            elemento = int(input(f"Ingrese un número para la posición {i + 1}: "))
            vector.append(elemento)
            break

    return vector

def copiar_en_orden_inverso(vector_original):
    vector_inverso = vector_original[::-1]
    return vector_inverso

while True:
    print("Menú:")
    print("1. Cargar vector manual")
    print("2. Copiar en orden inverso")
    print("3. Mostrar vector")
    print("4. Salir")
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
            vector_original = cargar_vector_manual()
            print("Vector manual cargado.")
        elif opcion == 2:
            if 'vector_original' in locals():
                vector_inverso = copiar_en_orden_inverso(vector_original)
                print("Vector inverso:", vector_inverso)
        elif opcion == 3:
            print("tu Vector es :", vector_original)
        elif opcion == 4:
            break
