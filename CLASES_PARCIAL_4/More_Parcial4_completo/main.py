import os.path
import pickle
import random

from registro import *


# =================================================================
#                   Opcion 1
# =================================================================
def validar_n():
    n = int(input("Ingresar cantidad de lotes a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de lotes a cargar: "))
    return n


def cargar_arreglo(v_lotes, n):
    # nombre STR , manzana(1, 35) , num_lote (1, 20), orientacion (1, 4), superficie FLOAT, importe FLOAT
    for i in range(n):
        nombre = random.choice("ABCDEF")    # STR
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
    # v_lotes = [   L1    ]

    izq, der = 0, len(v_lotes) - 1
    # izq = 0
    # der = -1

    while izq <= der:
        c = (izq + der) // 2        # c = 0

        # por lo que te pidan ordenar es el atributo al que accedes para las comparativas
        if v_lotes[c].nombre == nuevo_lote.nombre:
            pos = c
            break

        # si te piden de menor a mayor o mayor a menor esta determinado por la ">"
        elif v_lotes[c].nombre > nuevo_lote.nombre:
            der = c - 1

        else:
            izq = c + 1

    if izq > der:
        pos = izq

    # indices       0   1
    # v_lotes = [  L2,  L1,      ]
    # nombre        B   C
    v_lotes[pos:pos] = [nuevo_lote]


# =================================================================
#                   Opcion 2
# =================================================================
def mostrar_datos(v_lotes):
    # indices       0,      1       2
    # v_lotes = [   L1,     L2,     L3    ]
    for i in v_lotes:
        # i = L1 , L2 , L3
        print(i)


# =================================================================
#                   Opcion 3
# =================================================================
def generar_matriz(v_lotes, m):

    # crear la matriz
    f = 4    # f = filas = orientacion(1, 4) = lim_superior - lim_inferior + 1 = 4 - 1 + 1 = 4
    c = 35    # c = columnas = manzana(1, 35) = lim_superior - lim_inferior + 1 = 35 - 1 + 1 = 35
    matriz = [ [0] * c for i in range(f) ]

    #
    # orientacion(1,4)     1-1   2   3   4
    # indices_fila          0   1   2   3

    # manzana(1, 35)       1-1   2   3                   35
    # indices_columnas      0   1   2   3   ...     34

    # matriz[f][c]
    # [ [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#       [0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#       [0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  ]

    #
    # rellenar la matriz
    for i in v_lotes:
        # i = L1, L2, L3
        # matriz [f] [c]
        matriz[i.orientacion - 1][i.manzana - 1] += i.superficie
        # matriz[i.orientacion - 1][i.manzana - 1] += 1

    #
    # mostrar la matriz

    # Mostrar, además, la superficie total vendida para una manzana m
    acum = 0

    tupla_orientaciones = ("Norte", "Sur", "Este", "Oeste")

    for f in range(len(matriz)):    # range(4)
        # f = 0, 1, 2, 3

        for c in range(len(matriz[0])): # range(35)
            # c = 0, 1, 2, ..., 34

            # Solo mostrar las superficie vendidas mayores a 0
            if matriz[f][c] > 0:
                # print("Manzana:", c+1, "| Orientación:", f+1, "| Superficie vendida:", matriz[f][c])
                print("Manzana:", c+1, "| Orientación:", tupla_orientaciones[f], "| Superficie vendida:", matriz[f][c])

            # Solo mostrar las manzanas que esten entre m1 y m2
            # if m1 <= c+1 <= m2:
            #    pass # print()

            # Mostrar, además, la superficie total vendida para una manzana m
            if c+1 == m:
                acum += matriz[f][c]

    print("Para la manzana", m, "el acumulado de:", acum)


# =================================================================
#                   Opcion 4
# =================================================================
def generar_archivo_binario(v_lotes, fd, l1, l2):

    m = open(fd, "wb")      # primer parametro --> el nombre del archivo (fd)
                            # segundo parametro --> el modo de apertura ( "wb" )

    # wb = write binary = crea el archivo si no existe, sobre-escribe todo el contenido del archivo
    # ab = append binary = crea el archivo si no existe, agrega el contenido al final del archivo, conservando
    # todo lo anterior --> ab

    for i in v_lotes:
        # i = L1 , L2

        # el numero de lote este entre l1 y l2 ; solo guardar orientaciones Norte y Sur
        if l1 <= i.num_lote <= l2 and (i.orientacion == 1 or i.orientacion == 2):

            pickle.dump(i, m)   # primer parametro = que quiero guardar ( i )
                            # segundo parametro = donde lo quiero guardar ( m )

            m.flush()   # opcional --> se usa para guardar mejor el archivo

    print("Se genero el archivo.")  # opcional

    m.close()       # OBLIGATORIO


