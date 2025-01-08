import os.path
import pickle
import random


from registro import *


# ===========================================================================
#                               Opcion 1
# ===========================================================================
def validar_n():
    n = int(input("Ingresar cantidad de lotes a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de lotes a cargar: "))
    return n


def cargar_arreglo(v_lotes, n):
    # nombre STR, manzana(1, 35), num_lote(1, 20), orientacion(1, 4), superficie FLOAT, importe FLOAT
    for i in range(n):
        nombre = random.choice("ABCDEF")
        manzana = random.randint(1, 35)
        num_lote = random.randint(1, 20)
        orientacion = random.randint(1, 4)
        superficie = round(random.uniform(0.1, 10), 2)
        importe = round(random.uniform(0.1, 10), 2)

        nuevo_lote = Lote(nombre, manzana, num_lote, orientacion, superficie, importe)
        add_in_order(v_lotes, nuevo_lote)


def add_in_order(v_lotes, nuevo_lote):

    # L1.nombre     "C"
    # L2.nombre     "B"

    # indices       0
    # v_lotes = [   L1  ]
    # nombre        C

    izq, der = 0, len(v_lotes) - 1
    # izq = 0
    # der = -1

    while izq <= der:

        c = (izq + der) // 2        # c = centro = 0

        # el atributo por el que les pidan ordenar
        if v_lotes[c].nombre == nuevo_lote.nombre:
            pos = c
            break

        # la boquita ">" determinar si esta de menor a mayor o mayor a menor
        elif v_lotes[c].nombre > nuevo_lote.nombre:
            der = c - 1

        else:
            izq = c + 1

    if izq > der:
        pos = izq

    # indices       0       1
    # v_lotes = [   L2,     L1  ]
    # nombre         B       C
    v_lotes[pos:pos] = [nuevo_lote]     # el objeto ESTA ENTRE CORCHETES


# ===========================================================================
#                               Opcion 2
# ===========================================================================
def mostrar_datos(v_lotes):
    # indices       0       1       2
    # v_lotes = [   L1,     L2,     L3  ]
    for i in v_lotes:
        # i = L1,   L2  ,   L3
        print(i)


# ===========================================================================
#                               Opcion 3
# ===========================================================================
def generar_matriz(v_lotes, m):

    # crear la matriz
    f = 4     # f = filas = orientacion(1, 4) = lim_superior - lim_inferior + 1 = 4 - 1 + 1 = 4
    c = 35    # c = columnas = manzana(1, 35) = lim_superior - lim_inferior + 1 = 35 - 1 + 1 = 35
    matriz = [ [0] * c for i in range(f) ]

    # orientacion(1, 4)   1-1  2-1   3   4
    # fila_indices          0   1   2   3

    # manzana(1, 35)       1-1     2-1     3-1        ... 35-1
    # columnas_indices      0       1       2       3   ... 34

    # matriz[f][c]  --> la forma de acceso es al reves a como lo cree
    # [     [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ]

    #
    # rellenar la matriz
    for i in v_lotes:
        # i = L1,       L2,     L3
        # matriz[f][c]
        matriz[i.orientacion - 1][i.manzana - 1] += i.superficie

        # determinar la CANTIDAD por la combinacion posible de orientacion por manzana
        # matriz[i.orientacion - 1][i.manzana - 1] += 1

    #
    # mostrar la matriz
    tupla_orientaciones = ("Norte", "Sur", "Este", "Oeste")

    # Mostrar, además, la superficie total vendida para una manzana m
    acum = 0

    for f in range(len(matriz)):        # range(4)
        # f = 0, 1, 2, 3

        for c in range(len(matriz[0])):     # range(35)
            # c = 0, 1, 2, ... 34

            # solo mostrar las superficies acumuladas mayores a cero
            if matriz[f][c] > 0:
                print("Manzana:", c+1, "| Orientacion:", f+1, "| Superficie acumulada:", matriz[f][c])
                # print("Manzana:", c+1, "| Orientacion:", tupla_orientaciones[f], "| Superficie acumulada:", matriz[f][c])

            # solo mostrar las manzanas que esten entre m1 y m2 ( se cargan por teclado )
            # if m1 <= c+1 <= m2:
            #    print("Manzana:", c + 1, "| Orientacion:", f + 1, "| Superficie acumulada:", matriz[f][c])

            # Mostrar, además, la superficie total vendida para una manzana m
            if m == c+1:
                acum += matriz[f][c]

    print("Para la manzana:", m, "tenemos un acumulado de:", acum)


