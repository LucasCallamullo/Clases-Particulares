import random
from registro import *


# ===========================================================================
#               Opcion 1
# ===========================================================================
def validar_n():
    n = int(input("Cantidad de teles a cargar: "))
    while n <= 0:       # mientras la n sea igual o menor a cero
        n = int(input("Ingrese un valor positivo a cargar: "))
    return n


def cargar_arreglo(n, v_teles):

    marcas = ("Hitachi", "LG", "Samsung")

    for i in range(n):       # 5
        id = random.randint(1, 10)          # Int
        marca = random.choice(marcas)           # Str
        precio = round(random.uniform(0.1, 10), 2)    # Float
        pulgadas = random.randint(32, 50)
        tv = Tele(id, marca, precio, pulgadas)
        v_teles.append(tv)

        # v_teles = [tv0, tv1, tv2, tv3, tv4]


# ===========================================================================
#               Opcion 2
# ===========================================================================
def ordenar_arreglo(v_teles):
    n = len(v_teles)        # 5

    #              0    1    2    3    4
    # v_teles = [tv2, tv0, tv1, tv3, tv4]

    # id = 3, id = 4, id= 5, id= 10, id= 7

    for i in range(n-1):     # 4
        # 0, 1       2, 3

        #        range(start, stop)
        for j in range(i+1, n):     # 5
            # 2, 3, 4
            # si la i se come a la j, es de menor a mayor
            # si la j se come a la i, es de mayor a menor
            if v_teles[i].id > v_teles[j].id:           # la orientacion de la boquita

                v_teles[i], v_teles[j] = v_teles[j], v_teles[i]


def mostrar_datos(v_teles, t):
    cont = 0

    for i in v_teles:   # lista
        # i = tv0, tv1, tv2, tv3, tv4
        if i.id > t:
            print(i)
            cont += 1

    print("Se mostraron:", cont)
