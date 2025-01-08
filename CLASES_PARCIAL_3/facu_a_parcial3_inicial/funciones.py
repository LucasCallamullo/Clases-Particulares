

import random
from registro import *


# =======================================================================
#                       Opcion 1
# =======================================================================
def validar_n():
    n = int(input("Ingresar cantidad de teles a cargar: ")) # 3
    while n <= 0:   # mientras n sea menor o igual a CERO voy a pedir otro n
        n = int(input("Ingresar cantidad de teles a cargar: (DEBE SER POSITIVO) "))

    return n


def cargar_arreglo(v_teles, n):
    # lotes = ("Deposito 1", "Deposito 2", "Deposito 3")
    # id > 0 , marca STR, pulgadas(32, 50), importe > 0, lote(1, 3)

    # marcas = ("Hitachi", "LG", "Samsung")

    for i in range(n):      #
        id = random.randint(1, 10)
        marca = random.choice("ABCDEF")             # STR
        pulgadas = random.randint(32, 50)           # INT
        importe = round(random.uniform(0.1, 10), 2)     # Float
        lote = random.randint(1, 3)

        tv = Tele(id, marca, pulgadas, importe, lote)
        v_teles.append(tv)
        # v_teles = [Tv1, Tv2, Tv3]
    print("Se cargaron las", n, "teles.")


# =======================================================================
#                       Opcion 2
# =======================================================================
def ordenar_arreglo(v_teles):
    # indices     0    1    2
    # v_teles = [Tv2, Tv1, Tv3]
    # id          1    3    2
    n = len(v_teles)    # 3

    for i in range(n-1):    #
        # i = 0     , 1

        for j in range(i+1, n):
            # j = 1,     2
            # i = 0

            # la boquita determina si esta de menor a mayor o mayor a menor
            if v_teles[i].id > v_teles[j].id:

                v_teles[i], v_teles[j] = v_teles[j], v_teles[i]


def mostrar_arreglo(v_teles, t):

    # Mostrar cuanto es el promedio de los importes de las teles que se mostraron
    # promedio = acumulado / cantidad
    cont = 0
    acum = 0

    # indices     0    1    2
    # v_teles = [Tv2, Tv1, Tv3]

    for i in v_teles:
        # i = Tv2, Tv1, Tv3

        if i.importe > t:
            print(i)
            cont += 1
            acum += i.importe

    if cont > 0:
        prom = acum / cont
        print("El promedio de las teles que se mostraron:", prom)
    else:
        print("No se mostro nada.")