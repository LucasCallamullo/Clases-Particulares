

import random

from registro import *


# ================================================================
#                       Opcion 1
# ================================================================
def cargar_arreglo(v_figuritas, n):
    # tupla_posicion = ("Arquero", "Defensor", "Mediocampista", "Delantero")
    # pais (1, 32), num_jugador ( 1, 19), nombre, posicion (1, 4), importe > 0
    for i in range(n):          # 5
        pais = random.randint(1, 4)
        num_jugador = random.randint(1, 19)
        nombre = random.choice("ABCDEF")
        posicion = random.randint(1, 4)
        importe = round(random.uniform(0.1, 10), 2)          # FLoat

        figu = Figurita(pais, num_jugador, nombre, posicion, importe)
        v_figuritas.append(figu)
        # v_figuritas = [ F1, F2, F3, F4, F5 ]

    print("Se cargaron las", n, "figuritas.")


def validar_n():
    n = int(input("Ingrese la cantidad de figuritas a cargar: "))
    while n <= 0:       # mientras n sea igual o menor a cero, voy a pedir otra n
        n = int(input("Ingrese la cantidad de figuritas a cargar (Debe ser positivo el numero): "))
    return n


# ================================================================
#                       Opcion 2
# ================================================================
def mostrar_datos(v_figuritas, x):
    # promedio = acumulado / cantidad
    cont = 0
    acum = 0

    # v_figuritas = [ F1, F2, F3 ]
    for i in v_figuritas:
        # i = F1, F2

        if i.importe > x:
            print(i)
            cont += 1
            acum += i.importe

    # Si te pidieran calcular el promedio
    if cont > 0:
        prom = acum // cont
        print("El promedio de las figuritas mostradas es:", prom)
    else:
        print("No se mostro ninguna figurita.")


def ordenar_arreglo(v_figuritas):
    n = len(v_figuritas)
    #                  0   1   2
    # v_figuritas = [ F2, F1, F3 ] # 3

    for i in range(n-1):        # 2
        # i = 0         , 1

        for j in range(i+1, n): # 3
            # j = 1     , 2
            # i = 0
            if v_figuritas[i].nombre > v_figuritas[j].nombre:       # menor a mayor
                v_figuritas[i], v_figuritas[j] = v_figuritas[j], v_figuritas[i]