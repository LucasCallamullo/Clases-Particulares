import os.path
import pickle
import random
from registro import *


# ===========================================================================
#                           Opcion 1
# ===========================================================================
def validar_n():
    n = int(input("Ingresar cantidad de lotes a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de lotes a cargar: "))
    return n


def cargar_arreglo(v_lotes, n):
    # nombre STR, manzana(1, 35), num_lote(1, 20), orientacion(1, 4),
    # superficie FLOAT, importe FLOAT
    for i in range(n):
        nombre = random.choice("ABCDEF")
        manzana = random.randint(1, 35)
        num_lote = random.randint(1, 20)
        orientacion = random.randint(1, 4)
        superficie = round(random.uniform(0.1, 10), 2)
        importe = round(random.uniform(0.1, 10), 2)

        nuevo_lote = Lote(nombre, manzana, num_lote, orientacion, superficie, importe)
        add_in_order(v_lotes, nuevo_lote)


def add_in_order(v_lotes, nuevo_lote):

    # L1.nombre     "C"
    # L2.nombre     "B"

    # indices       0
    # v_lotes = [  L1  ]

    izq, der = 0, len(v_lotes) - 1
    # izq = 0
    # der = -1

    while izq <= der:

        c = (izq + der) // 2        # c = centro = 0

        # el atributo que nos piden ordenar puede cambiar
        if v_lotes[c].nombre == nuevo_lote.nombre:
            pos = c
            break

        # la orientacion de la boquita ">" define si esta de menor a mayor o mayor a menor
        elif v_lotes[c].nombre > nuevo_lote.nombre:
            der = c - 1

        else:
            izq = c + 1

    if izq > der:
        pos = izq

    # indices      0    1
    # v_lotes = [  L2,  L1 ]
    # nombre        B    C
    v_lotes[pos:pos] = [nuevo_lote]     # el objeto SIEMPRE VA ENTRE CORCHETES


# ===========================================================================
#                           Opcion 2
# ===========================================================================
def mostrar_datos(v_lotes):
    # indices      0    1
    # v_lotes = [  L1,  L2 ]
    for i in v_lotes:
        # i = L1, L2, L3
        print(i)


# ===========================================================================
#                           Opcion 3
# ===========================================================================
def generar_matriz(v_lotes, m):

    # crear la matriz
    f = 4  # f = filas = orientacion(1, 4) = lim_superior - lim_inferior + 1 = 4 - 1 + 1 = 4
    c = 35  # c = columnas = manzana(1, 35) = lim_superior - lim_inferior + 1 = 35 -1 +1 = 35
    matriz = [ [0] * c for i in range(f) ]

    # orientacion(1, 4)   1-1  2-1  3-1   4
    # fila_indices          0   1   2   3

    # manzana(1, 35)      1-1   2   3   ... 34  35
    # columnas_indices      0   1   2   3   ... 34

    # matriz[f][c]
    # [ [0, 1, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #   [0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #   [0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #   [0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   ]

    #
    # rellenar la matriz
    for i in v_lotes:
        # i = L1, L2, L3
        # matriz[f][c]
        matriz[i.orientacion - 1][i.manzana - 1] += i.superficie

    #
    # mostrar la matriz

    # Mostrar, además, la superficie total vendida para una manzana m
    acum = 0

    tupla_orientaciones = ("Norte", "Sur", "Este", "Oeste")

    for f in range(len(matriz)):    # range(4)
        # f = 0, 1, 2, 3

        for c in range(len(matriz[0])):     # range(35)
            # c = 0, 1, 2, 3, ..., 34

            # solo mostrar los que tengan una superficie vendida mayor a 0
            if matriz[f][c] > 0:
                # print("Manzana:", c+1, "| Orientación:", f+1, "| Supercicie vendida:", matriz[f][c])
                print("Manzana:", c+1, "| Orientación:", tupla_orientaciones[f], "| Supercicie vendida:", matriz[f][c])

            # solo mostrar las manzanas que esten entre m1 y m2
            # if m1 <= c+1 <= m2:
            #    print ----

            if m == c+1:
                acum += matriz[f][c]

    print("El acumulado de la manzana:", m," es:", acum)


# ===========================================================================
#                           Opcion 4
# ===========================================================================
def generar_archivo_binario(v_lotes, fd, l1, l2):
    m = open(fd, "wb")  # primer parametro el nombre del archivo ( fd )
                # segundo parametro el modo de apertura ( "wb" )
    # wb = write binary = crea el archivo si no existe, sobre escribe todo su contenido
    # ab = append binary = crea el archivo si no existe, agrega contenido al final del archiv
    # conservando todo su contenido anterior

    for i in v_lotes:
        # i = L1, L2, L3

        if l1 <= i.num_lote <= l2:
            pickle.dump(i, m)   # primer parametro: que quiero guardar ( i )
                            # segundo parametro: donde lo quiero guardar ( m )
            m.flush()   # opcional --> guarda mejor el archivo

    print("Se genero el archivo.")  # opcional -->
    m.close()   # OBLIGATORIO


