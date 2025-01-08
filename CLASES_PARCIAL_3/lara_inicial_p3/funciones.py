

import random

from registro import *


# =================================================================
#               Opcion 1
# =================================================================
def validar_n():
    n = int(input("Cantidad de Termos a cargar: ")) # 3
    while n <= 0:
        n = int(input("Cantidad de Termos a cargar: (N DEBE SER POSITIVO)"))
    return n


def cargar_arreglo(v_termos, n):
    # marca STR, capacidad(1,3), importe > 0, diametro(10cm, 30), id produccion > 0

    for i in range(n):  # range(3)
        marca = random.choice("ABCDEF")     # STR
        capacidad = random.randint(1, 3)    # INT
        importe = round(random.uniform(0.1, 10), 2) # FLOAT
        diametro = random.randint(10, 30)
        id = random.randint(1, 50)

        termo = Termo(marca, capacidad, importe, diametro, id)
        v_termos.append(termo)
        # v_termos = [T1, T2, T3]

    print("Se cargaron los", n, "Termos.")


# =================================================================
#               Opcion 2
# =================================================================
def mostrar_datos(v_termos, t):
    # al final mostrar el promedio de los termos que se mostraron
    # promedio = acumulado / cantidad
    acum = 0
    cont = 0

    # indices      0   1   2
    # v_termos = [T1, T2, T3]
    for i in v_termos:
        # i = T1, T2, T3
        if i.importe > t:
            print(i)
            cont += 1
            acum += i.importe

    if cont > 0:
        prom = acum / cont
        print("El promedio de la cantidad de termos que se mostraron:", prom)
    else:
        print("Nop se mostro nada")


def ordenar_arreglo(v_termos):
    # indices      0   1   2
    # v_termos = [T2, T1, T3]
    #             A    B    C
    n = len(v_termos)

    for i in range(n-1):  # 2
        # i = 0,         1

        for j in range(i+1, n):  # 3
            # j = 1,        2
            # i = 0

            # la > define si es de menor a mayor o de mayor a menor
            if v_termos[i].marca > v_termos[j].marca:

                v_termos[i], v_termos[j] = v_termos[j], v_termos[i]
