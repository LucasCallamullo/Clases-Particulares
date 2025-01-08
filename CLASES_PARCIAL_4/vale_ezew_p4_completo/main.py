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
    # isbn INT de 13 digitos, titulo STR, autor STR, idioma(1, 5), importe FLOAT, categoria(11, 13)

    for i in range(n):
        isbn = random.randint(1234567890000, 9234567890000)
        titulo = random.choice("ABCDEF")
        autor = random.choice("ABCDEF")
        idioma = random.randint(1, 5)
        categoria = random.randint(11, 13)
        importe = round(random.uniform(0.1, 10), 2)     # FLOAT

        nuevo_libro = Libro(isbn, titulo, autor, idioma, importe, categoria)
        add_in_order(v_libros, nuevo_libro)


def add_in_order(v_libros, nuevo_libro):

    izq, der = 0, len(v_libros) - 1

    while izq <= der:
        c = (izq + der) // 2

        # el atributo por el que les pidan ordenar es lo que cambian
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

    v_libros[pos:pos] = [nuevo_libro]


# ===========================================================================
#                   Opcion 2
# ===========================================================================
def mostrar_datos(v_libros):
    # v_libros = [ L1,      L2,     L3]

    for i in v_libros:
        # i = L1,   L2,  L3
        print(i)


# ===========================================================================
#                   Opcion 6
# ===========================================================================
def busqueda_binaria(v_libros, num_isbn):      # num_isbn = 7

    # indices       0       1       2
    # v_libros = [ L1,      L2,     L3]
    # isbn          3       5       7

    izq, der = 0, len(v_libros) - 1
    # izq = 2
    # der = 2

    while izq <= der:
        c = (izq + der) // 2        # c = centro = 2

        # if v_libros[c].isbn == nuevo_libro.isbn:
        if v_libros[c].isbn == num_isbn:
            pos = c
            # break
            return pos  # la posicion o indice dentro del arreglo donde tengo un
            # objeto que cumple con mi criterio de busqueda ; pos >= 0

        # elif v_libros[c].isbn > nuevo_libro.isbn:
        elif v_libros[c].isbn > num_isbn:
            der = c - 1

        else:
            izq = c + 1

    return -1       # cuando no existe un objeto que cumppla


# ===========================================================================
#                   Opcion 3
# ===========================================================================
def generar_matriz(v_libros, x):

    # crear la matriz
    f = 3    # f = filas = categoria(11, 13) = lim_superior - lim_inferior + 1 = 13 - 11 + 1 = 3
    c = 5    # c = columnas = idioma(1, 5) = 5 - 1 + 1 = 5
    matriz = [ [0] * c for i in range(f) ]

    # categoria(11, 13)   11-11   12-11    13
    # fila_indices          0       1       2

    # idioma(1, 5)     1-1 2-1 3-1   4   5
    # columna_indices   0   1   2   3   4

    # matriz[f][c] --> se accede al reves a como lo creamos
    # matriz = [    [0, 0, 0, 0, 0],
    #               [0, 0, 0, 0, 0],
    #               [0, 0, 0, 0, 0]   ]

    #
    # rellenar la matriz
    # v_libros = [ L1,      L2,     L3]
    for i in v_libros:
        # i = L1,   L2,  L3
        # matriz[f][c]
        matriz[i.categoria - 11][i.idioma - 1] += i.importe

        # si nos pidieran determinar la CANTIDAD por cada combinacion posible
        # matriz[i.categoria - 11][i.idioma - 1] += 1

    #
    # mostrar la matriz
    for f in range(len(matriz)):    # range(3)
        # f = 0, 1, 2

        for c in range(len(matriz[0])):     # range(5)
            # c = 0, 1, 2, 3, 4

            # solo mostrar los acumuladores que tengan un valor mayor a "x"
            if matriz[f][c] > x:
                print("Idioma:", c+1, "| Categoria:", f+11, "| Importe Acumulado:", matriz[f][c])

            # mostrar las categorias que sean iguales a 13
            # if 13 == f+11:
            #    print("Idioma:", c + 1, "| Categoria:", f + 11, "| Importe Acumulado:", matriz[f][c])


