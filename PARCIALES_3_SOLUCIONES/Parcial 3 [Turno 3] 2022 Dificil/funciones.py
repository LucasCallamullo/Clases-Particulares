import random
from registro import *


# ===============================================
# Opcion 1
def validar_n():
    n = 0
    while n <= 0:
        n = int(input("Ingresar cantidad de arreglos a cargar: "))

    return n


def cargar_arreglo(v_error, n):
    # hora (0 23)    cod_errror entre 1000 y 5000
    # def __init__(self, cod_error, num_sist, mensaje, hora, segundos):
    mensajes = ("A", "B", "C", "D")

    for i in range(n):
        cod_error = random.randint(1000, 5000)
        num_sist = random.randint(1, 3)
        mensaje = random.choice(mensajes)
        hora = random.randint(1, 3)
        segundos = random.randint(0, 59)
        er = Error(cod_error, num_sist, mensaje, hora, segundos)
        v_error.append(er)


# =================================
# Opcion 2
def ordenar_cod_error(v_error):
    n = len(v_error)
    for i in range(n-1):
        for j in range(i+1, n):
            if v_error[i].cod_error > v_error[j].cod_error:
                v_error[i], v_error[j] = v_error[j], v_error[i]


def mostrar_datos_op2(v_error, s1, s2):
    # v_error =  0  1  2  3
    # v_error = [E, E, E, E]

    # for i in range(len(v_error)):   # 4
        # i = 0, 1, 2, 3
        # print(v_error[i])

    cont = 0

    for i in v_error:
        # i = E, E
        if s1 <= i.segundos <= s2:
            print(i)
            cont += 1

    print("La cantidad de errores mostrados fue:", cont)


# ===================================
# Opcion 3
def completar_contadores_op3(v_error):
    # hora  =   100         123
    # i.hora =  0  1  2  3  4  5  6                                                  23
    # v_cont = [0, 0, 1, 2, 3, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    v_conteo = [0] * 24
    may = 0
    for i in v_error:
        v_conteo[i.hora-1] += 1

    for i in range(len(v_conteo)):  # 24
        # i = 0 1 2 3 4 5 6 ... 23
        if v_conteo[i] > 0:
            print("En la hora", i+1, " hubieron la siguiente cantidad de errores:", v_conteo[i])

        if v_conteo[i] > may:
            may = v_conteo[i]

    # may    =  3
    for i in range(len(v_conteo)):  # 24
        # i = 0 1 2 3 4 5 6 ... 23
        if v_conteo[i] == may:
            print("La hora con más errores fue:", i)
            # que solamente mostraras una hora con la mayor cantidad
            break


# =========================================
# Opcion 4
def busqueda_lineal(v_error, num, des):
    for i in range(len(v_error)):
        if v_error[i].num_sist == num and v_error[i].mensaje == des:
            return i
    return -1

