
# Libro: Define una clase Libro con atributos como título, género(1, 10), precio

# Se pide cargar el arreglo ordenado todo el tiempo por genero
# Se pide mostrar el arreglo

import os.path
import pickle
import random
from registro import *


# =============================================================================
#                       Opcion 1
# =============================================================================
def cargar_arreglo(v_libro, n):
    titulos = "ABCD"
    for i in range(n):      # n = 5
        # 0 1
        titulo = random.choice(titulos)
        genero = random.randint(1, 4)
        precio = round(random.uniform(0.1, 10), 2)
        year = random.randint(2000, 2020)
        librito = Libro(titulo, genero, precio, year)
        add_in_order(v_libro, librito)


def add_in_order(v_libro, librito):
    # len(v_libro) = 0      # primera vuelta    librito.genero = 5
    # len(v_libro) = 1      # segunda vuelta    librito.genero = 4

    izq, der = 0, len(v_libro) - 1

    while izq <= der:           # mientras
        c = (izq + der) // 2        #
        if v_libro[c].year == librito.year:
            pos = c
            break
        elif v_libro[c].year > librito.year:        # si se come al vector esta de menor a mayor
            der = c - 1                             # se se come al objeto esta de mayor a menor
        else:
            izq = c + 1

    if izq > der:
        pos = izq
                                            #       0                       1
    v_libro[pos:pos] = [librito]            # librito.genero = 4, primer librito.genero = 5


# =============================================================================
#                       Opcion 2
# =============================================================================
def mostrar_datos(v_libro):
    #            0  1  2  3  4
    # v_libro = [L, L, L, L, L]
    for i in v_libro:
        # i = L, L
        print(i)


# =============================================================================
#                       Opcion 3
# =============================================================================
def generar_matriz(v_libro):
    # genero(1,4)
    # año (2000, 2020)
    # creamos la matriz
    filas = 4
    columnas = 21

    matriz_conteo = [[0] * columnas for i in range(filas)]
    matriz_acum = [[0] * columnas for i in range(filas)]

    # rellenamos la matriz
    for i in v_libro:
        # i = L ,   L , L
        matriz_conteo[i.genero-1][i.year-2000] += 1
        matriz_acum[i.genero-1][i.year-2000] += i.precio

    #            0   1   2   3   4
    # v_libro = [1, L2, L3, L4, L5]
    #           [L1, L2, L3, L4, L5]

    # Mostrar la matriz
    #                               1           2           3           4
    # f                 0           1           2           3
    # indices           0           1           2           3
    desc_generos = ("Ficcion", "Romantico", "Ciencia", "Misterio")
    for f in range(len(matriz_conteo)):             # representa a las filas
        for c in range(len(matriz_conteo[0])):       # representa a las columnas
            if matriz_conteo[f][c] > 0 and c+2000 > 2012:
                print("La cantiddad Por genero:", desc_generos[f], "Y año:", c+2000)
                print("La cantidad total es:", matriz_conteo[f][c])


# =============================================================================
#                       Opcion 4
# =============================================================================
def generar_archivo(fd, v_libro, x):
    m = open(fd, "wb")
    #            0  1  2  3  4
    # v_libro = [L1, L2, L3, L4, L5]

    #
    cont = 0
    for i in v_libro:
        # i = L1    ; L2    ; L3    ; L4    ; L5
        if i.year > x and (i.genero == 3 or i.genero == 4):
            pickle.dump(i, m)
            m.flush()    # No es necesaria
            cont += 1
    print("La cantidad de objetos cargados en el archivo fue:", cont)
    m.close()


# =============================================================================
#                       Opcion 5
# =============================================================================
def mostrar_archivo(fd):
    if os.path.exists(fd):
        m = open(fd, "rb")
        tam = os.path.getsize(fd)       # obtiene el tamaño total en bytes del archivo

        #            0    1   2   3   4
        # v_libro = [L1, L2, L3, L4, L5]


        # fd    = [ L1          L2              L3 ]
        #         0      25             50          70

        cont = 0
        acum = 0
        while m.tell() < tam:
            lib = pickle.load(m)
            print(lib)

            if lib.year < 2015:
                cont += 1
                acum += lib.precio

        if cont > 0:
            prom = acum / cont
            print("El promedio de los libros publicados antes del 2015 es:", prom)

    else:
        print("El archivo no existe, por favor ingrese primero por la opcion 4.")


# =============================================================================
#                       Opcion 6
# =============================================================================
def busqueda_secuencial(v_libro, tit):
    se_encontro = False
    for i in range(len(v_libro)):
        # i = 0, 1, 2, 3 ...
        if v_libro[i].titulo == tit:
            print(v_libro[i])
            se_encontro = True

    if not se_encontro:         # se_encontro esta en falso
        print("No se encontro ningun titulo con ese nombre.")


# =============================================================================
#                       Opcion 7
# =============================================================================
def busqueda_binaria(v_libro, x):
    izq, der = 0, len(v_libro) - 1

    while izq <= der:           # mientras
        c = (izq + der) // 2        #
        if v_libro[c].year == x:
            return c
        elif v_libro[c].year > x:
            der = c - 1
        else:
            izq = c + 1
    return -1


def menu():
    print("=" * 50)
    # alt + 92 = \
    print(" 1 - Cargar arreglo."
          "\n 2 - Mostrar Datos."
          "\n 3 - Generar Matriz"
          "\n 4 - Generar Archivo Binario."
          "\n 5 - Mostrar Archivo Binario."
          "\n 6 - Busqueda Secuencial."
          "\n 7 - Busqueda Binaria."
          "\n "
          "\n 0 - Salir.")

    op = int(input("Ingrese una opcion: "))
    return op


def principal():

    # nuestra vector/lista/arreglo
    v_libro = []    # tam = 0


    # archivo principal
    fd = "libros.dat"


    op = -1
    while op != 0:

        op = menu()

        if op == 1:
            n = int(input("Ingrese cantidad de libros a cargar: "))
            cargar_arreglo(v_libro, n)


        elif op == 2:
            mostrar_datos(v_libro)

        elif op == 3:
            generar_matriz(v_libro)


        elif op == 4:
            x = int(input("Ingresar año a superar: "))
            generar_archivo(fd, v_libro, x)

        elif op == 5:
            mostrar_archivo(fd)

        elif op == 6:
            tit = input("Ingresar titulo a buscar: ")
            busqueda_secuencial(v_libro, tit)

        elif op == 7:
            x = int(input("Ingresar un año de publicacion a buscar: "))
            pos = busqueda_binaria(v_libro, x)
            if pos >= 0:
                # datos viejos
                print(v_libro[pos])

                # Modifcando el precio del librop que encontramos
                t = float(input("Ingresar nuevo precio a modifcar: "))
                v_libro[pos].precio = t

                # datos nuevos
                print(v_libro[pos])

            else:
                print("No se encontraron coincidencias.")


if __name__ == '__main__':
    principal()
