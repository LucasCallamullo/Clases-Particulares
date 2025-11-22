import os.path
import pickle
import random

from libros_registros import *


# ===========================================================================
#               Opcion 1
# ===========================================================================
def validar_n():
    n = int(input("Ingresar cantidad de libros a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de libros a cargar: "))
    return n


def cargar_arreglo(v_libros, n):
    # isbn 13 digitos INT, autor STR, titulo STR, idioma(1, 5), importe FLOAT, categoria(13,15)
    tupla_autores = ("autor1 apellidorandom.", "autor2 apellidorandom2.")

    for i in range(n):
        isbn = random.randint(1000000000000, 9000000000000)     # INT
        autor = random.choice(tupla_autores)         # STR
        titulo = random.choice("ABCDEF")         # STR
        idioma = random.randint(1, 5)
        categoria = random.randint(13, 15)
        importe = round(random.uniform(0.1, 10), 2)     # FLOAT

        nuevo_libro = Libro(isbn, autor, titulo, idioma, importe, categoria)
        add_in_order(v_libros, nuevo_libro)


def add_in_order(v_libros, nuevo_libro):

    # L3.isbn       4
    #

    # indices       0       1
    # v_libros [    L1,     L2 ]
    # isbn          3       5

    izq, der = 0, len(v_libros) - 1
    # izq = 1
    # der = 0

    while izq <= der:
        c = (izq + der) // 2        # c = 1

        # el atributo por el que les pidan ordenar
        if v_libros[c].isbn == nuevo_libro.isbn:
            pos = c
            break

        # la orientacion de la boquita ">" define si esta de menor a mayor o mayor a menor
        elif v_libros[c].isbn > nuevo_libro.isbn:
            der = c - 1

        else:
            izq = c + 1

    if izq > der:
        pos = izq

    # indices       0       1       2
    # v_libros [    L1,     L3,     L2 ]
    # isbn          3       4       5
    v_libros[pos:pos] = [nuevo_libro]       # este objeto VA ENTRE CORCHETES


# ===========================================================================
#               Opcion 2
# ===========================================================================
def mostrar_datos(v_libros):
    # indices       0       1       2
    # v_libros [    L1,     L2,     L3 ]

    for i in v_libros:
        # i = L1,    L2,     L3
        print(i)


# ===========================================================================
#               Opcion 3
# ===========================================================================
def generar_matriz(v_libros, x):

    # crear la matriz
    f = 5    # f = filas = idioma(1, 5) = lim_superior - lim_inferior + 1 = 5 - 1 + 1 = 5
    c = 3    # c = columnas = categoria(13, 15) = lim_superior - lim_inferior + 1 = 15 - 13 + 1 = 3
    matriz = [ [0] * c for i in range(f) ]      # IMPORTA QUE PUSE PRIMERO SI C O F

    # idioma(1, 5)     1-1 2-1 3   4   5
    # filas_indices     0   1   2   3   4

    # categoria(13, 15)   13-13    14-13    15-13
    # columnas_indices      0       1       2

    # matriz[f][c]      # AL REVES A COMO LA CREE A LA MATRIZ
    # matriz =      [   [5, 0, 0],
    #                   [0, 0, 0],
    #                   [0, 5, 0],
    #                   [0, 0, 0],
    #                   [0, 0, 0]       ]

    #
    # rellenar la matriz
    for i in v_libros:
        # i = L1,   L2,     L3
        # matriz[f][c]
        matriz[i.idioma - 1][i.categoria - 13] += i.importe

        # determinar y mostrar la CANTIDAD de libros posible por la combinacino de...
        # matriz[i.idioma - 1][i.categoria - 13] += 1

    #
    # mostrar la matriz
    tupla_idiomas = ("Español", "Inglés", "Portugués", "Francés", "Italiano")

    for f in range(len(matriz)):        # range(5)
        # f = 0, 1, 2, 3, 4

        for c in range(len(matriz[0])):     # range(3)
            # c = 0, 1, 2

            # solo mostrar los acumuladores que superen un valor "x"
            if matriz[f][c] > x:
                print("Idioma:", f+1, "| Categoría:", c+13, "| Importe Acumulado:", matriz[f][c])
                # print("Idioma:", tupla_idiomas[f], "| Categoría:", c+13, "| Importe Acumulado:", matriz[f][c])

            # solo mostrar la categoria "T" que es e carga por teclado
            # if T == c+13:
            #    print("Idioma:", f + 1, "| Categoría:", c + 13, "| Importe Acumulado:", matriz[f][c])

            #
            # solo mostrar los acumuladores de cinturas entre c1 y c2
            # if c1 < c+30 < c2:
            #    print("Largo:", f + 1, "| Cintura:", c + 13, "| Stock Acumulado:", matriz[f][c])

