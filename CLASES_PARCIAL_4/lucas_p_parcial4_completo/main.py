import os.path
import pickle
import random

from registro import *


# ==============================================================
#                   Opcion 1
# ==============================================================
def validar_n():
    n = int(input("Ingresar pantalones a cargar: "))
    while n <= 0:
        n = int(input("Ingresar pantalones a cargar: "))
    return n


def cargar_arreglo(v_pantalones, n):

    # codigo INT, nombre STR, largo (30, 50) , cintura (30, 50), tela ( 1, 3), stock INT, importe FLOAT
    for i in range(n):
        codigo = random.randint(1, 15)
        nombre = random.choice("ABCDEF")
        largo = random.randint(1, 4)
        cintura = random.randint(30, 50)
        tela = random.randint(1, 3)
        stock = random.randint(1, 10)
        importe = round(random.uniform(0.1, 10), 2)

        nuevo_pant = Pantalon(codigo, nombre, largo, cintura, tela, stock, importe)
        add_in_order(v_pantalones, nuevo_pant)


def add_in_order(v_pantalones, nuevo_pant):
    # P1.codigo =   3
    # P2.codigo =   2
    # v_pantalones = [  P1  ]

    izq, der = 0, len(v_pantalones) - 1
    # izq = 0
    # der = -1

    while izq <= der:

        c = (izq + der) // 2    # c = centro = 0

        # porque atributo lo comparamos
        if v_pantalones[c].codigo == nuevo_pant.codigo:
            pos = c
            break

        # la boquita define si esta ordenado de menor a mayor o mayor a menor
        elif v_pantalones[c].codigo > nuevo_pant.codigo:
            der = c - 1

        else:
            izq = c + 1

    if izq > der:
        pos = izq

    # indices           0
    # v_pantalones = [  P2,     P1]
    # codigo            2       3
    v_pantalones[pos:pos] = [nuevo_pant]        # --> el objeto va con CORCHETES


# ==============================================================
#                   Opcion 2
# ==============================================================
def mostrar_datos(v_pantalones):
    # indices           0       1
    # v_pantalones = [  P1,     P2]
    for i in v_pantalones:
        # i = P1, P2, P3 ...
        print(i)


# ==============================================================
#                   Opcion 3
# ==============================================================
def generar_matriz(v_pantalones, u):

    # crear matriz
    f = 4    # f = filas = largo(1, 4) = lim_superior - lim_inferior + 1 = 4 - 1 + 1 = 4
    c = 21    # c = columnas = cintura(30, 50) = lim_superior - lim_inferior + 1 = 50 - 30 + 1 = 21
    matriz = [[0] * c for i in range(f)]

    # largo(1, 4)      1-1 2-1 3-1 4-1
    # fila_indices      0   1   2   3

    # cintura(30, 50) 30-30 31-30  32
    # columnas_indices  0   1   2   3   ...                 20

    # matriz[f][c]
    # matriz = [    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #               [0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]     ]

    #
    # rellenar la matriz
    for i in v_pantalones:
        # i = P1, P2, P3
        # i.importe i.largo etc
        # matriz[f][c]
        matriz[i.largo - 1][i.cintura - 30] += i.stock
        # matriz[i.largo - 1][i.cintura - 30] += 1

    #
    # mostrar la matriz
    for f in range(len(matriz)):    # range(4)
        # f = 0, 1, 2, 3

        for c in range(len(matriz[0])):     # range(21)
            # c = 0, 1, 2, 3, ..., 20

            if matriz[f][c] > u:
                print("Talle Largo:", f+1, "| Talle Cintura:", c+30, "| Stock Disponible:", matriz[f][c])

            # solo mostrar los stocks de los talles de cintura entre "c1" y "c2"
            # if c1 <= c+30 <= c2:
            #    print( ... )


# ==============================================================
#                   Opcion 4
# ==============================================================
def generar_archivo_binario(v_pantalones, fd, t):

    m = open(fd, "wb")      # --> primer parametro es el nombre del archivo (fd)
                            # segundo parametro es el modo de apertura

    # write binary = crea el archivo si no existe, sobre escribe todo su contenido

    # "ab" append bionary = crea el archivo si no existe, agrega contenido al final del archivo
    # pero conserva todo lo anterior

    for i in v_pantalones:
        # i = P1, P2, P3
        # los datos de todos los pantalones con stock disponible y cuya tela sea t.
        if i.stock > 0 and i.tela == t:

            pickle.dump(i, m)   # primer parametro que quiero guardar ( i )
                                # segundo parametro donde lo quiero guardar ( m )

            m.flush()   # opcional --> guarda mejor el archivo

    print("Se genero el archivo.")  # opcional
    m.close()   # OBLIGATORIO


