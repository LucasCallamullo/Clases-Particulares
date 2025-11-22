import os.path
import pickle
import random

from registro import *


# ===========================================================
#               Opcion 1
# ===========================================================
def validar_n():
    n = int(input("Ingresar cantidad de lotes a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de lotes a cargar: "))
    return n


def cargar_arreglo(v_lotes, n):
    # nombre STR, manzana(3, 7), num_lote(1, 10), orientacion (1, 4), superficie FLOAT, importe FLOAT
    for i in range(n):
        nombre = random.choice("ABCDEF")
        manzana = random.randint(3, 7)
        num_lote = random.randint(1, 10)
        orientacion = random.randint(1, 4)
        superficie = round(random.uniform(0.1, 10), 2)      # FLOAT
        importe = round(random.uniform(0.1, 10), 2)      # FLOAT

        lotecito = Lote(nombre, manzana, num_lote, orientacion, superficie, importe)

        # SI O SI
        add_in_order(v_lotes, lotecito)

    print("Se cargaron la cantidad de lotes de:", n)


def add_in_order(v_lotes, lotecito):

    izq, der = 0, len(v_lotes) - 1

    while izq <= der:
        c = (der + izq) // 2

        # el atributo por el que te piden ordenar
        if v_lotes[c].nombre == lotecito.nombre:
            pos = c
            break

        # saber que la boquita ">" determinar si esta de menor a mayor o mayor a menor
        elif v_lotes[c].nombre > lotecito.nombre:
            der = c - 1

        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v_lotes[pos:pos] = [lotecito]


# ===========================================================
#               Opcion 2
# ===========================================================
def mostrar_datos(v_lotes):

    for i in v_lotes:
        # i = L1,   L2, L3

        # si la superficie es menor o igual a 5, incluir en el mensaje "Superficie Reducida"
        # y sino no mostrar ningun mensaje agregado
        if i.superficie <= 5:
            print(i, " - Superficie Reducida")
        else:
            print(i)


# ===========================================================
#               Opcion 3
# ===========================================================
def generar_matriz(v_lotes, m):
    # acumular y mostrar la superficie total vendida por cada manzana
    # posible combinada con cada orientación posible

    # generar la matriz:
    f = 5    # f = filas = manzana(3, 7) = lim_superior - lim_inferior + 1 = 7 - 3 + 1 = 5
    c = 4    # c = columnas = orientacion(1, 4) = lim_superior - lim_inferior + 1 = 4 - 1 + 1 = 4
    matriz = [ [0] * c for i in range(f) ]

    # manzana(3, 7)     = 3, 4, 5, 6, 7
    # filas             = 0, 1, 2, 3, 4

    # matriz    =   [   [0, 0, 0, 0],
    #                   [0, 0, 0, 0],
    #                   [0, 0, 0, 0],
    #                   [0, 0, 0, 0],
    #                   [0, 0, 0, 0]    ]

    # como acceder a cada contador/acumulador, se accede al reves a como lo creaste
    # se accede primero a f y despues c --> matriz[f][c]

    #
    # rellenar la matriz
    for i in v_lotes:
        # acumular y mostrar la superficie total vendida por cada manzana
        # posible combinada con cada orientación posible    ( matriz de acumulacion )
        matriz[i.manzana - 3][i.orientacion - 1] += i.superficie

        # determinar y mostrar la cantidad de lotes por cada manzana
        # posible combinada con cada orientación posible    ( matriz de conteo )
        # matriz[i.manzana - 3][i.orientacion - 1] += 1

    #
    # mostrar la matriz

    tupla_orientaciones = ("Norte", "Sur", "Este", "Oeste")


    # Mostrar, además, la superficie total vendida para una manzana m
    acum = 0

    for f in range(len(matriz)):        # 5
        # f = 0, 1, 2, 3, 4

        for c in range(len(matriz[0])):     # 4
            # c = 0, 1, 2, 3

            # solo mostrar los acumuladores que sean distintos de cero
            if matriz[f][c] != 0:
                # print("Manzana:", f+3, " - Orientacion:", c+1, " - Superficie Acumulador:", matriz[f][c])
                print("Manzana:", f+3, " - Orientacion:", tupla_orientaciones[c], " - Superficie Acumulador:", matriz[f][c])

            # solo mostrar las manzanas que esten entre m1 y m2
            # if m1 <= f+3 <= m2:
            #    print("Manzana:", f+3, " - Orientacion:", c+1, " - Superficie Acumulador:", matriz[f][c])

            # la superficie total vendida para una manzana m
            if f+3 == m:
                acum += matriz[f][c]


    print("La superficie acumulada para la manzana:", m, "es de:", acum)


