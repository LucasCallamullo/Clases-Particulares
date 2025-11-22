import os.path
import pickle
import random
from registro import *


# ==============================================================
#                   Opcion 1
# ==============================================================
def validar_n():
    n = int(input("INgresar valor a cargar:"))
    while n <= 0:
        n = int(input("INgresar valor a cargar:"))
    return n


def cargar_arreglo(v_pant, n):
    # codigo > 0, modelo STR, talle_largo (30, 50), talle_ancho(30, 50)
    # tela(1, 3), stock INT, precio FLOAT

    for i in range(n):      # 5
        codigo = random.randint(1, 10)
        modelo = random.choice("ABCDEF")
        talle_largo = random.randint(30, 50)
        talle_ancho = random.randint(30, 50)
        tela = random.randint(1, 3)
        stock = random.randint(1, 10)
        precio = round(random.uniform(0.1, 10), 2)          # FLOAT

        pant = Pantalon(codigo, modelo, talle_largo, talle_ancho, tela, stock, precio)

        add_in_order(v_pant, pant)

    print("Se cargaron", n, "pantalones")


def add_in_order(v_pant, pant):

    # indices    0
    # v_pant = [ P1 ]
    # pant1.codigo = 3
    # pant2.codigo = 2

    izq, der = 0, len(v_pant) - 1
    # izq = 0
    # der = -1

    while izq <= der:       # mientras izquierda sea igual o menor a derecha ingreso al ciclo
        c = (izq + der) // 2        # c = 0

        # lo unico que cambia son las condiciones segun el atributo que te pidan
        if v_pant[c].codigo == pant.codigo:
            pos = c
            break
        elif v_pant[c].codigo > pant.codigo:      # si se come al vector > es menor a mayor
            der = c - 1                         # si se come al objeto > es mayor a menor
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    #             0      1
    # v_pant = [  P2 ,     P1,   ]
    v_pant[pos:pos] = [pant]


# ==============================================================
#                   Opcion 2
# ==============================================================
def mostrar_datos(v_pant, x):

    # calculemos el promedio de los importes de los pantalones mostrados
    # promedio = sumatoria los importes / sobre la cantidad de importes
    acum = 0
    cont = 0

    # v_pant = [ P1, P2, P3 ]
    for i in v_pant:
        # i = P1, P2, P3

        # solo mostrar a todos los objetos
        # print(i)  # mostrar el objeto -->

        # solo mostrar los que tengan una cantidad de stock mayor a "x"
        if i.stock > x:
            print(i)  # mostrar el objeto -->
            acum += i.precio
            cont += 1

    # calcular promedio
    prom = 0
    if cont > 0:
        prom = acum // cont
    print("El promeido de importes:", prom)


# ==============================================================
#                   Opcion 4
# ==============================================================
def generar_archivo_binario(v_pant, fd, t):

    m = open(fd, "wb")  # primer parametro es el nombre del archivo (fd)
                        # segundo parametro es el modo de apertura "wb"
    # "wb" = write binary = sobreescribe todo el contenido del archivo
    # "ab" = append binary = conserva el contenido del archivo y agrega al final del archivo

    # recorrer la lista para cargar el archivo con las condiciones que nos pidan
    for i in v_pant:
        # i = P1, P2, P3

        #  se incluyan los datos de todos los pantalones con stock disponible y cuya tela sea t
        if i.stock > 0 and i.tela == t:

            pickle.dump(i, m)   # primer parametro es lo que quiero guardar, el objeto ( i )
                                # segundo parametro es el archivo, ( m )

    print("Se sobre escribio el archivo binario.")
    m.close()       # ES OBLIGATORIO


def generar_archivo_binario_con_promedio(v_pant, fd, t):
    """
    Guardar en un archivo binario todos los registros que superen el valor del precio promedio
    dentro del arreglo
    """
    # calcular promedio
    prom = acum = cont = 0
    for i in v_pant:
        acum += i.precio
        cont += 1
    prom = acum / cont

    #
    m = open(fd, "wb")
    for i in v_pant:
        # i = P1, P2, P3
        if i.precio > prom:
            pickle.dump(i, m)

    print("Se sobre escribio el archivo binario.")
    m.close()


# ==============================================================
#                   Opcion 5
# ==============================================================
def mostrar_archivo_binario(fd):

    bandera = os.path.exists(fd)    # return True or False segun si existe el archivo o no
                                    # os.path reciben a "fd"
    if bandera is False:
        print("El archivo no existe:", fd)
        return      # Cortar la funcion y noseguir leyendo porque no esta el archivo

    #
    # indicando además al final una línea extra con stock promedio de los pantalones guardados en el archivo.
    # promedio = sumatoria de los stocks / cantidad de los stocks sumados
    acum = 0
    cont = 0

    #
    # al final indicar cuantos pantalones se mostraron
    cont_pant = 0

    m = open(fd, "rb")      # read binary para leer el archivo
    tam = os.path.getsize(fd)       # nos devuelve el tamaño en bytes del archivo
    while m.tell() < tam:

        pant = pickle.load(m)    # recupera cada vuelta de ciclo un objeto
        # pant = P1,    P2,     P3      # son objetos dentro del archivo

        # mostrar todos los objetos guardados en el archivo
        print(pant)
        acum += pant.stock
        cont += 1

        cont_pant += 1

        # si tiene stock disponible mostrar el objeto
        # if pant.stock > 0:
        #    print(pant)
        #    acum += pant.stock
        #    cont += 1

    # calcular promedio por fuera del while
    prom = 0
    if cont > 0:
        prom = acum // cont
    print("El promedio de los stocks es:", prom)

    # mostrar cont_pant
    print("Cantidad de pantalones que se mostraron:", cont_pant)

    m.close()   # OBLIGATORIO