# ==============================================================
#                   Opcion 5
# ==============================================================
def mostrar_archivo_binario(fd):

    if os.path.exists(fd) is False:       # es True cuando el archivo existe, y False cuando NO EXISTE
        print("El archivo no existe.")
        return      # cortar una funcion

    m = open(fd, "rb")  # read binary = modo de lectura
    tam = os.path.getsize(fd)   # nos dice el tamaño en bytes del archivo = 384 bytes

    #
    # archivos = [      P1                  P2                  P3          ]
    # bytes      0              130                 260                     384
    # m.tell()   0              130                 260

    # indicando además al final una línea extra con stock promedio de los pantalones
    # con tela de "Gabardina" o "Jean" guardados en el archivo

    # promedio = acumulador ( del stock ) / cantidad de veces que acumulamos
    acum = 0
    cont = 0

    while m.tell() < tam:

        pant = pickle.load(m)
        # pant = P1,  P2
        print(pant)

        if pant.tela == 1 or pant.tela == 2:
            acum += pant.stock
            cont += 1

    # calcular el promedio
    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio es:", prom)

    m.close()       # OBLIGATORIO


# ==============================================================
#                   Opcion 6
# ==============================================================
def busqueda_binaria(v_pantalones, cod):
    izq, der = 0, len(v_pantalones) - 1

    while izq <= der:
        c = (izq + der) // 2

        # if v_pantalones[c].codigo == nuevo_pant.codigo:
        if v_pantalones[c].codigo == cod:
            pos = c
            # break
            return pos

        # elif v_pantalones[c].codigo > nuevo_pant.codigo:
        elif v_pantalones[c].codigo > cod:
            der = c - 1

        else:
            izq = c + 1

    return -1       # -1 No existe


def menu():
    print("1 - Cargar Arreglo.")
    print("2 - Mostrar Arreglo.")
    print("3 - Generar Matriz.")
    print("4 - Generar archivo binario.")
    print("5 - Leer archivo binario.")
    print("6 o 3 - Busqueda Binaria.")
    print("0 - Salir.")
    op = int(input("Ingresar opcion: "))
    return op


def principal():

    # vector / arreglo / lista de trabajo
    v_pantalones = []

    # nombre del archivo binario
    fd = "pantalones.dat"        # fd = file description = nombre del archivo

    op = -1
    while op != 0:

        op = menu()

        if op == 1:
            n = validar_n()
            cargar_arreglo(v_pantalones, n)

        elif op == 2:

            if len(v_pantalones) > 0:
                mostrar_datos(v_pantalones)
            else:
                print("Primero debe cargar el arreglo.")

        elif op == 3:
            """
            3 - . Determinar cuál es el stock disponible por cada combinación de talle de largo y talle de cintura. 
- Mostrar únicamente las combinaciones que disponen de un stock superior a "u" unidades, siendo u un valor que se 
ingresa por teclado.
            """
            if len(v_pantalones) > 0:
                u = int(input("Ingresar stock a superar: "))
                generar_matriz(v_pantalones, u)
            else:
                print("Primero debe cargar el arreglo.")

        elif op == 4:
            """
            4. A partir del arreglo generar un archivo binario donde se incluyan los datos de todos los 
        pantalones con stock disponible y cuya tela sea t (siendo t un valor ingresado por teclado).

            """

            if len(v_pantalones) > 0:

                t = int(input("Ingresar una tela a guardar ( 1, 3 ): "))
                generar_archivo_binario(v_pantalones, fd, t)

            else:
                print("Primero debe cargar el arreglo.")

        elif op == 5:
            """
            5 -  Mostrar el archivo generado en el punto anterior indicando además al final una 
        línea extra con stock promedio de los pantalones con tela de "Gabardina" o "Jean" guardados en el archivo
            """
            mostrar_archivo_binario(fd)

        elif op == 6:
            """
            6  - buscar si existe un pantalon con el codigo "cod" 
            si existe hacerle un descuento del 22% al importe si la tela era "Gabardina"
            si no existe informar
            """
            cod = int(input("Ingresar numero de codigo a buscar: "))
            pos = busqueda_binaria(v_pantalones, cod)

            if pos >= 0:
                print("datos sin actualizar: ", v_pantalones[pos])

                if v_pantalones[pos].tela == 2:
                    v_pantalones[pos].importe -= v_pantalones[pos].importe * 0.22

                print("datos actualizados: ", v_pantalones[pos])

            else:
                print("No existe")


if __name__ == '__main__':
    principal()

