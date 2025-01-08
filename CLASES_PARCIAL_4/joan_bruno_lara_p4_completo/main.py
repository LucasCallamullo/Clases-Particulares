import os.path
import pickle
import random

from registro import *


# ===========================================================================
#                           Opcion 1
# ===========================================================================
def validar_n():
    n = int(input("Ingresar cantidad de lotes a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de lotes a cargar: "))
    return n


def cargar_arreglo(v_lotes, n):
    # nombre STR, manzana(1, 35) INT, num_lote(1, 20), orientacion(1, 4), superficie FLOAT, importe FLOAT

    for i in range(n):
        nombre = random.choice("ABCDEF")
        manzana = random.randint(1, 35)
        num_lote = random.randint(1, 20)
        orientacion = random.randint(1, 4)
        superficie = round(random.uniform(0.1, 10), 2)
        importe = round(random.uniform(0.1, 10), 2)

        nuevo_lote = Lote(nombre, manzana, num_lote, orientacion, superficie, importe)
        add_in_order(v_lotes, nuevo_lote)

    print("Se genero el arreglo con la cantidad de", n, "registros.")  # opcional


def add_in_order(v_lotes, nuevo_lote):
    # L1.nombre     "C"
    # L2.nombre     "B"

    # indices       0
    # v_lotes    [  L1  ]
    # nombre        C

    izq, der = 0, len(v_lotes) - 1
    # izq = 0
    # der = -1

    while izq <= der:

        c = (izq + der) // 2        # c = 0

        # lo que cambia es el atributo por el que nos piden ordenar
        if v_lotes[c].nombre == nuevo_lote.nombre:
            pos = c
            break

        # la orientacion de la boquita ">" determina si esta de menor a mayor o mayor a menor
        elif v_lotes[c].nombre > nuevo_lote.nombre:
            der = c - 1

        else:
            izq = c + 1

    if izq > der:
        pos = izq

    # indices       0       1
    # v_lotes    [  L2,     L1  ]
    # nombre         B       C
    v_lotes[pos:pos] = [nuevo_lote]     # el objeto va ENTRE CORCHETES


# ===========================================================================
#                           Opcion 2
# ===========================================================================
def mostrar_datos(v_lotes):
    # indices       0       1
    # v_lotes    [  L1,     L2  ]
    for i in v_lotes:
        # i = L1,       L2      ,       L3 ,  --> la "i" vale como elemento
        # if i.importe > 0:
        print(i)

    #
    # for i in range(len(v_lotes)):
    #    # i = 0 ,1, 2, 3 --> aca toma valores de indice
    #    if v_lotes[i].importe > 0:
    #        print(v_lotes[i])


# ===========================================================================
#                           Opcion 3
# ===========================================================================
def generar_matriz(v_lotes, m):

    # crear la matriz
    f = 4   # f = filas = orientacion(1, 4) = lim_superior - lim_inferior + 1 = 4 - 1 + 1 = 4
    c = 35  # c = columnas = manzana(1, 35) = 35 - 1 + 1  = 35
    matriz = [ [0] * c for i in range(f) ]

    # orientacion(1, 4)    1-1     2-1       3       4
    # fila_indices          0       1       2       3

    # manzana(1, 35)   1-1 2-1  3-1   4   ...
    # columna_indices   0   1   2   3   4   ...

    # matriz[f][c] --> la forma de acceso es AL REVES a como lo cree
    # [ [0, 0, 0, 0, 5, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #   [5, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #   [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #   [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   ]

    #
    # rellenar la matriz
    for i in v_lotes:
        # i = L1,   L2,     L3
        # matriz[f][c]
        # acumular y mostrar la superficie total vendida por cada manzana y orientaicon
        matriz[i.orientacion - 1][i.manzana - 1] += i.superficie

        # si nos pidieran determinar la CANTIDAD posible de lotes por manzana y orientacion
        # matriz[i.orientacion - 1][i.manzana - 1] += 1

    #
    # mostrar la matriz
    tupla_orientaciones = ("Norte", "Sur", "Este", "Oeste")

    # Mostrar, además, la superficie total vendida para una manzana "m"
    acum = 0

    for f in range(len(matriz)):    # range(4=
        # f = 0, 1, 2, 3

        for c in range(len(matriz[0])):     # range(35)
            # c = 0, 1, 2, ..., 34

            # Solo mostrar los acumuladores que sean mayores a cero / "x"
            if matriz[f][c] > 0:        # if matriz[f][c] > x:
                print("Manzana:", c+1, "| Orientación:", f+1, "| Superficie Total:", matriz[f][c])
                # print("Manzana:", c+1, "| Orientación:", tupla_orientaciones[f], "| Superficie Total:", matriz[f][c])

            # solo mostrar las manzanas que estan entre m1 y m2
            # if m1 <= c+1 <= m2:
            #    print("Manzana:", c + 1, "| Orientación:", f + 1, "| Superficie Total:", matriz[f][c])

            # Mostrar, además, la superficie total vendida para una manzana "m"
            if m == c+1:
                acum += matriz[f][c]

    print("El acumulado de la manzana:", m, "es:", acum)


