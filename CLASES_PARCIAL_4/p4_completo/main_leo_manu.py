import os.path
import pickle
import random


from registro import *


# ===========================================================================
#                   Opcion 1
# ===========================================================================
def validar_n():
    n = int(input("Ingresar cantidad de libros a cargar:"))
    while n <= 0:
        n = int(input("Ingresar cantidad de libros a cargar:"))
    return n


def cargar_arreglo(v_libros, n):

    # ibsn 13 digitos INT, titulo STR, autor (13, 17), idioma(1, 5), importe FLOAT
    for i in range(n):
        isbn = random.randint(1000000000000, 9000000000000) # INT
        titulo = random.choice("ABCDEF")
        autor = random.randint(13, 17)
        idioma = random.randint(1, 5)                   # INT
        importe = round(random.uniform(0.1, 10), 2)     # FLOAT

        nuevo_libro = Libro(isbn, titulo, autor, idioma, importe)
        add_in_order(v_libros, nuevo_libro)


def add_in_order(v_libros, nuevo_libro):
    # L1.isbn       5
    # L2.isbn       3

    # indices       0
    # v_libros = [ L1 ]

    izq, der = 0, len(v_libros) - 1

    # izq = 0
    # der = -1

    while izq <= der:

        c = (izq + der) // 2        # c = centro = 0

        # el atributo que les piden ordenar es lo que cambia
        if v_libros[c].isbn == nuevo_libro.isbn:
            pos = c
            break

        # la orientacion de la boquita ">" determina si esta de menor a mayor o mayor a menor
        elif v_libros[c].isbn > nuevo_libro.isbn:
            der = c - 1

        else:
            izq = c + 1

    if izq > der:
        pos = izq

    # indices       0       1
    # v_libros = [  L2,     L1  ]
    # isbn           3       5
    v_libros[pos:pos] = [nuevo_libro]       # el objeto va ENTRE CORCHETES


# ===========================================================================
#                   Opcion 2
# ===========================================================================
def mostrar_datos(v_libros):
    # indices       0       1
    # v_libros = [  L1,     L2,     L3  ]
    for i in v_libros:
        # i = L1,       L2      ,   L3
        print(i)


# ===========================================================================
#                   Opcion 6
# ===========================================================================
def busqueda_binaria(v_libros, num_isbn):
    izq, der = 0, len(v_libros) - 1

    while izq <= der:

        c = (izq + der) // 2  # c = centro = 0

        # if v_libros[c].isbn == nuevo_libro.isbn:
        if v_libros[c].isbn == num_isbn:
            pos = c
            # break
            return pos      # indice = 0, 1, 2, 3, SI EXISTE UN OBJETO QUE CUMPLE EL CRITERIO DE BUSQUEDA

        # elif v_libros[c].isbn > nuevo_libro.isbn:
        elif v_libros[c].isbn > num_isbn:
            der = c - 1

        else:
            izq = c + 1

    return -1   # NO EXISTE UN OBJETO QUE CUMPLA


# ===========================================================================
#                   Opcion 4
# ===========================================================================
def generar_archivo_binario(v_libros, fd, a, p):

    m = open(fd, "wb")  # primer parametro: nombre del archivo ( fd )
                        # segundo parametro modo de apertura ( "wb" )
    # wb = write binary = CREA EL ARCHIVO SI NO EXISTE, sobre escribe todo el contenido
    # ab = append binary = CREA EL ARCHIVO SI NO EXISTE, agrega contenido al final del archivo
    # todo el contenido anterior se conserva

    # indices       0       1       2
    # v_libros = [  L1,     L2,     L3  ]
    for i in v_libros:
        # i = L1,   L2,     L3

        # guardar todos los libros del autor a cuyo precio no supere p
        if i.autor == a and i.importe < p:
            pickle.dump(i, m)   # primer parametro es que quiero guardar ( i )
                            # segundo parametro donde lo quiero guardar ( m )

    print("Se genero el archivo binario.")  # opcional

    m.close()   # OBLIGATORIO


# ===========================================================================
#                   Opcion 5
# ===========================================================================
def mostrar_archivo_binario(fd):

    bandera = os.path.exists(fd)    # retorna TRUE si el archivo existe, RETORNA FALSE si NO Existe
    if bandera is False:        # if not bandera
        print("No existe el archivo:", fd)
        return      # corta la funcion

    m = open(fd, "rb")  # read binary = modo de lectura
    tamanio = os.path.getsize(fd)   # nos devuelve el tamaño en bytes del archivo = 300

    # archivo = [   L1        L2          L3    ]
    # bytes     0       100         200         300
    # m.tell()  0       100         200

    # indicando, al final, cuánto es el promedio de precios de los libros se mostraron.
    # promedio = acumulado ( de importes ) / cantidad de veces que acumule
    acum = 0
    cont = 0

    while m.tell() < tamanio:

        librito = pickle.load(m)    # unico parametro el archivo ( m )
        # librito = L1,     L2

        print(librito)

        acum += librito.importe
        cont += 1

    # calcular promedio
    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio es:", prom)

    m.close()       # OBLIGATORIO


