import os.path
import pickle
import random

from registro import *


# ========================================================
#                   Opcion 1
# ========================================================
def validar_n():
    n = int(input("Ingresar cantidad de libros a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de libros a cargar: "))
    return n


def cargar_arreglo(v_libros, n):
    # isbn 13digitos INT , titulo STR, autor(2, 7),
    # idioma(1, 5) (1: Español, 2: Inglés, 3: Portugués, 4: Francés, 5: Italiano), importe FLOAT
    for i in range(n):
        isbn = random.randint(1000000000000, 9000000000100)     # INT
        titulo = random.choice("ABCDE")     # STR
        autor = random.randint(2, 7)
        idioma = random.randint(1, 5)
        importe = round(random.uniform(0.1, 10), 2)

        librito = Libro(isbn, titulo, autor, idioma, importe)
        add_in_order(v_libros, librito)


def add_in_order(v_libros, librito):
    # L1.isbn = 3
    # L2.isbn = 2

    # indices     0     1
    # v_libros = [L2,   L1    ]
    # isbn        2      3

    izq, der = 0, len(v_libros) - 1
    # izq = 0
    # der = -1

    while izq <= der:
        c = (izq + der) // 2
        # lo unico que cambia es el atributo por el que te pidan ordenar
        if v_libros[c].isbn == librito.isbn:
            pos = c
            break
        # lo que define si esta ordenador de menor a mayor o de mayor a menor es la ">"
        elif v_libros[c].isbn > librito.isbn:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v_libros[pos:pos] = [librito]


# ========================================================
#                   Opcion 2
# ========================================================
def mostrar_arreglo(v_libros):
    # indices      0   1   2
    # v_libros = [L1, L2, L3]
    for i in v_libros:
        # i = L1, L2, L3
        print(i)


# ========================================================
#                   Opcion 3
# ========================================================
def generar_matriz(v_libros, x):

    # crear la matriz
    f = 5    # f = filas = idiomas(1, 5) ; lim_superior - lim_inferio + 1 = 5 - 1 + 1 = 5
    c = 6    # c = columnas = autor(2, 7) ; lim_superior - lim_inferio + 1 = 7 - 2 + 1 = 6
    matriz = [ [0] * c for i in range(f) ]

    #
    # los indices de la fila deben hacer referencia a cada idioma
    # idiomas(1,5) 1-1  2  3  4  5
    # indices_fila  0, 1, 2, 3, 4

    # autor(2 , 7)     2-2   3   4   5   6   7
    # indices_columnas  0   1   2   3   4   5

    # matriz =      -> matriz[f][c] -> matriz[0][2] += 1
    # [ [0, 0, 1, 0, 0, 0],
    #   [0, 0, 0, 0, 0, 0],
    #   [0, 0, 0, 0, 0, 0],
    #   [0, 0, 0, 0, 0, 0],
    #   [0, 0, 0, 0, 0, 0]  ]

    # rellenar la matriz
    for i in v_libros:
        # i = L1, L2, L3
        # matriz[f][c]
        matriz[i.idioma - 1][i.autor - 2] += 1
        # matriz[i.idioma - 1][i.autor - 2] += i.importe

    # mostrar la matriz
    for f in range(len(matriz)):    # range(5)
        # f = filas = 0, 1, 2, 3, 4

        for c in range(len(matriz[0])):     # range(6)
            # c = 0, 1, 2, 3, 4, 5

            # solo mostrar los contadores que superen un valor "x"
            if matriz[f][c] > x:
                print("Idioma:", f+1, "| Autor:", c+2, "| Tiene la cantidad de:", matriz[f][c])

            # solo mostrar los autores del x1 al x2
            # if x1 <= c+2 <= x2:
            #    pass


# ========================================================
#                   Opcion 4
# ========================================================
def generar_archivo_binario(v_libros, fd, a, p):
    # open() recibe dos parametros
    m = open(fd, "wb")      # el primero es el nombre del archivo (fd) , y el segundo es el modo de apertura
    # write binary; escribir en binario, crea un archivo binario si no existe, sobreescribe tod0 su contenido
    # "ab" append binary; crea archivo si no existe, agrega contenido al final del archivo conservando tod0 lo anterior

    for i in v_libros:
        # i = L1, L2, L3
        # solo guardar los que tuvieran un autor "a" y precio menor a "p"
        if i.autor == a and i.importe < p:
            pickle.dump(i, m)   # recibe dos parametros -> el primero es lo que quiero guardar (i)
                                                #   -> el segundo es donde guardarlo (m)
            m.flush()   # opcional

    print("Se guardo el archivo binario.")
    m.close()   # OBLIGATORIO


