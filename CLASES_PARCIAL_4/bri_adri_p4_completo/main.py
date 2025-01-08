import os.path
import pickle
import random

from registro import *


# ===========================================================================
#                   Opcion 1
# ===========================================================================
def validar_n():
    n = int(input("Ingresar cantidad de pantalones a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de pantalones a cargar: "))
    return n


def cargar_arreglo(v_pantalones, n):
    # codigo INT > 0 , nombre STR, largo(30, 50), cintura(30, 50), tela(1, 3), stock INT, importe FLOAT
    for i in range(n):
        codigo = random.randint(1, 15)
        nombre = random.choice("ABCDEF")    # STR
        largo = random.randint(30, 50)
        cintura = random.randint(3, 7)
        tela = random.randint(1, 3)
        stock = random.randint(1, 10)
        importe = round(random.uniform(0.1, 10), 2)

        nuevo_pant = Pantalon(codigo, nombre, largo, cintura, tela, stock, importe)
        add_in_order(v_pantalones, nuevo_pant)


def add_in_order(v_pantalones, nuevo_pant):

    izq, der = 0, len(v_pantalones) - 1

    while izq <= der:

        c = (izq + der) // 2
        # cambia el atributo por el que les pidan ordenar
        if v_pantalones[c].codigo == nuevo_pant.codigo:
            pos = c
            break

        # la boquita ">" determina si esta de menor a mayor o mayor a menor
        elif v_pantalones[c].codigo > nuevo_pant.codigo:
            der = c - 1

        else:
            izq = c + 1

    if izq > der:
        pos = izq

    # v_pantalones = [ P2,  P1 ]
    # codigo            2    3

    v_pantalones[pos:pos] = [nuevo_pant]        # el objeto esta ENTRE CORCHETES


# ===========================================================================
#                   Opcion 2
# ===========================================================================
def mostrar_datos(v_pantalones):
    #
    # v_pantalones = [ P1,  P2 ]
    for i in v_pantalones:
        # i = P1,   P2. P3
        print(i)


# ===========================================================================
#                   Opcion 3
# ===========================================================================
def generar_matriz(v_pantalones, u):

    # crear la matriz       cintura x largo
    f = 5    # f = filas = cintura(3, 7) = lim_superior - lim_inferior + 1 = 7 - 3 + 1 = 5
    c = 21   # c = columnas = largo(30, 50) = lim_superior - lim_inferior + 1 = 50 - 30 + 1 = 21
    matriz = [ [0] * c for i in range(f) ]

    # cintura(3, 7)    3-3 4-3 5-3 6-3   7
    # fila_indices      0   1   2   3   4

    # largo(30, 50)  30-30 31-30  32  33  ... 50
    # columna_indices   0   1   2   3   ... 20

    # matriz[f][c]
    # [     [10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]     ]
    #

    #
    # rellenar la matriz
    for i in v_pantalones:
        # i = P1,   P2, P3, ...
        # matriz[f][c]
        matriz[i.cintura - 3][i.largo - 30] += i.stock

    #
    # Mostrar la matriz
    for f in range(len(matriz)):    # range(5)
        # f = 0, 1, 2, 3, 4

        for c in range(len(matriz[0])):     # range(21)
            # c = 0, 1, 2, ..., 20

            if matriz[f][c] > u:
                print("Cintura:", f+3, "| Talle Largo:", c+30, "| Stock acumulado:", matriz[f][c])

            # solo mostrar los valores de los stock que estan entre los talle de largo l1 y l2 que se cargan por teclado
            # if l1 <= c+30 <= l2:
            #    print("Cintura:", f + 3, "| Talle Largo:", c + 30, "| Stock acumulado:", matriz[f][c])


# ===========================================================================
#                   Opcion 4
# ===========================================================================
def generar_archivo_binario(v_pantalones, fd, t):

    m = open(fd, "wb")  # primer parametro es el nombre  del archivo ( fd )
                        # segundo parametro es el modo de apertura ( "wb" )
    # wb = write binary = crea el archivo si no existe, sobre escribe todo su contenido
    # ab = append binary = crea el archivo si no existe, agrega contenido al final del archivo
    # conservando todo su contenido anterior

    # v_pantalones = [ P1,  P2, P3 ]
    for i in v_pantalones:
        # i = P1,   P2,  P3

        # se incluyan los datos de todos los pantalones con stock disponible y cuya tela sea t
        if i.stock > 0 and i.tela == t:
            pickle.dump(i, m)   # primer parametro = lo que quiero guardar ( i )
                            # segundo parametro = donde lo quiero guardar ( m )

    print("Se genero el archivo.")  # Opcional
    m.close()   # OBLIGATORIO


