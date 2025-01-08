import os.path
import pickle
import random

from registro import *


# ===========================================================================
#                           Opcion 1
# ===========================================================================
def validar_n():
    n = int(input("Ingresar cantidad de pantalones a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de pantalones a cargar: "))
    return n


def cargar_arreglo(v_pants, n):
    # codigo INT, nombre STR, largo(0, 6), cintura(1, 2), tela(1, 3), stock INT, importe FLOAT

    for i in range(n):
        codigo = random.randint(1, 10)
        nombre = random.choice("ABCDEF")
        largo = random.randint(0, 6)
        cintura = random.randint(1, 2)
        tela = random.randint(1, 3)
        stock = random.randint(1, 10)
        importe = round(random.uniform(0.1, 10), 2)

        nuevo_pant = Pantalon(codigo, nombre, largo, cintura, tela, stock, importe)
        add_in_order(v_pants, nuevo_pant)


def add_in_order(v_pants, nuevo_pant):
    # P1.codigo     3
    # P2.codigo     2

    # indices      0
    # v_pants = [ P1 ]
    #

    izq, der = 0, len(v_pants) - 1
    # izq = 0
    # der = -1

    while izq <= der:
        c = (izq + der) // 2    # c = centro = 0

        # el atributo por el que les pidan ordenar el arreglo
        if v_pants[c].codigo == nuevo_pant.codigo:
            pos = c
            break

        # la boquita ">" determinar si esta de menor a mayor o mayor a menor
        elif v_pants[c].codigo > nuevo_pant.codigo:
            der = c - 1

        else:
            izq = c + 1

    if izq > der:
        pos = izq

    # indices    0      1
    # v_pants = [P2,    P1]
    # codigo      2      3
    v_pants[pos:pos] = [nuevo_pant]     # el objeto va ENTRE CORCHETES


# ===========================================================================
#                           Opcion 2
# ===========================================================================
def mostrar_datos(v_pants):
    # indices    0      1       2
    # v_pants = [P1,    P2,     P3]
    for i in v_pants:
        # i = P1, P2, P3
        print(i)


# ===========================================================================
#                           Opcion 3
# ===========================================================================
def generar_matriz(v_pants, u):

    # crear la matriz
    f = 2   # f = filas = cintura(1, 2) = lim_superior - lim_inferior + 1 = 2 - 1 + 1 = 2
    c = 7   # c = columnas = largo(0, 6) = lim_superior - lim_inferior + 1 = 6 - 0 + 1 = 7
    matriz = [ [0] * c for i in range(f) ]

    # cintura(1, 2)  1-1  2-1
    # fila_indices      0   1

    # largo(0, 6)       0   1   2   3   4   5   6
    # columna_indices   0   1   2   3   4   5   6

    # matriz[f][c]
    # matriz = [    [0, 5, 0, 0, 0, 0, 0],
    #               [0, 5, 0, 7, 0, 0, 0]       ]

    #
    # rellenar la matriz
    for i in v_pants:
        # i = P1, P2, P3
        # matriz[f][c]
        matriz[i.cintura - 1][i.largo] += i.stock
        # matriz[i.cintura - 1][i.largo] += 1

    #
    # mostrar la matriz
    for f in range(len(matriz)):        # range(2)
        # f = 0, 1

        for c in range(len(matriz[0])):     # range(7)
            # c = 0, 1, 2, 3, 4, 5, 6

            # Mostrar únicamente las combinaciones que disponen de un stock superior a u unidades
            if matriz[f][c] > u:    #  > 0
                print("Cintura:", f+1, "| Largo:", c, "| Cantidad Stock:", matriz[f][c])

            # Solo mostrar los talle de cintura que esten entre "x1" y x2
            # if x1 <= f+1 <= x2:
            #    print("Cintura:", f + 1, "| Largo:", c, "| Cantidad Stock:", matriz[f][c])


# ===========================================================================
#                           Opcion 4
# ===========================================================================
def generar_archivo_binario(v_pants, fd, t):

    m = open(fd, "wb")  # primer parametro: nombre del archivo ( fd )
                # segundo parametro: modo de apertura ( "wb" )
    # wb = write binary = si no existe el archivo lo crea, sobre escribe todo su contenido
    # ab = append binary = si no existe el archivo lo crea, agrega contenido al final del archivo
    # conservando todo su contenido anterior

    for i in v_pants:
        # i = p1, p2 , p3

        # guardar los datos de todos los pantalones con stock disponible y cuya tela sea t
        if i.stock > 0 and i.tela == t:
            pickle.dump(i, m)   # primer parametro: que quiero guardar ( i )
                            # segundo parametro: donde lo quiero guardar ( m )
            m.flush()   # opcional --> guardar mejor el archivo

    m.close()   # OBLIGATORIO