# ===================================================================
#                   Opccion 3
# ===================================================================
def generar_matriz(v_pant, u):

    # generar la matriz
    f = 21  # f --> filas --> talle_largo(30, 50) --> cantidad posibles de talles de largo
            # talle_largo(30, 50) = lim_superior - lim_inferior + 1 = 50 - 30 + 1 = 21

    c = 21  # c --> columnas --> talle_cintura(30, 50) --> lim_superior - lim_inferior + 1 = 50 - 30 + 1 = 21
    matriz = [ [0] * c for i in range(f) ]

    # matriz = [    [0, 0, 0],
    #               [0, 0, 0],
    #               [0, 0, 0],
    #               [0, 0, 0],
    #               [0, 0, 0]       ]

    # rellenar la matriz
    for i in v_pant:
        # i = P1, P2

        # Determinar cuál es el stock disponible por cada combinación de talle de largo y talle de cintura.
        matriz[ i.talle_largo - 30 ][ i.talle_cintura - 30 ] += i.stock

        # Determinar cuál es la cantidad de pantalones por cada combinación de talle de largo y talle de cintura.
        # matriz[i.talle_largo - 30][i.talle_cintura - 30] += 1

    # mostrar la matriz
    for f in range(len(matriz)):        # range(21)
        # f = 0, 1, 2, 3, ..., 20

        for c in range(len(matriz[0])):     # range(21)
            # c = 0, 1, 2, 3, ..., 20

            # Mostrar únicamente las combinaciones que disponen de un stock superior a u unidades
            if matriz[f][c] > u:
                print("Talle largo:", f+30, " - Talle Cintura:", c+30, " - (Acumuladores) Stock:", matriz[f][c])

            # Solo mostrar los talles de largo entre 35 y 45
            if f+30 > 35 and f+30 < 45:
                # print("Talle largo:", f+30, " - Talle Cintura:", c+30, " - (Acumuladores) Stock:", matriz[f][c])
                pass

            # Solo mostrar los talle de cintura entre l1 y l2:
            # if l1 < c+30 < l2:
                    # el print va aca despeus


# ===================================================================
#                   Opccion 3 - b
# ===================================================================

def busqueda_binaria(v_pant, cod):
    """
        Determinar si existe un codigo de producto "cod" que se cargar por teclado
        # Si existe realizar un descuento del 25% en su precio y mostrar su datos antes y despues
        # si no existe informar
        # detenerse al primer resultado
    """
    izq, der = 0, len(v_pant) - 1

    while izq <= der:
        c = (izq + der) // 2

        # if v_pant[c].codigo == pant.codigo:
        if v_pant[c].codigo == cod:
            # pos = c
            # break

            # se cumpla la condicion
            print("Datos sin cambiar:", v_pant[c])

            # descuento del 25%
            v_pant[c].precio -= v_pant[c].precio * 0.25

            print("Datos cambiados:", v_pant[c])

            return  # Cortar al primer resultado

        # elif v_pant[c].codigo > pant.codigo:
        elif v_pant[c].codigo > cod:
            der = c - 1
        else:
            izq = c + 1

    # si no existe informar
    print("No existe")


def menu():
    print(" 1 - Cargar arreglo")
    print(" 2 - Mostrar datos")
    print(" 3 - Generar Matriz")
    print(" 6 - Busqueda Binaria")
    print(" 4 - Cargar archivo binario")
    print(" 5 - Leer archivo binario")
    print(" 0 - Salir.")
    op = int(input("Ingresar opcion: "))
    return op


def principal():

    v_pant = []
    op = -1

    fd = "pantalones.dat"

    while op != 0:

        op = menu()

        if op == 1:
            n = validar_n()

            # Cada vez que se ingrese en esta opción, el arreglo debe ser creado desde cero y
            # todo contenido anterior debe ser eliminado.
            v_pant = []
            cargar_arreglo(v_pant, n)

        elif op == 2:
            if len(v_pant) == 0:
                print("El arreglo no esta cargado.")

            else:
                # solo mostrar los que tengan una cantidad de stock mayor a "x"
                x = int(input("INgresar a stock a superar: "))
                mostrar_datos(v_pant, x)

        elif op == 3:
            """ 
            Determinar cuál es el stock disponible por cada combinación de talle de largo y talle de cintura. 
            Mostrar únicamente las combinaciones que disponen de un stock superior a "u" unidades, 
            siendo u un valor que se ingresa por teclado.
            """
            if len(v_pant) == 0:
                print("El arreglo no esta cargado.")

            else:
                u = int(input("Ingresar acumlado stock a superar: "))
                generar_matriz(v_pant, u)

        elif op == 4:
            if len(v_pant) == 0:
                print("El arreglo no esta cargado.")

            else:
                t = int(input("Ingresar tela a guardar: "))
                generar_archivo_binario(v_pant, fd, t)

        elif op == 5:
            mostrar_archivo_binario(fd)

        elif op == 6:
            if len(v_pant) == 0:
                print("El arreglo no esta cargado.")

            else:
                """ 
                Determinar si existe un codigo de producto "cod" que se cargar por teclado
                # Si existe realizar un descuento del 25%
                # si no existe informar
                # detenerse al primer resultado
                
                """
                cod = int(input("INgresa codigo a buscar: "))
                busqueda_binaria(v_pant, cod)


if __name__ == '__main__':
    principal()


