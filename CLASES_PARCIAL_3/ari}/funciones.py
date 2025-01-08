

import random
from registro import *


# =========================================================================
#               Opcion 1
# =========================================================================
def cargar_arreglo(v_tablets, n):

    # marcas = 1=Apple. 2=Google. 3=OnePlus. 4=Samsung.
    # id > 0, pulgadas(8, 20), marca(1, 4), importe > 0, peso

    cadenas = ("A", "B", "C", "D", "E", "F")
    cadenas = "ABCDEF"

    for i in range(n):          # 5
        id = random.randint(1, 20)                      # INT
        pulgadas = random.randint(8, 20)                # INT
        marca = random.randint(1, 4)                    # STR
        importe = round(random.uniform(0.1, 10), 2)     # Float
        peso = round(random.uniform(0.1, 10), 2)        # Float
        # cadena_str = random.choice(cadenas)
        tablet = Tablet(id, pulgadas, marca, importe, peso)
        v_tablets.append(tablet)

    print("Se cargaron los", n, "objetos.")


# =========================================================================
#                       Opcion 2
# =========================================================================
def ordenar_arreglo(v_tablets):
    # indices   =   0   1   2   3
    # v_tablets = [T2, T1, T3, T4]

    n = len(v_tablets)      # 4
    for i in range(n-1):    # 3
        # i = 0, 1, 2

        for j in range(i+1, n):     # 1, 4
            # j = 1,         2, 3
            # i = 0
            if v_tablets[i].id > v_tablets[j].id:       # menor a mayor, si
                v_tablets[i], v_tablets[j] = v_tablets[j], v_tablets[i]


def mostrar_datos(v_tablets, t1, t2):

    # al final debe mostrar la cantidad de tablets que se mostraron
    cont = 0

    # al final debe mostrar el promedio de los precios de las tablets mostradas
    # promedio = acumulado / cantidad
    cont = 0
    acum = 0

    # indices   =   0   1   2   3
    # v_tablets = [T1, T2, T3, T4]
    for i in v_tablets:
        # i = T1, T2, T3, T4

        if t1 < i.importe < t2:
            print(i)
            cont += 1
            acum += i.importe

    # print("Se mostraron la cantidad de tablets igual a:", cont)

    if cont > 0:
        prom = acum / cont
        print("El promedio de los precios de las tablets que se mostraron fue:", prom)
    else:
        print("No se mostro ninguna tablet")


# =========================================================================
#                       Opcion 3
# =========================================================================
def generar_vector_acum(v_tablets, x):
    # Marca(1, 4) o sea que esto nos pide 4 contadores

    # generar o crear el vector de acumlacion / o conteo
    v_acum = [0] * 4

    # marca   1-1  2  3  4
    # indices   0  1  2  3
    # v_acum = [0, 0, 0, 0]

    # rellenar el vector

    #               0   1   2
    # T1.marca   2    importe 5.0
    # T2.marca   3    importe 3.5
    # T3.marca   2    importe 2.5

    # v_tablets = [T1, T2, T3]
    for i in v_tablets:
        # i = T1, T2, T3
        v_acum[i.marca - 1] += i.importe
        # v_conteo[i.marca-1] += 1

    #
    # indice    0   1    2   3
    # v_acum = [0, 7.5, 3.5, 0]

    # Mostrar el vecto de acumlacion / o de conteo
    for i in range(len(v_acum)):  # range(4)      4-1 = 3
        # i = 0, 1, 2, 3

        # solo mostrar los acumulados que tengan un acumulado superior a cero
        if v_acum[i] > x:
            print("Para la marca:", i + 1, "Su acumulado es:", v_acum[i])

        # mostrar las marcas 1:Apple y 4:Samsung
        if i + 1 == 1 or i + 1 == 4:
            pass
            # print("Para la marca:", i + 1, "Su acumulado es:", v_acum[i])

        # combinados de ambas condiciones
        if (i + 1 == 1 or i + 1 == 4) and v_acum[i] > x:
            pass
            # print("Para la marca:", i + 1, "Su acumulado es:", v_acum[i])


# =========================================================================
#                       Opcion 4
# =========================================================================
def busqueda_secuencial(v_tablets, f):      # f = 5
    pos = -1


    # T1.id         3
    # T2.id         8
    # T3.id         4

    #               0   1   2
    # v_tablets = [T1, T2, T3]

    for i in range(len(v_tablets)):     # 3 tablets range(5)
        # i = 0, 1, 2

        if v_tablets[i].id == f and v_tablets[i].marca == 4:
            pos = i     # 2
            break       # romper ciclos

    return pos  # 2         # -1    /      0 o mas que son los indices