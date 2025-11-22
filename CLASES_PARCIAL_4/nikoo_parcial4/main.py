import os.path
import pickle
import random

from registro import *


# ========================================================================
#               Opcion 1
# ========================================================================
def validar_n():
    n = int(input("Cantidad de piezas a cargar: "))
    while n <= 0:      # mientras n sea igual o menor a cero ingresar al while
        n = int(input("Cantidad de piezas a cargar (VALOR POSITIVO): "))
    return n


def cargar_arreglo(v_piezas, n):
    # id INT > 0 ; descripcion STR; tipo (0, 19) ; sector (10, 12) ; stock INT ; precio FLOAT
    for i in range(n):      # crear la cantidad exacta que pide el usuario
        # si n vale 3 damos 3 vueltas

        id = random.randint(1, 10)      # INT
        descripcion = random.choice("ABCDEF")   # STR
        tipo = random.randint(0, 19)    # INT
        sector = random.randint(10, 12)    # INT
        stock = random.randint(1, 10)    # INT
        precio = round(random.uniform(0.1, 10), 2)    # FLOAT

        piezita = Pieza(id, descripcion, tipo, sector, stock, precio)
        add_in_order(v_piezas, piezita)

    print("Se cargaron", n, "cantidad de piezas.")


def add_in_order(v_piezas, piezita):

    # indices           0
    # v_píezas = [ piezita1 ]
    # piezita1.id = 3
    # piezita2.id = 2

    izq, der = 0, len(v_piezas) - 1
    # izq = 0
    # der = -1

    while izq <= der:
        c = (izq + der) // 2    # c = 0

        # lo unico cambia son las condiciones segun porque atributo te pidan ordenar
        if v_piezas[c].id == piezita.id:
            pos = c
            break

        # esta boquita determina si esta de menor a mayor o de mayor a menor
        elif v_piezas[c].id > piezita.id:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    # indices           0       1
    # v_píezas = [ piezita2, piezita1 ]
    v_piezas[pos:pos] = [piezita]


# ========================================================================
#               Opcion 2
# ========================================================================
def mostrar_datos(v_piezas, x):

    # indices       0   1   2
    # v_píezas = [ P1,  P2, P3 ]
    for i in v_piezas:
        # i = P1, P2, P3   # la "i" vale como un objeto

        # Solo mostrar los que sean mayor o igual a un stock "x" que se carga por teclado
        if i.stock >= x:
            pass
            # print(i)

        # de forma que en cada línea se agregue un mensaje indicando "Stock reducido" si
        # la cantidad en stock de la pieza mostrada es inferior al valor "x"
        # Si la cantidad en stock es mayor io igual a x entonces no muestre mensaje
        # alguno para esa pieza.
        if i.stock < x:
            print(i, "Stock Reducido")
        else:
            print(i)

    """
    # por si te sirve otro tipo de for
    #
    # indices       0   1   2
    # v_píezas = [ P1,  P2, P3 ]
    for i in range(len(v_piezas)):      # range(3)
        # i = 0,    1, 2       # la "i" vale como indice

        # comprar el stock
        if v_piezas[i].stock < x:
            pass
    """

# ========================================================================
#               Opcion 3
# ========================================================================
def generar_matriz(v_piezas):

    # generar matriz
    # tipo(0, 19) -> cantidad total posible de tipos -> lim_superior - lim_inferior + 1 = 19 - 0 + 1 = 20
    # sector(10, 12) -> lim_superior - lim_inferior + 1 = 12 - 10 + 1 = 3
    c = 20  # c --> columns --> tipo(0, 19)
    f = 3   # f --> filas --> sector(10, 12)
    matriz = [ [0] * c for i in range(f) ]

    # [ [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    ]

    # la forma de acceso a cada cont/acum es al reves a como puse c f y al crearlo
    # o sea en este caso primero a la fila y despues la columna

    # rellenar la matriz
    for i in v_piezas:
        # i = P1,   P2,     P3,     P4 ...

        # Determinar el valor acumulado en stock por tipo de pieza y sector de almacenamiento
        matriz[i.sector-10][i.tipo] += i.stock      # matriz de acumulacion

        # Determinar la cantidad de piezas por cada combinacion de tipo y sector
        # matriz[i.sector - 10][i.tipo] += 1          # matriz de conteo

    #
    # mostrar la matriz
    for f in range(len(matriz)):        # range(3) elementos
        # f = 0,    1, 2

        for c in range(len(matriz[0])):     # range(20) elementos
            # f = 0
            # c = 0, 1, 2, 3, ..., 19

            # Mostrar únicamente los acumuladores que sean mayores a cero.
            if matriz[f][c] > 0:
                print("Sector:", f+10, " - Tipo:", c, " - Stock acum:", matriz[f][c])

            # Solo mostrar los tipos de pieza entre 1 y 5 ambos incluidos
            if 1 <= c <= 5:
                # print("Sector:", f + 10, " - Tipo:", c, " - Stock acum:", matriz[f][c])
                pass

            # solo mostrar un sector "p" que se carga por teclado
            # if f+10 == p:


