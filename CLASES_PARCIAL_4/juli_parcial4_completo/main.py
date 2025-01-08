import os.path
import pickle
import random

from registro import *


# ===========================================================================
#                   Opcion 1
# ===========================================================================
def validar_n():
    n = int(input("Ingresar cantidad de lotes a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de lotes a cargar: "))
    return n


def cargar_arreglo(v_lotes, n):
    # nombre STR, manzana(1, 35), num_lote(1, 20), orientacion(1, 4),
    # superficie FLOAT, importe FLOAT

    for i in range(n):      # 3
        nombre = random.choice("ABCDEF")
        manzana = random.randint(1, 35)
        num_lote = random.randint(1, 20)
        orientacion = random.randint(1, 4)
        superficie = round(random.uniform(0.1, 10), 2)
        importe = round(random.uniform(0.1, 10), 2)

        nuevo_lote = Lote(nombre, manzana, num_lote, orientacion, superficie, importe)
        add_in_order(v_lotes, nuevo_lote)


def add_in_order(v_lotes, nuevo_lote):

    # L1.nombre     "B"
    # L2.nombre     "A"

    # indices     0
    # v_lotes = [ L1  ]
    # nombre       B

    izq, der = 0, len(v_lotes) - 1
    # izq = 0
    # der = -1

    while izq <= der:

        c = (izq + der) // 2    # c = centro = 0

        # cambia el atributo por el que te pidan ordenarlo
        if v_lotes[c].nombre == nuevo_lote.nombre:
            pos = c
            break

        # la boquita ">" determina si esta de menor a mayor o mayor a menor
        elif v_lotes[c].nombre > nuevo_lote.nombre:
            der = c - 1

        else:
            izq = c + 1

    if izq > der:
        pos = izq

    # indices     0     1
    # v_lotes = [ L2,   L1 ]
    # nombre       A     B
    v_lotes[pos:pos] = [nuevo_lote]     # el OBJETO VA ENTRE CORCHETES


# ===========================================================================
#                   Opcion 2
# ===========================================================================
def mostrar_datos(v_lotes):
    # indices     0     1
    # v_lotes = [ L1,   L2 ]

    for i in v_lotes:
        # i = L1, L2
        print(i)


# ===========================================================================
#                   Opcion 3
# ===========================================================================
def generar_matriz(v_lotes, m):

    # crear la matriz
    f = 4   # f = filas = orientacion(1, 4) = lim_superior - lim_inferior + 1 = 4 - 1 + 1 = 4
    c = 35  # c = columnas = manzana(1, 35) = lim_superior - lim_inferior + 1 = 35 - 1 + 1 = 35
    matriz = [ [0] * c for i in range(f) ]

    #
    # orientacion(1, 4)    1-1   2   3   4
    # fila_indices =        0   1   2   3

    # manzana(1, 35)           1-1   2   3   4       35
    # columnas_indices          0   1   2   3   ... 34

    # matriz[f][c]
    # matriz =
    # [ [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #   [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #   [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #   [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   ]

    #
    # rellenar la matriz
    for i in v_lotes:
        # i = L1, L2, L3
        # i.manzana i.orientacion
        # matriz[f][c]
        matriz[i.orientacion - 1][i.manzana - 1] += i.superficie
        # matriz[i.orientacion - 1][i.manzana - 1] += 1

    #
    # mostrar la matriz

    # Mostrar, además, la superficie total vendida para una manzana m.
    acum = 0

    for f in range(len(matriz)):    # range ( 4 )
        # f = 0, 1, 2, 3

        for c in range(len(matriz[0])):     # range (35)
            # c = 0, 1, 2, 3, .., 34

            # solo mostrar los que tengan una superficie vendida mayor a 0
            if matriz[f][c] > 0:
                print("Manzana:", c+1, "| Orientacion:", f+1, "| Superficie vendida:", matriz[f][c])

            # solo mostrar las manzanas entre m1 y m2
            # if m1 <= c+1 <= m2:

            if m == c+1:
                acum += matriz[f][c]

    print("El acumulado manzana m es:", acum)


# ===========================================================================
#                   Opcion 4
# ===========================================================================
def generar_archivo_binario(v_lotes, fd, l1, l2):

    m = open(fd, "wb")  # primer parametro (fd), segundo parametro modo de apertura
    # wb = write binary = si no existe el archivo lo crea, sobre escribe todo su contenido
    # ab = append binary =  si no existe el archivo lo crea, conserva todo su contenido y
    # agrega el nuevo contenido al final del archivo

    for i in v_lotes:
        # i = L1, L2

        # que guardemos los num_lotes entre l1 y l2
        if l1 <= i.num_lote <= l2:

            pickle.dump(i, m)   # primer parametro es que quiero guardar ( i )
                            # segundo parametro es donde lo quiero guardar ( m )

            m.flush()   # opcional --> guarda mejor el archivo

    m.close()       # OBLIGATORIO


