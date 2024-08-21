

import random
from registro import *


# ===============================================
#               Opcion 1
# ===============================================
def validar_n():
    n = 0
    while n <= 0:
        n = int(input("Ingresar cantidad de arreglos a cargar: "))
    return n


def cargar_arreglo(v_paseo, n):
    # tipo (0 19)
    # def __init__(self, id, name, tipo, importe):
    nombres = ("A", "B", "C", "D", "E")
    for i in range(n):
        id = random.randint(1, 10)
        name = random.choice(nombres)
        tipo = random.randint(0, 19)
        importe = round(random.uniform(0.1, 10), 2)
        paseito = Paseo(id, name, tipo, importe)
        v_paseo.append(paseito)


# ===============================================
#               Opcion 2
# ===============================================
def ordenar(v_paseo):
    n = len(v_paseo)
    for i in range(n-1):
        for j in range(i+1, n):
            if v_paseo[i].id > v_paseo[j].id:
                v_paseo[i], v_paseo[j] = v_paseo[j], v_paseo[i]


def mostrar_datos(v_paseo):
    acum = 0
    for i in range(len(v_paseo)):
        acum += v_paseo[i].importe
        print(v_paseo[i])

    print("El acumulado total es:", round(acum, 2))


# ===============================================
#               Opcion 3
# ===============================================
def acumuladores_op3(v_paseo):
    # tipo 0 19
    #     1  2  3  4  5  6  7                                   19
    # [0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    v_acum = [0] * 20

    #
    # v_paseo = [P, P, P, P, P]
    for i in v_paseo:
        # i.tipo = 4
        # i.importe = 5
        v_acum[i.tipo] += i.importe

    print(v_acum)
    return v_acum


def mostrar_acum_op3(v_acum, c):
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(v_acum)):
        # 0 1 2 3 4
        if c < v_acum[i]:
            print("El total acumulado es", v_acum[i], "para el tipo de trabajo", i)


    # cont = -1
    # for i in v_acum:
    #    cont += 1
    #    if i > c:
    #        print("El total acumulado es", i, "para el tipo de trabajo", cont)


# ===============================================
#               Opcion 4
# ===============================================
def busqueda_secuencial(v_paseo, nom):
    n = len(v_paseo)
    for i in range(n):
        if nom == v_paseo[i].name:
            pos = i
            return pos

    return -1


 # 3- Mostrar los datos de todas las cuentas que tengan saldo negativo. Si ninguna cuenta tiene saldo
# negativo, muestre un mensaje de la forma: "Ninguna cuenta tiene saldo negativo".
def posible_del_enunciado():
    v = [0]
    existen_saldos_negativos = False
    for i in v:
        if i.saldo < 0:
            print(i)
            existen_saldos_negativos = True

    if not existen_saldos_negativos:
        print("Ninguna cuenta tiene saldo negativo")


 #  Mostrar los datos de todos los errores cuya cantidad de segundos fuera de línea esté entre los valores s1 y s2
# (ambos incluidos) que se cargan por teclado, y ordenados de menor a mayor por código de error. Indique al
# final la cantidad de errores mostrados en este listado
def posible_del_enunciado_2():
    pass
    # for i in v:
    #    if s1 <= v.segundos <= s2:
    #        pass


 # Determinar cuántos errores se produjeron en el rango de cada una de las horas posibles (24 contadores).
# Mostrar todos los conteos que sean diferentes de cero. Al final de este listado, mostrar cual fue la hora en la
# que se produjo la mayor cantidad de errores.
def posible_del_enunciado_3():
    v = [2, 8, 5, 9, 0]
    may = 0
    for i in v:
        if i > may:
            may = i










