

import random
from registro import *


# Opcion 1
def validar_n():
    n = int(input("Ingresar cantidad de figuritas a cargar: "))     # 3
    while n <= 0:
        n = int(input("Ingresar cantidad de figuritas a cargar(DEBE SER POSITIVO): "))  # 0
    return n


def cargar_arreglo(v_figus, n):
    # pais (1, 32) INT, num_jug(1, 19), nombre STR, posicion(1, 4), importe > 0 FLOAT
    for i in range(n):  # range(3)
        # i = 0, 1, 2
        pais = random.randint(1, 32)    # INT
        num_jug = random.randint(1, 19)    # INT
        nombre = random.choice("ABCDEF")        # STR
        posicion = random.randint(1, 4)     # INT
        importe = round(random.uniform(0.1, 10), 2)   # FLOAT

        figu = Figurita(pais, num_jug, nombre, posicion, importe)
        v_figus.append(figu)
        # v_figus = [F1, F2, F3]
    print("Se cargaron las", n, "figuritas.")


# opcion 2:
def ordenar_arreglo(v_figus):
    # indices       0       1       2
    # v_figus = [   F2,     F1,     F3]
    # nombre        A       S      B

    n = len(v_figus)    # 3

    for i in range(n-1):    # range(2)
        # i = 0,    1

        for j in range(i+1, n):
            # j = 1,    2
            # i = 0

            # la > es la que determina si esta de menor a mayor o de mayor a menor
            if v_figus[i].nombre > v_figus[j].nombre:
                v_figus[i], v_figus[j] = v_figus[j], v_figus[i]


def mostrar_arreglo(v_figus, p):

    # Al final del listado indicar el promedio de los importes de las figuritas mostradas
    # promedio = acum(de importes) / cant
    acum = 0
    cont = 0

    # indices       0       1       2
    # v_figus = [   F1,     F2,     F3]
    for i in v_figus:
        # i = F1, F2, F3
        if i.pais > p:
            print(i)
            cont += 1
            acum += i.importe

    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio de los importes mostrados es:", prom)


# opcion 3
def generar_vector_conteo(v_figus, m):

    # generar vector de conteo
    v_conteo = [0] * 32     # pais(1, 32) 32 contadores

    # pais         1-1 2-1 3-1   4
    # indices       0   1   2   3   4  --> cada indice hace referencia a cada pais posible
    # v_conteo = [  2,  1,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # rellenar el vector conteo/acum
    # indices       0       1       2
    # v_figus = [   F1,     F2,     F3]
    # pais          1       2       1
    for i in v_figus:
        # i = F1,   F2, F3
        v_conteo[i.pais-1] += 1
        # v_acum[i.pais-1] += i.importe

    # mostrar el vector de conteo/acum
    for i in range(len(v_conteo)):  # range(32)
        # i = 0, 1, 2, 3 --> cada indice hace referencia a cada pais posible

        # Solo mostrar los que tengan un contador con una cantidad mayor a "m"
        if v_conteo[i] > m:
            print("Pais:", i+1, "Tiene la cantidad de:", v_conteo[i])

        # Solo mostrar los que tengan un contador con una cantidad mayor a 0
        if v_conteo[i] > 0:
            pass

        # Solo mostrar los paises que sean Superiores o iguales a 3 o "x":
        if i+1 >= 3:
            pass