# ===========================================================================
#               Opcion 4
# ===========================================================================
def generar_archivo_binario(v_libros, fd, a, p):

    m = open(fd, "wb")  # primer parametro = el nombre del archivo ( fd )
                        # segundo parametro es el modo de apertura ( "wb" )
    # wb = write binary = CREA EL ARCHIVO SI NO EXISTE, sobre escribe todo el contenido del archivo
    # ab = append binary = CREA EL ARCHIVO SI NO EXISTE, agrega contenido al final del archivo
    # conservando todo su contenido anterior

    for i in v_libros:
        # i = L1,   L2,     L3

        # guarde los datos de todos los libros del autor "a" cuyo precio no supere "p"
        if i.autor == a and i.importe < p:
            pickle.dump(i, m)   # primer parametro que quiero guardar ( i )
                                # segundo parametro donde lo quiero guardar ( m )

    print("Se genero el archivo.")  # opcional

    m.close()   # OBLIGATORIO


# ===========================================================================
#               Opcion 5
# ===========================================================================
def mostrar_archivo_binario(fd):

    bandera = os.path.exists(fd)    # retora TRUE si existe el archivo, retorna FALSE si NO existe
    if bandera is False:        # if not bandera:
        print("El archivo no existe.")
        return          # corta la funcion

    m = open(fd, "rb")  # read binary --> modo de lectura
    tamanio = os.path.getsize(fd)   # nos dice el tamaño en bytes del archivo   = 300 bytes

    # archivo = [   L1      L2      L3  ]
    # bytes     0       100     200     300
    # m.tell()  0       100     200

    # al final Mostrar el promedio de los importes de los libros que se mostraron
    # promedio = acumulado ( de importes ) / la cantidad de veces que acumule
    acum = 0
    cont = 0

    while m.tell() < tamanio:
        librito = pickle.load(m)    # unico parametro el archivo ( m )
        # librito = L1      L2      L3
        print(librito)

        acum += librito.importe
        cont += 1

    # calcular el promedio
    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio de los importes es:", prom)

    m.close()       # OBLIGATORIO


# ===========================================================================
#               Opcion 6
# ===========================================================================
def busqueda_binaria(v_libros, num_isbn):
    """
    6 - Buscar un libro por ISBN. Si existe mostrar todos sus datos y si, además, el idioma
    del mismo es Francés, realizar un descuento del 22% sobre su precio de venta, mostrando los
    datos del libro antes y después de la actualización. Si el libro no existe informar con el
    mensaje “No contamos con el libro <ISBN> pero no deje de visitar nuestra sección de ofertas!”.
    """
    izq, der = 0, len(v_libros) - 1

    while izq <= der:
        c = (izq + der) // 2

        # if v_libros[c].isbn == nuevo_libro.isbn:
        # si existe tu objeto que cumpla con la condiucion de busqueda
        if v_libros[c].isbn == num_isbn:
            # pos = c
            # break

            # v_libros[c] ---> apunta a un objeto dentro del arreglo
            # si existe mostrar todos sus datos
            print(v_libros[c])

            # y si, además, el idioma del mismo es Francés, realizar un descuento del 22% sobre su
            # precio de venta, mostrando los datos del libro antes y después de la actualización.
            if v_libros[c].idioma == 4:
                print("Sin cambios:", v_libros[c])

                # realizar descuento del 22%
                v_libros[c].importe -= v_libros[c].importe * 0.22

                print("Con cambios:", v_libros[c])

            return  # cortar la funcion, o detenerse al primer resultado

        # elif v_libros[c].isbn > nuevo_libro.isbn:
        elif v_libros[c].isbn > num_isbn:
            der = c - 1

        else:
            izq = c + 1

    # fuera del while es porque no existe el objeto
    print("No contamos con el libro", num_isbn, "pero no deje de visitar nuestra sección de ofertas!")