# ========================================================================
#               Opcion 3 - b
# ========================================================================
def busqueda_binaria(v_piezas, cod):
    # determinar si existe el codigo de identifacion "cod" que se carga por teclado
    # y mostrar todos sus datos si existe y realizar un descuento del 25% a su precio
    # si no existe informar
    # debe detener la busqueda al primer resultado

    izq, der = 0, len(v_piezas) - 1

    while izq <= der:
        c = (izq + der) // 2  # c = 0

        # if v_piezas[c].id == piezita.id:
        if v_piezas[c].id == cod:
            # pos = c   # tampoco va
            # break     # tampoco va
            # esta condicion es cuando existe

            # mostrar todos sus datos si existe
            # print(v_piezas[c])

            # mostrar cambios antes y despues y realizar un descuento del 25%
            print("Datos sin cambios:", v_piezas[c])

            # descuento del 25% al precio
            v_piezas[c].precio -= v_piezas[c].precio * 0.25

            # ingresar un nuevo precio por teclado
            # v_piezas[c].precio = int(input("Ingresar nuevo precio: "))

            print("Datos cambiados:", v_piezas[c])

            # solo mostrar su descripcion y su precio
            print("Descripcion:", v_piezas[c].descripcion, " - Precio", v_piezas[c].precio)

            return      # detenerse al primer resultado

        # elif v_piezas[c].id > piezita.id:
        elif v_piezas[c].id > cod:
            der = c - 1
        else:
            izq = c + 1

    # si no existe informar
    print("No existe esa pieza con ese codigo:", cod)


# ========================================================================
#               Opcion 4
# ========================================================================
def generar_archivo_binario(v_piezas, fd, j1, j2, desc):

    # A partir del arreglo generar un archivo binario donde se incluyan
    # los datos de todas las piezas cuyo tipo de pieza este entre j1 y j2 que son valores que
    # se cargan por teclado y que sea de la descripcion "desc" que se carga por teclado

    m = open(fd, "wb")  # primero parametro es el nombre del archivo
                        # segundo parametro es el modo de apertura ( "Write binary" )

    for i in v_piezas:
        # i = P1,   P2,     P3

        # A partir del arreglo generar un archivo binario donde se incluyan
        # los datos de todas las piezas cuyo tipo de pieza este entre j1 y j2 (ambos incluids) que son valores que
        # se cargan por teclado y que sea de la descripcion "desc" que se carga por teclado

        # if i.tipo >= j1 and i.tipo <= j2:
        if j1 <= i.tipo <= j2 and i.descripcion == desc:
            pickle.dump(i, m)   # primero es lo que quiero guardar ( el objeto -> i )
                                # segundo parametro es el archivo ( m )

    print("Se genero el archivo binario.")
    m.close()       # OBLIGATORIO


# ========================================================================
#               Opcion 5
# ========================================================================
def mostrar_archivo_binario(fd):

    bandera = os.path.exists(fd)    # las funciones del modulo os.path reciben a "fd"
                                    # retorna True or False segun exista o no el archivo en tu carpeta

    if not bandera:     # if bandera is False:  # if not bandera:
        print("No existe el archivo:", fd)
        return      # cortar la funcion

    m = open(fd, "rb")      # rb -> read binary -> leer el archivo
    tam = os.path.getsize(fd)       # retorna el tamaño en bytes del archivo

    # indicando además al final una línea extra con la cantidad en stock promedio de todas las piezas mostradas.
    # prom = sumatoria stock / la cantidad de veces que sumamos
    acum = 0
    cont = 0

    #
    # piezas.dat        =   [   P1             P2                 P3 ]
    # bytes                 0           150             300          450
    # m.tell()              0           150

    while m.tell() < tam:

        piezita = pickle.load(m)    #  unico parametro el archivo en cuestion ( "m" )
        # piezita = P1

        # solo mostrar los objeto que tengan un precio mayor a cero
        if piezita.precio > 0:
            print(piezita)
            acum += piezita.stock
            cont += 1

    # calcular promedio
    prom = 0
    if cont > 0:
        prom = acum / cont

    print("el promedio de stock es:", prom)

    m.close()       # OBLIGATORIO


def menu():
    # ctrl + d
    print("1 - Cargar arreglo")
    print("2 - Mostrar arreglo")
    print("3 - Matriz")
    print("3-b - Busqueda Binaria")
    print("4 - Generar archivo binario ")
    print("5 - Mostrar arhivo binario ")
    print("0 - Salir. ")
    op = int(input("Ingresar opcion: "))        # 5
    return op


def principal():

    v_piezas = []

    fd = "piezas.dat"   # nombre del archivo binario

    op = -1
    while op != 0:

        op = menu()     # op = 5

        if op == 1:
            n = validar_n()     # 3
            cargar_arreglo(v_piezas, n)

        elif op == 2:
            if len(v_piezas) == 0:
                print("El arreglo no esta cargado.")
            else:
                x = int(input("Ingresar cantidad de stock a superar: "))
                mostrar_datos(v_piezas, x)

        elif op == 3:
            if len(v_piezas) == 0:
                print("El arreglo no esta cargado.")
            else:
                generar_matriz(v_piezas)

        elif op == 6:
            if len(v_piezas) == 0:
                print("El arreglo no esta cargado.")
            else:
                # determinar si existe el codigo de identifacion "cod" que se carga por teclado
                # y mostrar todos sus datos si existe y realizar un descuento del 25% a su precio
                # si no existe informar
                # debe detener la busqueda al primer resultado
                cod = int(input("Ingresar id a buscar: "))
                busqueda_binaria(v_piezas, cod)

        elif op == 4:
            if len(v_piezas) == 0:
                print("El arreglo no esta cargado.")
            else:
                # A partir del arreglo generar un archivo binario donde se incluyan
                # los datos de todas las piezas cuyo tipo de pieza este entre j1 y j2 que son valores que
                # se cargan por teclado y que sea de la descripcion "desc" que se carga por teclado
                j1 = int(input("Ingresar tipo de pieza a superar: "))
                j2 = int(input("Ingresar tipo de pieza a ser menor: "))
                desc = input("Ingresar descripcion a guardar: ")

                generar_archivo_binario(v_piezas, fd, j1, j2, desc)

        elif op == 5:
            mostrar_archivo_binario(fd)


if __name__ == '__main__':
    principal()







