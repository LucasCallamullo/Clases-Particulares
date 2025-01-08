import os.path
import pickle
import random

from registro import *



# =========================================================
#                       Opcion 1
# =========================================================
def validar_n():
    n = int(input("Ingresar cantidad de pantalones a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de pantalones a cargar: "))
    return n


def cargar_arreglo(v_pantalones, n):
    # codigo INT, nombre STR, talle_largo(30, 50), talle_cintura(30, 50), tela(1, 3), stock INT
    # importe FLOAT
    for i in range(n):
        codigo = random.randint(1, 50)
        nombre = random.choice("ABCDEF")
        talle_largo = random.randint(30, 50)
        talle_cintura = random.randint(10, 13)
        tela = random.randint(1, 3)
        stock = random.randint(1, 10)
        importe = round(random.uniform(0.1, 10), 2)

        nuevo_pantalon = Pantalon(codigo, nombre, talle_largo, talle_cintura, tela, stock, importe)
        add_in_order(v_pantalones, nuevo_pantalon)


def add_in_order(v_pantalones, nuevo_pantalon):
    izq, der = 0, len(v_pantalones) - 1

    while izq <= der:

        c = (izq + der) // 2
        # es el atributo por el que te pidan ordenarlo
        if v_pantalones[c].codigo == nuevo_pantalon.codigo:
            pos = c
            break
        # la boquita ">" determina si esta de menor a mayor o mayor a menor
        elif v_pantalones[c].codigo > nuevo_pantalon.codigo:
            der = c - 1

        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v_pantalones[pos:pos] = [nuevo_pantalon]    # el objeto va entre corchetes


# =========================================================
#                       Opcion 2
# =========================================================
def mostrar_datos(v_pantalones):
    for i in v_pantalones:
        # i = P1, P2, P3
        print(i)


# =========================================================
#                       Opcion 3
# =========================================================
def generar_matriz(v_pantalones, u):

    # crear la matriz
    f = 4     # f = filas = talle_cintura(10, 13) = lim_superior - lim_inferior + 1 = 13 - 10 + 1 = 4
    c = 21    # c = columnas = talle_largo(30, 50)  = lim_superior - lim_inferior + 1 = 50 - 30 + 1 = 21
    matriz = [ [0] * c for i in range(f) ]

    # talle_cintura(10, 13) 10-10  11  12  13
    # indices de la fila    0   1   2   3

    # talle_largo(30, 50)30-30 31  32  ...     50
    # indices columnas = 0  1   2   ...     20

    # matriz =  [   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ]

    # rellena la matriz
    for i in v_pantalones:
        # i = P1, P2, P3
        # matriz[f][c]
        matriz[i.talle_cintura - 10][i.talle_largo - 30] += i.stock
        # matriz[i.talle_cintura - 10][i.talle_largo - 30] += 1

    # mostrar la matriz
    for f in range(len(matriz)):        # range(4)
        # f = 0, 1, 2, 3

        for c in range(len(matriz[0])):     # range(21)
            # c = 0, 1, 2, ..., 21

            if matriz[f][c] > u:
                print("Talle Largo:", c+30, "| Talle Cintura:", f+10, "| Cantidad Stock:", matriz[f][c])

            # solo mostrar los talles de largo entre 30 y 40
            # if l1 <= c+30 <= l2:
            #    pass


# =========================================================
#                       Opcion 4
# =========================================================
def generar_archivo_binario(v_pantalones, fd, t):

    m = open(fd, "wb")  # primer parametro es el nombre del archivo (fd)
                        # segundo parametro es el modo de apertura ("wb")
    # wb = write binary = crea el archivo si no existe, sobre escribe todo su contenido
    # ab = append binary = crea el archivo si no existe, agrega el contenido al final, conservando lo anterior

    for i in v_pantalones:
        # i = P1, P2, P3

        # stock disponible y una tela igual "t"
        if i.stock > 0 and i.tela == t:

            pickle.dump(i, m)   # primer parametro es lo que quiero guardar ( i )
                                # segundo parametro donde lo quiero guardar ( m )
            m.flush()   # opcional --> guarda mejor el archivo

    print("Se creo el archivo.")    # opcional
    m.close()   # OBLIGATORIO


