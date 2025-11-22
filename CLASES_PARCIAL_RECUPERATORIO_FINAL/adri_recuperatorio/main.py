import os.path
import pickle
import random

# from registro import *
# Alquiler

import registro
# registro.Alquiler


# =================================================================
#                   Opcion 1
# =================================================================
def validar_n():
    n = int(input("Ingresar cantidad de alquileres a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de alquileres a cargar: "))
    return n    # 3


def cargar_arreglo(n):
    v = []

    nombre1 = ("CoD.", "Fortnite.", "Among Us.", "League of Legends.", "Minecraft.")
    nombres = ("Lucas.", "Matias.", "Ariana.")

    # nombre_juego STR, nombre STR, tipo (0, 4) INT, mes (1, 12), monto FLOAT, stock INT
    for i in range(n):  # vamos a dar 3 vueltas
        nombre_juego = random.choice(nombre1)
        nombre = random.choice(nombres)         # STR
        tipo = random.randint(10, 14)     # INT
        mes = random.randint(1, 12)     # INT
        monto = round(random.uniform(0.1, 10), 2)   # FLOAT
        stock = random.randint(1, 10)

        juego = registro.Alquiler(nombre_juego, nombre, tipo, mes, monto, stock)
        add_in_order(v, juego)

    print("se cargo el arreglo con la cantidad de alquileres de:", n)
    return v        # lista cargada


def add_in_order(v, juego):
    izq, der = 0, len(v) - 1
    pos = 0

    while izq <= der:

        c = (izq + der) // 2

        # la condicion es lo unico que cambia
        # segun el atributo por el que nos pidan ordenar
        if v[c].nombre_juego == juego.nombre_juego:
            pos = c
            break

        # la orientacion de la boquita indica el order de menor a mayor o mayor a menor
        elif v[c].nombre_juego > juego.nombre_juego:
            der = c - 1

        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v[pos:pos] = [juego]


# =================================================================
#                   Opcion 2
# =================================================================
def mostrar_arreglo(v_alquileres):
    """
        Mostrar todos los alquileres del arreglo, a razón de un registro por línea, solo mostrar los
    alquileres que posean un monto superior a cero, en vez de mostrar su tipo de juego numerico
    muestre su descripción
    """

    # indices           0   1   2   3
    # v_alquileres = [ A1,  A2, A3, A4 ]
    n = len(v_alquileres)       # 4
    for i in range(n):
        # i = 0,            1, 2, 3

        # v_alquileres[i]       ---> apuntamos al primer objetop

        print(v_alquileres[i])

        # solo mostrar los alquileres que posean un monto superior a cero
        # if v_alquileres[i].monto > 0:
        #    print(v_alquileres[i])


# =================================================================
#                   Opcion 3
# =================================================================
def generar_matriz(v_alquileres):
    """
     A partir del arreglo, determinar por cada tipo de juego y mes de publicación,
     el monto acumulado (60 acumuladores). Mostrar solo los valores de los acumuladores mayores cero.
    """

    # generar matriz
    f = 5    # f = filas = tipo(10, 14) = lim_superior - lim_inferior + 1 =  14 - 10 + 1 = 5
    c = 12    # c = columnas = mes(1, 12) = 12 - 1 + 1 = 12
    matriz = [ [0] * c for i in range(f) ]

    # matriz[f][c]  # a modo practico se accede al reves a como cremos la matriz

    # tipo(10, 14)  =   10-10  11  12  13  14
    # f(0, 4)       =   0   1   2   3   4

    # mes(1, 12)    =   1-1   2   3   ...
    # c(0, 11)      =   0   1   2

    # [     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]        ]

    #
    # rellenar la matriz
    for i in range(len(v_alquileres)):
        # i = 0, 1, 2, 3, ...
        # v_alquileres[i]  --> hacía referencia a un objeto

        fila = v_alquileres[i].tipo - 10        # tipo 11 --> fila 1
        columna = v_alquileres[i].mes - 1       #

        # determinar por cada tipo de juego y mes de publicación, el monto acumulado (60 acumuladores)
        matriz[fila][columna] += v_alquileres[i].monto

        # determinar cuantos alquileres hay por cada tipo de juego y mes de publicación
        # matriz[fila][columna] += 1

    #
    # mostrar la matriz
    # m1 = int(input("Ingresar mes a superar: "))
    # m2 = int(input("Ingresar mes a ser menor: "))

    for f in range(len(matriz)):        # 5
        # f = 0, 1, 2, 3, 4

        for c in range(len(matriz[0])):     # 12
            # c = 0, 1, 2, 3, ..., 11

            # Mostrar solo los valores de los acumuladores mayores cero.
            if matriz[f][c] > 0:
                print("Tipo:", f+10, " - Mes:", c+1, " - Acumulado:", matriz[f][c])

            # Mostrar solo los valores de meses entre m1 y m2 (ambos incluido) que se cargar por teclado
            # if m1 <= c+1 <= m2:
                # print("Tipo:", f + 10, " - Mes:", c + 1, " - Acumulado:", matriz[f][c])


