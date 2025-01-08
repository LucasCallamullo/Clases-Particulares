

import random
from registro import *


# Opcion 1
def validar_n():
    n = int(input("Ingresar cantidad de paquetes a cargar: "))  # 3
    while n <= 0:
        n = int(input("Ingresar cantidad de paquetes a cargar(DEbe ser positivo): "))

    return n


def cargar_arreglo(v_paquetes, n):
    # id > 0 INT, descripcion STR, tipo(10, 13), cantidad INT, importe > 0 FLOAT
    for i in range(n): # generar n paquetes
        id = random.randint(1, 10)      # INT
        descripcion = random.choice("ABCDEF")   # STR
        tipo = random.randint(10, 13)
        cantidad = random.randint(1, 20)
        importe = round(random.uniform(0.1, 10), 2) # FLOAT

        pack = Paquete(id, descripcion, tipo, cantidad, importe)
        v_paquetes.append(pack)
        # v_paquetes = [ P1, P2, P3 ]

    print("Se cargaron los", n, "paquetes.")


# Opcion 2:
def ordenar_arreglo(v_paquetes):
    # indices           0       1       2
    # v_paquetes = [    P2,     P1,     P3 ]
    # id                3       5        4

    n = len(v_paquetes)     # 3
    for i in range(n-1):       # range(2)
        # i = 0,        1

        for j in range(i+1, n):
            # j = 1,    2
            # i = 0

            # la boquita > define si es de menor a mayor o mayor a menor
            if v_paquetes[i].id > v_paquetes[j].id:

                v_paquetes[i], v_paquetes[j] = v_paquetes[j], v_paquetes[i]


def mostrar_arreglo(v_paquetes, d1, d2):
    # Al final del listado mostrar el promedio de los importes de los paquetes que se mostraron
    # Promedio = acumulado(de importes) / cantidad
    acum = 0
    cont = 0

    # indices           0       1       2
    # v_paquetes = [    P1,     P2,     P3 ]
    for i in v_paquetes:
        # i = P1, P2 , P3
        if d1 <= i.cantidad <= d2:
            print(i)
            cont += 1
            acum += i.importe

    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio de los importes mostrados es:", prom)