

import random

# traernos todo0 el modulo de registro
from registro import *


# ===========================================================================
#                       Opcion 1
# ===========================================================================
def cargar_arreglo(v_teles, n):

    # id > 0 INT, marca STR, pulgadas (32, 50) INT, importe > 0 FLOAT
    marcas = "ABCDEF"

    for i in range(n):
        id = random.randint(1, 10)      # int
        marca = random.choice(marcas)       #
        pulgadas = random.randint(32, 50)   # int
        importe = round(random.uniform(0.1, 10), 2)   # Float
        tele = Tele(id, marca, pulgadas, importe)
        v_teles.append(tele)

    print("Se cargaron", n, "teles en el arreglo.")


# ===========================================================================
#                       Opcion 2
# ===========================================================================
def ordenar_arreglo(v_teles):
    # v_teles = [T1, T2, T3, T4 ]

    # ordenamiento por seleccion directa
    n = len(v_teles)        # 4
    for i in range(n - 1):      # 3
        # i = 0,         1, 2

        for j in range(i+1, n):     # 4
            # j = 1, 2, 3

            if v_teles[i].id > v_teles[j].id:
                v_teles[i], v_teles[j] = v_teles[j], v_teles[i]


def mostrar_arreglo(v_teles, s1, s2):
    # v_teles = [T1, T2, T3, T4 ]

    # calcular el promedio de los importes mostrados  = acum / cont
    cont = acum = 0

    for i in v_teles:
        # i = T1, T2, T3, T4
        if s1 <= i.pulgadas <= s2:
            print(i)
            cont += 1
            acum += i.importe

    if cont > 0:
        prom = acum / cont
        print("El promedio de las Teles es:", prom)

    else:
        print("No se mostro ningun arreglo")


# ===========================================================================
#                       Opcion 3
# ===========================================================================
def generar_vector_conteo(v_teles, x):
    # pulgadas (32, 50)   18 + 1 = 19

    # Crear el vector de conteo/acum
    v_conteo = [0] * 19

    # pulgadas   32 33 34 35                                            50
    # indices     0  1  2  3                                           18           32
    # v_conteo = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Rellenar el vector conteo/acum
    for i in v_teles:
        # i = T1, T2, T3 ...
        v_conteo[i.pulgadas - 32] += 1
        # v_acum[i.pulgadas-32] += i.importe

    # Mostrar el vector

    # Al final de este listado, mostrar cual es la pulgada con mayor cantidad de teles
    may = None
    pulgada = None

    for i in range(len(v_conteo)):  # 19
        # i = 0, 1, 2, 3, 4, ..., 18

        # if v_conteo[i] > 0:
        if v_conteo[i] > x:
            print("Para las pulgadas:", i + 32, "existe la cantidad de:", v_conteo[i])

        if may is None or v_conteo[i] > may:
            may = v_conteo[i]
            pulgada = i + 32

    print("La pulgada con mayor cantidad de teles es:", pulgada, "con: ", may)


# ===========================================================================
#                       Opcion 4
# ===========================================================================
def busqueda_secuencial(v_teles, x, t):
    pos = -1
    for i in range(len(v_teles)):
        # i = 0, 1, 2,
        if v_teles[i].id == x and v_teles[i].importe >= t:
            pos = i
            break
    return pos      # -1 , 0 +
