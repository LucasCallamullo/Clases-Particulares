import os.path
import pickle
import random

from registro import *


# ===========================================================================
#                   Opcion 1
# ===========================================================================
def validar_n():
    n = int(input("Ingresar cantidad de libros a cargar: "))    # -1
    while n <= 0:
        n = int(input("Ingresar cantidad de libros a cargar: "))    # 3
    return n


def cargar_arreglo(v_libros, n):
    # isbn 13 digitos INT, autor STR, titulo STR, idioma(1, 5), importe FLOAT, categoria(13, 17)
    for i in range(n):
        isbn = random.randint(1234567890123, 9234567890123)
        autor = random.choice("ABCDEF")
        titulo = random.choice("ABCDEF")
        idioma = random.randint(1, 5)
        importe = round(random.uniform(0.1, 10), 2)     # FLOAT
        categoria = random.randint(13, 16)

        nuevo_libro = Libro(isbn, autor, titulo, idioma, importe, categoria)
        add_in_order(v_libros, nuevo_libro)


def add_in_order(v_libros, nuevo_libro):

    # L1.isbn       3
    # L2.isbn       1

    # indices       0
    # v_libros = [ L1 ]
    # isbn          3

    izq, der = 0, len(v_libros) - 1
    # izq = 0
    # der = -1

    while izq <= der:   # mientras

        c = (izq + der) // 2        # c = centro = 0

        # cambia el atributo por el que les pidan ordenar
        if v_libros[c].isbn == nuevo_libro.isbn:
            pos = c
            break

        # la boquita ">" determinar si esta de menor a mayor o mayor a menor
        elif v_libros[c].isbn > nuevo_libro.isbn:
            der = c - 1

        else:
            izq = c + 1

    if izq > der:
        pos = izq

    # indices       0       1
    # v_libros = [  L2,     L1  ]
    # isbn           1      3
    v_libros[pos:pos] = [nuevo_libro]       # el objeto VA ENTRE CORCHETES


# ===========================================================================
#                   Opcion 2
# ===========================================================================
def mostrar_arreglo(v_libros):
    # indices       0       1       2
    # v_libros = [  L1,     L2,     L3  ]
    for i in v_libros:
        # i = L1 ,      L2  ,   L3

        # que supere el importe > 0
        if i.importe > 0:
            print(i)


# ===========================================================================
#                   Opcion 6
# ===========================================================================
def busqueda_binaria(v_libros, num_isbn):

    izq, der = 0, len(v_libros) - 1

    while izq <= der:  # mientras

        c = (izq + der) // 2  # c = centro = 0

        # if v_libros[c].isbn == nuevo_libro.isbn:
        if v_libros[c].isbn == num_isbn:
            pos = c     # un indice dentro del arreglo donde tengo un objeto que cumple
            # mi criterio de busqueda
            # break
            return pos  # pos >= 0

        # elif v_libros[c].isbn > nuevo_libro.isbn:
        elif v_libros[c].isbn > num_isbn:
            der = c - 1

        else:
            izq = c + 1

    return -1       # NO existe un objeto que cumpla mi criterio de busqueda


# ===========================================================================
#                   Opcion 3
# ===========================================================================
def generar_matriz(v_libros, m):

    # crear la matriz
    f = 5   # f = filas = idioma(1, 5) = lim_superior - lim_inferior + 1 = 5 - 1 + 1 = 5
    c = 4   # c = columnas = categoria(13, 16) = 16 - 13 + 1 = 4
    matriz = [ [0] * c for i in range(f) ]

    # idioma(1, 5)     1-1     2-1     3-1       4       5
    # fila_indices      0       1       2       3       4

    # categoria(13, 16)  13-13    14-13   15-13      16
    # columnas_indices      0       1       2       3

    # matriz[f][c]  # AL REVES COMO LO CREE
    # matriz = [    [0, 0, 0, 0],
    #               [0, 5, 0, 0],
    #               [0, 0, 5, 0],
    #               [5, 0, 0, 0],
    #               [0, 0, 0, 0]    ]

    #
    # rellenar la matriz
    for i in v_libros:
        # i = L1,   L2  ,   L3
        # matriz[f][c]
        matriz[i.idioma - 1][i.categoria - 13] += i.importe

        # determinar la CANTIDAD por combinacion posible categoria con idioma
        # matriz[i.idioma - 1][i.categoria - 13] += 1

    #
    # mostrar la matriz
    tupla_idiomas = ("Español", "Inglés", "Portugués", "Francés", "Italiano")

    # Mostrar, además, el importe total vendida para una categoria "m"
    acum = 0

    for f in range(len(matriz)):    # range(5)
        # f = 0, 1, 2, 3, 4

        for c in range(len(matriz[0])):     # range(4)
            # c = 0, 1, 2, 3

            # Solo mostrar los acumuladores que fueran mayores a 0
            if matriz[f][c] > 0:
                print("Categoría:", c+13, "| Idiomas:", f+1, "| Importe Acumulado:", matriz[f][c])
                # print("Categoría:", c+13, "| Idiomas:", tupla_idiomas[f], "| Importe Acumulado:", matriz[f][c])

            # Solo mostrar el idioma Ingles Portugues Frances ( 2, 3, 4 )
            # if 2 <= f+1 <= 4:
            #    print("Categoría:", c + 13, "| Idiomas:", f + 1, "| Importe Acumulado:", matriz[f][c])

            # Mostrar, además, el importe total vendida para una categoria "m"
            if m == c+13:
                acum += matriz[f][c]

    print("El acumulado es:", acum, "para la categoria", m)


