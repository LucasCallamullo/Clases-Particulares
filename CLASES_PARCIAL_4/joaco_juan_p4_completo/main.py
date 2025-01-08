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
    # isbn 13 digitos INT, titulo STR, autor STR, idioma(1, 5), importe FLOAT, categoria(13, 15)

    for i in range(n):
        isbn = random.randint(1000000000, 9000000000)       # INT
        titulo = random.choice("ABCDEF")        # STR
        autor = random.choice("ABCDEF")        # STR
        idioma = random.randint(1, 5)   # INT
        importe = round(random.uniform(0.1, 10), 2)     # FLOAT
        categoria = random.randint(13, 15)

        nuevo_libro = Libro(isbn, titulo, autor, idioma, importe, categoria)
        add_in_order(v_libros, nuevo_libro)

    print("Se cargaron la cantidad de", n, "libros.")


def add_in_order(v_libros, nuevo_libro):
    # L1.isbn   3
    # L2.isbn   1

    # indices           0
    # v_libros =    [  L1 ]
    # isbn              3

    izq, der = 0, len(v_libros) - 1
    # izq = 0
    # der = -1

    while izq <= der:

        c = (izq + der) // 2        # c = centro = 0

        # el atributo por el que nos piden ordenar
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

    # indices           0       1
    # v_libros =    [   L2,     L1  ]
    # isbn               1       3
    v_libros[pos:pos] = [nuevo_libro]   # el objeto VA ENTRE CORCHETES


# ===========================================================================
#               Opcion 2
# ===========================================================================
def mostrar_datos(v_libros):
    # indices           0       1
    # v_libros =    [   L1,     L2  ]

    for i in v_libros:
        # i = L1,   L2,     L3
        print(i)


# ===========================================================================
#               Opcion 6
# ===========================================================================
def busqueda_binaria(v_libros, num_isbn):   # num_isbn = 7
    # indices           0       1
    # v_libros =    [   L1,     L2  ]
    # isbn              3       5
    izq, der = 0, len(v_libros) - 1

    while izq <= der:

        c = (izq + der) // 2  # c = centro = 0

        # if v_libros[c].isbn == nuevo_libro.isbn:
        if v_libros[c].isbn == num_isbn:
            pos = c     # la posicion/indice donde tengo mi objeto que cumple
            # break     # con mi cretierio de busqueda
            return pos      # pos >= 0 es un indice

        # elif v_libros[c].isbn > nuevo_libro.isbn:
        elif v_libros[c].isbn > num_isbn:
            der = c - 1

        else:
            izq = c + 1

    return -1       # cuando no existe un resultado valido


# ===========================================================================
#               Opcion 3
# ===========================================================================
def generar_matriz(v_libros, x):

    # crear la matriz
    f = 3   # f = filas = categoria(13, 15) = lim_superior - lim_inferior + 1 = 15 - 13 + 1 = 3
    c = 5   # c = columnas = idioma(1, 5) = 5 - 1 + 1 = 5
    matriz = [ [0] * c for i in range(f) ]

    # categoria(13, 15)    13-13   14-13      15
    # fila_indices          0       1       2

    # idioma(1, 5)       1-1  2-1  3-1   4   5
    # columna_indices     0    1   2    3   4

    # matriz[f][c]  --> se accede al reves a como la cree
    # matriz = [    [0, 0, 0, 0, 0],
    #               [0, 0, 0, 0, 0],
    #               [0, 0, 0, 0, 0]     ]

    #
    # rellenar la matriz
    for i in v_libros:
        # i = L1,   L2,     L3
        # matriz[f][c]
        matriz[i.categoria - 13][i.idioma - 1] += i.importe

        # si no hubieras pedido determinar la CANTIDAD
        # matriz[i.categoria - 13][i.idioma - 1] += 1

    #
    # mostrar la matriz

    tupla_idiomas = ("Español", "Inglés", "Portugués", "Francés", "Italiano")

    for f in range(len(matriz)):        # range(3)
        # f = 0,    1,  2

        for c in range(len(matriz[0])):     # range(5)
            # c = 0, 1, 2, 3, 4

            # mostrar solo los acumuladores que superen a un valor "x"
            if matriz[f][c] > x:
                print("Categoría:", f+13, "| Idioma:", c+1, "| Importe Acumulado:", matriz[f][c])
                # print("Categoría:", f+13, "| Idioma:", tupla_idiomas[c], "| Importe Acumulado:", matriz[f][c])

            # solo mostrar la categoria "t" que se carga por teclado
            # if t == f+13:
            #    print("Categoría:", f + 13, "| Idioma:", c + 1, "| Importe Acumulado:", matriz[f][c])


