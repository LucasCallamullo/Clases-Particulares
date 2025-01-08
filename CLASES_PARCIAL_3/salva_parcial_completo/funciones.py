

import random
from registro import *


# Opcion1
def validar_n():
    n = int(input("Ingresar cantidad de figuritas a cargar: "))     # 3
    while n <= 0:       # mientras n sea igual o menor a cero
        n = int(input("Ingresar cantidad de figuritas a cargar (DEBE SER POSITIVO): "))
    return n


def cargar_arreglo(v_figuritas, n):
    # pais(1, 32) INT, num_jug (1, 19) INT, nombre STR, posicion(1, 4) INT, importe > 0 FLOAT
    for i in range(n):  # 3 vueltas
        pais = random.randint(1, 32)        # INT
        num_jug = random.randint(1, 19)     # INT
        nombre = random.choice("ABCDEF")            # STR
        posicion = random.randint(1, 4)     # INT
        importe = round(random.uniform(0.1, 10), 2)       # FLOAT

        figu = Figurita(pais, num_jug, nombre, posicion, importe)
        v_figuritas.append(figu)
        # v_figurias = [F1, F2, F3]
    print("Se cargaron las", n, "figuritas.")


# opcion 2
def ordenar_arreglo(v_figuritas):
    # indices           0       1       2
    # v_figurias = [    F2,     F1,     F3]
    # nombre            A       X       B

    #
    n = len(v_figuritas)    # 3
    for i in range(n-1):    # range(2)
        # i = 0,    1

        for j in range(i+1, n):
            # j = 1,        2
            # i = 0

            # la boquita > determina si es de menor a mayor o de mayor a menor
            if v_figuritas[i].nombre > v_figuritas[j].nombre:

                v_figuritas[i], v_figuritas[j] = v_figuritas[j], v_figuritas[i]


def mostrar_datos(v_figuritas, x):

    # Al final del listado mostrar el promedio de los importes de las figuritas mostradas
    # promedio = acumulado(de importes) / cantidad
    acum = 0
    cont = 0

    #
    # indices           0       1       2
    # v_figurias = [    F1,     F2,     F3]
    for i in v_figuritas:
        # i = F1 , F2 , F3
        if i.importe > x:
            print(i)
            cont += 1
            acum += i.importe

    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio de los importes mostrados es: ", prom)


# Opcion 3:
def generar_vector_conteo(v_figuritas, m):
    # generar vector de conteo/acum
    v_conteo = [0] * 4  # posicion(1, 4) hay 4 contadores

    #
    # posicion     1-1 2-1 3-1 4-1
    # indices       0   1   2   3  ->>> hacen referencia a cada posible posicion
    # v_conteo = [  1,  0,  0,  0]

    # rellenar el vector de conteo/acum
    # indices           0       1       2
    # v_figurias = [    F1,     F2,     F3]
    # posicion           1       2       1
    for i in v_figuritas:
        # i = F1 , F2, F3
        v_conteo[i.posicion - 1] += 1
        # v_acum[i.posicion-1] += i.importe

    # mostrar vector de conteo/acum
    for i in range(len(v_conteo)):  # range(4)
        # i = 0,     1, 2, 3  --> hacen referencia a cada posible posicion

        if v_conteo[i] > m:
            print("Para la Posicion:", i + 1, "Tengo la cantidad de figuritas de:", v_conteo[i])

        # Solo mostrar los contadores que superen una cantidad de 0
        # if v_conteo[i] > 0:

        # Solo mostrar el contador de la posicion 3
        # if i+1 == 3:


# Opcion 4
def busqueda_secuencial(v_figuritas, p):  # p = 2
    pos = -1

    # indices           0       1       2
    # v_figurias = [    F1,     F2,     F3]
    # pais              1       2       1

    for i in range(len(v_figuritas)):  #
        # i = 0, 1, 2
        if v_figuritas[i].pais == p and v_figuritas[i].posicion == 4:
            pos = i
            break  # romper ciclos

    return pos  # 0 o +    SI EXISTE   /   -1   NO EXISTE
