import os.path
import pickle
import random

from registro import *



# ===================================================
#               Opcion 1
# ===================================================
def validar_n():
    n = int(input("Ingresar cantidad de pantalones a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de pantalones a cargar: "))

    return n


def cargar_arreglo(v_pantalones, n):
    # codigo INT , nombre STR, largo(30, 50), cintura(3, 7), tela(1, 3), stock INT, importe FLOAT
    for i in range(n):

        codigo = random.randint(1, 15)
        nombre = random.choice("ABCDEF")
        largo = random.randint(30, 50)
        cintura = random.randint(3, 7)
        tela = random.randint(1, 3)
        stock = random.randint(1, 10)
        importe = round(random.uniform(0.1, 10), 2)

        nuevo_pant = Pantalon(codigo, nombre, largo, cintura, tela, stock, importe)
        add_in_order(v_pantalones, nuevo_pant)


def add_in_order(v_pantalones, nuevo_pant):

    izq, der = 0, len(v_pantalones) - 1

    while izq <= der:
        c = (izq + der) // 2

        # se ordena por el atributo que pidan
        if v_pantalones[c].codigo == nuevo_pant.codigo:
            pos = c
            break

        # la boquita ">" determina si esta de menor a mayor o mayor a menor
        elif v_pantalones[c].codigo > nuevo_pant.codigo:
            der = c - 1

        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v_pantalones[pos:pos] = [nuevo_pant]    # --> el objeto va con corchetes SI O SI


# ===================================================
#               Opcion 2
# ===================================================
def mostrar_datos(v_pantalones):

    # indices           0       1       2
    # v_pantalones = [ P1,      P2,     P3]
    for i in v_pantalones:
        # i = P1, P2 , P3
        print(i)


# ===================================================
#               Opcion 3
# ===================================================
def generar_matriz(v_pantalones, u):

    # crear la matriz
    f = 5    # f = filas = cintura(3, 7) = lim_superior - lim_inferior + 1 = 7 - 3 + 1 = 5
    c = 21     # c = columnas = largo(30, 50) = lim_superior - lim_inferior + 1 = 50 - 30 + 1 = 21
    matriz = [ [0] * c for i in range(f) ]

    #
    # cintura(3, 7)    3-3  4-3   5   6   7
    # indices_fila      0   1   2   3   4

    # largo(30, 50)       30-30                     50-30
    # indices_columna =     0   1   2   3   4   ... 20

    # matriz[f][c]
    # matriz = [    [0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #               [0, 2, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]     ]

    #
    # rellenar la matriz
    for i in v_pantalones:
        # i = P1, P2, P3
        # matriz[f][c]
        matriz[i.cintura - 3][i.largo - 30] += i.stock
        # matriz[i.cintura - 3][i.largo - 30] += 1

    #
    # mostrar la matriz
    for f in range(len(matriz)):        #  range(5)
        # f = 0, 1, 2, 3, 4

        for c in range(len(matriz[0])):     # range(21)
            # c = 0, 1, 2, ..., 20

            # solo mostrar los que tengan un stock mayor a "u" o 0
            if matriz[f][c] > u:
                print("Cintura:", f+3, "| Largo:", c+30, "| Stock disponible:", matriz[f][c])

            # solo mostrar los talles de largo entre l1 y l2
            # if l1 <= c + 30 <= l2:
            #    pass # print()


# ===================================================
#               Opcion 4
# ===================================================
def generar_archivo_binario(v_pantalones, fd, t):
    m = open(fd, "wb")      # primer parametro: recibe el nombre del archivo ( fd )
                            # segundo parametro: es el modo de apertura ( "wb" )
    # wb = write binary = crea el archivo si no existe, sobre escribe todo su contenido
    # ab = append binary = crea el archivo si no existe, agrega contenido al final de archivo, conservando
    # todo su contenido anterior

    for i in v_pantalones:
        # i = P1, P2, P3

        # guardar los datos de todos los pantalones con stock disponible y cuya tela sea t
        if i.stock > 0 and i.tela == t:
            pickle.dump(i, m)   # primer parametro es lo que quiero guardar ( i )
                                # segundo parametro es donde lo quiero guardar ( m )
            m.flush()   # opcional --> guardar mejor el archivo .

    print("Se genero el archivo.")  # opcional

    m.close()   # OBLIGATORIO


