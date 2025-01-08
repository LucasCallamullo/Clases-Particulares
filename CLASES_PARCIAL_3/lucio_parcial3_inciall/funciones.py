

import random
from registro import *


# opcion 1
def validar_n():
    n = int(input("Cantidad de figuritas a cargar: "))      # 5
    while n <= 0:   # mientras la n sea igual o menor a cero
        n = int(input("Cantidad de figuritas a cargar: (DEBE SER POSITIVO): "))
    return n


def cargar_arreglo(v_figuritas, n):
    # posiciones = ("Arquero", "Defensor", "Mediocampista", "Delantero")
    # pais(1, 32) , num_jug(1, 19), nombre STR, posicion(1, 4), importe > 0

    for i in range(n):  # 5
        pais = random.randint(1, 32)        # INT
        num_jug = random.randint(1, 19)        # INT
        nombre = random.choice("ABCDEF")        # STR
        posicion = random.randint(1, 4)  # INT
        importe = round(random.uniform(0.1, 10), 2)   # FLOAT

        figu = Figurita(pais, num_jug, nombre, posicion, importe)
        v_figuritas.append(figu)
        # v_figuritas = [F1, F2, F3]
    print("Se cargaron las", n, "figuritas.")


# opcion 2
def ordenar_arreglo(v_figuritas):
    #  indices       0      1       2
    # v_figuritas = [F3,    F2,     F1]
    # nombre         A      C       B

    n = len(v_figuritas)    # 3
    for i in range(n-1):    # range(2)
        # i = 0,        1

        for j in range(i+1, n):
            # j = 2
            # i = 1

            # la > determina si es de menor a mayor o mayor a menor
            if v_figuritas[i].nombre > v_figuritas[j].nombre:

                v_figuritas[i], v_figuritas[j] = v_figuritas[j], v_figuritas[i]


def mostrar_arreglo(v_figuritas, v):
    # indicar cuantas figuritas se mostraron al final
    cont = 0

    # INdicar el promedio de los importes de las figuritas mostradas
    # Promedio = acumulado(importes) / cantidad
    cont = 0
    acum = 0

    #  indices       0      1       2
    # v_figuritas = [F1,    F2,     F3]
    for i in v_figuritas:       # solo leer el contenido de nuestro arreglo
        # i = F1, F2, F3

        if i.importe > v:
            print(i)
            cont += 1
            acum += i.importe

    if cont > 0:
        prom = acum / cont
        print("El promedio de los importes que se mostraron:", round(prom, 2))

    print("Se mostraron la cantida de figuritas de:", cont)


# opcion 3
def generar_vector_conteo(v_figuritas, c):

    # generar el vector     # pais(1, 32)
    v_cont = [0] * 32       # por cada posible pais

    # pais     1-1 2-1  3   4   5   6                                                                               32
    # indices   0   1   2   3   4   5   6  ... --> estos indices representan a cada posible pais                   31
    # v_cont = [0,  1,  1,  0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # rellenar el vector
    #  indices       0      1       2
    # v_figuritas = [F1,    F2,     F3]
    # pais           2       3       2
    for i in v_figuritas:
        # i = F1, F2, F3
        v_cont[i.pais-1] += 1
        # v_acum[i.pais-1] += i.importe

    #
    # mostrar el vector de conteo/acum
    for i in range(len(v_cont)):        # 32
        # i = 0,     1, 2, 3, ..., 31

        if v_cont[i] > c:
            print("Para el pais:", i+1, "tiene la cantidad de figuritas de:", v_cont[i])

        # solo mostrar del pais 5 al 15:
        # if 5 <= i+1 <= 15:
        #    pass


# opcion 4
def busqueda_secuencial(v_figuritas, j):    # j = 5
    pos = -1

    #  indices       0      1       2
    # v_figuritas = [F1,    F2,     F3]
    # num_jug         1     5       2
    for i in range(len(v_figuritas)):
        # i = 0,    1,      2
        if v_figuritas[i].num_jug == j and (v_figuritas[i].posicion == 1 or v_figuritas[i].posicion == 2):
            pos = i         # 1
            break       # romper ciclos

    return pos      # 0 o más       / -1 es porque no existe