# ===========================================================================
#                           Opcion 4
# ===========================================================================
def generar_archivo_binario(v_lotes, fd, l1, l2):
    m = open(fd, "wb")  # primer parametro nombre del archivo ( fd )
                # segundo parametro: modo de apertura ( "wb" )

    # wb = write binary = crea el archivo si no existe, sobre escribe todo su contenido
    # ab = append binary = crea el archivo si no existe, agrega contenido al final del archivo
    # conserva todo su contenido anterior

    for i in v_lotes:
        # i = L1,   L2  ,       L3

        # contenga los datos de todos los lotes cuyo número de lote esté comprendido entre l1 y l2
        if l1 < i.num_lote < l2:
            pickle.dump(i, m)   # primer parametro que quiero guardar ( i )
                            # segundo parametro donde lo quiero guardar ( m )

    print("Se genero el archivo.")  # opcional

    m.close()       # OBLIGATORIO


# ===========================================================================
#                           Opcion 5
# ===========================================================================
def mostrar_archivo_binario(fd):
    bandera = os.path.exists(fd)    # retorna TRUE si existe el archivo, FALSE si no existe
    if bandera is False:        # if not bandera
        print("El archivo no existe:", fd)
        return      # cortar la funcion

    m = open(fd, "rb")  # read binary = modo de lectura
    tamanio = os.path.getsize(fd)   # nos dice el tamaño en bytes del archivo = 300

    # archivo = [   L1      L2      L3  ]
    # bytes     0       100     200     300
    # m.tell()  0       100     200

    # agregue una línea que informe el valor promedio de venta de los lotes con orientacion al NORTE SUR
    # contenidos en el archivo.
    # PROMEDIO = acumulado ( de importes ) / la cantidad de veces que acumule
    acum = 0
    cont = 0

    while m.tell() < tamanio:

        lotecito = pickle.load(m)   # recibe como unico parametro el archivo ( m )
        # lotecito = L1 ,       L2      ,       L3

        print(lotecito)

        if lotecito.orientacion == 1 or lotecito.orientacion == 2:
            acum += lotecito.importe
            cont += 1

    # calcular el promedio
    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio de importe es:", prom)

    m.close()   # OBLIGATORIO


# ===========================================================================
#                           Opcion 6
# ===========================================================================
def busqueda_binaria(v_lotes, nom):
    izq, der = 0, len(v_lotes) - 1

    while izq <= der:

        c = (izq + der) // 2  # c = 0

        # if v_lotes[c].nombre == nuevo_lote.nombre:
        if v_lotes[c].nombre == nom:
            pos = c
            # break
            return pos  # pos >= 0 si existe un objeto que cumple

        # elif v_lotes[c].nombre > nuevo_lote.nombre:
        elif v_lotes[c].nombre > nom:
            der = c - 1

        else:
            izq = c + 1

    return -1   # NO EXISTE UN OBJETO QUE CUMPLA


# ===========================================================================
#                           Principal
# ===========================================================================
def menu():
    print("1 - Cargar arreglo.")
    print("2 - Mostrar arreglo.")
    print("3 - Generar matriz.")
    print("4 - Generar archivo binario.")
    print("5 - Mostrar archivo binario.")
    print("6 - Busqueda binario.")
    print("0 - Salir.")
    op = int(input("Ingresar opción: "))
    return op


def principal():

    # vector arreglo o lista de trabajo
    v_lotes = []

    # nombre del archivo binario
    fd = "lotes.dat"  # file descripcion ; nombre del archivo

    op = -1
    while op != 0:
        op = menu()

        if op == 1:
            n = validar_n()
            # Cada vez que se ingrese en esta opción, el arreglo debe ser creado desde cero
            # y todo contenido anterior debe ser eliminado.
            v_lotes = []
            cargar_arreglo(v_lotes, n)

        elif op == 2:
            if len(v_lotes) > 0:
                mostrar_datos(v_lotes)
            else:
                print("El arreglo no esta cargado.")

        elif op == 3:
            """
            3 - A partir del arreglo generado en el punto 1, acumular y mostrar la 
            superficie total vendida por cada manzana posible combinada con cada orientación 
            posible. Mostrar, además, la superficie total vendida para una
            manzana m (siendo m un valor que se ingresa por teclado).
            """
            if len(v_lotes) > 0:
                m = int(input("Manzana a acumular su superficie: "))
                generar_matriz(v_lotes, m)
            else:
                print("El arreglo no esta cargado.")

        elif op == 4:
            """
            4 - A partir del arreglo, genere un archivo binario que 
            contenga los datos de todos los lotes cuyo número de lote
            esté comprendido entre l1 y l2, siendo estos valores que se ingresan por teclado.
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
            línea que informe el valor promedio de venta de los lotes con orientacion al NORTE SUR
            contenidos en el archivo.
            """
            mostrar_archivo_binario(fd)

        elif op == 6:
            """
            6 - buscar un nombre "nom" , si existe relizar un descuento de su importe por un 22%
            y mostrar su datos antes y post actualizacion
            y si no existe informar con el emnsaje "No existe el propietario <nom> bla bla bla"
            """
            nom = input("Ingresar nombre a buscar: ")
            pos = busqueda_binaria(v_lotes, nom)

            if pos >= 0:
                print("Datos sin actualizar:", v_lotes[pos])

                # relizar un descuento de su importe por un 22%
                v_lotes[pos].importe -= v_lotes[pos].importe * 0.22

                # ingresar un nuevo importe por teclado.
                # v_lotes[pos].importe = float(input("Ingresar nuevo importe: "))

                print("Datos actualizados:", v_lotes[pos])

            else:   # cuando pos es -1
                print("No existe el propietario", nom, "bla bla bla")

        elif op == 0:
            print("Gracias por usar el programa.")


if __name__ == "__main__":
    principal()