# ===========================================================
#               Opcion 4
# ===========================================================
def generar_archivo_binario(v_lotes, fd, l1, l2):

    m = open(fd, "wb")  # primer parametro es el nombre del archivo
                        # segundo parametro modo de apertura
    # "wb" = write binary = vas a sobreescribir todo el contenido de tu archivo
    # "ab" = append binary = agregar contenido al final, conservando todo el contenido anterior

    for i in v_lotes:
        # i = L1, L2, L3

        # todos los lotes cuyo número de lote esté comprendido entre l1 y l2 ( ambos incluidos )
        # if i.num_lote >= l1 and i.num_lote <= l2:
        if l1 <= i.num_lote <= l2:

            # generar/crear el archivo binario
            pickle.dump(i, m)   # primer parametro es lo que queres guardar, en este caso el objeto ( i )
                                # segundo parametro es el archivo ( m )

    print("Se sobre escribio el archivo binario.")
    m.close()       # OBLIGATORIO


# ===========================================================
#               Opcion 4
# ===========================================================
def generar_archivo_binario_promedio(v_lotes, fd):
    """
    generar un archivo binario que guarde a todos los lotes que supéren al importe promedio de los
    lotes en el arreglo

    # calcules el promedio de los importes en el arreglo
    # guardes en el archivo binario los objetos que superan al importe
    """
    # calcular promedio
    acum = cont = 0

    for i in v_lotes:
        acum += i.importe
        cont += 1

    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio de importe es:", prom)

    # guardar el archivo
    m = open(fd, "wb")

    for i in v_lotes:
        if i.importe > prom:
            pickle.dump(i, m)

    print("Se sobre escribio el archivo binario.")
    m.close()


# ===========================================================
#               Opcion 5
# ===========================================================
def mostrar_archivo_binario(fd):
    # todos las funciones os.path reciben "fd" como parametro
    if not os.path.exists(fd):  # return True or False segun exista el archivo un te carpeta
        print("El archivo no existe:", fd)
        return  # es para cortar la funcion y no seguir trabajando

    m = open(fd, "rb")  # read binary --> lee el contenido del archivo binario
    tam = os.path.getsize(fd)   # devuelve el tamaño en bytes del archivo

    #
    # archivo(m)    [   L1              L2              L3 ]
    # bytes         0           150             300         450
    # m.tell        0           150             300


    # luego de mostrarlo agregue una línea que informe el valor
    # promedio de venta de los lotes mostrados.
    # prom = acum i.importe / cont
    acum = 0
    cont = 0

    while m.tell() < tam:

        lotecito = pickle.load(m)       # recibe como unico parametro el archivo ( m )
        # lotecito = L1,        L2,         L3

        # solo mostrar los que superficie de 5
        if lotecito.superficie > 5:
            print(lotecito)
            acum += lotecito.importe
            cont += 1

    # calcular el proemdio
    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio de importe es:", prom)

    m.close()   # OBLIGATORIO


def menu():
    print("1 - Cargar arreglo")
    print("2 - Mostrar arreglo")
    print("3 - Generar matriz")
    print("4 - Generar archivo binario")
    print("5 - Mostrar archivo binario")
    return int(input("Ingresar opcion: "))


def principal():

    v_lotes = []

    # para los puntos de archivos binarios el 4 y el 5
    fd = "lotes.dat"       # nombre del archivo

    op = -1
    while op != 0:

        op = menu()

        if op == 1:
            n = validar_n()

            # Cada vez que se ingrese en esta opción, el arreglo debe ser creado desde cero y
            # todo contenido anterior debe ser eliminado.
            v_lotes = []
            cargar_arreglo(v_lotes, n)

        elif op == 2:
            if len(v_lotes) > 0:
                mostrar_datos(v_lotes)
            else:
                print("El arreglo no esta cargado")


        elif op == 3:
            if len(v_lotes) > 0:
                # Mostrar, además, la superficie total vendida para una
                # manzana m (siendo m un valor que se ingresa por teclado).
                m = int(input("Ingresar manzana a calcular su superficie total."))
                generar_matriz(v_lotes, m)

            else:
                print("El arreglo no esta cargado")

        elif op == 4:
            if len(v_lotes) > 0:
                # todos los lotes cuyo número de lote esté comprendido entre l1 y l2
                l1 = int(input("Ingresar numero de lote a superar: "))
                l2 = int(input("Ingresar numero de lote a ser menor: "))
                generar_archivo_binario(v_lotes, fd, l1, l2)


            else:
                print("El arreglo no esta cargado")

        elif op == 5:
            mostrar_archivo_binario(fd)





if __name__ == '__main__':
    principal()
