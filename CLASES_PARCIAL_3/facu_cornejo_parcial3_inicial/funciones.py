

import random
from registro import *


# opcion 1
def validar_n():
    n = int(input("Ingresar la cantidad de teles a cargar:"))
    while n <= 0:   # mientras n sea menor a cero
        n = int(input("Ingresar la cantidad de teles a cargar (solo debe ingresar un valor positivo):"))
    return n


def cargar_arreglo(v_teles, n):
    # id INT > 0, marca, pulgadas(32, 42), importe > 0
    for i in range(n):      # 5
        id = random.randint(1, 5)       # int
        marca = random.choice("ABCDEF")     # str
        pulgadas = random.randint(32, 42)
        importe = round(random.uniform(0.1, 10), 2)   # float

        tv = Tele(id, marca, pulgadas, importe)
        v_teles.append(tv)
        # v_teles = [T1, T2, T3]
    print("Se ingresaron:", n, "teles.")


# opcion 2
def ordenar_arreglo(v_teles):

    # indices     0     1       2
    # v_teles = [T3,    T1,     T2]
    # id          2      7       3

    n = len(v_teles)        # tamaño = 3
    for i in range(n-1):    # range(2)
        # i = 0,    1

        for j in range(i+1, n):
            # j = 1,        2
            # i = 0

            # la boquita indica si se ordena de menor a mayor o mayor a menor
            if v_teles[i].id > v_teles[j].id:

                v_teles[i], v_teles[j] = v_teles[j], v_teles[i]


def mostrar_datos(v_teles, t):

    # Al final del listado muestre el promedio de los importes de las teles que se mostraron
    # promedio = acumulado(importes) / cantidad
    cont = 0
    acum = 0

    #
    # v_teles = [T1, T2, T3]
    for i in v_teles:
        # i = T1, T2, T3
        if i.importe > t:
            print(i)
            cont += 1
            acum += i.importe

    if cont > 0:
        prom = acum / cont
        print("El promedio de los importes de las teles mostradas es:", prom)