import os.path
import pickle
import random

from registro import *


# ===========================================================================
#                       Opcion 1
# ===========================================================================
def validar_n():
    n = int(input("Ingresar cantidad de pantalones a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de pantalones a cargar: "))
    return n


def cargar_arreglo(v_pantalones, n):
    # codigo INT , nombre STR, largo(30, 50), cintura( 5, 9 ), tela(1, 3), stock INT, importe FLOAT
    for i in range(n):
        codigo = random.randint(1, 30)
        nombre = random.choice("ABCDEF")
        largo = random.randint(30, 50)
        cintura = random.randint(5, 9)
        tela = random.randint(1, 3)
        stock = random.randint(1, 10)
        importe = round(random.uniform(0.1, 10), 2)

        nuevo_pant = Pantalon(codigo, nombre, largo, cintura, tela, stock, importe)
        add_in_order(v_pantalones, nuevo_pant)


def add_in_order(v_pantalones, nuevo_pant):
    # P1.codigo         4
    # P2.codigo         2
    # P6

    # indices           0
    # v_pantalones = [ P1 P2]
    # codigo            4

    izq, der = 0, len(v_pantalones) - 1
    # izq = 0
    # der = -1

    while izq <= der:
        c = (izq + der) // 2        # c = centro = 0

        # es el atributo que te pidan ordenar
        if v_pantalones[c].codigo == nuevo_pant.codigo:
            pos = c
            break

        # la boquita ">" determina si esta ordenador de menor  a mayor o mayor a menor
        elif v_pantalones[c].codigo > nuevo_pant.codigo:
            der = c - 1

        else:
            izq = c + 1

    if izq > der:
        pos = izq

    # indices          0    1
    # v_pantalones = [ P2,  P1]
    # codigo            2    4
    v_pantalones[pos:pos] = [nuevo_pant]        # el objeto va ENTRE CORCHETES [ ]


# ===========================================================================
#                       Opcion 2
# ===========================================================================
def mostrar_datos(v_pantalones):
    # indices          0    1
    # v_pantalones = [ P1,  P2]
    for i in v_pantalones:
        # i = P1, P2
        # i.importe i.nombre -->
        print(i)


# ===========================================================================
#                       Opcion 3
# ===========================================================================
def generar_matriz(v_pantalones, u):

    # crear la matriz
    f = 5       # f = filas = cintura(5, 9) = lim_superior - lim_inferior + 1 = 9 - 5 + 1 = 5
    c = 21      # c = columnas = largo(30, 50) = lim_superior - lim_inferior + 1 = 50 - 30 + 1 = 21
    matriz = [ [0] * c for i in range(f) ]

    # cintura(5, 9)   5-5   6   7   8   9
    # filas_indices     0   1   2   3   4

    # largo(30, 50)       30-30 31  32  33
    # columnas_indices      0   1   2   3   4   ...     21

    # matriz[f][c] =
    # matriz = [    [5, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #               [0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]     ]

    #
    # rellenar la matriz
    for i in v_pantalones:
        # i = P1, P2 , P3
        # i.cintura i.largo
        # matriz[f][c]
        matriz[i.cintura - 5][i.largo - 30] += i.stock
        # matriz[i.cintura - 5][i.largo - 30] += 1

    #
    # mostrar la matriz
    for f in range(len(matriz)):    # range(5)
        # f = 0, 1, 2, 3, 4

        for c in range(len(matriz[0])):     # range( 21 )
            # c = 0, 1, 2, 3, ... 20

            if matriz[f][c] > u:        # > 0
                print("Cintura:", f+5, "| Talle Largo:", c+30, "| Stock Disponible:", matriz[f][c])

            # si te pidieran solo mostras los talles de largo entre t1 y t2
            # if t1 <= c+30 <= t2:


# ===========================================================================
#                       Opcion 4
# ===========================================================================
def generar_archivo_binario(v_pantalones, fd, t):

    m = open(fd, "wb")  # primer parametro = nombre del archivo ( fd )
                        # segundo parametro = es el modo de apertura
    # wb = write binary = crea el archivo si no existe, sobre escribe todo su contenido cada vez
    # ab = append binary = crea el archivo si no existe, agrega contenido al final conservando
    # todo su contenido anterior

    for i in v_pantalones:
        # i = P1, P2, P3

        # los pantalones con stock disponible y cuya tela sea t
        if i.stock > 0 and i.tela == t:
            pickle.dump(i, m)       # primer parametro es que quiero guardar ( i )
                                    # segundo parametro donde lo quiero guardar ( m )
            m.flush()   # opcional --> para guardar mejor el archivo

    print("Se genero el archivo binario.")  # opcional
    m.close()   # OBLIGATORIO