# ===========================================================================
#                               Opcion 4
# ===========================================================================
def generar_archivo_binario(v_lotes, fd, l1, l2):
    m = open(fd, "wb")  # primer parametro el nombre del archiv ( fd )
                        # segundo parametro es el modo de apertura "wb"
    # wb = crea el archivo y ademas sobre escribe todo el contenido.
    # ab = crea el archivo, agrega contenido al final del archivo conservando todo lo anterior

    for i in v_lotes:
        # i = L1,   L2, L3

        # contenga los datos de todos los lotes cuyo número de lote esté comprendido entre l1 y l2
        if l1 < i.num_lote < l2:
            pickle.dump(i, m)   # primer parametro lo que quiero guardar ( i )
                        # segundo parametro donde lo quiero guardar ( m )

    print("Se genero el archivo")   # opcional

    m.close()   # OBLIGATORIO


# ===========================================================================
#                               Opcion 5
# ===========================================================================
def mostrar_archivo_binario(fd):

    bandera = os.path.exists(fd)    # retorna TRUE si existe el archivo, retorna FALSE si NO existe
    if bandera is False:        # if not bandera
        print("No existe el archivo:", fd)
        return      # corta la funcion

    m = open(fd, "rb")  # read binary --> modo de lectura
    tamanio = os.path.getsize(fd)   # nos dice el tamaño en bytes del archivo = 300

    # archivo = [   L1      L2      L3  ]
    # bytes     0       100     200     300
    # m.tell()  0       100     200

    # luego de mostrarlo agregue una línea que informe el valor
    # promedio de venta de los lotes contenidos en el archivo.
    # promedio = acumulado ( de importes ) / la cantidad de veces que acumule
    acum = 0
    cont = 0

    while m.tell() < tamanio:

        lotecito = pickle.load(m)   # unico parametro el archivo ( m )
        # lotecito = L1,    L2  ,   L3
        print(lotecito)

        acum += lotecito.importe
        cont += 1

    # calcular promedio
    prom = 0
    if cont > 0:
        prom = acum / cont

    print("El promedio de los importes es:", prom)

    m.close()       # OBLIGATORIO


# ===========================================================================
#                               Opcion 6
# ===========================================================================
def busqueda_binaria(v_lotes, nom):     # nom C
    izq, der = 0, len(v_lotes) - 1

    # indices       0       1       2
    # v_lotes = [   L1,     L2,     L3  ]
    # nombre        A        B      C

    while izq <= der:

        c = (izq + der) // 2  # c = centro = 0

        # if v_lotes[c].nombre == nuevo_lote.nombre:
        if v_lotes[c].nombre == nom:
            pos = c
            # break
            return pos  # posicion donde tengo un objeto que cumple mi criterio de busqueda

        # elif v_lotes[c].nombre > nuevo_lote.nombre:
        elif v_lotes[c].nombre > nom:
            der = c - 1

        else:
            izq = c + 1

    return -1       # no existe un objeto que cumpla con el criterio de busqueda


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

    # arreglo / vector / lista de trabajo
    v_lotes = []

    # nombre del archivo binario
    fd = "lotes.dat"

    op = -1
    while op != 0:
        op = menu()

        if op == 1:
            n = validar_n()
            cargar_arreglo(v_lotes, n)

        elif op == 2:
            # if v_lotes:     # si v_lotes tiene contenido
            if len(v_lotes) > 0:
                mostrar_datos(v_lotes)
            else:
                print("El arreglo no esta cargado")

        elif op == 3:
            """
            3 - A partir del arreglo generado en el punto 1, acumular y mostrar la superficie total vendida por cada manzana
posible combinada con cada orientación posible. Mostrar, además, la superficie total vendida para una
manzana m (siendo m un valor que se ingresa por teclado).
            """
            if len(v_lotes) > 0:
                m = int(input("Ingresar manzana a totalizar: "))
                generar_matriz(v_lotes, m)
            else:
                print("El arreglo no esta cargado")

        elif op == 4:
            """
            A partir del arreglo, genere un archivo binario que contenga los datos de todos los lotes 
            cuyo número de lote esté comprendido entre l1 y l2, siendo estos valores que se 
            ingresan por teclado.
            """
            if len(v_lotes) > 0:
                l1 = int(input("Ingresar num_lote a superar: "))
                l2 = int(input("Ingresar num_lote a ser menor: "))
                generar_archivo_binario(v_lotes, fd, l1, l2)
            else:
                print("El arreglo no esta cargado")

        elif op == 5:
            """
            Mostrar el archivo generado en el punto anterior y luego de mostrarlo agregue una 
            línea que informe el valor promedio de venta de los lotes contenidos en el archivo
            """
            mostrar_archivo_binario(fd)

        elif op == 6:
            """
            buscar por nombre "nom" si existe realizar un descuento en su importe del 22% 
            mostrar sus datos antes y despues del cambio
            si no existe informar
            """
            nom = input("Ingresar nombre a buscar: ")
            pos = busqueda_binaria(v_lotes, nom)

            if pos >= 0:
                print("Datos sin actualizar:", v_lotes[pos])

                v_lotes[pos].importe -= v_lotes[pos].importe * 0.22

                print("Datos actualizados:", v_lotes[pos])

            else:   # pos = -1
                print("No existe!")


if __name__ == "__main__":
    principal()