# ===========================================================================
#               Opcion 4
# ===========================================================================
def generar_archivo_binario(v_libros, fd, a, p):

    m = open(fd, "wb")  # primer paramtro es el nombre del archivo ( fd )
                        # segundo parametro el modo de apertura ( "wb" )
    # wb = write binary = crea el archivo si no existe, sobre escribe todo el contenido
    # ab = append binary = crea el archivo si no existe, agrega contenido al final del archivo
    # conserva todo su contenido anterior

    for i in v_libros:
        # i = L1,   L2,     L3

        # contenga los datos de todos los libros del autor a cuyo precio no supere p
        if i.autor == a and i.importe < p:
            pickle.dump(i, m)   # primer parametro es que quiero guardar ( i )
                            # segundo parametro es donde lo quiero guardar ( m )
            m.flush()   # opcional --> guarda mejor el contenido del archivo

    print("Se genero el archivo binario.")  # opcional

    m.close()   # OBLIGATORIO


# ===========================================================================
#               Opcion 5
# ===========================================================================
def mostrar_archivo_binario(fd):
    # al final, indicar el promedio de venta de los libros con
    # idiomas Frances, portuges y italiano.

    bandera = os.path.exists(fd)    # retorna TRUE si existe el archivo, retorna FALSE si NO EXISTE
    if bandera is False:    # if not bandera:
        print("No existe el archivo:", fd)
        return      # corta la funcion

    m = open(fd, "rb")  # read binary --> modo de lectura
    tam = os.path.getsize(fd)   # nos dice el tamaño en bytes del archivo   = 300 bytes

    # archivo = [   L1      L2      L3  ]
    # bytes     0       100     200     300
    # m.tell()  0       100     200

    # al final, indicar el promedio de venta de los libros con idiomas Frances, portuges
    # e italiano
    # promedio = acumlado ( de importes ) / la cantidad de veces que acumule
    acum = 0
    cont = 0

    while m.tell() < tam:

        librito = pickle.load(m)    # unico parametro el archivo ( m )
        # librito = L1,         L2,         L3
        print(librito)

        if 3 <= librito.idioma <= 5:
            acum += librito.importe
            cont += 1

    # calcular promedio
    prom = 0
    if cont > 0:
        prom = acum / cont

    print("El promedio de los importes es:", prom)

    m.close()       # OBLIGATORIO


# ===========================================================================
#               PRINCIPAL
# ===========================================================================
def menu():
    print()
    print("1 - Cargar arreglo.")
    print("2 - Mostrar arreglo.")
    print("3 - Generar matriz.")
    print("4 - Generar archivo binario.")
    print("5 - Mostrar archivo binario.")
    op = int(input("Ingresar opción: "))
    return op


def principal():

    # vector / arreglo / lista de trabajo
    v_libros = []

    # nombre del archivo binario
    fd = "libros.dat"       # file description ; nombre del archivo

    op = -1
    while op != 0:
        op = menu()

        if op == 1:
            n = validar_n()
            # Cada vez que se ingrese en esta opción, el arreglo debe ser creado
            # desde cero y todo contenido anterior debe ser eliminado.
            v_libros = []
            cargar_arreglo(v_libros, n)

        elif op == 2:
            if len(v_libros) > 0:
                mostrar_datos(v_libros)
            else:
                print("El arreglo no esta cargado.")

        elif op == 3:
            """
            3 - Determinar la sumatoria de los importes por cada posible 
            idioma combinado con cada posible categoria
            # mostrar solo los acumuladores que superen a un valor "x"
            """
            if len(v_libros) > 0:
                x = int(input("Ingresar importe acumulado a superar: "))
                generar_matriz(v_libros, x)
            else:
                print("El arreglo no esta cargado.")

        elif op == 4:
            """
            4 - A partir del arreglo genere un archivo binario que 
            contenga los datos de todos los libros del autor a cuyo precio
            no supere p, 
            siendo a y p dos valores ingresados por teclado
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
            al final, indicar el promedio de venta de los libros con idiomas Frances, portuges
            y italiano.
            """
            mostrar_archivo_binario(fd)

        elif op == 6:
            """
            3 - Buscar un libro por ISBN. Si existe mostrar todos sus datos y si, 
            además, el idioma del mismo es Francés, realizar un descuento del 22% 
            sobre su precio de venta, mostrando los datos del libro antes y después 
            de la actualización. Si el libro no existe informar con el mensaje 
            “No contamos con el libro <ISBN> pero no deje de
            visitar nuestra sección de ofertas!”.
            """
            if len(v_libros) > 0:
                num_isbn = int(input("Ingresar ISBN a buscar: "))
                pos = busqueda_binaria(v_libros, num_isbn)

                if pos >= 0:
                    print(v_libros[pos])

                    # el idioma del mismo es Francés
                    if v_libros[pos].idioma == 4:
                        # realizar un descuento del 22% sobre su precio de venta
                        v_libros[pos].importe -= v_libros[pos].importe * 0.22

                        print("Datos actualizados:", v_libros[pos])

                        # ingresar el nuevo importe por teclado
                        v_libros[pos].importe = float(input("Ingresar nuevo importe: "))

                else:  # pos es -1
                    print("No contamos con el libro", num_isbn, "pero no deje de "
                                                                "visitar nuestra sección de ofertas!")
            else:
                print("El arreglo no esta cargado.")


if __name__ == "__main__":
    principal()
