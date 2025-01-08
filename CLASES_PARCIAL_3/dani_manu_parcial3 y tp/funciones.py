

import random
from registro import *


# ====================================================================
#                       Opcion 1
# ====================================================================
def validar_n():
    n = int(input("Ingresar cantidad de mascotas a cargar: "))      # 4
    while n <= 0:       # mientras n sea igual o menor a cero
        n = int(input("Ingresar cantidad de mascotas a cargar (SOLO UN N POSITIVO): "))

    return n


def cargar_arreglo(v_mascotas, n):
    nombres = ("Coco", "Michi", "Dante")

    # tipos = ("Perro", "Gato", "Conejo")
    # id > 0 , nombre, tipo(1, 3), importe > 0
    for i in range(n):      #
        id = random.randint(1, 10)          # INT
        nombre = random.choice("ABCDEF")          # STR
        tipo = random.randint(1, 3)         # INT
        importe = round(random.uniform(0.1, 10), 2)   # Float
        edad = random.randint(1, 10)    # INT

        mascotita = Mascota(id, nombre, tipo, importe, edad)
        v_mascotas.append(mascotita)
        # v_mascotas = [M1, M2, M3]
    print("Se cargaron", n, "mascotas.")


# ====================================================================
#                       Opcion 2
# ====================================================================
def ordenar_arreglo(v_mascotas):
    # indices        0      1       2
    # v_mascotas = [M2,     M1,     M3]
    # id            3       5       4

    n = len(v_mascotas) # 3
    for i in range(n-1):    # 2
        # i = 0,    1

        for j in range(i+1, n):
            # j = 1,     2
            # i = 0

            # esta condicion, que define la > si esta de menor a mayor o viceversa
            if v_mascotas[i].id > v_mascotas[j].id:

                v_mascotas[i], v_mascotas[j] = v_mascotas[j], v_mascotas[i]


def mostrar_arreglo(v_mascotas, t):

    # Al final del listado mostrar cuantas mascotas se mostraron
    cont = 0

    # Indicar al final El promedio de los importes de las mascotas mostradas
    # promedio = acumulado(de los importes) / cantidad
    cont = 0
    acum = 0

    # indices        0   1   2
    # v_mascotas = [M1, M2, M3]
    for i in v_mascotas:
        # i = M1, M2, M3

        if i.importe > t:
            print(i)
            cont += 1
            acum += i.importe

    if cont > 0:
        prom = acum / cont
        print("El promedio de los importes de las mascotas mostradas es:", prom)

    print("Se mostraron la cantidad de mascotas de:", cont)