# ===========================================================================
#               Opcion 7
# ===========================================================================
def busqueda_secuencial(v_libros, a):
    """
    7 - Determinar si existe un libro cuyo autor sea "a" y si existe mostrar solo su precio de venta
    y su numero de isbn, si no existe informar, debe deternse al primer resultado

    for i in v_libros:
        if i.autor == a:
            print("Precio:", i.importe, "- ISBN:", i.isbn)
            return
    print("No existe")
    """

    for i in range(len(v_libros)):
        # i = 0, 1, 2, 3

        # v_libros[i]  --> aputna a mi objeto
        if v_libros[i].autor == a:

            # si existe mostrar solo su precio de venta y su numero de isbn
            print("Precio:", v_libros[i].importe, "- ISBN:", v_libros[i].isbn)

            return v_libros[i].autor      # corta la funcion y se detiene al primer resultado

    # fuera del for es que no existe que cumpla con ese autor
    mensaje = "No existe."
    print(mensaje)
    return mensaje


# ===========================================================================
#               Opcion 8
# ===========================================================================
def analisis_cadena(cadena_autor):
    """
    ¿Cuál es la cantidad de palabras de esa cadena que contienen una letra "r" en la segunda o
    en la tercera posición (en mayúsculas o minúsculas) y que además no contienen ningún dígito?
    """
    cant_palabras = 0

    cont_caracteres = 0
    cont_r_pos2_pos3 = 0
    cont_digitos = 0

    print("La cadena a analizar es:", cadena_autor)

    for i in cadena_autor:
        # i = H o l a

        # dentro de la palabra
        if i != " " and i != ".":

            cont_caracteres += 1

            if (cont_caracteres == 2 or cont_caracteres == 3) and i.lower() == "r":
                cont_r_pos2_pos3 += 1

            if i in "0123456789":
                cont_digitos += 1

        # fuera de la palabra
        else:

            if cont_r_pos2_pos3 > 0 and cont_digitos == 0:
                cant_palabras += 1

            # reinicar contadores/banderas
            cont_caracteres = 0
            cont_r_pos2_pos3 = 0
            cont_digitos = 0

    print("Las palabras que cumplen son:", cant_palabras)


def mostrar_archivo_binario_porcentaje(fd):
    if not os.path.exists(fd):
        print("El archivo no existe.")
        return  # corta la funcion

    m = open(fd, "rb")
    tamanio = os.path.getsize(fd)

    # Al final del listado indicar el porcentaje que representan los idiomas frances y español
    # de libros sobre el total de registros mostrados.

    # porcentaje:    cant_total   --- 100%
    #                cant_cumplen    ----  X  = cant_cumplen * 100 / cant_total
    cant_total = 0
    cant_cumplen = 0

    while m.tell() < tamanio:
        librito = pickle.load(m)
        print(librito)
        cant_total += 1

        if librito.idioma == 1 or librito.idioma == 4:
            cant_cumplen += 1

    # calcular procentaje
    porc = cant_cumplen * 100 / cant_total
    print("El porcentaje es:", porc)

    m.close()



def vector_conteo(v_libros):
    # determinar la cantidad de libros por cada categoria posible, solo mostrar los contadores
    # se superen la cantidad de cero

    # generar vector conteo
    # categoria(13,15) = 15 - 13 + 1 = 3   -  13 14 15
    v_conteo = [0] * 3

    # categoria(13,15)  13-13
    # indice              0  1  2
    # v_conteo          [ 0, 0, 0 ]

    # rellenar el vector
    for i in v_libros:
        v_conteo[i.categoria - 13] += 1

    # mostrar el evector
    for i in range(len(v_conteo)):
        # i = 0, 1, 2

        # solo mostrar los contadores se superen la cantidad de cero
        if v_conteo[i] > 0:
            print("Categoria:", i+13, "Cantidad de libros:", v_conteo[i])





def menu():
    print("1 - Cargar arreglo.")
    print("2 - Mostrar arreglo.")
    print("3 - Generar matriz.")
    print("4 - Generar archivo binario.")
    print("5 - Mostrar archivo binario.")
    print("6 - busqueda binaria.")
    print("7 - busqueda secuencial.")
    print("8 - analisis de cadena.")
    op = int(input("Ingresar opción: "))
    return op


