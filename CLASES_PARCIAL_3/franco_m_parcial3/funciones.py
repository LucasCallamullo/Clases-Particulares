

import random


# que me traiga desde registro.py el * t odo
from registro import *


# =======================================================================
#           Opcion 1
# =======================================================================
def validar_n():
    n = int(input("Cantidad de estudiantes a cargar: "))
    # generemos un ciclo while donde solo el usuario puede permitir entrar un "n" positivo
    while n <= 0:       # mientras n sea igual o menor a cero
        n = int(input("Cantidad de estudiantes a cargar (DEBE SER POSITIVO): "))
    return n


def cargar_arreglo(v_estudiantes, n):
    # Legajo , Nombre (str) , Carrera ( 1, 4 ), cuota importe > 0 ( float )
    # def __init__(self, legajo, nombre, carrera, importe):
    nombres = "ABCDEF"
    for i in range(n):      # 5
        legajo = random.randint(1, 1000)
        nombre = random.choice(nombres)
        carrera = random.randint(1, 4)
        importe = round(random.uniform(0.1, 10), 2)     # esto es para flotantes
        est = Estudiante(legajo, nombre, carrera, importe)
        v_estudiantes.append(est)
    # return v_estudiantes


# =======================================================================
#           Opcion 2
# =======================================================================
def mostrar_arreglo(v_estudiantes, t, t2):
    # al final mostrar el promedio de los importes de las cuotas
    cont, acum = 0, 0

    for est in v_estudiantes:
        # v_estudiantes = [ Est1, Est2, Est3, Est4, Est5 ]
        # i = Est1, Est2, Est3
        if t < est.importe < t2:
            print(est)
            cont += 1
            acum += est.importe

    if cont != 0:
        prom = acum // cont
        print("El promedio es:", prom)
        # print(f"El promedio es: {prom}")
    else:
        print("No existe un promedio o no hay estudiantes")


def ordenar_arreglo(v_estudiantes):
    """ Metodo de ordenamiento por seleccion directa """
    n = len(v_estudiantes)      # 5

    # v_estudiantes = [ Est3, Est2, Est1, Est4, Est5 ]
    for i in range(n-1):            # 4 : 0, 1 , 2 ,3
        # i : 1
        for j in range(i+1, n):     # i: 0  ;  j : 4
            # se define ordenado por ascendente o descendente por el ">" , "<"
            if v_estudiantes[i].legajo > v_estudiantes[j].legajo:
                v_estudiantes[i], v_estudiantes[j] = v_estudiantes[j], v_estudiantes[i]


# =======================================================================
#           Opcion 3
# =======================================================================
def generar_vector_conteo(v_estudiantes, x):

    # carrera(1, 4)

    # Crear el vector de conteo
    v_conteo = [0] * 4

    # carrera    1-1 2-1  3  4
    # indices     0  1  2  3
    # v_conteo = [1, 2, 0, 0]

    # Rellenar el vector de conteo
    # i =
    # Est1, carrera 2
    # Est2, carrera 1
    # Est3  carrera 2
    for i in v_estudiantes:
        # i = Est1, Est2, Est3
        v_conteo[i.carrera-1] += 1

        # cuando a vos te pidan un vector que acumule los importe de las cuotas por cada carrera
        # v_acum[i.carrera-1] += i.importe

    #
    # Mostrar el vector que generaste
    tupla_carreras = ("Sistemas", "Civil", "Industrial", "Quimica")

    # carreras    1  2  3  4
    # indices     0  1  2  3
    # v_conteo = [1, 2, 3, 1]
    for i in range(len(v_conteo)):      # 4
        # i = 0, 1, 2, 3

        # lo de que supere "x" que es la cantidad de estudiantes por carrera
        if v_conteo[i] > x:
            pass

        if (i+1 == 3 or i+1 == 4) and v_conteo[i] > x:
            print("La cantidad de estudiantes es:", v_conteo[i], "para la carrera:", tupla_carreras[i])
        # si te piden que solo muestres en este caso las carreras de 3:Industrial y 4:Quimica


# =======================================================================
#           Opcion 4
# =======================================================================
def busqueda_secuencial(v_estudiantes, leg):
    pos = -1

    # indices            0    1     2
    # v_estudiantes = [Est1, Est2, Est3 ]
    for i in range(len(v_estudiantes)):
        # i = 0     , 1, 2,
        if v_estudiantes[i].legajo == leg and v_estudiantes[i].carrera == 1:
            pos = i
            break

    return pos      # -1    /    0  o  +
