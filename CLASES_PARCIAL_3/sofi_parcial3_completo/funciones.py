

import random
from registro import *


# ======================================================
#                       Opcion 1
# ======================================================
def validar_n():
    n = int(input("Ingresar cantidad de errores a cargar: "))   # 0
    while n <= 0:   # mientras n sea menor o igual a cero, pedir nuevamente n
        n = int(input("Ingresar cantidad de errores a cargar (DEBE SER POSITIVO): "))   # 3
    return n


def cargar_arreglo(v_errores, n):

    # errores ( 1:"Error 404", 2:"Error 500", 3:"Error 505"
    # codigo (1000, 5000) INT, mensaje STR, hora(1, 24), importe > 0, errores(1, 3)
    for i in range(n):      # 3
        codigo = random.randint(1000, 5000)     # INT
        mensaje = random.choice("ABCDEF")       # STR
        hora = random.randint(1, 24)        # INT
        importe = round(random.uniform(0.1, 10), 2)   # Float
        errores = random.randint(1, 3)

        e = Error(codigo, mensaje, hora, importe, errores)
        v_errores.append(e)
        # v_errores = [E1, E2, E3]
    print("Se cargaron los", n, "errores.")


# ======================================================
#                       Opcion 2
# ======================================================
def ordenar_arreglo(v_errores):
    n = len(v_errores)      # 3
    # indices   =   0       1       2
    # v_errores = [E2,      E1,     E3]
    # codigo        4       5       3

    for i in range(n-1):    # range(2)
        # i = 0,         1

        for j in range(i+1, n):
            # j = 1,    2
            # i = 0

            # la boquita determina si esta de menor a mayor o mayor a menor
            if v_errores[i].codigo > v_errores[j].codigo:
                v_errores[i], v_errores[j] = v_errores[j], v_errores[i]


def mostrar_arreglo(v_errores, s1, s2):

    # Al final del listado mmostrar el promedio de los importes de los errores que se mostraron
    # promedio = acumulado(importes) / cantidad
    cont = 0
    acum = 0

    # indices   =   0   1   2
    # v_errores = [E1, E2, E3]
    for i in v_errores:         # leer el contenido del arreglo
        # i = E1, E2, E3

        if s1 <= i.hora <= s2:
            print(i)
            cont += 1
            acum += i.importe

    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio de los importes es:", round(prom, 2))


# ======================================================
#                       Opcion 3
# ======================================================
def generar_vector_conteo(v_errores):
    # generar el vector         hora(1, 24) * 24
    v_conteo = [0] * 24

    # hora(1, 24)1-1    2-1     3-1 4  5  6
    # indices     0     1       2   3  4  5 ---> indices representan a cada posible hora
    # v_conteo = [1,    1,      0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # rellenar el vector
    for i in v_errores:
        # i = E1, E2, E3
        # hora 1  2
        v_conteo[i.hora - 1] += 1
        # v_acum[i.hora-1] += i.importe

    #
    # mostrar el vector de conteo / acum

    # Al final de este listado, mostrar cual fue la hora en la
    # que se produjo la mayor cantidad de errores
    mayor = None
    hora = None

    for i in range(len(v_conteo)):  # range(24)
        # i = 0, 1, 2, ..., --> indices referencian a cada hora

        # Solo mostrar las horas que sean superiores o iguales a "x"
        # if i+1 >= 3:

        # solo mostrar los que tengan una cantidad mayor a 0, "x"
        if v_conteo[i] > 0:
            print("Para la Hora:", i + 1, "Tiene la cantidad de errores de:", v_conteo[i])

        if mayor is None or v_conteo[i] > mayor:
            mayor = v_conteo[i]
            hora = i + 1

    print("La hora:", hora, "Tuvo la mayor cantidad de errores con:", mayor)


# ======================================================
#                       Opcion 4
# ======================================================
def busqueda_secuencial(v_errores, m):
    pos = -1
    for i in range(len(v_errores)):

        # i = 0, 1, 2,
        if v_errores[i].mensaje == m:
            pos = i
            break   # romper ciclos
    return pos      # 0 o +     /  -1