import os.path
import pickle
import random

from registro import *


# ==============================================================
#                   Opcion 1
# ==============================================================
def validar_n():
    n = int(input("Ingresar cantidad de lotes a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de lotes a cargar: "))
    return n


def cargar_arreglo(v_lotes, n):
    # nombre STR, manzana(1, 35), num_lote(1, 20), orientacion(1, 4), superficie FLOAT, importe FLOAT
    for i in range(n):
        nombre = random.choice("ABCDEF")
        manzana = random.randint(36, 53)
        num_lote = random.randint(1, 20)
        orientacion = random.randint(1, 4)
        superficie = round(random.uniform(0.1, 10), 2)
        importe = round(random.uniform(0.1, 10), 2)

        nuevo_lote = Lote(nombre, manzana, num_lote, orientacion, superficie, importe)
        add_in_order(v_lotes, nuevo_lote)


def add_in_order(v_lotes, nuevo_lote):
    izq, der = 0, len(v_lotes) - 1

    while izq <= der:

        c = (izq + der) // 2
        # el atributo por el que nos piden ordenar
        if v_lotes[c].nombre == nuevo_lote.nombre:
            pos = c
            break

        # lo que determina si esta ordenado de menor a mayor o mayor a menor es la boquita ">"
        elif v_lotes[c].nombre > nuevo_lote.nombre:
            der = c - 1

        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v_lotes[pos:pos] = [nuevo_lote]     # --> el objeto SIEMPRE VA ENTRE CORCHETES


# ==============================================================
#                   Opcion 2
# ==============================================================
def mostrar_datos(v_lotes):
    # indices       0       1       2
    # v_lotes   = [ L1,     L2,     L3 ]

    for i in v_lotes:
        # i = L1, L2 , L3
        print(i)


# ==============================================================
#                   Opcion 3
# ==============================================================
def generar_matriz(v_lotes, m):

    # crear la matriz
    f = 4     # f = filas = orientacion(1, 4) = lim_superior - lim_inferior + 1 = 4 - 1 + 1 = 4
    c = 18    # c = columnas = manzana(36, 53) = lim_superior - lim_inferior + 1 = 53 - 36 + 1 = 18
    matriz = [ [0] * c for i in range(f) ]

    #
    # orientacion      1-1 2-1   3   4
    # indices_fila      0   1   2   3

    # manzana         36-36 37-36  38  39       53
    # indices_columnas  0   1   2   3   4   ... 17

    # matriz[f][c]

    # matriz =  [   [6, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #               [3, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #               [2, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]      ]

    #
    # rellenar la matriz
    for i in v_lotes:
        # i = L1, L2, L3
        # matriz[f][c]
        matriz[i.orientacion - 1][i.manzana - 36] += i.superficie

        # determinar cantidad de lotes por orientacion y manzana posible
        # matriz[i.orientacion - 1][i.manzana - 36] += 1

    #
    # mostrar la matriz

    # Mostrar, además, la superficie total vendida para una manzana m.
    acum = 0

    for f in range(len(matriz)):        # range(4)
        # f = 0, 1, 2, 3

        for c in range(len(matriz[0])):     # range(18)
            # c = 0, 1, 2, ..., 17

            # solo mostrar las superficies vendidas mayores a cero
            if matriz[f][c] > 0:
                print("Manzana:", c+36, "| Orientacion:", f+1, "| Superficie vendida:", matriz[f][c])

            # solo mostrar las manzanas que esten entre m1 y m2
            # if m1 <= c+36 <= m2:
            #    pass

            if m == c+36:
                acum += matriz[f][c]

    print("EL acumulado de la manzana es:", acum)


# ==============================================================
#                   Opcion 4
# ==============================================================
def generar_archivo_binario(v_lotes, fd, l1, l2):

    m = open(fd, "wb")  # primer parametro es el nombre del archivo ( fd )
                        # segundo parametro el modo de apertura ( "wb" )
    # wb = write binary = si el archivo no existe lo crea, sobre escribe todo su contenido
    # ab = append binary = si el archivo no existe lo crea, agrega el contenido al final del archivo, es
    # decir que conserva todo su contenido

    for i in v_lotes:
        # i = L1, L2, L3

        # guardemos los que tienen num_lote entre l1 y l2
        if l1 <= i.num_lote <= l2:

            pickle.dump(i, m)   # primero parametro es que quiero guardar ( i )
                                # segundo parametro es donde lo quiero guardar ( m )

            m.flush()   # opcional --> guarda mejor el archivo

    print("Se genero el archivo.")  # opcional
    m.close()   # OBLIGATORIO