# ===========================================================================
#                   Opcion 5
# ===========================================================================
def mostrar_archivo_binario(fd):

    bandera = os.path.exists(fd)    # retorna TRUE si existe el archivo, retorna FALSE si NO EXISTE
    if bandera is False:    # if not bandera
        print("El archivo no existe.")
        return      # cortar la funcion

    m = open(fd, "rb")  # rb = read binary -> modo de lectura
    tam = os.path.getsize(fd)   # nos dice el tamaño en bytes del archivo  = 300 bytes

    # archivo = [   P1        P2         P3     ]
    # bytes     0       100         200         300
    # m.tell()  0       100         200

    # indicando además al final una línea extra con stock promedio de los pantalones guardados en el archivo.
    # promedio = acumulado ( de stock ) / la cantidad de veces que acumule
    acum = 0
    cont = 0

    while m.tell() < tam:
        pant = pickle.load(m)   # unico parametro el archivo ( m )
        # pant = P1, P2
        print(pant)

        acum += pant.stock
        cont += 1

    # calcular el promedio
    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio es:", prom)

    m.close()   # OBLIGATORIO


# ===========================================================================
#                   Opcion 6
# ===========================================================================
def busqueda_binaria(v_pantalones, cod):
    izq, der = 0, len(v_pantalones) - 1

    while izq <= der:

        c = (izq + der) // 2
        # if v_pantalones[c].codigo == nuevo_pant.codigo:
        if v_pantalones[c].codigo == cod:
            pos = c
            # break
            return pos  # pos = es un indice del arreglo donde existe un objeto que cumple mi criterio
                        # de busqueda   ( 0 o mas )

        # elif v_pantalones[c].codigo > nuevo_pant.codigo:
        elif v_pantalones[c].codigo > cod:
            der = c - 1

        else:
            izq = c + 1

    return -1   # no existe un pantalon que cumpla


def menu():
    print("1 - Cargar arreglo.")
    print("2 - Mostrar arreglo.")
    print("3 - Generar matriz.")
    print("4 - Generar archivo binario.")
    print("5 - Mostrar archivo binario.")
    print("6 - busqueda binaria.")
    op = int(input("Ingresar opción: "))
    return op


def principal():

    # arreglo / lista / vector de trabajo
    v_pantalones = []

    # nombre del archivo binario
    fd = "pantalones.dat"

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
                print("Debe cargar el arreglo en la opcion 1.")

        elif op == 3:
            """
            3 - Determinar cuál es el stock disponible por cada combinación de talle de largo
            y talle de cintura. Mostrar únicamente las combinaciones que disponen de un stock 
            superior a "u" unidades, siendo u un valor que se ingresa por teclado.
            """
            if len(v_pantalones) > 0:
                u = int(input("Ingresar stock a superar: "))
                generar_matriz(v_pantalones, u)
            else:
                print("Debe cargar el arreglo en la opcion 1.")

        elif op == 4:
            """
            4 -  A partir del arreglo generar un archivo binario donde se incluyan 
            los datos de todos los pantalones con stock
            disponible y cuya tela sea t (siendo t un valor ingresado por teclado).
            """
            if len(v_pantalones) > 0:
                t = int(input("Ingresar tela a buscar ( 1, 3 ) : "))
                generar_archivo_binario(v_pantalones, fd, t)
            else:
                print("Debe cargar el arreglo en la opcion 1.")

        elif op == 5:
            """
            5 - Mostrar el archivo generado en el punto anterior indicando además al final una 
            línea extra con stock promedio de los pantalones guardados en el archivo.
            """
            mostrar_archivo_binario(fd)

        elif op == 6:
            """
            6 - buscar un pantalon por "cod" codigo, si existe mostrar datos antes y despues de hacer
            un descuento del 22%, si no existe informar
            """
            cod = int(input("Ingresar codigo a buscar: "))
            pos = busqueda_binaria(v_pantalones, cod)

            if pos >= 0:
                print("Datos sin actualizar:", v_pantalones[pos])

                # hacer un descuento del 22%
                v_pantalones[pos].importe -= v_pantalones[pos].importe * 0.22

                print("Datos actualizados:", v_pantalones[pos])

            else:   # pos = -1
                print("No existe.")


if __name__ == "__main__":
    principal()