# ===========================================================================
#                       Opcion 5
# ===========================================================================
def mostrar_archivo_binario(fd):
    bandera = os.path.exists(fd)      # retorna True si existe el archivo, retorna False si no existe
    if bandera is False:    # if not bandera
        print("El archivo no existe.")
        return          # cortar la funcion

    m = open(fd, "rb")  # read binary = modo de lectura
    tam = os.path.getsize(fd)       # nos devuelve el tamaño en bytes   # 256 bytes

    # archivo = [  P1           P2  ]
    # bytes     0       128          256
    # m.tell()  0       128         256

    # además al final una línea extra con stock promedio de los pantalones guardados en el archivo.
    # promedio = acumulado ( de stock ) / cantidad de veces que acumulamos
    acum = 0
    cont = 0

    while m.tell() < tam:
        pant = pickle.load(m)
        # pant = P1,    P2, ...
        print(pant)

        acum += pant.stock
        cont += 1

    # calcular promedio
    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio es:", prom)

    m.close()    # OBLIGATORIO


# ===========================================================================
#                       Opcion 6
# ===========================================================================
def busqueda_binaria(v_pantalones, cod):
    izq, der = 0, len(v_pantalones) - 1

    while izq <= der:
        c = (izq + der) // 2  # c = centro = 0

        # if v_pantalones[c].codigo == nuevo_pant.codigo:
        if v_pantalones[c].codigo == cod:
            pos = c
            # break
            return pos      # la posicion dentro del arreglo donde un objeto cumple con la busqueda

        # elif v_pantalones[c].codigo > nuevo_pant.codigo:
        elif v_pantalones[c].codigo > cod:
            der = c - 1

        else:
            izq = c + 1

    return -1   # no existe


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
    v_pantalones = []

    # nombre del archivo binario
    fd = "pantalones.dat"   # file description ; nombre del archivo

    op = -1
    while op != 0:
        op = menu()

        if op == 1:
            n = validar_n()
            """
            Cada vez que se ingrese en esta opción, el arreglo debe ser creado desde cero y todo contenido 
            anterior debe ser eliminado. """
            v_pantalones = []
            cargar_arreglo(v_pantalones, n)

        elif op == 2:
            if len(v_pantalones) > 0:
                mostrar_datos(v_pantalones)

            else:
                print("El arreglo no esta cargado")

        elif op == 3:
            """
            3 Determinar cuál es el stock disponible por cada combinación de talle de largo y talle de cintura. 
            Mostrar únicamente las combinaciones que disponen de un stock superior a u unidades, siendo 
            u un valor que se ingresa por teclado.
            """
            if len(v_pantalones) > 0:
                u = int(input("Ingrese stock a superar: "))
                generar_matriz(v_pantalones, u)

            else:
                print("El arreglo no esta cargado")

        elif op == 4:
            """
            4 - A partir del arreglo generar un archivo binario donde se incluyan los datos de todos 
            los pantalones con stock disponible y cuya tela sea t (siendo t un valor ingresado por teclado).
            """
            if len(v_pantalones) > 0:
                t = int(input("Ingresar tela a guardar: "))
                generar_archivo_binario(v_pantalones, fd, t)

            else:
                print("El arreglo no esta cargado")

        elif op == 5:
            """
            5 - Mostrar el archivo generado en el punto anterior indicando además al final una línea 
            extra con stock promedio de los pantalones guardados en el archivo.
            """
            mostrar_archivo_binario(fd)

        elif op == 6:
            """
            6 - buscar un codigo "cod" si existe y su tela era gabardina o jean hace un descuento del 22% y 
            si no existe informar con el siguiente mensaje "No existe asdasdadas"
            """
            cod = int(input("Ingresar codigo a buscar: "))
            pos = busqueda_binaria(v_pantalones, cod)
            if pos >= 0:

                print("Datos sin actualizar: ", v_pantalones[pos])

                if v_pantalones[pos].tela == 1 or v_pantalones[pos].tela == 2:
                    v_pantalones[pos].importe -= v_pantalones[pos].importe * 0.22

                print("Datos actualizados: ", v_pantalones[pos])

            else:   # pos = -1
                print("No existe asdasdadas")


if __name__ == "__main__":
    principal()
