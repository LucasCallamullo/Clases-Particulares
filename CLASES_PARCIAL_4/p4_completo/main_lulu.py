import os.path
import pickle
import random
from registro import *


# ===========================================================================
#                               Opcion 1
# ===========================================================================
def validar_n():
    n = int(input("Ingresar cantidad de libros a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de libros a cargar: "))
    return n


def cargar_arreglo(v_libros, n):
    # ibsn 13 digitos INT, titulo STR, autor(11, 17), idioma(1, 5), importe FLOAT
    for i in range(n):
        isbn = random.randint(1000000000000, 9000000000000)
        titulo = random.choice("ABCDEF")
        autor = random.randint(11, 17)
        idioma = random.randint(1, 5)
        importe = round(random.uniform(0.1, 10), 2)

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
#                               Opcion 2
# ===========================================================================
def mostrar_datos(v_libros):
    for i in v_libros:
        # i = L1,   L2
        print(i)


# ===========================================================================
#                               Opcion 6
# ===========================================================================
def busqueda_binaria(v_libros, num_isbn):
    izq, der = 0, len(v_libros) - 1

    while izq <= der:

        c = (izq + der) // 2  # c = centro = 0

        # if v_libros[c].isbn == nuevo_libro.isbn:
        if v_libros[c].isbn == num_isbn:
            pos = c
            # break
            return pos  # pos >= 0 son valores de indice

        # elif v_libros[c].isbn > nuevo_libro.isbn:
        elif v_libros[c].isbn > num_isbn:
            der = c - 1

        else:
            izq = c + 1

    return -1       # cuando no existe un objeto que cumpla


# ===========================================================================
#                               Opcion 4
# ===========================================================================
def generar_archivo_binario(v_libros, fd, a, p):

    m = open(fd, "wb")

    for i in v_libros:
        # i = L1 L2 L3

        # guardar  los datos de todos los libros del autor a cuyo precio no supere p
        if i.autor == a and i.importe < p:
            pickle.dump(i, m)
            m.flush()   # opcional --> para guardar mejor el archivo

    print("Se genero el archivo binario") # opcional
    m.close()   # OBLIGATORIO


# ===========================================================================
#                               Opcion 5
# ===========================================================================
def mostrar_archivo_binario(fd):

    if os.path.exists(fd) is False:
        print("El archivo no existe:", fd)
        return      # cortar la funcion

    m = open(fd, "rb")
    tam = os.path.getsize(fd)

    #  al final, cuántos libros se mostraron.
    cont = 0

    # al final mostrar el promedio de los importes de los libritos guardados en el archivo
    # promedio = acumulado ( de importes ) / la cantidad de veces qeu acumule
    acum = 0
    cont = 0

    while m.tell() < tam:
        librito = pickle.load(m)
        # librito = L1  L2  L3
        print(librito)
        acum += librito.importe
        cont += 1

    # calcular promedio
    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio es:", prom)

    print("La cantidad que se mostro es:", cont)

    m.close()


# ===========================================================================
#                               Opcion 3
# ===========================================================================
def generar_matriz(v_libros, x):

    # crear la matriz
    f = 5    # f = filas = idioma(1, 5) = 5 - 1 + 1 = 5
    c = 7    # c = columnas = autor(11, 17) = 17 - 11 + 1 = 7
    matriz = [ [0] * c for i in range(f) ]

    # rellenar la matriz
    for i in v_libros:
        # i = L1,   L2, L3
        # matriz[f][c]
        matriz[i.idioma - 1][i.autor - 11] += 1

        # acumular el importe por cada combinacion de autor e idioma
        # matriz[i.idioma - 1][i.autor - 11] += i.importe

    # mostrar la matriz
    tupla_idiomas = ("Español", "Inglés", "Portugués", "Francés", "Italiano")

    # acumular la cantidad total de libros para un autor "a" que se cargar por teclado
    acum = 0

    for f in range(len(matriz)):
        # f = 0, 1, 2, 3, 4

        for c in range(len(matriz[0])):

            # solo mostrar las cantidades de libros superiores a "x"
            if matriz[f][c] > x:
                # print("Idioma:", f+1, "| Autor:", c+11, "| Cantidad:", matriz[f][c])
                print("Idioma:", tupla_idiomas[f], "| Autor:", c+11, "| Cantidad:", matriz[f][c])

            # Solo mostrar los idiomas 1:ESPAÑOL Y 4:FRANCES
            # if 1 == f+1 or 4 == f+1:
            #    print("Idioma:", f + 1, "| Autor:", c + 11, "| Cantidad:", matriz[f][c])

            # acumular la cantidad total de libros para un autor "a" que se cargar por teclado
            if c+11 == 11:  # con la  "a"
                acum += matriz[f][c]

    print("El acumulado del autor '11' es:", acum)


def menu():
    print("1 - Cargar arreglo.")
    print("2 - Mostrar arreglo.")
    print("3 - Generar matriz.")
    print("4 - Generar archivo binario.")
    print("5 - Mostrar archivo binario.")
    print("6 - busqueda binario.")
    op = int(input("Ingresar opción: "))
    return op

def principal():

    # vector de trabajo
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
            3 - Determianr la cantidad de libros por cada posible combinacion de autores con 
            idiomas posibles, solo mostrar los cantidades de libros superiores a "x"
            """
            if len(v_libros) > 0:
                x = int(input("Ingresar cantidad a superar: "))
                generar_matriz(v_libros, x)

            else:
                print("El arreglo no esta cargado.")

        elif op == 6:
            """
            6 - Buscar un libro por ISBN. Si existe mostrar todos sus datos y si, además, 
            el idioma del mismo es Francés, realizar un descuento del 22% sobre su precio de venta,
            mostrando los datos del libro antes y después de la actualización. Si el libro no 
            existe informar con el mensaje “No contamos con el libro <ISBN> pero no deje de
            visitar nuestra sección de ofertas!”.
            """
            num_isbn = int(input("Num_ISBN a buscar: "))
            pos = busqueda_binaria(v_libros, num_isbn)

            if pos >= 0:
                print(v_libros[pos])

                # el idioma del mismo es Francés, realizar un descuento del 22% sobre su precio de venta
                if v_libros[pos].idioma == 4:
                    v_libros[pos].importe -= v_libros[pos].importe * 0.22

                print("Datos actualizados:", v_libros[pos])

            else:   # cuando pos es -1
                print("No contamos con el libro", num_isbn, "pero no deje de visitar nuestra sección "
                      "de ofertas!")

        elif op == 4:
            """
            4 - A partir del arreglo genere un archivo binario que contenga los datos de 
            todos los libros del autor a cuyo precio no supere p, siendo a y p dos valores 
            ingresados por teclado.
            """
            if len(v_libros) > 0:
                a = int(input("INgresar autor a guardar: "))
                p = float(input("Ingresar precio a no superar: "))
                generar_archivo_binario(v_libros, fd, a, p)

        elif op == 5:
            """
            5 - Mostrar el archivo generado en el punto anterior indicando, al final, 
            cuántos libros se mostraron.
            """
            mostrar_archivo_binario(fd)


if __name__ == "__main__":
    principal()