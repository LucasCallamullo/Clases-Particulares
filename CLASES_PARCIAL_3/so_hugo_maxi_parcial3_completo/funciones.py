
import random
from registro import *


# Opcion 1
def validar_n():
    n = int(input("Cantidad de figuritas a cargar: "))  # 3
    while n <= 0:       # mientras n sea igual o menor a cero
        n = int(input("Cantidad de figuritas a cargar (DEBE SER POSITIVO): "))  # 1

    return n    # 3


def cargar_arreglo(v_figus, n):
    # pais (1, 32), num_jug (1, 19) INT, nombre STR, posicion(1, 4), importe > 0 FLOAT
    for i in range(n):      # dar 3 vuueltas osea cargamos 3 objetos
        pais = random.randint(1, 32)        # INT
        num_jug = random.randint(1, 19)        # INT
        nombre = random.choice("ABCDEF")                # STR
        posicion = random.randint(1, 4)         # INT
        importe = round(random.uniform(0.1, 10), 2)   # FLOAT

        figu = Figurita(pais, num_jug, nombre, posicion, importe)
        v_figus.append(figu)
        # v_figus = [F1, F2, F3]

    print("Se cargaron las", n, "figuritas")


# opcion 2
def ordenar_arreglo(v_figus):
    # indices       0       1       2
    # v_figus = [   F2,     F1,     F3]
    # nombre        B       C       A

    n = len(v_figus)        # 3

    for i in range(n-1):        # range(2)
        # i = 0,    1

        for j in range(i+1, n):
            # j = 1,    2
            # i = 0

            # la boquita > determina si esta ordenado de menor a mayor o mayor a menor
            if v_figus[i].nombre > v_figus[j].nombre:
                v_figus[i], v_figus[j] = v_figus[j], v_figus[i]


def mostrar_arreglo(v_figus, p):

    # Al final del listado mostrar el promedio de los importes de las figuritas mostradas
    # Promedio = Acumulado(importes) / cantidad
    acum = 0
    cont = 0

    # indices       0       1       2
    # v_figus = [   F1,     F2,     F3]
    for i in v_figus:
        # i = F1, F2, F3

        if i.pais > p:
            print(i)
            cont += 1
            acum += i.importe

    #
    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio de los importes acumulados es:", prom)


# Opcion 3
def generar_vector_conteo(v_figus, m):

    # generar vector de conteo/acum
    v_conteo = [0] * 32     # pais (1, 32)   o sea 32 contadores

    # pais         1-1 2-1 3-1  4
    # indices       0   1   2   3   4  --> estos indices referencian a cada posible pais                                                                             31
    # v_conteo = [  1,  1,  0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # rellenar el vector
    # indices       0       1       2
    # v_figus = [   F1,     F2,     F3]
    # pais          1       2       1
    for i in v_figus:
        # i = F1,    F2 , F3
        v_conteo[i.pais-1] += 1
        # v_acum[i.pais-1] += i.importe

    # mostrar el vector de conteo/acum
    for i in range(len(v_conteo)):      # range(32)
        # i = 0,    1, 2, 3, 4 ..., 31 --> estos indices referencian a cada posible pais

        # Solo mostrar los contadores qu superan m
        if v_conteo[i] > m:
            print("El pais:", i+1, "Tiene la cantidad de figuritas de:", v_conteo[i])

        # Solo mostrar los contadores qu superan 0
        if v_conteo[i] > 0:
            pass

        # Solo mostrar los pais mayores o iguales a 3  a "p":
        if i+1 >= 3:
            pass


# Opcion 4
def busqueda_secuencial(v_figus, nom):  # nom = S
    pos = -1
    # indices       0       1       2
    # v_figus = [   F1,     F2,     F3]
    # nombre         X       S       A
    for i in range(len(v_figus)):   # range(3)
        # i = 0,    1,  2
        if v_figus[i].nombre == nom and (v_figus[i].posicion == 1 or v_figus[i].posicion == 2):
            pos = i
            break   # romper ciclos     nos saca de los ciclos for

    return pos          # 0 o más  SI EXISTE        / -1 NO EXISTE
