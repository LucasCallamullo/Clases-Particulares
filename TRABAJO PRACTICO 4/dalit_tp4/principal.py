import envio
import os.path
import pickle


def validar_rango(inf, sup, msj):
    valor = int(input(msj))
    while sup < valor or valor < inf:
        print("El valor ingresado no es correcto. Intente nuevamente.")
        valor = int(input(msj))
    return valor


def generar_archivo_binario(fdt, fdb):
    if not os.path.exists(fdt):
        print("El archivo", fdt, "no existe...")
        print("Controle y vuelva por aquí...")
        return

    datos = open(fdt, "rt")

    # leo la linea de timestamp...
    ts = datos.readline()

    # leo la linea de encabezados...
    hd = datos.readline()

    # apertura del archivo de salida...
    m = open(fdb, "wb")

    for linea in datos:
        d = linea.split(",")
        cp = d[0]
        de = d[1]
        te = int(d[2])
        fp = int(d[3])
        env = envio.Envio(cp, de, te, fp)
        pickle.dump(env, m)

    datos.close()
    m.close()


def agregar_envio(fdb):
    cod = input("Ingrese el código postal: ")
    dp = input("Ingrese la dirección: ")
    tip = validar_rango(0, 6, "Ingrese el tipo de envío (0-6): ")
    fp = validar_rango(1, 2, "Ingrese el tipo de pago (1: Efectivo, 2: Tarjeta): ")

    nuevo_env = envio.Envio(cod, dp, tip, fp)

    m = open(fdb, 'ab')
    pickle.dump(nuevo_env, m)
    print("Envío agregado con éxito.")
    m.close()


def mostrar_archivo_binario(fdb):
    if not os.path.exists(fdb):
        print("El archivo", fdb, "no existe...")
        print("Controle y vuelva por aquí...")
        return

    print("Listado general de envios...")
    c = 0
    m = open(fdb, "rb")
    t = os.path.getsize(fdb)
    while m.tell() < t:
        env = pickle.load(m)
        print(env)
        c += 1
    m.close()
    print("Se listaron", c, "registros...")


def busqueda_cp(fdb):
    if not os.path.exists(fdb):
        print("El archivo", fdb, "no existe...")
        print("Controle y vuelva por aquí...")
        return

    cp = input("Ingrese el código postal a buscar: ")
    print("Listado de envíos con código postal", cp, "\b:")

    c = 0
    m = open(fdb, "rb")
    t = os.path.getsize(fdb)

    while m.tell() < t:
        env = pickle.load(m)
        if cp == env.codigo:
            print(env)
            c += 1

    m.close()
    print("Se mostraron", c, "registros.")


# ===========================================================
#               Opcion 6
# ===========================================================
def opcion6(fdb):
    bandera = os.path.exists(fdb)   # retorna True si existe el archivo, retorna False si NO existe
    if bandera is False:    # if not bandera:  if bandera == 0:
        print("El archivo", fdb, "no existe...")
        print("Controle y vuelva por aquí...")
        return  # cortaba la funcion

    # crear la matriz
    f = 2   # f = filas = pago(1, 2) = lim_superior - lim_inferior + 1 = 2 - 1 + 1 = 2
    c = 7   # c = columnas = tipo(0, 6) = lim_superior - lim_inferior + 1 = 6 - 0 + 1 = 7
    matriz = [ [0] * c for i in range(f) ]

    # pago(1, 2)       1-1  2-1
    # fila_indices      0   1

    # tipo(0, 6)        0   1   2   3   4   5   6
    # columnas_indices  0   1   2   3   4   5   6

    # matriz[f][c]
    # matriz = [    [1, 0, 0, 5, 0, 2, 0],
    #               [7, 0, 0, 0, 0, 0, 0]       ]

    #
    # rellenar la matriz
    # v_envios = [ E1, E2, E3 ]
    # for i in v_envios:
    #   # i = E1, E2, E3
    #   matriz[i.pago - 1][i.tipo] += 1

    m = open(fdb, "rb")     # read binary --> modo de lectura
    tam = os.path.getsize(fdb)  # nos devuelve la cantidad en bytes del archivo = 1500 bytes

    # archivo = [   E1      e2           e3 ]
    # bytes     0       500     1000        1500
    # m.tell()  0       500     1000

    while m.tell() < tam:

        env = pickle.load(m)    #
        # env = E1, E2, E3
        # matriz[f][c]
        matriz[env.pago - 1][env.tipo] += 1

    m.close()   # OBLIGATORIO

    # mostrar la matriz
    for f in range(len(matriz)):    # range(2)
        # f = 0, 1

        for c in range(len(matriz[0])):     # range( 7 )
            # c = 0, 1, 2, 3, 4, 5, 6

            #  Muestre solo los contadores cuyo valor final sea diferente de cero
            if matriz[f][c] > 0:
                print("Tipo de Envio:", c, "| Forma de Pago:", f+1, "| Cantidad:", matriz[f][c])

            # Muestre solo los contadores de la forma de pago cuyo valor sea "p" que se carga por teclado
            # if p == f+1:
            #    print()

    return matriz


# Opcion 7
def opcion7(matriz):
    # totalizar las filas
    for f in range(len(matriz)):    # range(2)
        # f = 0     , 1
        acum = 0

        for c in range(len(matriz[0])):     # range( 7 )
            # c = 0, 1, 2, 3, 4, 5, 6
            # f = 1
            acum += matriz[f][c]

        print("Para la forma de pago:", f+1, "tiene total de:", acum)

    # totalizar las columnas
    for c in range(len(matriz[0])):  # range( 7 )
        # c = 0, 1, 2, 3, 4, 5, 6
        acum = 0

        for f in range(len(matriz)):  # range(2)
            # f = 0, 1
            acum += matriz[f][c]

        print("Para el tipo de envio:", c, "tiene total de:", acum)





def principal():
    fdt = "envios-tp4.csv"
    fdb = "envios-tp4.dat"
    op = 0

    matriz = None

    while op != 9:
        print("Menú de opciones:")
        print("1. Crear archivo binario")
        print("2. Agregar un envío")
        print("3. Mostrar todos los envíos")
        print("4. Mostrar envíos por código postal")
        print("5. Buscar envío por dirección")
        print("6. Cantidad de envíos por tipo y forma de pago")
        print("7. Totales por tipo de envío y forma de pago")
        print("8. Promedio y envíos mayores al promedio")
        print("9. Salir")
        op = int(input("Seleccione una opción: "))

        if op == 1:
            generar_archivo_binario(fdt, fdb)
            print("Terminado...")

        elif op == 2:
            agregar_envio(fdb)

        elif op == 3:
            mostrar_archivo_binario(fdb)

        elif op == 4:
            busqueda_cp(fdb)

        elif op == 5:
            pass

        elif op == 6:
            matriz = opcion6(fdb)

        elif op == 7:
            if matriz is None:
                print("pase por la opcion 6 primero.")

            else:
                opcion7(matriz)

        elif op == 8:
            pass

        elif op == 9:
            print("Programa terminado.")


if __name__ == "__main__":
    principal()
