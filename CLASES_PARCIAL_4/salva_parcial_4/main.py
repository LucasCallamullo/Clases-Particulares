import os.path
import pickle
import random

from registro import *


# ===========================================================================
#                   Opcion 1
# ===========================================================================
def validar_n():
    n = int(input("Ingresar cantidad de libros a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de libros a cargar: "))
    return n


def cargar_arreglo(v_libros, n):
    # isbn INT 13 digitos, titulo STR, autor(3, 7), idioma(1, 5), importe FLOAT
    for i in range(n):      # 3
        isbn = random.randint(1000000000000, 9000000000000)
        titulo = random.choice("ABCDEF")
        autor = random.randint(3, 7)
        idioma = random.randint(1, 5)
        importe = round(random.uniform(0.1, 10), 2)

        nuevo_libro = Libro(isbn, titulo, autor, idioma, importe)
        add_in_order(v_libros, nuevo_libro)


def add_in_order(v_libros, nuevo_libro):

    # L1.isbn       3
    # L2.isbn       1
    # L6

    # indices       0
    # v_libros = [ L1 L2 L3 L4 L5 ]

    izq, der = 0, len(v_libros) - 1
    # izq = 0
    # der = -1

    while izq <= der:

        c = (izq + der) // 2        # centro = c = 0

        # el atributo por el que te pidan ordenarlo
        if v_libros[c].isbn == nuevo_libro.isbn:
            pos = c
            break
        # esta boquita ">" determina si esta de menor a mayor o mayor a menor
        elif v_libros[c].isbn > nuevo_libro.isbn:
            der = c - 1

        else:
            izq = c + 1

    if izq > der:
        pos = izq

    # indices       0    1
    # v_libros = [  L2,  L1   ]
    # isbn           1     3

    v_libros[pos:pos] = [nuevo_libro]       # el objeto VA ENTRE CORCHETES


# ===========================================================================
#                   Opcion 2
# ===========================================================================
def mostrar_datos(v_libros):
    # indices       0    1
    # v_libros = [  L1,  L2   ]
    for i in v_libros:
        # i = L1, L2
        print(i)


# ===========================================================================
#                   Opcion 3
# ===========================================================================
def busqueda_binaria(v_libros, num_isbn):
    izq, der = 0, len(v_libros) - 1

    while izq <= der:

        c = (izq + der) // 2  # centro = c = 0

        # if v_libros[c].isbn == nuevo_libro.isbn:
        if v_libros[c].isbn == num_isbn:
            pos = c
            # break
            return pos      # 0 + existe

        # elif v_libros[c].isbn > nuevo_libro.isbn:
        elif v_libros[c].isbn > num_isbn:
            der = c - 1

        else:
            izq = c + 1

    return -1       # no existe un objeto que cumpla


# ===========================================================================
#                   Opcion 4
# ===========================================================================
def generar_archivo_binario(v_libros, fd, a, p):

    m = open(fd, "wb")  # primer parametro es el nombre del archivo ( fd )
                    # segundo parametro el modo de apertura ( "wb" )
    # wb = write binary = crea el archivo si no existe, sobre escribe todo su contenido
    # ab = append binary = crea el archivo si no existe, agrega todo el nuevo contenido al final del archivo

    for i in v_libros:
        # i = L1, L2, L3

        # guardar los datos de todos los libros del autor a cuyo precio no supere p
        if i.autor == a and i.importe < p:

            pickle.dump(i, m)   # primer parametro que quiero guardar ( i )
                            # segundo parametro donde lo quiero guardar ( m )
            m.flush()   # opcional --> guarda mejor el archivo

    print("Se genero el archivo.")  # opcional

    m.close()   # OBLIGATORIO


# ===========================================================================
#                   Opcion 5
# ===========================================================================
def mostrar_archivo_binario(fd):

    bandera = os.path.exists(fd)    # retorna True si existe, retorna False si no existe

    if bandera is False:        # if not bandera
        print("El archivo no existe.")
        return      # cortar la funcion

    #
    m = open(fd, "rb")      # read binary --> modo de lectura
    tam = os.path.getsize(fd)   # nos dice el tamaño en bytes del archivo,  218

    #
    # archivo = [   L1         L2  ]
    # bytes     0        109        218
    # m.tell()  0        109

    # al final, indique el promedio de los importes de los libros se mostraron.
    # solo el promedio de los idiomas frances y portugues
    # promedio = acumulador ( de importes ) / cantidad de veces que acumulamos
    acum = 0
    cont = 0

    while m.tell() < tam:

        librito = pickle.load(m)    # unico parametroel archivo ( m )
        # librito = L1, L2
        print(librito)

        if librito.idioma == 3 or librito == 4:
            acum += librito.importe
            cont += 1

    # calcular promedio
    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio es:", prom)

    m.close()