# ========================================================
#                   Opcion 5
# ========================================================
def mostrar_archivo_binario(fd):
    if os.path.exists(fd) is False:
        print("El archivo no existe.")
        return

    m = open(fd, "rb")  # read binary, leer el contenido del archivo
    tam = os.path.getsize(fd)   # nos dice el tamaño en bytes del archivo = 218 bytes

    # indices      0   1   2
    # v_libros = [L1, L2, L3]

    #
    # archivo = [ L1            L2  ]
    # bytes     0       104         218
    # m.tell()  0       104         218

    # al final del listado calcular el promedio de los importes de los libros que se mostraron
    # promedio = acumulador ( importes ) / cantidad
    acum = 0
    cont = 0

    while m.tell() < tam:
        librito = pickle.load(m)
        # librito = L1, L2

        # solo mostrar los que sean del idioma  "Inglés" y "Francés"
        if librito.idioma == 2 or librito.idioma == 4:
            print(librito)
            acum += librito.importe
            cont += 1

    # calcular el promedio
    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio de los importes mostrados es:", prom)

    m.close()       # OBLIGATORIO


# ========================================================
#                   Opcion 6
# ========================================================
def busqueda_binaria(v_libros, x):
    izq, der = 0, len(v_libros) - 1
    # izq = 0
    # der = -1

    while izq <= der:
        c = (izq + der) // 2
        # if v_libros[c].isbn == librito.isbn:
        if v_libros[c].isbn == x:
            # pos = c
            # break
            return c
        # elif v_libros[c].isbn > librito.isbn:
        elif v_libros[c].isbn > x:
            der = c - 1
        else:
            izq = c + 1

    return -1


def menu():
    print("1 - Cargar Arreglo.")
    print("2 - Mostrar Arreglo.")
    print("3 - Generar una matriz.")
    print("4 - Generar Archivo Binario.")
    print("5 - Mostrar Archivo Binario.")
    print("6 - Busqueda binaria.")
    print("0 - Salir.")
    op = int(input("Ingresar opción: "))
    return op


def principal():

    # lista/vector/arreglo de trabajo
    v_libros = []

    # nombre del archivo binario de trabajo
    fd = "libros.dat"   # file description ; nombre del archivo

    op = -1
    while op != 0:

        op = menu()
        if op == 1:
            n = validar_n()
            # Cada vez que se ingrese en esta opción, el arreglo debe ser creado desde cero y
            # tod0 contenido anterior debe ser eliminado.
            v_libros = []
            cargar_arreglo(v_libros, n)

        elif op == 2:
            if len(v_libros) > 0:
                mostrar_arreglo(v_libros)
            else:
                print("debe primero cargar el arreglo con la opcion 1.")

        elif op == 3:
            """
            3 - determinar cuantos libros hay por cada posible autor y cada posible idioma
            - solo mostrar los contadores que sean mayores a "x"
            """
            if len(v_libros) > 0:
                x = int(input("Ingresar cantidad a cargar: "))
                generar_matriz(v_libros, x)
            else:
                print("debe primero cargar el arreglo con la opcion 1.")

        elif op == 4:
            """
            4 - A partir del arreglo genere un archivo binario que contenga los datos 
            de todos los libros del autor a cuyo precio no supere p, siendo a y p dos valores 
            ingresados por teclado
            """
            if len(v_libros) > 0:
                a = int(input("Ingresar autor a guardar(2, 7): "))
                p = float(input("Ingresar precio a no superar: "))
                generar_archivo_binario(v_libros, fd, a, p)
            else:
                print("debe primero cargar el arreglo con la opcion 1.")

        elif op == 5:
            """
            5 - Mostrar el archivo generado en el punto anterior indicando, al final, 
            cuánto es el promedio de los libros que se mostraron
            """
            mostrar_archivo_binario(fd)

        elif op == 6:
            """
            6 - Buscar un vehículo por ISBN. Si existe mostrar todos sus datos y si, además, 
            el idioma del mismo es Francés, realizar un descuento del 22% sobre su precio de venta,
            mostrando los datos del libro antes y después de la actualización. Si el libro 
            no existe informar con el mensaje “No contamos con el libro <ISBN> pero no deje de
            visitar nuestra sección de ofertas!”.
            """
            if len(v_libros) > 0:
                x = int(input("Ingresar numero ISBN a buscar: "))
                pos = busqueda_binaria(v_libros, x)

                if pos >= 0:
                    print("Datos sin actualizar:", v_libros[pos])

                    if v_libros[pos].idioma == 4:
                        v_libros[pos].importe -= v_libros[pos].importe * 0.22

                    print("Datos actualizados:", v_libros[pos])

                else:
                    print("No contamos con el libro", x, "pero no deje de visitar nuestra sección de ofertas!")

            else:
                print("debe primero cargar el arreglo con la opcion 1.")





if __name__ == '__main__':
    principal()

