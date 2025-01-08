

import random
from registro import *


# ======================================================
#                   Opcion 1
# ======================================================
def cargar_arreglo(v_parlantes, n):

    tuplas = ("JBL", "Marca2")

    # colores = ("Negro", "Blanco", "Azul")
    # id > 0, Marca, Color(1, 3), importe > 0
    for i in range(n):      # 4
        # i = 0, 1, 2, 3
        id = random.randint(1, 30)    # INT
        marca = random.choice(tuplas)             # STR
        color = random.randint(1, 3)
        importe = round(random.uniform(0.1, 10), 2)     # FLoat
        parlante = Parlante(id, marca, color, importe)

        v_parlantes.append(parlante)
        # v_parlantes = [ P1, P2, P3 ]

    print(f"Se cargaron {n} parlantes en el arreglo.")


# ======================================================
#                   Opcion 2
# ======================================================
def ordenar_arreglo(v_parlantes):
    # indices          0   1   2
    # v_parlantes = [ P1, P2, P3 ]

    n = len(v_parlantes)    # 3
    for i in range(n-1):     # 2
        # i = 0         , 1

        for j in range(i+1, n): # 1 , 3
            # j = 1,         2
            # i = 0

            # menor a mayor o mayor a menor
            if v_parlantes[i].id > v_parlantes[j].id:
                v_parlantes[i], v_parlantes[j] = v_parlantes[j], v_parlantes[i]


def mostrar_datos(v_parlantes, t):

    # Al final mostrar el promedio de los importes de los parlantes que se mostraron
    # promedio = acumulado / cantidad
    cont = 0
    acum = 0

    # indices          0   1   2
    # v_parlantes = [ P1, P2, P3 ]
    for i in v_parlantes:
        # i = P1, P2, P3

        if i.importe > t:
            print(i)
            cont += 1
            acum += i.importe

    if cont > 0:
        prom = acum / cont
        print("El promedio de los parlantes mostrados es:", round(prom, 2))
    else:
        print("No se mostro nada")