# =========================================================
#                       Opcion 5
# =========================================================
def mostrar_archivo_binario(fd):

    if os.path.exists(fd) is False:
        print("El archivo no existe.")
        return      # corta la funcion

    m = open(fd, "rb")  # read binary , modo de lectura
    tam = os.path.getsize(fd)   # nos dice el tamaño en bytes   = 280

    # archivo = [ P1            P2 ]
    # bytes     0        140        280
    # m.tell    0        140        280

    # al final una línea extra con stock promedio de los pantalones cuya tela sea
    #  "Jean" o "Gabardina" guardados en el archivo.
    # promedio = acumulado ( de stock ) / cantidad de veces que acumulamos
    acum = 0
    cont = 0

    while m.tell() < tam:
        pant = pickle.load(m)   # P1,   P2
        print(pant)

        if pant.tela == 1 or pant.tela == 2:
            acum += pant.stock
            cont += 1

    # calcular promedio
    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio es:", prom)

    m.close()   # OBLIGATORIO


# =========================================================
#                       Opcion 6
# =========================================================
def busqueda_binaria(v_pantalones, cod):
    izq, der = 0, len(v_pantalones) - 1

    while izq <= der:

        c = (izq + der) // 2
        # if v_pantalones[c].codigo == nuevo_pantalon.codigo:
        if v_pantalones[c].codigo == cod:
            pos = c
            # break
            return pos
        # elif v_pantalones[c].codigo > nuevo_pantalon.codigo:
        elif v_pantalones[c].codigo > cod:
            der = c - 1

        else:
            izq = c + 1

    return -1


def menu():

    print("1 - Cargar Arreglo. ")
    print("2 - Mostrar Arreglo.")
    print("3 - Generar Matriz.")
    print("4 - Generar archivo binario.")
    print("5 - Mostrar archivo binario.")
    print("0 - Salir.")
    op = int(input("Ingresar opcion: "))
    return op


def principal():

    # arreglo / vector / lista de trabajo
    v_pantalones = []

    # nombre del archivo binario
    fd = "pantalones.dat"     # file description, nombre del archivo

    op = -1
    while op != 0:

        op = menu()

        if op == 1:
            n = validar_n()
            # Cada vez que se ingrese en esta opción, el arreglo debe ser creado desde cero
            # y tod0 contenido anterior debe ser eliminado
            v_pantalones = []
            cargar_arreglo(v_pantalones, n)

        elif op == 2:
            if len(v_pantalones) > 0:
                mostrar_datos(v_pantalones)
            else:
                print("El arreglo no esta cargado.")

        elif op == 3:
            """
            Determinar cuál es el stock disponible por cada combinación de talle de largo y talle de cintura. Mostrar
únicamente las combinaciones que disponen de un stock superior a u unidades, siendo u un valor que se ingresa
por teclado.
            """
            if len(v_pantalones) > 0:
                u = int(input("Cantidad de stock a superar: "))
                generar_matriz(v_pantalones, u)

            else:
                print("El arreglo no esta cargado.")

        elif op == 4:
            if len(v_pantalones) > 0:
                """
                4 - A partir del arreglo generar un archivo binario donde se incluyan 
                los datos de todos los pantalones con stock disponible y cuya tela sea t 
                (siendo t un valor ingresado por teclado).
                """
                t = int(input("Ingresar tela a guardar: "))
                generar_archivo_binario(v_pantalones, fd, t)

            else:
                print("El arreglo no esta cargado.")

        elif op == 5:
            """
            5 - Mostrar el archivo generado en el punto anterior indicando además 
            al final una línea extra con stock promedio de los pantalones cuya tela sea
            "Jean" o "Gabardina" guardados en el archivo.
            """
            mostrar_archivo_binario(fd)

        elif op == 6:
            """
            buscar por codigo "cod" 
            """
            cod = int(input("Ingresar codigo a buscar: "))
            pos = busqueda_binaria(v_pantalones, cod)
            if pos >= 0:
                # aumentarle su importe
                pass

            else:
                print("No existe")


if __name__ == '__main__':
    principal()
