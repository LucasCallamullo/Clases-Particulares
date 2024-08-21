import random
from registro import *


# ==============================================
# Opcion 1
def validar_n():
    n = int(input("Ingresar cantidad de Equipos a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de Equipos a cargar (El n debe ser positivo): "))
    return n


def cargar_arreglo(v_equipo, n):
    # importe e id > 0   ;     cand de dias tiene que ser entre 5 y 10
    # def __init__(self, id, desc, importe, cant_d):
    descripciones = ("A", "B", "C", "D")

    for i in range(n):
        id = random.randint(1, 10)
        desc = random.choice(descripciones)
        importe = round(random.uniform(0.1, 10), 2)
        cant_d = random.randint(5, 10)
        equi = Equipo(id, desc, importe, cant_d)
        v_equipo.append(equi)


# =============================
# Opcion 2
def ordenar(v_equipo):
    n = len(v_equipo)
    for i in range(n-1):
        for j in range(i+1, n):
            if v_equipo[i].importe > v_equipo[j].importe:
                v_equipo[i], v_equipo[j] = v_equipo[j], v_equipo[i]


def mostrar_datos(v_equipo, t):
    # for i in range(len(v_equipo)):
    #    if v_equipo[i].importe > t:
    #        print(v_equipo[i])

    # v_equipo [P, P, P, P
    for i in v_equipo:
        # i = P
        if i.importe > t:
            print(i)


# =========================================
# Opcion 3
def funcion_op3(v_equipo, d):
    cumple = False
    for i in v_equipo:
        if i.cant_d > d:
            print(i)
            cumple = True
            break

    # not cumple = False
    if not cumple:
        print("Ningún equipo fue alquilado por esa cantidad de días o más.")


# =========================================
# Opcion 4
def busqueda_lineal(v_equipo, c):

    for i in range(len(v_equipo)):      # 5
        # i = 0, 1, 2, 3, 4
        if v_equipo[i].desc == c:
            return i

    return -1