# =================================================================
#                   Opcion 4
# =================================================================
def generar_archivo_binario(fd, v_alquileres):
    """
    A partir del arreglo, generar un archivo binario donde se incluyan los datos de
    todos los alquileres de aquellos juegos con el nombre de juego "nom" que se cargar por teclado
    se ingresa por teclado.
    """
    nom = input("Ingresar nombre de juego a guardar: ")   # str

    m = open(fd, "wb")      # primer paramtro: el nombre del archivo ( fd )
                            # segundo parametro: modo de apertura ( "wb" )

    for i in range(len(v_alquileres)):
        # v_alquileres[i]   --> objeto

        # los datos de todos los alquileres de aquellos juegos con el nombre de juego "nom"
        if v_alquileres[i].nombre_juego == nom:

            pickle.dump(v_alquileres[i], m)     # el primer parametro es lo que quiero guardar ( v_alquileres[i] )
                                                # el segundo parametro: el archivo ( m )

    m.close()   # OBLIGATORIO


def generar_archivo_binario_con_promedio(fd, v_alquileres):
    """
        A partir del arreglo, generar un archivo binario donde se incluyan los datos de
    todos los alquileres que superan el monto promedio de todos los alquileres en el arreglo

        # primero deberia calcular el promedio de montos de mi arreglo
        # segundo guardar el archivo con los montos promedio
    """
    # calcular promedio de montos
    # promedio = sumatoria ( de montos )  //  cantidad de veces que sume
    acum = cont = 0

    for i in range(len(v_alquileres)):
        acum += v_alquileres[i].monto
        cont += 1

    prom = 0
    if cont > 0:
        prom = acum / cont

    print("El promedio es:", prom)

    # generar el archivo
    m = open(fd, "wb")

    for i in range(len(v_alquileres)):

        if v_alquileres[i].monto > prom:
            pickle.dump(v_alquileres[i], m)

    m.close()


# =================================================================
#                   Opcion 5
# =================================================================
def mostrar_archivo_binario(fd):

    bandera = os.path.exists(fd)    # return True si existe, False si no existe
    if not bandera:      # las funciones de os.path reciben de parametro a "fd"
        print("el archivo no existe:", fd)
        return  # cortar la funcion

    m = open(fd, "rb")      # read binary , leer el archivo
    tam = os.path.getsize(fd)   # obtiene la cantidad de bytes del tamaño del archivo

    #
    # archivo = [   A1              A2              A3  ]
    # bytes     0           150         300             450
    # m.tell()  0           150         300

    # Al final del listado indicar el monto promedio del de los registros mostrados.
    # promedio = sumatoria ( de montos ) // cantidad de veces que sume
    acum = 0
    cont = 0

    while m.tell() < tam:
        juego = pickle.load(m)  # recuperar un objeto distinto cada vuelta de ciclo
        # juego = A2        -->> mi variable "juego" hace referencia a mi objeto

        # mostrar los objetos dentro del archivo
        print(juego)
        acum += juego.monto
        cont += 1

    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El monto promedio es:", round(prom, 2))

    m.close()