# ===================================================
#               Opcion 5
# ===================================================
def mostrar_archivo_binario(fd):

    bandera = os.path.exists(fd)        # return True si existe el archivo, False  si NO EXISTE
    if bandera is False:
        print("El archivo no existe.")
        return      # corta funciones , dejo de leer a partir de aca

    m = open(fd, "rb")  # read binary -> modo de lectura
    tam = os.path.getsize(fd)       # nos dice o nos devuelve el tamaño en bytes --> 256 bytes

    # archivo = [   P1          P2  ]
    # bytes     0        128        256
    # m.tell()  0        128

    # además al final una línea extra con stock promedio de los pantalones que tuvieran una tela
    # de "JEAN" guardados en el archivo.
    # promedio = acumulador ( de stock ) / cantidad
    acum = 0
    cont = 0

    while m.tell() < tam:

        pant = pickle.load(m)   # unico parametro el archivo ( m )
        # pant = P1,    P2
        print(pant)

        if pant.tela == 1:
            acum += pant.stock
            cont += 1

    # calcular promedio
    prom = 0
    if cont > 0:
        prom = acum / cont

    print("El promedio es:", prom)

    m.close()   # OBLIGATORIO


# ===================================================
#               Opcion 6
# ===================================================
def busqueda_binaria(v_pantalones, cod):    # 5

    # indices           0       1       2
    # v_pantalones = [P1    ,   P2,     P3]
    # codigo            1       3       5

    izq, der = 0, len(v_pantalones) - 1

    while izq <= der:
        c = (izq + der) // 2

        # if v_pantalones[c].codigo == nuevo_pant.codigo:
        if v_pantalones[c].codigo == cod:
            pos = c
            # break
            return pos      #

        # elif v_pantalones[c].codigo > nuevo_pant.codigo:
        elif v_pantalones[c].codigo > cod:
            der = c - 1

        else:
            izq = c + 1

    return -1       # -1 No existe el objeto que cumple con mi busuqeda



def menu():
    print("1 - Cargar arreglo.")
    print("2 - Mostrar arreglo.")
    print("3 - Generar matriz.")
    print("4 - Generar archivo binario.")
    print("5 - Mostrar archivo binario.")
    op = int(input("Ingresar opción: "))
    return op


def principal():

    # vector / arreglo / lista de trabajo
    v_pantalones = []

    # nombre del archivo
    fd = "pantalones.dat"       # file description ; nombre del archivo

    op = -1
    while op != 0:
        op = menu()

        if op == 1:
            n = validar_n()
            cargar_arreglo(v_pantalones, n)

        elif op == 2:

            if len(v_pantalones) > 0:
                mostrar_datos(v_pantalones)

            else:
                print("El arreglo no esta cargado.")

        elif op == 3:
            """
            3 - Determinar cuál es el stock disponible por cada combinación de talle de largo y talle de cintura. 
            Mostrar únicamente las combinaciones que disponen de un stock superior a "u" unidades, siendo u un 
            valor que se ingresa por teclado
            """
            if len(v_pantalones) > 0:
                u = int(input("Ingresar cantidad de stock a superar: "))
                generar_matriz(v_pantalones, u)

            else:
                print("El arreglo no esta cargado.")

        elif op == 4:
            """
            4 - A partir del arreglo generar un archivo binario donde se incluyan los datos de todos los pantalones 
            con stock disponible y cuya tela sea t (siendo t un valor ingresado por teclado)
            """
            if len(v_pantalones) > 0:
                t = int(input("Ingresar tela a guardar: "))
                generar_archivo_binario(v_pantalones, fd, t)

            else:
                print("El arreglo no esta cargado.")

        elif op == 5:
            """
            5 - Mostrar el archivo generado en el punto anterior indicando además al final una línea 
            extra con stock promedio de los pantalones guardados en el archivo.
            """
            mostrar_archivo_binario(fd)

        elif op == 6:
            """
            6 - Buscar por un codigo "cod" y si existe hacer un duescuento del 22% y si no existe informar
            """
            cod = int(input("Ingresar codigo a buscar: "))
            pos = busqueda_binaria(v_pantalones, cod)

            if pos >= 0:
                print("datos sin actualizar:", v_pantalones[pos])

                if v_pantalones[pos].tela == 1:     # si la tela era jean
                    v_pantalones[pos].importe -= v_pantalones[pos].importe * 0.22

                print("datos actualizados:", v_pantalones[pos])

            else:   # cuando pos es - 1
                print("No existe!")


if __name__ == "__main__":
    principal()
