import os.path
import pickle
import random


from registro import *


# ===========================================================================
#                       Opcion 1
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

    izq, der = 0, len(v_lotes) - 1

    while izq <= der:
        c = (izq + der) // 2

        # es el atributo por el que te pidan ordenar
        if v_lotes[c].nombre == nuevo_lote.nombre:
            pos = c
            break

        # la boquita ">" determina si esta de menor a mayor o de mayor a menor
        elif v_lotes[c].nombre > nuevo_lote.nombre:
            der = c - 1

        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v_lotes[pos:pos] = [nuevo_lote]     # el objeto ESTA ENTRE CORCHETES


# ===========================================================================
#                       Opcion 2
# ===========================================================================
def mostrar_datos(v_lotes):
    # v_lotes = [ L1, L2, L3]

    for i in v_lotes:
        # i = L1    ,   L2,     L3
        print(i)


# ===========================================================================
#                       Opcion 3
# ===========================================================================
def generar_matriz(v_lotes, m):
    # crear la matriz
    f = 4    # f = filas = orientacion(1, 4) = lim_superior - lim_inferior + 1 = 4 - 1 + 1 = 4
    c = 35   # c = columnas = manzana(1, 35) = lim_superior - lim_inferior + 1 = 35 - 1 + 1 = 35
    matriz = [ [0] * c for i in range(f) ]

    # orientacion(1, 4)    1-1   2   3   4
    # fila_indices          0   1   2   3

    # manzana(1, 35)       1-1   2   3   4        ...
    # columna_indices       0   1   2   3   4   5 ...

    # matriz[f][c]
    # [ [0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #   [0, 4, 0, 5, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   ]

    #
    # rellenar la matriz
    for i in v_lotes:
        # i = L1, L2, L3
        # matriz[f][c]
        matriz[i.orientacion - 1][i.manzana - 1] += i.superficie
        # matriz[i.orientacion - 1][i.manzana - 1] += 1   # si a ustedes les pidieran CUANTOS lotes hay por cada posible
        # orientaicon y manzana

    #
    # mostrar la matriz

    # Mostrar, además, la superficie total vendida para una manzana m
    acum = 0

    tupla_orientaciones = ("Norte", "Sur", "Este", "Oeste")

    for f in range(len(matriz)):    # range(4)
        # f = 0, 1, 2, 3

        for c in range(len(matriz[0])):    # range(35)
            # c = 0, 1, 2, 3 ... 34

            # Solo mostrar los que tengan un superficie vendida mayor a 0   # "x"
            # if matriz[f][c] > x:
            if matriz[f][c] > 0:
                print("Manzana:", c+1, "| Orientación:", f+1, "| Superficie Vendida:", matriz[f][c])
                # print("Manzana:", c+1, "| Orientación:", tupla_orientaciones[f], "| Superficie Vendida:", matriz[f][c])

            # Solo mostrar las manzanas que esten entre m1 y m2
            # if m1 <= c+1 <= m2:
            #    print("Manzana:", c + 1, "| Orientación:", f + 1, "| Superficie Vendida:", matriz[f][c])

            # Mostrar, además, la superficie total vendida para una manzana m
            if m == c+1:
                acum += matriz[f][c]

    print("El acumulado de la manzana", m, "es:", acum)


# ===========================================================================
#                       Opcion 4
# ===========================================================================
def generar_archivo_binario(v_lotes, fd, l1, l2):
    m = open(fd, "wb")  # primer parametro: nombre del archivo ( fd )
                        # segundo parametro: el modo de apertura ( "wb" )
    # wb = write binary = crea el archivo si no existe, sobre escribe todo el contenido del archivo
    # ab = append binary = crea el archivo si no existe, agrega contenido al final del archivo
    # conserva todo su contenido

    for i in v_lotes:
        # i = L1, L2, L3
        # condicion un num_lote entree l1 y l2
        if l1 < i.num_lote < l2:

            pickle.dump(i, m)   # primer parametro: el objeto que quiero guardar ( i )
                                # segundo parametro: donde lo quiero guardar ( m )

    print("Se genero el archivo.")  # Opcional

    m.close()   # OBLIGATORIO


