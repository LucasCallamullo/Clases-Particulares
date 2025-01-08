import os.path
import pickle


# ===============================================================
#                   Opcion 3
# ===============================================================
def opcion3(fd):
    bandera = os.path.exists(fd) # retora True si existe, return FALSE si NO existe
    if bandera is False:        # if not bandera
        print("El archivo no existe, debe genrarlo.")
        return      # corta la funcion

    m = open(fd, "rb")  # primer parametro: el nombre del archivo ( fd )
    #            # segundo parametro: el modo de apertura ( "rb" )
    # rb = read binary -> modo de lectura

    tam = os.path.getsize(fd)    # nos devuelve/nos dice el tamaño del archivo en bytes = 1500 bytes

    # archivo = [ E1       E2      E3   ]
    # bytes     0     500      1000      1500
    # m.tell()  0     500      1000

    while m.tell() < tam:

        env = pickle.load(m)    # unico parametro el archivo ( m )
        # env = E1, E2, E3
        print(env)

    m.close()   # OBLIGATORIO


# ===============================================================
#                   Opcion 6
# ===============================================================
def generar_matriz(fd):
    bandera = os.path.exists(fd) # retora True si existe, return FALSE si NO existe
    if bandera is False:        # if not bandera
        print("El archivo no existe, debe genrarlo.")
        return      # corta la funcion

    m = open(fd, "rb")  # primer parametro: el nombre del archivo ( fd )
    #            # segundo parametro: el modo de apertura ( "rb" )
    # rb = read binary -> modo de lectura
    tam = os.path.getsize(fd)    # nos devuelve/nos dice el tamaño del archivo en bytes = 1500 bytes

    # crear la matriz
    f = 2    # f = filas = pago(1, 2) = lim_superior - lim_inferior + 1 = 2 - 1 + 1 = 2
    c = 7    # c = columnas = tipo(0, 6) = lim_superior - lim_inferior + 1 = 6 - 0 + 1 = 7
    matriz = [ [0] * c for i in range(f) ]

    # pago(1, 2)   1-1  2-1
    # fila_indices  0   1

    # tipo(0, 6)        0   1   2   3   4   5   6
    # columnas_indices  0   1   2   3   4   5   6

    # matriz[f][c]
    # matriz = [    [0, 2, 0, 0, 0, 0, 0],
    #               [0, 3, 0, 4, 0, 5, 0]       ]

    #
    # rellenar la amtriz
    # for i in v_envios:
    #   # i = E1, E2, E3
    #   matriz[i.pago - 1][i.tipo] += 1

    while m.tell() < tam:

        env = pickle.load(m)    # unico parametro el archivo ( m )
        # env = E1, E2, E3
        # matriz[f][c]
        matriz[env.pago - 1][env.tipo] += 1

    m.close()   # OBLIGATORIO

    #
    # Mostrar la matriz
    for f in range(len(matriz)):        # range(2)
        # f = 0, 1

        for c in range(len(matriz[0])):  # range(7)
            # c = 0, 1, 2, 3, 4, 5, 6

            # Muestre solo los contadores cuyo valor final sea diferente de cero.
            if matriz[f][c] > 0:
                print("Tipo de Envío:", c, "| Forma de Pago:", f+1, "| Cantidad:", matriz[f][c])

            # solo mostrar los contadores de la forma de pago "x" qeu se carga por teclado
            # if x == f+1:
            #    print(Etc)

    return matriz


# ===============================================================
#                   Opcion 7
# ===============================================================
def opcion7(matriz):
    # Totalizar filas
    for f in range(len(matriz)):        # range(2)
        # f = 0     , 1
        acum = 0

        for c in range(len(matriz[0])):  # range(7)
            # c = 0, 1, 2, 3, 4, 5, 6
            # f = 0
            acum += matriz[f][c]

        print("Para la forma de pago:", f+1, "tenemos el total de:", acum)

    # Totalizar filas
    for c in range(len(matriz[0])):  # range(7)
        # c = 0, 1, 2, 3, 4, 5, 6
        acum = 0

        for f in range(len(matriz)):  # range(2)
            #
            # f = 0, 1
            acum += matriz[f][c]

        print("Para el tipo de envio:", c, "tenemos el total de:", acum)


# ===============================================================
#                   Opcion 8
# ===============================================================
def calcular_promedio_opcion8(fd):
    bandera = os.path.exists(fd)
    if bandera is False:
        print("El archivo no existe, debe genrarlo.")
        return

    m = open(fd, "rb")
    tam = os.path.getsize(fd)

    # promedio = acumulado ( de importes ) / cantidad de veces que acumulamos
    acum = 0
    cont = 0

    while m.tell() < tam:
        env = pickle.load(m)  # unico parametro el archivo ( m )
        # env = E1, E2, E3

        importe = env.calcular_importe()    # retorna el importe final
        acum += importe
        cont += 1

    #  calcular promedio
    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio es:", prom)

    m.close()

    return prom


def opcion8(fd, prom):
    bandera = os.path.exists(fd)
    if bandera is False:
        print("El archivo no existe, debe genrarlo.")
        return

    m = open(fd, "rb")
    tam = os.path.getsize(fd)

    v_envios = []

    while m.tell() < tam:
        env = pickle.load(m)  # unico parametro el archivo ( m )
        # env = E1, E2, E3
        importe = env.calcular_importe()  # retorna el importe final

        if importe > prom:
            add_in_order(v_envios, env)

    m.close()

    # mostrar arreglo
    for i in v_envios:
        # i = E1, E2, E3
        print(i)


def add_in_order(v_envios, env):
    izq, der = 0, len(v_envios) - 1
    pos = 0     # realmente no es necesario es solo para que no tire el error de que puede no existir.

    while izq <= der:
        c = (izq + der) // 2
        if v_envios[c].codigo == env.codigo:
            pos = c
            break
        elif v_envios[c].codigo >= env.codigo:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v_envios[pos:pos] = [env]


def principal():

    # nombre del archivo
    fd = "envios.dat"

    matriz = None

    op = -1
    while op != 0:
        # menu()
        op = int(input("Ingresar opcion: "))

        if op == 1:
            pass

        elif op == 3:
            opcion3(fd)

        elif op == 6:
            matriz = generar_matriz(fd)

        elif op == 7:
            if matriz is None:
                print("primero debe pasar por la opcion 6.")

            else:
                opcion7(matriz)

        elif op == 8:
            prom = calcular_promedio_opcion8(fd)
            opcion8(fd, prom)




if __name__ == '__main__':
    principal()