# ===========================================================================
#                   Opcion 5
# ===========================================================================
def mostrar_archivo_binario(fd):
    bandera = os.path.getsize(fd)   # return True si el archivo si existe, return False si no existe

    if bandera is False:    # if not bandera:
        print("El archivo no existe.")
        return      # corta la funcion

    m = open(fd, "rb")  # read binary -> modo de lectura
    tam = os.path.getsize(fd)   # nos devuelve el tamaño en bytes del archivo = 200bytes

    #
    # archivo = [    L1            L2   ]
    # bytes     0         100           200
    # m.tell()  0         100           200

    #
    # y luego de mostrarlo agregue una línea que informe el valor
    # promedio de venta de los lotes contenidos en el archivo.
    # promedio = acumulador ( de importes ) / la cantidad que acumulamos
    acum = 0
    cont = 0

    while m.tell() < tam:
        lotecito = pickle.load(m)
        # lotecito = L1 , L2
        print(lotecito)
        acum += lotecito.importe
        cont += 1

    # calcular promedio
    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio es:", prom)

    m.close()   # OBLIGATORIO


# ===========================================================================
#                   Opcion 6
# ===========================================================================
def busqueda_binaria(v_lotes, nom):
    izq, der = 0, len(v_lotes) - 1

    while izq <= der:

        c = (izq + der) // 2  # c = centro = 0

        # if v_lotes[c].nombre == nuevo_lote.nombre:
        if v_lotes[c].nombre == nom:
            pos = c
            # break
            return pos  # si existe retorna 0 o +

        # elif v_lotes[c].nombre > nuevo_lote.nombre:
        elif v_lotes[c].nombre > nom:
            der = c - 1

        else:
            izq = c + 1

    return -1   # si no existe un objeto con nuestro criterio de busqueda


def menu():
    print("1 - Cargar arreglo.")
    print("2 - Mostrar arreglo.")
    print("3 - Generar matriz.")
    print("4 - Generar archivo binario.")
    print("5 - Mostrar archivo binario.")
    print("6-  Busqueda Binaria.")
    op = int(input("Ingresar opción: "))
    return op


def principal():

    # vector / arreglo / lista de trabajo
    v_lotes = []

    # nombre del archivo binario
    fd = "lotes.dat"    # file description ; nombre del archivo

    op = -1
    while op != 0:
        op = menu()

        if op == 1:
            n = validar_n()

            # Cada vez que se ingrese en esta opción, el arreglo debe ser
            # creado desde cero y todo contenido anterior debe ser eliminado.
            v_lotes = []
            cargar_arreglo(v_lotes, n)

        elif op == 2:
            if len(v_lotes) > 0:
                mostrar_datos(v_lotes)

            else:
                print("El arreglo no esta cargado.")

        elif op == 3:
            """
            3 - A partir del arreglo generado en el punto 1, acumular y mostrar la 
            superficie total vendida por cada manzana posible combinada con cada 
            orientación posible. Mostrar, además, la superficie total vendida para una
            manzana m (siendo m un valor que se ingresa por teclado).
            """
            if len(v_lotes) > 0:
                m = int(input("Ingresar manzana a totalizar: "))
                generar_matriz(v_lotes, m)

            else:
                print("El arreglo no esta cargado.")

        elif op == 4:
            """
            4 - A partir del arreglo, genere un archivo binario que contenga los 
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
             mostrarlo agregue una línea que informe el valor
            promedio de venta de los lotes contenidos en el archivo.
            """
            mostrar_archivo_binario(fd)

        elif op == 6:
            """
            6 - buscar por nombre "nom" y si existe hacer un descuento del 22%
            si no existe informar con el mensaje "ASDASDASD"
            """
            nom = input("Ingresar nombre a buscar: ")
            pos = busqueda_binaria(v_lotes, nom)

            if pos >= 0:
                print("Datos sin actualizar: ", v_lotes[pos])

                v_lotes[pos].importe -= v_lotes[pos].importe * 0.22

                print("Datos actualizados: ", v_lotes[pos])

            else:
                print("ASDASDASD")


if __name__ == "__main__":
    principal()