# ===========================================================================
#                           Opcion 5
# ===========================================================================
def mostrar_archivo_binario(fd):

    bandera = os.path.exists(fd)  # retorna TRUE si existe el archivo, retorna FALSE si NO existe
    if bandera is False:        # if not bandera:
        print("El archivo no existe.")
        return       # cortemos la funcion

    m = open(fd, "rb")  # read binary ; modo de lectura
    tam = os.path.getsize(fd)   # devolvernos el tamaño en bytes del archivo  = 300 bytes

    # archivo = [   L1       L2      L3 ]
    # bytes     0       100     200     300
    # m.tell()  0       100     200

    # agregue al final una línea que informe el valor promedio de venta de los
    # lotes con orientaciones NORTE y SUR contenidos en el archivo.
    # promedio = acumulado ( de importes ) / la cantidad de veces que acumulamos
    acum = 0
    cont = 0

    while m.tell() < tam:
        lotecito = pickle.load(m)     # unico parametro al archivo ( m )
        # lotecito = L1,    L2,     L3
        print(lotecito)

        if lotecito.orientacion == 1 or lotecito.orientacion == 2:
            acum += lotecito.importe
            cont += 1

    # calcular promedio
    prom = 0
    if cont > 0:
        prom = acum / cont

    print("el promedio es:", prom)

    m.close()   # OBLIGATORIO


# ===========================================================================
#                           Opcion 6
# ===========================================================================
def busqueda_binaria(v_lotes, nom):
    izq, der = 0, len(v_lotes) - 1

    while izq <= der:

        c = (izq + der) // 2  # c = centro = 0

        # if v_lotes[c].nombre == nuevo_lote.nombre:
        if v_lotes[c].nombre == nom:
            pos = c
            # break
            return pos  # pos es un indice donde esta el objeto que cumple mi criterio de busqueda

        # elif v_lotes[c].nombre > nuevo_lote.nombre:
        elif v_lotes[c].nombre > nom:
            der = c - 1

        else:
            izq = c + 1

    return -1   # para cuando no existia


def menu():
    print("1 - Cargar arreglo.")
    print("2 - Mostrar arreglo.")
    print("3 - Generar matriz.")
    print("4 - Generar archivo binario.")
    print("5 - Mostrar archivo binario.")
    op = int(input("Ingresar opción: "))
    return op


def principal():

    # vector / lista / arreglo de trabajo
    v_lotes = []

    # nombre del archivo binario
    fd = "lotes.dat"

    op = -1
    while op != 0:
        op = menu()

        if op == 1:
            n = validar_n()
            # Cada vez que se ingrese en esta opción, el arreglo debe ser creado
            # desde cero y todo contenido anterior debe ser eliminado.
            v_lotes = []
            cargar_arreglo(v_lotes, n)

        elif op == 2:
            if len(v_lotes) > 0:
                mostrar_datos(v_lotes)
            else:
                print("El arreglo no esta cargado.")

        elif op == 3:
            if len(v_lotes) > 0:
                m = int(input("Manzana a totalizar su superficie vendida: "))
                generar_matriz(v_lotes, m)
            else:
                print("El arreglo no esta cargado.")

        elif op == 4:
            """
            4-  A partir del arreglo, genere un archivo binario que contenga los 
            datos de todos los lotes cuyo número de lote esté comprendido entre l1 y l2, 
            siendo estos valores que se ingresan por teclado.
            """
            if len(v_lotes) > 0:
                l1 = int(input("Ingresar num_lote a superar: "))
                l2 = int(input("Ingresar num_lote a ser menor: "))
                generar_archivo_binario(v_lotes, fd, l1, l2)
            else:
                print("El arreglo no esta cargado.")

        elif op == 5:
            """
            5 - Mostrar el archivo generado en el punto anterior y luego de 
            mostrarlo agregue una línea que informe el valor promedio de venta de l
            os lotes con orientaciones NORTE y SUR contenidos en el archivo.
            """
            mostrar_archivo_binario(fd)

        elif op == 6:
            """
            6 - Buscar un nombre "nom" si existe hacer un descuenta del 22%
            si no existe
            """
            nom = input("Ingresar nombre a buscar: ")
            pos = busqueda_binaria(v_lotes, nom)

            if pos >= 0:
                print("Datos sin acutalizar:", v_lotes[pos])

                v_lotes[pos].importe -= v_lotes[pos].importe * 0.22

                print("Datos acutalizados:", v_lotes[pos])

            else:
                print("No existe")


if __name__ == "__main__":
    principal()
