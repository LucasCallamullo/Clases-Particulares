import os.path
import pickle
import random

from registro import *


# =====================================================
#           Opcion 1
# =====================================================
def validar_n():
    n = int(input("Ingresar cantidad de lotes a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de lotes a cargar: "))
    return n


def cargar_arreglo(v_lotes, n):
    # nombre STR, manzana(1, 35), num_lote(1, 20), orientacion(1, 4), superficie FLOAT, importe FLOAT
    for i in range(n):  # 3 vueltas
        # i = 0
        nombre = random.choice("ABCDEF")
        manzana = random.randint(1, 35)
        num_lote = random.randint(1, 20)
        orientacion = random.randint(1, 4)
        superficie = round(random.uniform(0.1, 10), 2)
        importe = round(random.uniform(0.1, 10), 2)

        nuevo_lote = Lote(nombre, manzana, num_lote, orientacion, superficie, importe)
        add_in_order(v_lotes, nuevo_lote)


def add_in_order(v_lotes, nuevo_lote):
    # L1.nombre = C
    # L2.nombre = B
    # v_lotes = [ L1 ]
    izq, der = 0, len(v_lotes) - 1
    # izq = 0
    # der = -1

    while izq <= der:       # mientras izq sea menor o igual que derecha ingreso al ciclo
        c = (izq + der) // 2
        # c = 0
        # el atributo a comparar que te pidan
        if v_lotes[c].nombre == nuevo_lote.nombre:
            pos = c
            break

        # la boquita ">" determinar si esta de mayor a menor o menor a mayor
        elif v_lotes[c].nombre > nuevo_lote.nombre:
            der = c - 1

        else:
            izq = c + 1

    if izq > der:
        pos = izq

    # v_lotes = [L2, L1]
    v_lotes[pos:pos] = [nuevo_lote]     # no te olvides los corchetes


# =====================================================
#           Opcion 2
# =====================================================
def mostrar_datos(v_lotes):

    # indices =     0       1
    # v_lotes = [   L1,     L2]
    for i in v_lotes:
        # i = L1 , L2
        print(i)


# =====================================================
#           Opcion 3
# =====================================================
def generar_matriz(v_lotes, m):

    # crear la matriz
    f = 4    # f = fila = orientacion(1, 4) --> lim_superior - lim_inferior + 1 = 4 - 1 + 1 = 4
    c = 35    # c = columna = manzana(1, 35)  --> lim_superior - lim_inferior + 1 = 35 - 1 + 1 = 35
    matriz = [ [0] * c for i in range(f) ]  # generar una matriz

    # orientacion(1, 4)                1-1 2-1   3   4
    # los indices de la fila (0, 3)     0   1   2   3

    # manzana(1, 35)               1-1  2  3  ...  35
    # los indices de las columnas   0, 1, 2, ..., 34

    # [ [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   ]

    # rellenar la matriz
    for i in v_lotes:
        # i = L1, L2, L3
        # matriz[f][c] += i.superficie
        matriz[i.orientacion - 1][i.manzana - 1] += i.superficie
        # matriz[i.orientacion - 1][i.manzana - 1] += 1

    # -----
    # mostrar la matriz
    # ----

    # Mostrar, además, la superficie total vendida para una numero manzana m (se ingresa por teclado).
    acum = 0

    for f in range(len(matriz)):    # range(4)
        # f = filas = 0, 1, 2, 3

        for c in range(len(matriz[0])): # range(35)
            # c = columnas = 0, 1, 2, ..., 34

            # solo muestres los que superan un contador/acumulador mayor a 0
            if matriz[f][c] > 0:
                print("Orientación:", f+1, "| Manzana:", c+1, "| Superficie vendida:", matriz[f][c])

            # solo mostrar los que tengan una orientacion distinta de oeste
            if f+1 != 4:
                pass
                # print("Orientación:", f + 1, "| Manzana:", c + 1, "| Superficie vendida:", matriz[f][c])

            if c+1 == m:
                acum += matriz[f][c]

    print("El acumulado de la superficie para la manzana:", m, "es:", acum)


# =====================================================
#           Opcion 4
# =====================================================
def generar_archivo_binario(v_lotes, fd, l1, l2):

    m = open(fd, "wb")  # primer parametro: NOMBRE DEL ARCHIVO (fd)
    # segundo parametro: MODO DE APERTURA -->
    #   "WB" write binary: crea el archivo si no existe, y sobre escribe tod0 su contenido
    #   "AB" append binary: crea el archivo si no existe, y agrega al contenido al final, conservando tod0 lo anterior

    for i in v_lotes:
        # i = L1, L2
        # solo guardar los numeros de lote entre l1 y l2
        if l1 <= i.num_lote <= l2:
            pickle.dump(i, m)   # primer parametro: LO QUE QUIERO GUARDAR (i)
                                # segundo parametro: DONDE LO QUIERO GUARDAR (m)
            m.flush()   # OPCIONAL

    print("Se genero el archivo binario.")
    m.close()  # OBLIGATORIO