# ===========================================================================
#                   Opcion 4
# ===========================================================================
def generar_archivo_binario(v_libros, fd, a, p):

    m = open(fd, "wb")  # primer parametro nombre del archivo ( fd )
                        # segundo parametro modo de apertura ( "wb" )

    # indices       0       1       2
    # v_libros = [ L1,      L2,     L3]
    for i in v_libros:
        # i = L1,   L2,     L3

        # guardar los datos de todos los libros del autor a cuyo precio no supere p
        if i.autor == a and i.importe < p:
            pickle.dump(i, m)   # primer parametro objeto a guardar ( i )
                                # segundo parametro el archivo ( m )

    print("Se genero el archivo.")  # opcional

    m.close()       # OBLIGATORIO


# ===========================================================================
#                   Opcion 5
# ===========================================================================
def mostrar_archivo_binario(fd):

    bandera = os.path.exists(fd)  # retorna TRUE si existe el archivo, retorna FALSE si no existe
    if bandera is False:        # if not bandera:
        print("No existe el archivo:", fd)
        return      # corta la funcion

    m = open(fd, "rb")  # read binary  -> modo de lectura
    tamanio = os.path.getsize(fd)   # nos dice el tamaño del archivo

    # al final, cuántos libros se mostraron.
    cont = 0

    # al final mostrar el promedio de los importes de los libros cargados en el archivo
    # promedio = acumulado ( de importes ) / la cantidad de veces que acumule
    acum = 0
    cont = 0

    while m.tell() < tamanio:

        librito = pickle.load(m)
        # librito = L1, L2, L3
        print(librito)

        acum += librito.importe
        cont += 1

    # calcular el promedio
    prom = 0
    if cont > 0:
        prom = acum / cont

    print("El promedio de importes es:", prom)

    print("Se mostraron la cantidad:", cont)

    m.close()       # OBLIGATORIO


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
    v_libros = []

    # nombre del archivo binario
    fd = "libros.dat"

    op = -1
    while op != 0:
        op = menu()

        if op == 1:
            n = validar_n()
            cargar_arreglo(v_libros, n)

        elif op == 2:
            if len(v_libros) > 0:
                mostrar_datos(v_libros)
            else:
                print("El arreglo no esta cargado.")

        elif op == 3:
            """
            3 - Determinar y mostrar el importe acumulado para las posibles combinaciones
            de idiomas con categorias
            solo mostrar los acumuladores que tengan un valor mayor a "x"
            """
            if len(v_libros) > 0:
                x = int(input("Ingresar acumulador a sueprar: "))
                generar_matriz(v_libros, x)
            else:
                print("El arreglo no esta cargado.")

        elif op == 4:
            """
            4 - A partir del arreglo genere un archivo binario que contenga 
            los datos de todos los libros del autor a cuyo precio
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
            3 - Buscar un libro por ISBN. Si existe mostrar todos sus datos 
            y si, además, el idioma del mismo es Francés, realizar un descuento 
            del 22% sobre su precio de venta, mostrando los datos del libro antes 
            y después de la actualización. 
            Si el libro no existe informar con el mensaje “No contamos con el 
            libro <ISBN> pero no deje de visitar nuestra sección de ofertas!”.
            """
            num_isbn = int(input("Ingresar ISBN a buscar: "))
            pos = busqueda_binaria(v_libros, num_isbn)

            if pos >= 0:
                print(v_libros[pos])

                # y si, además, el idioma del mismo es Francés,
                if v_libros[pos].idioma == 4:

                    # realizar un descuento del 22% sobre su precio de venta
                    v_libros[pos].importe -= v_libros[pos].importe * 0.22

                    print("Datos actualizados:", v_libros[pos])

                    # ingresar el nuevo importe por teclado
                    v_libros[pos].importe = float(input("Ingresar nuevo importe: "))

            else:       # pos es -1
                print("No contamos con el libro", num_isbn, "pero no deje de visitar "
                      "nuestra sección de ofertas!")


if __name__ == "__main__":
    principal()