# =================================================================
#                   Opcion 5
# =================================================================
def mostrar_archivo_binario(fd):
    bandera = os.path.exists(fd)    # return True si existe, return False si no existe
    if bandera is False:
        print("El archivo no existe.")
        return      # cortar una funcion

    m = open(fd, "rb")  # rb = read binary = modo de lectura
    tam = os.path.getsize(fd)   # nos dice el peso del archivo 270 bytes

    #
    # archivo = [       L1             L2       ]
    # bytes     0               130             270
    # m.tell()  0               130             270

    # agregue una línea que informe el valor promedio de venta de los lotes contenidos en el
    # archivo que pertenezcan a la orientacion Norte.
    # promedio = acumulador ( de importe ) / cantidad
    acum = 0
    cont = 0

    while m.tell() < tam:

        lotecito = pickle.load(m)   # unico parametro el archivo (m)
        # lotecito = L1 ,        L2

        print(lotecito)

        if lotecito.orientacion == 1:
            acum += lotecito.importe
            cont += 1

    # calcular el promedio
    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio es:", prom)

    m.close()   # OBLIGATORIO


# =================================================================
#                   Opcion 6
# =================================================================
def busqueda_binaria(v_lotes, nom):
    izq, der = 0, len(v_lotes) - 1

    while izq <= der:
        c = (izq + der) // 2  # c = 0

        # if v_lotes[c].nombre == nuevo_lote.nombre:
        if v_lotes[c].nombre == nom:
            pos = c
            # break
            return pos      # 0 o mas

        # elif v_lotes[c].nombre > nuevo_lote.nombre:
        elif v_lotes[c].nombre > nom:
            der = c - 1

        else:
            izq = c + 1

    return -1           # -1 cuando No existe


def menu():
    print("1 - Cargar Arreglo.")
    print("2 - Mostrar Arreglo.")
    print("3 - Generar Matriz.")
    print("4 - Generar el archivo binario.")
    print("5 - Mostrar el archivo binario.")
    print("6 - Busqueda Binaria.")
    op = int(input("Ingresar opción: "))
    return op


def principal():

    # vector / arreglo de trabajo
    v_lotes = []

    # nombre del archivo binario
    fd = "lotes.dat"   # file description ; nombre del archivo

    op = -1
    while op != 0:
        op = menu()

        if op == 1:
            n = validar_n()
            # si te piden generar nuevamente el arreglo cada vez que se ingrese a la opcion
            v_lotes = []
            cargar_arreglo(v_lotes, n)

        elif op == 2:

            # if v_lotes:     # si existe, cuando tiene contenido
            if len(v_lotes) > 0:        # significa que tiene contenido
                mostrar_datos(v_lotes)
            else:
                print("El arreglo no esta cargado.")

        elif op == 3:
            """ 
            3 - A partir del arreglo generado en el punto 1, acumular y mostrar la superficie total 
            vendida por cada manzana posible combinada con cada orientación posible. Mostrar, además, 
            la superficie total vendida para una manzana m (siendo m un valor que se ingresa por teclado)
            """
            if len(v_lotes) > 0:        # significa que tiene contenido
                m = int(input("Ingresar superficie total a superar: "))
                generar_matriz(v_lotes, m)

            else:
                print("El arreglo no esta cargado.")

        elif op == 4:
            """
            4 - A partir del arreglo, genere un archivo binario que contenga los datos de todos 
            los lotes cuyo número de lote esté comprendido entre l1 y l2 y además sean de la orientacion 
            Norte o Sur, siendo estos valores que se ingresan por teclado.
            """

            if len(v_lotes) > 0:        # significa que tiene contenido
                l1 = int(input("Ingresar num_lote a superar: "))
                l2 = int(input("Ingresar num_lote a ser menor: "))
                generar_archivo_binario(v_lotes, fd, l1, l2)

            else:
                print("El arreglo no esta cargado.")

        elif op == 5:
            """
            5 -  Mostrar el archivo generado en el punto anterior y luego de mostrarlo agregue una
            línea que informe el valor promedio de venta de los lotes contenidos en el archivo que pertenezcan
            a la orientacion Norte.
            """
            mostrar_archivo_binario(fd)

        elif op == 6:
            """
            6 - buscar por nombre "nom" y si existe hacerle un descuento del 22% y si no existe informar 
            el mensaje "no existe asd"
            """
            nom = input("Nombre a buscar: ")
            pos = busqueda_binaria(v_lotes, nom)

            if pos >= 0:
                print("Datos sin actualizar:", v_lotes[pos])

                v_lotes[pos].importe -= v_lotes[pos].importe * 0.22

                print("Datos actualizados:", v_lotes[pos])

            else:
                print("no existe asd.")


if __name__ == "__main__":
    principal()

