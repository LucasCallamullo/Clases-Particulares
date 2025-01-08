

import os.path
import pickle
import random
from registro import *


# =================================================================
#                   Opcion 1
# =================================================================
def validar_n():
    n = int(input("Ingresar la cantidad de vehiculos a cargar: "))
    while n <= 0:
        n = int(input("Ingresar la cantidad de vehiculos a cargar: "))
    return n


def cargar_arreglo(v_vehiculos, n):
    # marca STR , id INT > 0, tam (1, 4), tipo(0, 4), importe FLOAT

    for i in range(n):  # n = 3
        # i = 0, 1
        marca = random.choice("ABCDEF")
        id = random.randint(1, 10)
        tam = random.randint(1, 4)
        tipo = random.randint(5, 9)
        importe = round(random.uniform(0.1, 10), 2)

        auto = Vehiculo(marca, id, tam, tipo, importe)
        add_in_order(v_vehiculos, auto)


def add_in_order(v_vehiculos, auto):
    """
    Este algoritmo es siempre igual solo cambia el atributo por el que comparas
    y la "<" define si esta de menor a mayor o mayor a menor
    """

    # A1.id         3
    # A2.id         2

    # indices        0
    # v_vehiculos = [A1]
    # id             3
    izq, der = 0, len(v_vehiculos) - 1

    # izq = 0
    # der = -1

    while izq <= der:       # mientrass izq sea menor o igual a cero , ingreso al ciclo

        c = (izq + der) // 2        # c = centro
        # c = 0
        if v_vehiculos[c].id == auto.id:
            pos = c
            break
        elif v_vehiculos[c].id > auto.id:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    # indices           0   1
    # v_vehiculos = [   A2, A1]
    # id                2   3
    v_vehiculos[pos:pos] = [auto]       # no te olvides los corchetes en el objeto


# =================================================================
#                   Opcion 2
# =================================================================
def mostrar_arreglo(v_vehiculos, s1, s2):

    for i in v_vehiculos:
        # i = V1, V2, V3
        if s1 <= i.importe <= s2:
            print(i)


# =================================================================
#                   Opcion 4
# =================================================================
def generar_archivo_binario(v_vehiculos, fd, t):
    """
    # recibe dos parametros, el primero es el nombre del archivo (fd), y el segundo el modo de apertura
    # write binary, escribir en binario, sobre-escribe tod0 el contenido del archivo, y lo crea si no existiera
    # "ab" append binary, agrega contenido al final del archivo, conserva su contenido anterior, y tambien lo crea si no existe
    """
    m = open(fd, "wb")

    for i in v_vehiculos:
        # i = V1, V2, V3
        if i.importe > t and (i.tam == 3 or i.tam == 4):
            pickle.dump(i, m)   # recibir dos parametros, el primero es "m", y el segundo lo que queremos guardar(i)
            m.flush()    # opcional

    m.close()   # OBLIGATORIO


# =================================================================
#                   Opcion 5
# =================================================================
def mostrar_archivo_binario(fd):

    if os.path.exists(fd):

        m = open(fd, "rb")  # read binary, leer el archivo
        size = os.path.getsize(fd)      # nos devuelve el tamaño en bytes del archivo

        # indices   0   1   2
        # listas = [V1, V2, V3]

        # archivo = [ V1        V2          V3       V4]
        #           0     100        200       300       396

        # calcular el promedio de alquileres ( importe )
        # promedio = acumulador ( importes ) / cantidad
        acum = 0
        cont = 0

        while m.tell() < size:
            # auto = v1, v2
            auto = pickle.load(m)   # nos devuelve un objeto a la vez y mueve el puntero (tell)

            print(auto)

            if auto.tipo == 8 or auto.tipo == 9:
                acum += auto.importe
                cont += 1

        prom = 0
        if cont > 0:
            prom = acum / cont
        print("El promedio de los importes del tipo hidrogeno y electrico es:", round(prom, 2))

        m.close()   # no te lo olvides

    # No existe el archivo creado
    else:
        print("No existe el archivo:", fd)