# =====================================================
#           Opcion 5
# =====================================================
def mostrar_archivo_binario(fd):

    if os.path.exists(fd) is False:
        print("El archivo no existe.")
        return

    m = open(fd, "rb")  # read binary = leer el archivo
    tam = os.path.getsize(fd)   # nos dice el tamaño del archivo: 540 bytes

    # indices =     0       1
    # v_lotes = [   L1,     L2]

    # archivo = [ L1         L2          L3             L4 ]
    # bytes     0       125         250         375         540
    # m.tell()  0       125         250

    """ informe al final del listado el valor promedio de venta de los lotes contenidos 
    en el archivo que sean de la orientacion Norte y Sur."""
    # promedio = acumulado ( de importes ) / cantidad
    acum = 0
    cont = 0

    while m.tell() < tam:   # 125 < 540:
        lotecito = pickle.load(m)    # primer parametro, de donde recupero los objetos (m)
        # lotecito = L1, L2, L3, L4
        print(lotecito)

        if lotecito.orientacion == 1 or lotecito.orientacion == 2:
            acum += lotecito.importe
            cont += 1

    # calcular el promedio
    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio de los importes de los lotes norte y sur: ", round(prom, 2))

    m.close()       # OBLIGATORIO


# =====================================================
#           Opcion 6
# =====================================================
def busqueda_binaria(v_lotes, nom): # A
    # indices =     0       1
    # v_lotes = [   L1,     L2,     L3,     L4 ]
    # nombre        A

    izq, der = 0, len(v_lotes) - 1

    while izq <= der:
        c = (izq + der) // 2

        # if v_lotes[c].nombre == nuevo_lote.nombre:
        if v_lotes[c].nombre == nom:
            pos = c
            # break
            return pos

        # la boquita ">" determinar si esta de mayor a menor o menor a mayor
        # elif v_lotes[c].nombre > nuevo_lote.nombre:
        elif v_lotes[c].nombre > nom:
            der = c - 1

        else:
            izq = c + 1

    return -1


def menu():
    print(" 1 - Cargar Arreglo.")
    print(" 2 - Mostrar Arreglo.")
    print(" 3 - Generar Matriz.")
    print(" 4 - Generar Archivo Binario.")
    print(" 5 - Mostrar archivo binario.")
    print(" 6 - Busqueda Binaria.")
    print(" 0 - Salir.")
    op = int(input("Ingresar opcion: "))
    return op


def principal():

    # vector/arreglo/lista de trabajo
    v_lotes = []

    # el nombre de nuestro archivo binario
    fd = "lotes.dat"    # fd, file description, nombre del archivo

    op = -1
    while op != 0:

        op = menu()

        if op == 1:
            n = validar_n()
            # Cada vez que se ingrese en esta opción, el arreglo debe ser creado desde cero y
            # tod0 contenido anterior debe ser eliminado.
            v_lotes = []
            cargar_arreglo(v_lotes, n)

        elif op == 2:
            if len(v_lotes) > 0:
                mostrar_datos(v_lotes)
            else:
                print("El arreglo no esta cargado.")

        elif op == 3:
            """
            3 - A partir del arreglo generado en el punto 1, acumular y mostrar la superficie total 
            vendida por cada manzana posible combinada con cada orientación posible. Mostrar, además, 
            la superficie total vendida para una manzana m (siendo m un valor que se ingresa por teclado).
            """
            if len(v_lotes) > 0:
                m = int(input("Ingresar manzana a buscar: "))
                generar_matriz(v_lotes, m)
            else:
                print("El arreglo no esta cargado.")

        elif op == 4:
            """ 
            4 - A partir del arreglo, genere un archivo binario que contenga los datos de todos 
            los lotes cuyo número de lote esté comprendido entre l1 y l2, siendo estos valores 
            que se ingresan por teclado.
            """
            if len(v_lotes) > 0:
                l1 = int(input("Ingresar num_lote a superar: "))
                l2 = int(input("Ingresar num_lote a ser menor: "))
                generar_archivo_binario(v_lotes, fd, l1, l2)
            else:
                print("El arreglo no esta cargado.")

        elif op == 5:
            """
            5 - Mostrar el archivo generado en el punto anterior y luego de mostrarlo 
            agregue una línea que informe el valor promedio de venta de los lotes contenidos 
            en el archivo que sean de la orientacion Norte y Sur.
            """
            mostrar_archivo_binario(fd)

        elif op == 6:
            """
            6 - buscar un nombre de propietario "nom" que se carga por teclado
            si se encuentra hacer un descuento del 22% y mostrar sus datos antes y despues del cambio, 
            y si tiene una orientacion norte poner un mensaje
            que diga "Buena ubicación!" , informar si no existe
            """

            if len(v_lotes) > 0:

                nom = input("Ingresar nombre a buscar: ")
                pos = busqueda_binaria(v_lotes, nom)

                if pos >= 0:
                    print("Datos sin actualizar:", v_lotes[pos])

                    v_lotes[pos].importe -= v_lotes[pos].importe * 0.22

                    print("Datos actualizados:", v_lotes[pos])

                    if v_lotes[pos].orientacion == 1:
                        print("Buena ubicación!")

                else:
                    print("El Lote con ese propietario no existe.")

            else:
                print("El arreglo no esta cargado.")


if __name__ == '__main__':
    principal()