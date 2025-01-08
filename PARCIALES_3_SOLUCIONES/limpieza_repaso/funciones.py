import random
from registro import *


# =================================================================================
#                               Opcion 1                                          #
# =================================================================================
def validar_n():
    n = int(input("Ingrese cantidad de Trabajos a agregar."))
    while n <= 0:       #
        n = int(input("Ingrese cantidad de Trabajos a agregar(Ingresar un valor positivo)."))
    return n


def cargar_arreglo(v_trabajo, n):
    # tipo_t = un valor de 1 a 4, 0: interior, 1: exterior, 2: piletas, 3: tapizados
    # id e importe > 0
    # def __init__(self, id, desc, tipo_t, importe, cant_p):
    descripciones = ("A", "B", "C", "D")

    for i in range(n):
        id = random.randint(1, 10)
        desc = random.choice(descripciones)
        tipo_t = random.randint(1, 4)
        # Elegir valores flotantes
        importe = round(random.uniform(1, 10), 2)
        cant_p = random.randint(1, 5)
        trabajito = Trabajo(id, desc, tipo_t, importe, cant_p)
        # agregar elementos a la lista
        v_trabajo.append(trabajito)


# =================================================================================
#                               Opcion 2                                          #
# =================================================================================
def ordenar(v_trabajo):
    n = len(v_trabajo)
    for i in range(n-1):
        for j in range(i+1, n):
            if v_trabajo[i].importe < v_trabajo[j].importe:
                v_trabajo[i], v_trabajo[j] = v_trabajo[j], v_trabajo[i]


def mostrar_datos(v_trabajo, t):
    # v_trabajo = [ T, T, T, T ]
    for i in v_trabajo:
        # i = T ,   T,          T
        if i.importe > t:
            print(i)


# =================================================================================
#                               Opcion 3                                          #
# =================================================================================
def calcular_mayor_op3(v_trabajo):
    may = 0
    # v_trabajo = [ T, T, T ]
    # determine el may, la mayor cant de personas que tiene algun registro/objeto del arreglo/lista/vector
    for i in v_trabajo:
        # i = T,    T,      T
        if i.cant_p > may:
            may = i.cant_p

    # may = la mayor cantidad de personas

    # v_trabajo = [ T , T 2, T 1 ]
    for i in v_trabajo:
        # T
        if i.cant_p == may:
            print(i)
            break


# =================================================================================
#                               Opcion 4                                          #
# =================================================================================
def busqueda_lineal(v_trabajo, d, t):
    #               0   1   2
    # v_trabajo = [ T , T , T ]
    # tamaño, size, longitud, len(v_trabajo)
    for i in range(len(v_trabajo)):
        # i = 0 1 2    ...
        if v_trabajo[i].desc == d and v_trabajo[i].importe > t:
            return i

    return -1


# =================================================================================
#                               Opcion 5                                          #
# =================================================================================
def v_contadores_op5(v_trabajo):
    # i.tipo_t
    # tipo_t (1, 4)
    # tipo_t      1  2  3  4
    #             0  1  2  3
    # v_conteo = [0, 2, 1, 0]

    v_conteo = [0] * 4

    for i in v_trabajo:
        # v_trabajo = [ T , T , T ]
        # i = T     T       T
        #
        v_conteo[i.tipo_t-1] += 1

    # v_conteo = [0, 2, 1, 0]
    for i in range(len(v_conteo)):
        # i = 0 1 2 3
        if v_conteo[i] > 0:
            tipo_str = tipo_t_to_str(i+1)
            print("Del tipo_t:", tipo_str, "hay una cantidad de:", v_conteo[i])
