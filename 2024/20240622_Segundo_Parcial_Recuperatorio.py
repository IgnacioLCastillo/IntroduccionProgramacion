# -*- coding: utf-8 -*-
def udf_agregar_producto(plis_productos, plis_categorias, plis_precios, plis_cantidades):
    unnombre = input("Ingrese el nombre del producto:")
    unacategoria = input("Ingrese la categoria del producto (A=Alimentos, H=Higiene, E=Electrodomesticos, B=Bazar): ")
    while True:
        unprecio = float(input("Ingrese el precio del producto (debe ser mayor que 0): "))
        if unprecio < 0:
            print("El precio debe ser mayor que 0.")
            continue
        else:
            break

    while True:
        unacantidad = int(input("Ingrese la cantidad en stock del producto (debe ser mayor o igual que 0): "))
        if unacantidad >= 0:
            break
        else:
            print("La cantidad en stock debe ser mayor o igual que 0.")

    plis_productos.append(unnombre)
    plis_categorias.append(unacategoria)
    plis_precios.append(unprecio)
    plis_cantidades.append(unacantidad)


def udf_buscar_producto(nombre_producto, plis_productos):
    indice_producto = None
    for i in range(len(plis_productos)):
        if plis_productos[i] == nombre_producto:
            indice_producto = i
            break
    return indice_producto

def udf_agregar_stock(plis_productos, plis_cantidades):
    nombre_producto = input("Ingrese el nombre del producto al que desea agregar stock: ")
    indice_producto = udf_buscar_producto(nombre_producto, plis_productos)

    if indice_producto is not None:
        while True:
            cantidad_stock = int(input(f"Ingrese la cantidad de stock a agregar al producto '{nombre_producto}': "))
            if cantidad_stock >= 0:
                #plis_cantidades[indice_producto] += cantidad_stock
                plis_cantidades[indice_producto]=plis_cantidades[indice_producto]+cantidad_stock
                print(f"Stock actualizado para '{nombre_producto}': {plis_cantidades[indice_producto]}")
                break
            else:
                print("La cantidad de stock debe ser mayor o igual que 0.")
    else:
        print(f"No se encontró el producto '{nombre_producto}' en la lista.")

def udf_mostrar_productos(plis_productos, plis_categorias, plis_precios, plis_cantidades):
    if not plis_productos:
        print("No hay productos en el inventario.")
        return
    print(f"{'Nombre':<20} {'Categoría':<15} {'Precio':<10} {'Cantidad en Stock':<20}")
    for i in range(len(plis_productos)):
        print(f"{plis_productos[i]:<20} {plis_categorias[i]:<15} {plis_precios[i]:<10.2f} {plis_cantidades[i]:<20}")


def udf_calcular_promedio_categoria(plis_categorias, plis_precios):
    categoria_buscar = input("Ingrese la categorIa para calcular el promedio de precios: ")
    total_precio = 0
    cantidad_productos = 0
    for i in range(len(plis_categorias)):
        if plis_categorias[i] == categoria_buscar:
            #total_precio += plis_precios[i]
            total_precio=total_precio+plis_precios[i]
            #cantidad_productos += 1
            cantidad_productos=cantidad_productos+1

    if cantidad_productos == 0:
        print("No hay productos en la categoría especificada.")
    else:
        promedio = total_precio / cantidad_productos
        print(f"El promedio de precios para la categoría {categoria_buscar} es: {promedio:.2f}")


def udf_encontrar_producto_mas_caro(plis_precios):
    if not plis_precios:
        print("No hay productos en el inventario.")
        return
    indice_mas_caro = 0
    precio_mas_caro = plis_precios[0]
    for i in range(1, len(plis_precios)):
        if plis_precios[i] > precio_mas_caro:
            precio_mas_caro = plis_precios[i]
            indice_mas_caro = i

    return indice_mas_caro



def udf_productos_poco_stock(plis_productos, plis_categorias, plis_precios, plis_cantidades):
    for i in range(len(plis_cantidades)):
        if plis_cantidades[i] <= 5:
            print("Productos con poco stock:")
            print(f"{'Nombre':<20} {'Categoria':<15} {'Precio':<10} {'Cantidad en Stock':<20}")
            print(f"{plis_productos[i]:<20} {plis_categorias[i]:<15} {plis_precios[i]:<10.2f} {plis_cantidades[i]:<20}")


def udf_mostrar_producto_especifico(plis_productos, plis_categorias, plis_precios, plis_cantidades):
    productoabuscar=input("Ingrese el nombre del producto que desea buscar: ")
    for i in range(len(plis_productos)):
        if plis_productos[i].upper() == productoabuscar.upper():
            return i

    return -1


def mimain():
    lis_productos = []
    lis_categorias = []
    lis_precios = []
    lis_cantidades = []
    while True:
        print("\nMenú Principal:")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Calcular promedio de precios por categoría")
        print("4. Encontrar producto más caro")
        print("5. Productos con poco stock")
        print("6. Agregar stock")
        print("7. Salir")
        opcion = int(input("Ingrese el número de la opción que desea realizar: "))
        if opcion == 1:
            udf_agregar_producto(lis_productos, lis_categorias, lis_precios, lis_cantidades)
        elif opcion == 2:
            udf_mostrar_productos(lis_productos, lis_categorias, lis_precios, lis_cantidades)
        elif opcion == 3:
            udf_calcular_promedio_categoria(lis_categorias, lis_precios)
        elif opcion == 4:
            atrapa_indice=udf_encontrar_producto_mas_caro(lis_productos, lis_categorias, lis_precios, lis_cantidades)
            print("El producto mas caro es:")
            print(f"Nombre: {lis_productos[atrapa_indice]}")
            print(f"Categoria: {lis_categorias[atrapa_indice]}")
            print(f"Precio: {lis_precios[atrapa_indice]:.2f}")
            print(f"Cantidad en Stock: {lis_cantidades[atrapa_indice]}")
        elif opcion == 5:
            udf_productos_poco_stock(lis_productos, lis_categorias, lis_precios, lis_cantidades)
        elif opcion == 6:
            udf_mostrar_productos(lis_productos, lis_categorias, lis_precios, lis_cantidades)
            udf_agregar_stock(lis_productos, lis_cantidades)
        elif opcion == 7:
            atrapa_indice=udf_mostrar_producto_especifico(lis_productos, lis_categorias, lis_precios, lis_cantidades)
            if atrapa_indice != -1:
                print(f"Nombre: {lis_productos[atrapa_indice]}")
                print(f"Categoria: {lis_categorias[atrapa_indice]}")
                print(f"Precio: {lis_precios[atrapa_indice]:.2f}")
                print(f"Cantidad en Stock: {lis_cantidades[atrapa_indice]}")
            else:
                print("El producto no se encuentra en la lista
        elif opcion == 8:
            print("Saliendo del programa.")
            break
        else:
            print("Opcion invalida.")

#*-*-*-*-*-*-*- Area global -*-*-*-*-*-*-*-
mimain()