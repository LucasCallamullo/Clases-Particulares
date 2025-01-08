
import random
from registro import *


# Opcion 1
def validar_n():
    n = int(input("Ingresar cantidad de errores a cargar: "))   # 3
    while n <= 0:
        n = int(input("Ingresar cantidad de errores a cargar(DEBE SER POSITIVO): "))    # 1
    return n


def cargar_arreglo(v_errores, n):
    # codigo (1000, 5000) INT, mensaje STR, Hora ( 1 , 24 ), num_error(1, 3) , importe FLOAT
    for i in range(n):
        codigo = random.randint(1000, 5000)     # INT
        mensaje = random.choice("ABCDEF")             # STR
        hora = random.randint(1, 24)            # INT
        num_error = random.randint(1, 3)        # INT
        importe = round(random.uniform(0.1, 10), 2)  # FLOAT

        er = Error(codigo, mensaje, hora, num_error, importe)
        v_errores.append(er)

        # v_errores = [E1, E2, E3]
    print("Se cargaron los", n, "errores.")


# Opcion 2
def ordenar_arreglo(v_errores):
    n = len(v_errores)
    for i in range(n-1):
        for j in range(i+1, n):

            # La > determina si esta de menor a mayor o mayor a menor
            if v_errores[i].codigo > v_errores[j].codigo:

                v_errores[i], v_errores[j] = v_errores[j], v_errores[i]


def mostrar_arreglo(v_errores, t):

    # al final del listado determinar el promedio de los importes mostrados
    # promedio = acumlado(de los importes) / cantidad
    acum = 0
    cont = 0

    for i in v_errores:
        # i = E1, E2, E3

        # si tuviera que estar entre t1 y t2
        # if t1 <= i.importe <= t2:

        if i.importe > t:
            print(i)
            cont += 1
            acum += i.importe

    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio de los importes mostrados es:", prom)


# Opcion 3:
def generar_vector_conteo(v_errores, m):

    # generar vector de conteo/acum
    v_conteo = [0] * 24     # hora(1, 24)   24 contadores

    # hora         1-1 2-1      4    5
    # indices       0   1   2   3   4   --> los indices hacen una referencia a cada posible hora
    # v_conteo = [  1,  0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # rellenar vector de conteo/acum
    for i in v_errores:
        # i = E1, E2, E3 ...
        v_conteo[i.hora-1] += 1
        # v_acum[i.hora-1] += i.importe

    #
    # Al final de este listado, mostrar cual fue la hora en la
    # que se produjo la mayor cantidad de errores.
    mayor = None
    hora = None

    # mostrar el vector de conteo/acum
    for i in range(len(v_conteo)):      # range(24)
        # i = 0,    1, 2 .. --> los indices hacen una referencia a cada posible hora

        # solo mostrar los contadores que superen a m
        if v_conteo[i] > m:
            print("La hora:", i+1, "Tiene la cantidad de:", v_conteo[i])

        # solo mostrar los contadores que superen a 0
        if v_conteo[i] > 0:
            pass

        # mostrar solo las horas superior o iguales 4
        if i+1 >= 4:
            pass

        # calcular el mayor
        if mayor is None or v_conteo[i] > mayor:
            mayor = v_conteo[i]
            hora = i+1

    print("La hora:", hora, "Tuvo la mayor cantidad de errores:", mayor)


# Opcion 4
def busqueda_secuencial(v_errores, cod):
    pos = -1
    for i in range(len(v_errores)):
        # i = 0, 1, 2
        if v_errores[i].codigo == cod:
            pos = i
            break   # romper ciclos
    return pos  # 0 o + SI EXISTE  /  -1 NO EXISTE
