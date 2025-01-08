

import random
from registro import *


# Opcion 1
def validar_n():
    n = int(input("Ingresar la cantidad de juicios a cargar: "))    # 3
    while n <= 0:       # mientras n <= 0 pida de nuevo n
        n = int(input("Ingresar la cantidad de juicios a cargar ( DEBE SER POSTIVIO): "))
    return n


def cargar_arreglo(v_juicios, n):

    # codigo > 0 INT , descripcion STR, tipo (1, 15), cliente(1, 3), importe > 0 FLOAT
    for i in range(n):  # 3 vueltas -> 3 objetos
        codigo = random.randint(1, 10)      # INT
        descripcion = random.choice("ABCDEF")       # STR
        tipo = random.randint(1, 15)    # INT
        cliente = random.randint(1, 3)    # INT
        importe = round(random.uniform(0.1, 10), 2)   # FLOAT
        j = Juicio(codigo, descripcion, tipo, cliente, importe)
        v_juicios.append(j)
        # v_juicios = [J1, J2, J3]
    print("Se cargaron los", n, "juicios.")


# Opcion 2
def ordenar_arreglo(v_juicios):
    # indices       0       1       2
    # v_juicios = [ J2,     J1,     J3]
    # descripcion    A      X      B

    n = len(v_juicios)      # 3
    for i in range(n-1):    # range(2)
        # i = 0,    1

        for j in range(i+1, n): #
            # j = 1,  2
            # i = 0

            # la > determina si esta de menor a mayor o mayor a menor
            if v_juicios[i].descripcion > v_juicios[j].descripcion:

                v_juicios[i], v_juicios[j] = v_juicios[j], v_juicios[i]


def mostrar_datos(v_juicios, mon):

    # Al final del listado indiquen cual es el promedio de los importes qeu se mostraron
    # promedio = acumulado(los importes) / cantidad
    acum = 0
    cont = 0

    # indices       0       1       2
    # v_juicios = [ J1,     J2,     J3]
    for i in v_juicios:
        # i = J1, J2, J3

        if i.importe > mon:
            print(i)
            cont += 1
            acum += i.importe

    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio de los juicios mostrados es:", prom)


# opcion 3
def generar_vector_conteo(v_juicios, c):

    # generar el vector de conteo/acum
    v_conteo = [0] * 15     # tipo(1, 15)

    # tipo         1-1 2-1 3-1   4                                           15
    # indices       0   1   2   3   4   --> los indices hacen referencia a cada tipo posible         ... 14
    # v_conteo = [  2,  1,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # rellenar el vector
    # indices       0       1       2
    # v_juicios = [ J1,     J2,     J3]
    # tipo          1      2      1
    for i in v_juicios:
        # i = J1 , J2, J3
        v_conteo[i.tipo-1] += 1
        # v_acum[i.tipo-1] += i.importe

    #
    # mostrar datos del vector conteo/ acum
    for i in range(len(v_conteo)):      # 15
        # i = 0,    1, 2, 3, 4 --> los "i" hacen referencia a cada tipo posible

        if v_conteo[i] > c:
            print("Tipo de juicio:", i+1, "Tiene la cantidad de:", v_conteo[i])

        # solo mostrar los que superan un contador de 0
        # if v_conteo[i] > 0:

        # Solo mostrar los tipo de juicios mayores o iguales a 3
        # if i+1 >= 3:


# Opcion 4
def busqueda_secuencial(v_juicios, cod, t): # t = 2
    pos = -1
    # indices       0       1       2
    # v_juicios = [ J1,     J2,     J3]
    # tipo          1      2      1
    for i in range(len(v_juicios)): # range(3)
        # i = 0, 1, 2
        if v_juicios[i].codigo == cod and v_juicios[i].tipo == t:
            pos = i
            break   # romper ciclos

    return pos      # 0 o más SI EXISTE   /  -1  NO EXISTE