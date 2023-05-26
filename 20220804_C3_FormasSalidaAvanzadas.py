minumero = int(input("ingresa un numero:"))
miResultado = minumero * minumero
if miResultado>=100:
    print("El Resultado es:" + str(miResultado) + " y repito " + str(miResultado))

    print("El Resultado es:", miResultado, "repito", miResultado)

    print("El Resultado es: {} y repito {} ".format(miResultado, miResultado))

    print("El Resultado es: %3d, y repito : %2d" % (miResultado, miResultado))

    print(f"El Resultado es: {miResultado} y repito {miResultado}")
else:
    print (f"no es mayor a 100 el resultado que fue {miResultado} ")