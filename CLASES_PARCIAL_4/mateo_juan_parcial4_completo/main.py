import os.path
import pickle
import random

from registro import *


# ===========================================================================
#               Opcion 1
# ===========================================================================
def validar_n():
    n = int(input("Ingresar cantidad de libros a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de libros a cargar: "))
    return n


def cargar_arreglo(v_libros, n):

    for i in range(n):
        # isbn 13 digitos INT, titulo STR, autor STR, idioma(1, 5), categoria(13, 15), importe FLOAT
        isbn = random.randint(1000000000000, 9000000000000)
        titulo = random.choice("ABCDEF")
        autor = random.choice("ABCDEF")
        idioma = random.randint(1, 5)
        categoria = random.randint(13, 15)
        importe = round(random.uniform(0.1, 10), 2)

        nuevo_libro = Libro(isbn, titulo, autor, idioma, categoria, importe)
        add_in_order(v_libros, nuevo_libro)


def add_in_order(v_libros, nuevo_libro):
    izq, der = 0, len(v_libros) - 1

    while izq <= der:
        c = (izq + der) // 2    # c = centro

        # cambia el atributo por el que les pidan ordenar
        if v_libros[c].isbn == nuevo_libro.isbn:
            pos = c
            break

        # la boquita ">" determina si esta de menor a mayor o mayor a menor
        elif v_libros[c].isbn > nuevo_libro.isbn:
            der = c - 1

        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v_libros[pos:pos] = [nuevo_libro]       # el objeto va ENTRE CORCHETES


# ===========================================================================
#               Opcion 2
# ===========================================================================
def mostrar_datos(v_libros):
    # indices       0   1   2
    # v_libros = [ L1, L2, L3 ]
    for i in v_libros:
        # i = L1, L2, L3
        print(i)


# ===========================================================================
#               Opcion 3
# ===========================================================================
def generar_matriz(v_libros, m):

    # crear la matriz
    f = 3    # f = filas = categoria(13, 15) = lim_superior - lim_inferior + 1 = 15 - 13 + 1 = 3
    c = 5    # c = columnas = idioma(1, 5) = lim_superior - lim_inferior + 1 = 5 - 1 + 1 = 5
    matriz = [ [0] * c for i in range(f) ]

    # categoria(13, 15)  13-13  14-13  15-13
    # fila_indices          0   1   2

    # idioma(1, 5)             1-1   2   3   4   5
    # columnas_indices =        0   1   2   3   4

    # matriz[f][c]
    # matriz =  [   [5, 0, 5, 0, 5],    # categoria 13
    #               [0, 5, 0, 0, 0],
    #               [0, 0, 5, 0, 0]     ]

    #
    # rellenar la matriz
    for i in v_libros:
        # i = L1, L2, L3
        # matriz[f][c]
        matriz[i.categoria - 13][i.idioma - 1] += i.importe
        # matriz[i.categoria - 13][i.idioma - 1] += 1

    #
    # mostrar la matriz

    # Mostrar, además, el importe total vendido para una categoria "m" (siendo m un valor que se ingresa por teclado).
    acum = 0

    tupla_idiomas = ("Español", "Inglés", "Portugués", "Francés", "Italiano")

    for f in range(len(matriz)):    # range(3)
        # f = 0, 1, 2

        for c in range(len(matriz[0])): # range(5)
            # c = 0, 1, 2, 3, 4

            # solo mostrar los que superen un importe acumulado mayor a 0
            if matriz[f][c] > 0:
                # print("Categoria:", f+13, "| Idioma:", c+1, "| Importe acumulado:", matriz[f][c])
                print("Categoria:", f+13, "| Idioma:", tupla_idiomas[c], "| Importe acumulado:", matriz[f][c])

            # solo mostrar el idioma "Frances" o "Español"
            if c+1 == 1 or c+1 == 4:
                pass    # exactamenet el mismo print

            if f+13 == m:
                acum += matriz[f][c]

    print("El acumulado de la categoria:", m, "es:", acum)


# ===========================================================================
#               Opcion 6
# ===========================================================================
def busqueda_binaria(v_libros, num_isbn):
    izq, der = 0, len(v_libros) - 1

    while izq <= der:
        c = (izq + der) // 2  # c = centro

        # if v_libros[c].isbn == nuevo_libro.isbn:
        if v_libros[c].isbn == num_isbn:
            pos = c
            # break
            return pos      # pos 0 o +, si existe un objeto que cumple

        # elif v_libros[c].isbn > nuevo_libro.isbn:
        elif v_libros[c].isbn > num_isbn:
            der = c - 1

        else:
            izq = c + 1

    return -1   # no existe un objeto que cumpla