def principal():

    # arreglo / vector / lista de trabajo
    v_libros = []

    # nombre del archivo binario
    fd = "libros.dat"

    cadena_autor = None

    op = -1
    while op != 0:
        op = menu()

        if op == 1:
            n = validar_n()
            # Cada vez que se ingrese en esta opción, el arreglo debe ser creado desde cero y
            # todo contenido anterior debe ser eliminado.
            v_libros = []
            cargar_arreglo(v_libros, n)

        elif op == 2:

            if len(v_libros) > 0:
                mostrar_datos(v_libros)
            else:
                print("El arreglo no esta cargado.")

        elif op == 3:
            """ 
            3 - a partir de arreglo, determinar y mostrar el acumulado de los importes de los libros 
            para cada posible combinacion
            entre idioma y categoria, solo mostrar los acumuladores que superen un valor "x"
            """
            if len(v_libros) > 0:
                x = int(input("Ingresar importe acumulado a superar: "))
                generar_matriz(v_libros, x)
            else:
                print("El arreglo no esta cargado.")

        elif op == 4:
            """
            4 - A partir del arreglo genere un archivo binario que contenga los datos de 
            todos los libros del autor a cuyo precio no supere p, siendo a y p dos valores 
            ingresados por teclado.
            """
            if len(v_libros) > 0:
                a = input("Ingresar autor a guardar: ")
                p = float(input("Ingresar importe a no superar: "))
                generar_archivo_binario(v_libros, fd, a, p)
            else:
                print("El arreglo no esta cargado.")

        elif op == 5:
            """
            5 - Mostrar el archivo generado en el punto anterior indicando, al final, 
            cuántos libros se mostraron.
            al final Mostrar el promedio de los importes de los libros que se mostraron.
            """
            mostrar_archivo_binario(fd)

        elif op == 6:
            """
            6 - Buscar un libro por ISBN. Si existe mostrar todos sus datos y si, además, el idioma 
            del mismo es Francés, realizar un descuento del 22% sobre su precio de venta, mostrando los 
            datos del libro antes y después de la actualización. Si el libro no existe informar con el 
            mensaje “No contamos con el libro <ISBN> pero no deje de visitar nuestra sección de ofertas!”.
            """
            if len(v_libros) > 0:
                num_isbn = int(input("Ingresar ISBN a buscar: "))
                busqueda_binaria(v_libros, num_isbn)
            else:
                print("El arreglo no esta cargado.")

        elif op == 7:
            """ 
            7 - Determinar si existe un libro cuyo autor sea "a" y si existe mostrar solo su precio de venta
            y su numero de isbn y ademas retornar en una variable el autor para utilizarlo luego en el punto
            8, si no existe retornar el mensaje "no existe" para ser utilizado en el punto 8 
            """
            if len(v_libros) > 0:
                a = input("Ingresar autor a buscar: ")
                cadena_autor = busqueda_secuencial(v_libros, a)
            else:
                print("El arreglo no esta cargado.")

        elif op == 8:
            """ 
            analizar el autor retornado por el punto 7, ¿Cuál es la cantidad de
            palabras de esa cadena que contienen una letra "r" en la segunda o en la tercera posición (en
            mayúsculas o minúsculas) y que además no contienen ningún dígito?
            """
            if cadena_autor is None:
                print("Pasar primero por el punto 7")
            else:
                analisis_cadena(cadena_autor)

        elif op == 9:
            # analizar el autor del primer libro/objeto del arreglo
            cadena = v_libros[0].autor
            analisis_cadena(cadena)

            # analizar el autor del ultimo libro/objeto del arreglo
            ultimo = len(v_libros) - 1
            cadena = v_libros[ultimo].autor
            analisis_cadena(cadena)

            # analizar el autor del centro libro/objeto del arreglo
            centro = len(v_libros) // 2
            cadena = v_libros[centro].autor
            analisis_cadena(cadena)

        elif op == 10:
            # Al final del listado indicar el porcentaje que representan las Ventas
            # de productos de origen Importado sobre el total de registros mostrados.
            mostrar_archivo_binario_porcentaje(fd)


        elif op == 11:
            # determinar la cantidad de libros por cada categoria posible, solo mostrar los contadores
            # se superen la cantidad de cero
            vector_conteo(v_libros)


if __name__ == "__main__":
    principal()
