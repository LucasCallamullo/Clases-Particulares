
import random
from registro import *


# Opcion 1
def validar_n():
    n = int(input("La cantidad de figuritas a cargar: "))   # 3
    while n <= 0:   # mientras n sea menor a cero pedimos de vuelta n
        n = int(input("La cantidad de figuritas a cargar (DEBE SER POSITIVO): "))
    return n


def cargar_arreglo(v_figus, n):
    # pais(1, 32) INT , num_jug(1, 19) INT, nombre STR, posicion(1, 4), importe > 0 Float
    for i in range(n):
        pais = random.randint(1, 32)        # INT
        num_jug = random.randint(1, 19)        # INT
        nombre = random.choice("ABCDEF")        # STR
        posicion = random.randint(1, 4)     # INT
        importe = round(random.uniform(0.1, 10), 2)   # FLOAT

        figu = Figurita(pais, num_jug, nombre, posicion, importe)
        v_figus.append(figu)
        # v_figus = [F1, F2, F3]

    print("Se cargaron las", n, "figuritas.")


# Opcion 2
def ordenar_arreglo(v_figus):
    # indices    0      1       2
    # v_figus = [F2,    F1,     F3]
    # nombre     A      X      Z

    n = len(v_figus)        # 3
    for i in range(n-1):    # range(2)
        # i = 0,        1

        for j in range(i+1, n):
            # j = 1,    2
            # i = 0

            # la boquita define si esta de menor a mayor o mayor a menor
            if v_figus[i].nombre > v_figus[j].nombre:

                v_figus[i], v_figus[j] = v_figus[j], v_figus[i]


def mostrar_arreglo(v_figus, p):

    # Al final del listado calcular el promedio de los importes de las figurtas mostradas
    # promedio = acumulado(de importes) / cantidad
    acum = 0
    cont = 0

    # indices    0      1       2
    # v_figus = [F1,    F2,     F3]
    for i in v_figus:
        # i = F1, F2, F3
        if i.pais > p:
            print(i)
            cont += 1
            acum += i.importe

    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio de los importes mostrados es:", prom)


# opcion 3
def generar_vector_conteo(v_figus, c):

    # generar el vector         # pais(1, 32) * 32 contadores
    v_conteo = [0] * 32

    #
    # pais         1-1 2-1 3-1  4   5  6
    # indices       0   1   2   3   4  5 -->  los indices representan a cada posible pais                                                                        31
    # v_conteo = [  1,  1,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # rellenar el vector
    # indices    0      1       2
    # v_figus = [F1,    F2,     F3]
    # pais       1      2       1
    for i in v_figus:
        # i = F1,   F2,     F3
        v_conteo[i.pais-1] += 1
        # v_acum[i.pais-1] += i.importe     # aca se acumula el atributo que te pidan


    # mostrar al final cual es el pais con la mayor cantidad de figuritas y su cantidad de figus
    mayor = None
    pais = None

    # Mostrar el vector de conteo/acum
    for i in range(len(v_conteo)):      # range(32)
        # i = 0,    1, 2, 3, ..., 31   --> los indices representan a cada posible pais

        if v_conteo[i] > 0:
            print("El pais:", i+1, "Tiene la cantidad de figuritas:", v_conteo[i])

        # solo mostrar los que tengan contadores mayores a "c"
        # if v_conteo[i] > c:

        # solo mostrar los que tengan contadores mayores a 0
        # if v_conteo[i] > 0:

        # Solo mostrar los pais que sean mayores a 4     -- -mayor "p"
        # if i+1 > 4:

        # mostrar al final cual es el pais con la mayor cantidad de figuritas y su cantidad de figus
        if mayor is None or v_conteo[i] > mayor:
            mayor = v_conteo[i]
            pais = i+1

    print("El pais:", pais, "fue el que tuvo la mayor cantidad con:", mayor)


def busqueda_secuencial(v_figus, nom): # B
    pos = -1
    # indices    0      1       2
    # v_figus = [F1,    F2,     F3]
    # nombre      A      B       C
    for i in range(len(v_figus)):
        # i = 0, 1, 2 ...
        if v_figus[i].nombre == nom and (v_figus[i].posicion == 1 or v_figus[i].posicion == 2):
            pos = i
            break   # romper ciclos
    return pos      # 0 o más SI EXISTE   / -1 SI NO EXISTE