# ===========================================================================
#                           Opcion 5
# ===========================================================================
def mostrar_archivo_binario(fd):

    bandera = os.path.exists(fd)    # retora TRUE si existe el archivo, FALSE si NO existe
    if bandera is False:    # if not bandera
        print("No existe el archivo.")
        return      # corta la funcion

    m = open(fd, "rb")  # read binary = modo de lectura
    tam = os.path.getsize(fd)   # nos devuelve el tamaño en bytes del archivo 300 bytes

    # archivo = [   P1       P2    ]
    # bytes     0       150         300
    # m.tell()  0       150         300

    # al final una línea extra con stock promedio de los pantalones del tipo de tela "Gabardina"
    # guardados en el archivo.
    # promedio = acumulado (de stock) / cantidad de veces que acumulamos
    acum = 0
    cont = 0

    while m.tell() < tam:
        pant = pickle.load(m)   # unico parametro el archivo ( m )
        # pant = P1,    P2,     P3
        print(pant)

        if pant.tela == 2:
            acum += pant.stock
            cont += 1

    # calcular promedio
    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio es:", prom)

    m.close()   # OBLIGATORIO


# ===========================================================================
#                           Opcion 6
# ===========================================================================
def busqueda_binaria(v_pants, cod):
    izq, der = 0, len(v_pants) - 1

    while izq <= der:
        c = (izq + der) // 2  # c = centro = 0

        # if v_pants[c].codigo == nuevo_pant.codigo:
        if v_pants[c].codigo == cod:
            pos = c
            # break
            return pos  # 0 o + ; la posicion donde tengo un objeto que cumple mi criterio de busqueda

        # elif v_pants[c].codigo > nuevo_pant.codigo:
        elif v_pants[c].codigo > cod:
            der = c - 1

        else:
            izq = c + 1

    return -1   # el objeto no existe que cumple mi criterio de busqueda


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

    # vector / lista / arreglo de trabajo
    v_pants = []

    # nombre del archivo
    fd = "pantalones.dat"   # file description ; nombre del archivo

    op = -1
    while op != 0:
        op = menu()

        if op == 1:
            n = validar_n()
            cargar_arreglo(v_pants, n)

        elif op == 2:
            if len(v_pants) > 0:
                mostrar_datos(v_pants)
            else:
                print("Ingresar a la opcion 1 primero.")

        elif op == 3:
            """
            3 - Determinar cuál es el stock disponible por cada combinación de talle de largo y talle de cintura. Mostrar
únicamente las combinaciones que disponen de un stock superior a u unidades, siendo u un valor que se ingresa
por teclado
            """
            if len(v_pants) > 0:
                u = int(input("Cantidad de stock a superar para mostrar: "))
                generar_matriz(v_pants, u)
            else:
                print("Ingresar a la opcion 1 primero.")

        elif op == 4:
            """
            4 - A partir del arreglo generar un archivo binario donde se incluyan los datos de todos los 
            pantalones con stock disponible y cuya tela sea t (siendo t un valor ingresado por teclado).
            """
            if len(v_pants) > 0:
                t = int(input("Ingresar tela a buscar (1, 3): "))
                generar_archivo_binario(v_pants, fd, t)
            else:
                print("Ingresar a la opcion 1 primero.")

        elif op == 5:
            """
            5 - Mostrar el archivo generado en el punto anterior indicando además al final una 
            línea extra con stock promedio de los pantalones guardados en el archivo.
            """
            mostrar_archivo_binario(fd)

        elif op == 6:
            """
            6 - Buscar por codigo "cod" un producto. si existe mostrar sus datos y si ademas su tipo de tela
            era "Jean" o "Gabardina" realizar un descuento en su importe del 22% y mostrar sus datos actualizados
            Si no existe informar con un mensaje "el producto <cod> no existe"
            """
            cod = int(input("Codigo a buscar: "))
            pos = busqueda_binaria(v_pants, cod)

            if pos >= 0:
                print("Datos sin actualizar:", v_pants[pos])

                if v_pants[pos].tela == 1 or v_pants[pos].tela == 2:
                    # realizar un descuento en su importe del 22%
                    v_pants[pos].importe -= v_pants[pos].importe * 0.22

                    # sea igual a un valor ingresado por teclado
                    # v_pants[pos].importe = float(input("ingresar nuevo valor: "))

                print("Datos actualizados:", v_pants[pos])

            else:   # pos = -1
                print("el producto", cod, "no existe")



if __name__ == "__main__":
    principal()