# ===========================================================================
#               Opcion 4
# ===========================================================================
def generar_archivo_binario(v_libros, fd, a, p):
    m = open(fd, "wb")  # primer parametro nombre del archivo ( fd )
                        # segundo parametro modo de apertura ( "wb" )

    # wb = write binary = crea el archivo si no existe, sobre escribe todo su contenido
    # ab = append binary = crea el archivo si no existe, agrega contenido al final del archivo
    # conservando todo su contenido

    for i in v_libros:
        # i = L1, L2, L3

        if i.autor == a and i.importe < p:
            pickle.dump(i, m)   # primer parametro que quiero guardar ( i )
                                # segundo parametro donde lo quiero guardar ( m )
            m.flush()   # opcional --> guarda mejor el archivo

    m.close()   # OBLIGATORIO


# ===========================================================================
#               Opcion 5
# ===========================================================================
def mostrar_archivo_binario(fd):

    bandera = os.path.exists(fd)    # retorna True si el archivo existe, False si NO existe
    if bandera is False:        # if not bandera:
        print("el archivo no existe.")
        return      # corta la funcion

    m = open(fd, "rb")  # read binary --> modo de lectura
    tam = os.path.getsize(fd)   # el tamaño del archivo en bytes    # = 300

    # archivo = [   L1        L2         L3  ]
    # bytes     0       100       200         300
    # m.tell()  0       100       200         300

    # al final, cuántos libros se mostraron
    cont = 0

    # al final, el promedio de los importes de los libros que se mostraron
    # promedio = acumulado (de importes) / cantidad de veces que acumule
    acum = 0
    cont = 0

    while m.tell() < tam:

        librito = pickle.load(m)    # unico parametro el archivo ( m )
        # librito = L1, L2, L3
        print(librito)
        acum += librito.importe
        cont += 1

    print("Se mostraron la cantidad de libros de:", cont)

    # calcular promedio
    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio es:", prom)

    m.close()   # OBLIGATORIO


def menu():
    print("1 - Cargar arreglo.")
    print("2 - Mostrar arreglo.")
    print("3 - Generar matriz.")
    print("4 - Generar archivo binario.")
    print("5 - Mostrar archivo binario.")
    print("6 - Busqueda binaria.")
    op = int(input("Ingresar opción: "))
    return op


def principal():

    # vector / arreglo / lista de trabajo
    v_libros = []

    # nombre del archivo
    fd = "libros.dat"   # file description ; nombre del archivo

    op = -1
    while op != 0:
        op = menu()

        if op == 1:
            n = validar_n()
            # Cada vez que se ingrese en esta opción, el arreglo debe ser creado desde cero
            # y todo contenido anterior debe ser eliminado.
            v_libros = []
            cargar_arreglo(v_libros, n)

        elif op == 2:

            # if v_libros:    # si el vector libros esta cargado
            if len(v_libros) > 0:       # si el tamaño es mas grande que cero
                mostrar_datos(v_libros)

            else:
                print("El arreglo debe ser cargado.")

        elif op == 3:
            """
            3 - determinar cuanto es la sumatora de los importe dentro de arreglo
            por cada combinacion posible de idioma y de categoria
            - Mostrar, además, el importe total vendido para una
            categoria "m" (siendo m un valor que se ingresa por teclado).
            -
            -
            """
            if len(v_libros) > 0:       # si el tamaño es mas grande que cero
                m = int(input("INgresar categoria a totalizar ( 13 , 15 ) : "))
                generar_matriz(v_libros, m)

            else:
                print("El arreglo debe ser cargado.")

        elif op == 4:
            """
            4 - A partir del arreglo genere un archivo binario que contenga los datos 
            de todos los libros del autor a cuyo precio no supere p, siendo a y p dos 
            valores ingresados por teclado.
            """
            if len(v_libros) > 0:       # si el tamaño es mas grande que cero
                a = input("Ingresar autor a guardar: ")
                p = float(input("Ingresar importe a no superar: "))
                generar_archivo_binario(v_libros, fd, a, p)

            else:
                print("El arreglo debe ser cargado.")

        elif op == 5:
            """
            5 - Mostrar el archivo generado en el punto anterior indicando, al final, 
            cuántos libros se mostraron.
            """
            mostrar_archivo_binario(fd)

        elif op == 6:
            """
            6 - Buscar un vehículo por ISBN. Si existe mostrar todos sus datos y si, 
            además, el idioma del mismo es Francés, realizar un descuento del 22% sobre su 
            precio de venta, mostrando los datos del libro antes y después de la
            actualización. Si el libro no existe informar con el mensaje “No contamos con 
            el libro <ISBN> pero no deje de visitar nuestra sección de ofertas!”.
            """
            num_isbn = int(input("Ingresar numero a buscar: "))
            pos = busqueda_binaria(v_libros, num_isbn)

            if pos >= 0:
                print("datos sin actualizar", v_libros[pos])

                if v_libros[pos].idioma == 4:
                    v_libros[pos].importe -= v_libros[pos].importe * 0.22

                print("datos actualizados", v_libros[pos])

            else:   # pos = -1
                print("No contamos con el libro", num_isbn, "pero no deje de visitar nuestra sección de ofertas")


if __name__ == "__main__":
    principal()