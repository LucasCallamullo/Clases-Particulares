

import random
from registro import *          # que me importe todo lo que esta en registro


# ===========================================================
#                       Opcion 1
# ===========================================================
def validar_n():
    n = int(input("Ingresar cantidad de estudiantes a generar: "))
    while n <= 0:  # mientras n sea igual o menor a cero
        n = int(input("Ingresar cantidad de estudiantes a generar (Debe ser un n positivo): "))

    return n


def cargar_arreglo(n, v_est):
    nombres = ("Lucas", "Brian", "Azul")

    for i in range(n):  # 3
        # i = 0, 1, 2
        nombre = random.choice(nombres)  # lucas
        edad = random.randint(18, 25)  # incluye a los intervalos , 20
        legajo = random.randint(1, 9)
        carrera = random.randint(1, 4)
        cuota_importe = round(random.uniform(0.1, 10), 2)     # genera un decimal con 2 decimales
        est = Estudiante(nombre, edad, legajo, carrera, cuota_importe)
        v_est.append(est)

    # v_est = [Est1, Est2, Est3]


# ===========================================================
#                       Opcion 2
# ===========================================================
def ordenar_arreglo(v_est):
    """ Metodo por seleccion directa, bubble sort o ordenamiento burbuja"""
    # Nombre: Azul | Edad: 22 | Legajo: 4 | Carrera: B | cuota: 100
    # Nombre: Azul | Edad: 22 | Legajo: 9 | Carrera: A | cuota: 100
    # Nombre: Brian | Edad: 24 | Legajo: 9 | Carrera: E | cuota: 200

    # v_est = [ Est1, Est2, Est3 ]

    n = len(v_est)      # 3
    for i in range(n-1):        # 1
        # i = 0

        for j in range(i+1, n):         # 1, 2
            # j = 1

            # el atributo que quiero ordenar es el legajo
            if v_est[i].legajo > v_est[j].legajo:   # 9 > 4
                v_est[i], v_est[j] = v_est[j], v_est[i]


def mostrar_arreglo(v_est, t):
    # solamente muestra los datos de los estudiantes que superan una edad "t"

    # Mostrar al final cuantos registros/objetos se mostraron
    cont = 0

    # Mostrar el promedio de la cuota de los estudiantes que se mostraron
    acum = 0
    cont2 = 0

    for i in v_est:
        # i = Est1, Est2, Est3

        if i.edad > t:
            print(i)
            cont += 1

            # prom
            acum += i.cuota_importe
            cont2 += 1

    if cont2 != 0:
        prom = acum / cont2
        print("El promedio es:", prom)
    else:
        print("El promedio es:", 0)

    print("Se mostraron:", cont)


# ===========================================================
#                       Opcion 3
# ===========================================================
def generar_vector_acum(v_est, c, x):

    # Crear vector acum/cont
    # Edad (18, 25)             # 8 acumuladores
    v_acum = [0] * 8

    #          18 19 20 21          25
    #           0  1  2  3           7
    # v_acum = [100, 0, 0, 0, 0, 0, 0, 0]

    #            0    1      2
    # v_est = [Est1, Est2, Est3]

    # Rellenar el vector
    for i in v_est:
        # i = Est1, Est2, Est3
        v_acum[i.edad-18] += i.cuota_importe

        # Cuantos estudiantes hay registrados por cada edad
        v_acum[i.edad-18] += 1

    # Mostrar el vector
    for i in range(len(v_acum)):            # 8
        # i = 0, 1, 2, 3
        if c <= v_acum[i] <= x:
            print("Para la edad:", i+18, "Tiene un acumulado de:", v_acum[i])

        # Que supere una edad "x": 19
        if i+18 > x:
            pass

        # Que muestres los distintos de 0
        if v_acum[i] != 0:
            pass


# ===========================================================
#                       Opcion 4
# ===========================================================
def busqueda_secuencial(v_est, z):
    # v_est = [Est1, ...
    pos = -1
    for i in range(len(v_est)):
        # i = 0, 1, 2, 3, 4
        if v_est[i].legajo == z:
            pos = i
            break

    return pos