# ===========================================================================
#                   Opcion 4
# ===========================================================================
def generar_archivo_binario(v_libros, fd, a, p):

    m = open(fd, "wb")  # primer parametro nombre del archivo ( fd )
                        # segundo parametro el modo de apertura ( "wb" )
    # wb = write binary = crea el archivo si no existe, sobre escribe todo el contenido del archivo
    # ab = append binary = crea el archivo si no existe, agrega contenido al final del archivo
    # conservando todo su contenido anterior.

    for i in v_libros:
        # i = L1, L2,   L3

        # gaurdar los libros del autor "a" cuyo precio no supere p
        if i.autor == a and i.importe < p:

            pickle.dump(i, m)   # primer parametro que quiero guardar ( i )
                            # segundo parametro donde lo quiero guardar ( m )

            m.flush()   # opcional --> guarda mejor el archivo

    print("Se genero el archivo.")  # Opcional
    m.close()   # OBLIGATORIO


# ===========================================================================
#                   Opcion 5
# ===========================================================================
def mostrar_archivo_binario(fd):

    bandera = os.path.exists(fd)    # retorna TRUE si existe, retorna FALSE si no existe
    if bandera is False:    # if not bandera   if bandera == 0
        print("No existe el archivo:", fd)
        return      # corta la funcion que tal

    m = open(fd, "rb")  # read binary = modo de lectura
    tamanio = os.path.getsize(fd)       # nos dice el tamaño en bytes dentro del archivo = 300 bytes

    # archivo = [   L1      L2      L3  ]
    # bytes     0       100     200     300
    # m.tell()  0       100     200

    # al final, cuántos libros se mostraron.
    cont = 0

    # al final mostrar el promedio de los importes mostrados
    # promedio = acumulado ( de importes ) / la cantidad de veces que acumule
    acum = 0
    cont = 0

    while m.tell() < tamanio:

        librito = pickle.load(m)    # cada vuelta de ciclo recupera un objeto diferente
        # librito = L1,      L2,     L3
        print(librito)

        acum += librito.importe
        cont += 1

    # calcular promedio
    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio de los importes:", prom)

    m.close()       # OBLIGATORIO


def menu():
    print("1 - Cargar arreglo.")
    print("2 - Mostrar arreglo.")
    print("3 - Generar matriz.")
    print("4 - Generar archivo binario.")
    print("5 - Mostrar archivo binario.")
    print("6 - busqueda binario.")
    print("0 - Salir.")
    op = int(input("Ingresar opción: "))
    return op


def principal():

    # vector / arreglo / lista  de trabajo
    v_libros = []       # list()

    # nombre del archivo
    fd = "libros.dat"

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
            if len(v_libros) > 0:
                mostrar_arreglo(v_libros)

            else:
                print("El arreglo no esta cargado.")

        elif op == 3:
            """
            3 - Determinar y mostrar el acumulado de precios de venta por cada posible combinacion
            entre idioma y categoria.
            -  Mostrar, además, el importe total vendida para una categoria "m" (siendo m un valor que se ingresa por teclado).
            """
            if len(v_libros) > 0:
                m = int(input("Ingresar categoria a totalizar: "))
                generar_matriz(v_libros, m)

            else:
                print("El arreglo no esta cargado.")

        elif op == 4:
            """
            4 -  A partir del arreglo genere un archivo binario que contenga los datos 
            de todos los libros del autor "a" cuyo precio
            no supere p, siendo a y p dos valores ingresados por teclado.
            """
            if len(v_libros) > 0:
                a = input("Ingresar autor a guardar: ")
                p = float(input("Ingresar importe a no superar: "))
                generar_archivo_binario(v_libros, fd, a, p)

            else:
                print("El arreglo no esta cargado.")

        elif op == 5:
            """
            5 - Mostrar el archivo generado en el punto anterior indicando, 
            al final, cuántos libros se mostraron.
            """
            mostrar_archivo_binario(fd)

        elif op == 6:
            """
            6 - Buscar un libro por ISBN. Si existe mostrar todos sus datos y si, 
            además, el idioma del mismo es Francés, realizar un descuento del 22% 
            sobre su precio de venta, mostrando los datos del libro antes y después de la
            actualización. Si el libro no existe informar con el mensaje “No contamos con el libro
            <ISBN> pero no deje de visitar nuestra sección de ofertas!”
            """
            if len(v_libros) > 0:
                num_isbn = int(input("Ingresar ISBN a buscar: "))
                pos = busqueda_binaria(v_libros, num_isbn)

                if pos >= 0:
                    print(v_libros[pos])

                    # y si, además, el idioma del mismo es Francés
                    if v_libros[pos].idioma == 4:
                        # realizar un descuento del 22% sobre su precio de venta
                        v_libros[pos].importe -= v_libros[pos].importe * 0.22

                        print("Datos actualizados:", v_libros[pos])

                else:  # pos = -1
                    print("No contamos con el libro", num_isbn, "pero no deje de visitar nuestra "
                                                                "sección de ofertas!")

            else:
                print("El arreglo no esta cargado.")


        elif op == 0:
            print("Te odio valerio.")




if __name__ == "__main__":
    principal()