# =================================================================
#                   Opcion 6
# =================================================================
def busqueda_binaria(v_alquileres):
    """
        si lo encuentra mostrar el registro, actualizar el monto de dicho alquiler en
        un nuevo monto que se ingresa por teclado y mostrar nuevamente el registro actualizado

        Si me piden buscar el mismo atributo por el que esta ordenado en mi punto 1
        es SI O SI busqueda binaria
    """
    nom = input("Ingresar nombre de juego a buscar: ")

    izq, der = 0, len(v_alquileres) - 1
    while izq <= der:

        c = (izq + der) // 2
        # v_alquileres[c] ---> hace referencia al objeto

        # if v_alquileres[c].nombre_juego == juego.nombre_juego:
        if v_alquileres[c].nombre_juego == nom:
            # pos = c
            # break

            # mostrar datos antes de realizar cambios
            print("antes de cambios:", v_alquileres[c])

            # modificar el monto por un valor que se carga por teclado
            v_alquileres[c].monto = int(input("Ingresar nuevo monto: "))

            # mostrar datos despues de realizar cambios
            print("despues del cambio:", v_alquileres[c])

            return  # cortar la funcion, para detenerse al primer resultado

        # elif v_alquileres[c].nombre_juego > juego.nombre_juego:
        elif v_alquileres[c].nombre_juego > nom:
            der = c - 1

        else:
            izq = c + 1

    # Sino existe indicar con un mensaje debe poner le mensaje "No existe bla bla".
    print("No existe bla bla.")


# =================================================================
#                   Opcion 7
# =================================================================
def busqueda_secuencial(v_alquileres):
    """
        Determinar si existe un alquiler para el nombre de persona "nom" pero que no sea
        del mes de diciembre, si existe realizar en aumento del 25% a su monto, mostrar datos antes y despues
        del cambio

        Si me piden buscar un atributo DISTINTO por el que esta ordenado en mi punto 1
        es SI O SI busqueda secuencial
    """
    nom = input("Ingresar nombre de persona a buscar: ")

    for i in range(len(v_alquileres)):
        # i = 0, 1, 2, 3
        # v_alquileres[i]  ---> objeto

        if v_alquileres[i].nombre == nom:

            # mostrar datos antes de realizar cambios
            print("antes de cambios:", v_alquileres[i])

            # realizar un aumento del 25% a su monto
            v_alquileres[i].monto += v_alquileres[i].monto * 0.25

            # realizar un descuento del 10% a su monto
            # v_alquileres[i].monto -= v_alquileres[i].monto * 0.10

            # mostrar datos despues de realizar cambios
            print("despues del cambio:", v_alquileres[i])

            # solo mostrar si existe su nombre de juego y tipo
            print("nombre juego:", v_alquileres[i].nombre_juego, "- tipo", v_alquileres[i].tipo)

            return  # cortar la funcion, para detenerse al primer resultado


def menu():
    # ctrl + d
    print("1 - Cargar arreglo")
    print("2 - Mostrar arreglo")
    print("3 - Matriz")
    print("4 - Generar archivo binario")
    print("5 - Mostrar archivo binario")
    print("6 - Busqueda Binaria")
    print("7 - Busqueda Secuencial")
    x = int(input("Ingresar opcion: "))
    return x


def principal():

    # vector - arreglo - lista - array
    v_alquileres = []       # list()

    fd = "alquileres.dat"     # file description --> nombre del archivo

    op = -1
    while op != 0:  # mientras op sea distinto ingresamos al ciclo while

        op = menu()

        if op == 1:
            n = validar_n()     # 3
            v_alquileres = cargar_arreglo(n)        # v_alquileres = lista cargada

        elif op == 2:
            # if len(v_alquileres) == 0:
            if v_alquileres:
                mostrar_arreglo(v_alquileres)
            else:
                print("El arreglo no esta cargado.")

        elif op == 3:
            if v_alquileres:
                generar_matriz(v_alquileres)
            else:
                print("El arreglo no esta cargado.")

        elif op == 4:
            if v_alquileres:
                generar_archivo_binario(fd, v_alquileres)
            else:
                print("El arreglo no esta cargado.")

        elif op == 5:
            mostrar_archivo_binario(fd)

        elif op == 6:
            if v_alquileres:
                busqueda_binaria(v_alquileres)
            else:
                print("El arreglo no esta cargado.")

        elif op == 7:
            if v_alquileres:
                busqueda_secuencial(v_alquileres)
            else:
                print("El arreglo no esta cargado.")


if __name__ == '__main__':
    principal()