# ===========================================================================
#                   Opcion 3
# ===========================================================================
def generar_matriz(v_libros, x):

    # crear la matriz
    f = 5    # f = filas = idioma(1, 5) = lim_superior - lim_inferior + 1 = 5
    c = 5    # c = columnas = autor(13, 17) = lim_superior - lim_inferior + 1 = 17 - 13 + 1 = 5
    matriz = [ [0] * c for i in range(f) ]

    # idioma(1, 5)     1-1 2-1 3-1   4   5
    # fila_indices      0   1   2   3   4

    # autor(13, 17)  13-13 14-13
    # columna_indices   0   1   2   3   4

    # matriz[f][c]
    # matriz = [    [5, 0, 0, 0, 0],
    #               [0, 0, 0, 0, 0],
    #               [1, 5, 0, 0, 0],
    #               [0, 0, 0, 0, 0],
    #               [2, 0, 0, 0, 0]     ]

    #
    # rellenar la matriz
    for i in v_libros:
        # i = L1,   L2,     L3
        # matriz[f][c]
        matriz[i.idioma - 1][i.autor - 13] += i.importe
        # matriz[i.idioma - 1][i.autor - 13] += 1

    #
    # mostrar la matriz

    # acumular los importes del autor x
    acum = 0

    for f in range(len(matriz)):    # range(5)
        # f = 0, 1, 2, 3, 4

        for c in range(len(matriz[0])):     # range(5)
            # c = 0, 1, 2, 3, 4

            # Solo mostrar los que tengan un importe acumulado mayores a 0
            if matriz[f][c] > 0:
                print("Idioma:", f+1, "| Autor:", c+13, "| Importe acumulado:", matriz[f][c])

            if c+13 == x:
                acum += matriz[f][c]

    # al final fuera de los dos ciclos
    print("Para el autor:", x, "tengo el acumulado de:", acum)




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

    # arreglo / vector de trabajo
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
            """ Determinar cual es la sumatoria d elos importes por cada posible combinacion entre
            autores e idioma, 
            - mostrar el acumulado de los importes de un autor "x" que se carga por teclado 
            
            """
            x = int(input("Ingresar autor a totalizar: "))

            generar_matriz(v_libros, x)


        elif op == 4:
            """
            4 - A partir del arreglo genere un archivo binario que contenga los datos 
            de todos los libros del autor a cuyo precio no supere p, siendo a y p dos
             valores ingresados por teclado
            """
            if len(v_libros) > 0:
                a = int(input("Autor a guardar (13, 17):"))
                p = float(input("Ingresar precio a no superar para guardar: "))
                generar_archivo_binario(v_libros, fd, a, p)
            else:
                print("El arreglo no esta cargado.")

        elif op == 5:
            """
            5 - Mostrar el archivo generado en el punto anterior indicando, al final, 
            cuánto es el promedio de precios de los libros se mostraron.
            """
            mostrar_archivo_binario(fd)


        elif op == 6:
            """
            6 - Buscar un libro por ISBN. Si existe mostrar todos sus datos y si, además, 
            el idioma del mismo es Francés, realizar un descuento del 22% sobre su precio de venta,
            mostrando los datos del libro antes y después de la actualización. Si el libro no 
            existe informar con el mensaje “No contamos con el libro <ISBN> pero no deje de
            visitar nuestra sección de ofertas!” 
            """
            num_isbn = int(input("Ingresar ISBN a buscar: "))
            pos = busqueda_binaria(v_libros, num_isbn)

            if pos >= 0:
                print(v_libros[pos])

                #  el idioma del mismo es Francés
                if v_libros[pos].idioma == 4:
                    # realizar un descuento del 22% sobre su precio de venta
                    v_libros[pos].importe -= v_libros[pos].importe * 0.22
                    # v_libros[pos].importe = round(v_libros[pos].importe, 2)
                    print("Datos actualizados: ", v_libros[pos])

                    # debe ingresar un nuevo importe por telcado
                    # v_libros[pos].importe = int(input("Ingresar nuevo importe: "))

            else:   # esto es cuando pos = -1
                print("No contamos con el libro", num_isbn, "pero no deje de visitar nuestra "
                      "sección de ofertas!")

        elif op == 4:
            pass

        elif op == 5:
            pass


if __name__ == "__main__":
    principal()