# ===========================================================================
#                       Opcion 5
# ===========================================================================
def mostrar_archivo_binario(fd):
    bandera = os.path.exists(fd)    # retorna TRUE si existe el archivo y FALSE si NO EXISTE
    if bandera is False:        # if not bandera
        print("No existe el archivo:", fd)
        return      # cortar la funcion, la termina aca

    m = open(fd, "rb")  # rb = read binary = modo de lectura
    tam = os.path.getsize(fd)   # nos dice el tamaño en bytes del archivo   = 300

    #
    # archivo = [   L1      L2       L3 ]
    # bytes     0       100     200     300
    # m.tell()  0       100     200     300

    # al final indicar en una línea que informe el valor promedio de venta de los lotes que
    # tengan una orientacion NORTE O SUR contenidos en el archivo.
    # promedio = acumulado ( de importes ) / sobre la cantidad de veces que acumule
    acum = 0
    cont = 0

    while m.tell() < tam:

        lotecito = pickle.load(m)   # unico parametro es el archivo ( m )
        # lotecito = L1,         L2,     L3
        print(lotecito)

        if lotecito.orientacion == 1 or lotecito.orientacion == 2:
            acum += lotecito.importe
            cont += 1

    # calcular promedio
    prom = 0
    if cont > 0:
        prom = acum / cont
    print("el promedio es:", prom)

    m.close()   # OBLIGATORIO


# ===========================================================================
#                       Opcion 6
# ===========================================================================
def busqueda_binaria(v_lotes, nom):
    # indices       0      1       2       3       4
    # v_lotes = [   L1,   L2,     L3,     L4,     L5 ]

    izq, der = 0, len(v_lotes) - 1

    while izq <= der:
        c = (izq + der) // 2

        # if v_lotes[c].nombre == nuevo_lote.nombre:
        if v_lotes[c].nombre == nom:
            pos = c
            # break
            return pos  # pos es un indice del arreglo, es la posicion donde existe un objeto que cumple
                        # con mi criterio de busqueda   v_lotes[pos]
                        # pos --> puede ser valores de cero o más

        # elif v_lotes[c].nombre > nuevo_lote.nombre:
        elif v_lotes[c].nombre > nom:
            der = c - 1

        else:
            izq = c + 1

    return -1   # no encontro un objeto que cumpla


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

    # vector / arreglo de trabajo
    v_lotes = []

    # nombre del archivo binario
    fd = "lotes.dat"

    op = -1
    while op != 0:
        op = menu()

        if op == 1:
            n = validar_n()
            # Cada vez que se ingrese en esta opción, el arreglo debe ser
            # creado desde cero y todo contenido anterior debe ser eliminado
            v_lotes = []   # 0
            cargar_arreglo(v_lotes, n)   # 4

        elif op == 2:
            if len(v_lotes) > 0:
                mostrar_datos(v_lotes)

            else:
                print("El arreglo no esta cargado.")

        elif op == 3:
            if len(v_lotes) > 0:
                # Mostrar, además, la superficie total vendida para una
                # manzana m (siendo m un valor que se ingresa por teclado).
                m = int(input("Manzana a totalizar: "))
                generar_matriz(v_lotes, m)

            else:
                print("El arreglo no esta cargado.")

        elif op == 4:
            """
            A partir del arreglo, genere un archivo binario que contenga los datos de todos los 
            lotes cuyo número de lote esté comprendido entre l1 y l2, siendo estos valores que se 
            ingresan por teclado.
            """
            if len(v_lotes) > 0:
                l1 = int(input("Ingresar num_lote a superar: "))
                l2 = int(input("Ingresar num_lote a ser menor: "))
                generar_archivo_binario(v_lotes, fd, l1, l2)

            else:
                print("El arreglo no esta cargado.")

        elif op == 5:
            """
            5 - Mostrar el archivo generado en el punto anterior y luego de mostrarlo agregue una 
            línea que informe el valor promedio de venta de los lotes contenidos en el archivo.
            """
            mostrar_archivo_binario(fd)

        elif op == 6:
            """
            6 - Buscar un lotes por un nombre de propietario "nom", si existe y su orientacion era
            NORTE SUR O ESTE, realizar un descuento del 22% en su importe y mostrar sus datos antes y despues de la
            modificacion , pero si no existe informar con el mensaje
            "No existe un propietario con ese nombre <nom>"
            """
            nom = input("Ingresar nombre a buscar: ")
            pos = busqueda_binaria(v_lotes, nom)

            if pos >= 0:

                print("Datos sin actualizar: ", v_lotes[pos])

                # NORTE SUR O ESTE
                if 1 <= v_lotes[pos].orientacion <= 3:

                    # realizar un descuento del 22%
                    v_lotes[pos].importe -= v_lotes[pos].importe * 0.22

                    # igual a un valor qeu se carga por teclado
                    v_lotes[pos].importe = float(input("Ingresar nuevo importe: "))

                print("Datos actualizados: ", v_lotes[pos])

            else:   # pos = -1
                print("No existe un propietario con ese nombre", nom)



if __name__ == "__main__":
    principal()
