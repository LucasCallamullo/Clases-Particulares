

import random

from registros import *


# =====================================================================
#                       Opcion 1
# =====================================================================
def validar_n():
    n = int(input("Ingresar cantidad de estudiantes a cargar: "))  # 4
    while n <= 0:
        n = int(input("Ingresar cantidad de estudiantes a cargar: (DEBE SER POSITIVO)"))

    return n


def cargar_arreglo(v_estudiantes, n):
    # carreras = ("Sistemas", "Civil", "Industrial", "Quimica")
    # legajo INT > 0, nombre STR, carrera(1, 4) INT, cuota a pagar - importe FLOATS > 0

    for i in range(n):  # 4
        legajo = random.randint(1, 10)  # INT
        nombre = random.choice("ABCDEF")  # STR
        carrera = random.randint(1, 4)  # INT
        importe = round(random.uniform(0.1, 10), 2)  # Float
        est = Estudiante(legajo, nombre, carrera, importe)
        v_estudiantes.append(est)

        # v_estudiantes = [Est1, Est2, ... ]

    print("se cargaron", n, "estudiantes")


# =====================================================================
#                       Opcion 2
# =====================================================================
def ordenar_arreglo(v_estudiantes):
    n = len(v_estudiantes)      # 3

    # v_estudiantes = [Est2, Est3, Est5 ]
    #                   2       3   5
    for i in range(n-1):    # 2
        # i = 0,    1

        for j in range(i+1, n):
            # j = 1, 2
            # i = 0

            # la boquita te dice es menor a mayor o mayor a menor
            if v_estudiantes[i].legajo > v_estudiantes[j].legajo:

                v_estudiantes[i], v_estudiantes[j] = v_estudiantes[j], v_estudiantes[i]


def mostrar_arreglo(v_estudiantes, x):

    # Si te pide al final mostrar el promedio de los importes de los estudiantes que se mostraron
    # promedio = acumulado / cantidad
    cont = 0
    acum = 0

    # indices            0     1     2
    # v_estudiantes = [Est2, Est3, Est5 ]
    for i in v_estudiantes:
        # i = Est2,     Est3, Est5

        if i.importe > x:
            print(i)
            cont += 1
            acum += i.importe

    prom = calcular_promedio(acum, cont)
    print("El promedio de los importes de los estudiantes mostrados es:", prom)


def calcular_promedio(acum, cont):
    prom = 0
    if cont > 0:
        prom = acum / cont
    return prom


# =====================================================================
#                       Opcion 3
# =====================================================================
def generar_vector_conteo(v_estudiantes, c):
    # generar el vector de conteo/acum
    v_conteo = [0] * 4  # carreras(1, 4) * 4

    # carreras     1-1 2-1 3-1  4-1
    # indices       0   1   2   3  --> estos indices hacen referencia a cada carrera.
    # v_conteo = [  2,  1,  0,  0 ]

    # rellenar el vector de conteo/acum
    # indices            0     1     2
    # v_estudiantes = [Est1, Est2, Est3 ]
    # carrera           1       2      1
    for i in v_estudiantes:
        # i = Est1,     Est2, Est3
        v_conteo[i.carrera - 1] += 1

    # mostrar el vector de conte/acum

    # Al final mostrar la carrera que obtuvo la mayor cantidad de estudiantes
    mayor = None
    carrera = None
    carreras = ("Sistemas", "Civil", "Industrial", "Quimica")

    for i in range(len(v_conteo)):  # range(4)
        # i = 0,    1, 2, 3        --> hacen referencia a cada carrera

        # solo mostrar los contadores que superan una cantidad "c"
        if v_conteo[i] > c:
            print("La carrera:", carreras[i], "Tiene la cantidad de:", v_conteo[i])

        # solo mostrar los contadores que superan una cantidad 0
        if v_conteo[i] > 0:
            pass

        # solo muestres las carreras mayores o iguales a 2:  a "c"
        # if i+1 >= 2:

        if mayor is None or v_conteo[i] > mayor:
            mayor = v_conteo[i]
            carrera = i + 1

    print("La carrera", carrera, "Obtuvo la mayor cantidad con:", mayor)


# =====================================================================
#                       Opcion 4
# =====================================================================
def busqueda_secuencial(v_estudiantes, t):
    pos = -1

    # indices            0     1     2
    # v_estudiantes = [Est2, Est3, Est5 ]
    for i in range(len(v_estudiantes)):  # 3
        # i = 0, 1, 2, ..

        if v_estudiantes[i].legajo == t and v_estudiantes[i].carrera == 3:
            pos = i
            break  # romper ciclos

    return pos  # -1        / 0 o más