# ==============================================================
#                   Opcion 5
# ==============================================================
def mostrar_archivo_binario(fd):

    bandera = os.path.exists(fd)    # retornta True si el archivo existe, retorna False si no existe
    if bandera is False:        # if not bandera or bandera == 0
        print("El archivo no existe.")
        return      # corta la funcion

    m = open(fd, "rb")      # read binary = modo de lectura
    tam = os.path.getsize(fd)   # nos devuelve el tamaño en bytes del archivo = 405 bytes

    # indices       0       1       2
    # v_lotes   = [ L1,     L2,     L3 ]

    # archivos = [      L1          L2              L3 ]
    # bytes      0            130          260          405
    # m.tell()   0            130          260

    #
    # y luego de mostrarlo agregue una línea que informe el valor promedio de venta de los
    # lotes contenidos en el archivo de orientacion SUR.
    # promedio = acumulado ( de importes ) / cantidad
    acum = 0
    cont = 0

    while m.tell() < tam:

        lotecito = pickle.load(m)   # unico parametro el archivo
        # lotecito = L1,    L2, L3
        print(lotecito)

        if lotecito.orientacion == 2:
            acum += lotecito.importe
            cont += 1

    # calcular el promedio
    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio es:", prom)

    m.close()   # OBLIGATORIO


# ==============================================================
#                   Opcion 6
# ==============================================================
def busqueda_binaria(v_lotes, nom):
    # indices      0      1    2
    # v_lotes = [ L1,    L2,   L3

    izq, der = 0, len(v_lotes) - 1

    while izq <= der:

        c = (izq + der) // 2

        # if v_lotes[c].nombre == nuevo_lote.nombre:
        if v_lotes[c].nombre == nom:
            pos = c
            # break
            return pos      # pos >= 0

        # elif v_lotes[c].nombre > nuevo_lote.nombre:
        elif v_lotes[c].nombre > nom:
            der = c - 1

        else:
            izq = c + 1

    return -1   # -1 no existe el objeto que cumple


# ==============================================================
#                   Opcion 7
# ==============================================================
def busqueda_secuencial(v_lotes, manz):
    pos = -1
    for i in range(len(v_lotes)):

        if v_lotes[i].manzana == manz:
            pos = i
            break

    return pos


def menu():
    print("1 - Cargar arreglo.")
    print("2 - Mostrar arreglo.")
    print("3 - Generar matriz.")
    print("4 - Generar archivo binario.")
    print("5 - Mostrar archivo binario.")
    op = int(input("Ingresar opción: "))
    return op


def principal():

    # arreglo / vector / lista de trabajo
    v_lotes = []

    # nombre del archivo
    fd = "lotes.dat"        # file description ; nombre del archivo

    op = -1
    while op != 0:

        op = menu()

        if op == 1:
            n = validar_n()

            # Cada vez que se ingrese en esta opción, el arreglo debe ser creado desde cero
            # y todo contenido anterior debe ser eliminado
            v_lotes = []
            cargar_arreglo(v_lotes, n)

        elif op == 2:

            if len(v_lotes) > 0:
                mostrar_datos(v_lotes)

            else:
                print("Debe cargar el arreglo.")

        elif op == 3:
            """
            3 - A partir del arreglo generado en el punto 1, acumular y mostrar la superficie total 
            vendida por cada manzana posible combinada con cada orientación posible. Mostrar, además, 
            la superficie total vendida para una manzana m (siendo m un valor que se ingresa por teclado).
            """

            if len(v_lotes) > 0:
                m = int(input("Ingresar manzana a totalizar: "))
                generar_matriz(v_lotes, m)

            else:
                print("Debe cargar el arreglo.")

        elif op == 4:
            """
            4 - A partir del arreglo, genere un archivo binario que contenga los datos de todos 
            los lotes cuyo número de lote esté comprendido entre l1 y l2, siendo estos valores 
            que se ingresan por teclado.        
            """
            if len(v_lotes) > 0:
                l1 = int(input("Ingresar numero de lote a superar: "))
                l2 = int(input("Ingresar numero de lote a ser menor: "))
                generar_archivo_binario(v_lotes, fd, l1, l2)

            else:
                print("Debe cargar el arreglo.")

        elif op == 5:
            """
            5 - Mostrar el archivo generado en el punto anterior y luego de mostrarlo agregue 
            una línea que informe el valor promedio de venta de los lotes contenidos en el archivo.
            """
            mostrar_archivo_binario(fd)

        elif op == 6:
            """            
            6 - buscar un nombre "nom" y si existe y su orientacion era Norte hacer un descuento del 
            22% mostrar sus datos antes y despues, si no existe informar con un mensaje que diga
            "No existe un nombre con ese <nom>"
            """
            nom = input("Ingresar nombre a buscar: ")
            pos = busqueda_binaria(v_lotes, nom)

            if pos >= 0:

                print("Datos sin actualizar: ", v_lotes[pos])

                if v_lotes[pos].orientacion == 1:
                    v_lotes[pos].importe -= v_lotes[pos].importe * 0.22

                print("Datos actualizados: ", v_lotes[pos])

            else:   # pos es -1
                print("No existe un nombre con ese", nom)


if __name__ == "__main__":
    principal()


