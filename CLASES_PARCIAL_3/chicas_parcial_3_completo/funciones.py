

import random
from registro import *


# ===============================================================
#                   PUNTO 1
# ===============================================================
def cargar_arreglo(v_paseos, n):        # n = 5

    # id > 0 INT, nombre STR, tipo (0, 19) INT, importe > 0 FLOAT
    tupla_nombres = ("Lucas", "Azul", "Camila")
    nombres = "ABCDEF"

    for i in range(n):          # 5 vueltas
        id = random.randint(1, 100)   # elige un numero al azar entre ese intervalo, incluyendo los intervalos
        nombre = random.choice(tupla_nombres)       # STR
        tipo = random.randint(0, 19)
        importe = round(random.uniform(0.1, 10), 2) # FLotantes
        destino = random.randint(1, 3)
        paseito = Paseo(id, nombre, tipo, importe, destino)
        v_paseos.append(paseito)
        # v_paseos = [P1, P2, P3, P4, P5]

    print("Se cargaron correctamente los", n, "paseos.")


# ===============================================================
#                   PUNTO 2
# ===============================================================
def ordenar_arreglo(v_paseos):
    # indices      0   1   2
    # v_paseos = [P2, P1, P3]
    # id           1   3   2

    n = len(v_paseos)       # 3
    for i in range(n-1):       # range(2)
        # i = 0, 1

        for j in range(i+1, n):     #    3
            # j = 2
            # i = 0

            # esta condicion nos indice con la >
            # si es de menor a mayor o mayor a menor
            if v_paseos[i].id > v_paseos[j].id:

                v_paseos[i], v_paseos[j] = v_paseos[j], v_paseos[i]


def mostrar_arreglo(v_paseos, t):
    #             0   1   2    3
    # v_paseos = [P1, P2, P3, ..., ]        # P1 = es un objeto

    # Si les pidieran indicar cuantos paseos se mostraron al final
    cont = 0

    # Si les pidieran capaz mostrasr el promedio de los importes de todos los paseos que se mostraron
    # promedio = Acumulado(de importes) / cantidad
    cont = 0
    acum = 0

    for i in v_paseos:
        # i = P1, P2, P3, ...

        """ Si tiene que superar el importe t """
        if i.importe > t:
            print(i)
            cont += 1
            acum += i.importe

    prom = acum / cont
    print("El promedio es:", prom)

    print("Se mostraron la cantidad de paseos:", cont)


# ===============================================================
#                   PUNTO 3
# ===============================================================
def generar_vector_conteo(v_paseos, x):

    # destino( 1, 3 )

    # generar el vector - de todos los posibles "destino" en este caso
    v_conteo = [0] * 3


    # destino     1-1   2-1     3-1
    # indice      0     1       2           # c/u de los indices hace referencia a cada destino
    # v_conteo = [1,    1,      1]

    # indices      0   1   2
    # v_paseos = [P1, P2, P3]

    # rellenar el vector
    for i in v_paseos:
        # i = P1, P2, P3
        v_conteo[i.destino-1] += 1
        # v_acum[i.destino-1] += i.importe

    #
    # destino     1-1   2-1     3-1
    # indice      0     1       2           # c/u de los indices hace referencia a cada destino
    # v_conteo = [1,    1,      0]
    # mostrar el vector de conteo/acum
    for i in range(len(v_conteo)):  # 3
        # i = 0, 1, 2

        # si les piden que solo muestre los que tienen un contador mayor a cero
        # if v_conteo[i] > 0:

        if v_conteo[i] > x:
            print("Para el destino:", i+1, "Tiene la cantidad de:", v_conteo[i])

        # solo mostrar los del destino 2 y 3:
        if i+1 == 2 or i+1 == 3:
            print("Para el destino:", i + 1, "Tiene la cantidad de:", v_conteo[i])


# ===============================================================
#                   PUNTO 4
# ===============================================================
def busqueda_secuencial(v_paseos, t):  # t = 5
    # indices      0   1   2
    # v_paseos = [P1, P2, P3 ]
    # id           3   5   7

    pos = -1
    for i in range(len(v_paseos)):  # range(3)
        # i = 0, 1, 2                       # toma valores de indice

        if v_paseos[i].id == t and (v_paseos[i].destino == 1 or v_paseos[i].destino == 2):
            pos = i         # 1
            break           # romper ciclos

    return pos      # -1        /        0 o mas