# ===========================================================================
#                   Opcion 6
# ===========================================================================
def generar_matriz(v_libros, u):
    # crear la matriz
    f = 5    # f = filas = autor(3, 7) = lim_superior - lim_inferior + 1 = 7 - 3 + 1 = 5
    c = 5    # c = columnas = idioma(1, 5) # lim_superior - lim_inferior + 1 = 5 - 1 + 1 = 5
    matriz = [ [0] * c for i in range(f) ]

    # autor(3, 7)      3-3   4   5   6   7
    # indices_fila      0   1   2   3   4

    # idioma(1, 5)     1-1   2   3   4   5
    # indices_columnas  0   1   2   3   4

    # matriz[f][c]
    # matriz = [    [0, 0, 0, 0, 0],
    #               [0, 0, 0, 0, 0],
    #               [0, 0, 0, 0, 0],
    #               [0, 0, 0, 0, 0],
    #               [0, 0, 0, 0, 0]     ]

    #
    # rellenar la matriz
    for i in v_libros:
        # i = L1, L2
        # matriz[f][c]
        matriz[i.autor - 3][i.idioma - 1] += i.stock
        # matriz[i.autor - 3][i.idioma - 1] += 1

    #
    # mostrar la matriz
    for f in range(len(matriz)):    # range(5)
        # f = 0, 1, 2, 3, 4

        for c in range(len(matriz[0])): # range(5)
            # c = 0, 1, 2, 3, 4

            if matriz[f][c] > u:
                print("Autor:", f+3, "| Idioma:", c+1, "| Cantidad de Stock:", matriz[f][c])

            # solo mostrar el autor 3
            # if 3 == f+3:


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

    # vector / arreglo de trabajo
    v_libros = []

    # nombre del archivo
    fd = "libros.dat"       # file description ; nombre del archivo

    op = -1
    while op != 0:
        op = menu()

        if op == 1:
            n = validar_n()
            # Cada vez que se ingrese en esta opción, el arreglo debe ser creado desde
            # cero y todo contenido anterior debe ser eliminado.
            v_libros = []
            cargar_arreglo(v_libros, n)

        elif op == 2:

            if len(v_libros) > 0:
                mostrar_datos(v_libros)

            else:
                print("debe cargar el arreglo porque no esta cargado.")

        elif op == 6:
            """
            6 - . Buscar un libro por ISBN. Si existe mostrar todos sus datos y si, además, 
            el idioma del mismo es Francés,
realizar un descuento del 22% sobre su precio de venta, mostrando los datos del libro antes y 
después de la actualización. Si el libro no existe informar con el mensaje “No contamos con 
el libro <ISBN> pero no deje de visitar nuestra sección de ofertas!”.
            """
            if len(v_libros) > 0:
                num_isbn = int(input("Ingresar num isbn a buscar: "))
                pos = busqueda_binaria(v_libros, num_isbn)

                if pos >= 0:
                    print("Datos sin actualizar:", v_libros[pos])

                    if v_libros[pos].idioma == 4:
                        v_libros[pos].importe -= v_libros[pos].importe * 0.22

                    print("Datos actualizados:", v_libros[pos])

                else:
                    print("No contamos con el libro", num_isbn, "pero no deje de visitar nuestra sección de ofertas!")

            else:
                    print("debe cargar el arreglo porque no esta cargado.")


        elif op == 4:
            """
            4 - A partir del arreglo genere un archivo binario que contenga los datos de
             todos los libros del autor a cuyo precio no supere p, siendo a y p dos 
             valores ingresados por teclado.
            """
            if len(v_libros) > 0:
                a = int(input("El autor va de 3 a 7: "))
                p = float(input("Ingresar importe a no superar: "))
                generar_archivo_binario(v_libros, fd, a, p)

            else:
                print("debe cargar el arreglo porque no esta cargado.")

        elif op == 5:
            """
            5. Mostrar el archivo generado en el punto anterior indicando, al final, 
            el promedio de los importes de los libros se mostraron.
            """
            mostrar_archivo_binario(fd)

        elif op == 3:
            """
            3 - determinar la sumatoria de los importes por cada posible autor con cada posible 
            idiooma, Mostrar únicamente las combinaciones que disponen de un stock superior a u unidades,
            """
            if len(v_libros) > 0:
                u = int(input("Ingresar stock a sueprar: "))
                generar_matriz(v_libros, u)

            else:
                print("debe cargar el arreglo porque no esta cargado.")




if __name__ == "__main__":
    principal()




