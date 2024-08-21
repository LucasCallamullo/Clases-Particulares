import random
from registro import *


# opcion 1
def validar_n():
    n = int(input("Ingresar cant de Servicios a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cant de Servicios a cargar(ingrese un valor positivo): "))

    return n


def cargar_arreglo(v_servicio, n):
    # tipo s = 0, 14        ; id > 0
    # def __init__(self, id, desc, tipo_s, importe, cant_p):
    descs = "ABCD"
    for i in range(n):
        id = random.randint(1, 10)
        desc = random.choice(descs)
        tipo_s = random.randint(1000, 1014)
        importe = round(random.uniform(0.1, 10), 2)
        cant_p = random.randint(1, 10)

        serv = Servicio(id, desc, tipo_s, importe, cant_p)
        v_servicio.append(serv)


# opcion 2
def ordenar(v_servicio):
    n = len(v_servicio)
    for i in range(n-1):
        for j in range(i+1, n):
            if v_servicio[i].id > v_servicio[j].id:
                v_servicio[i], v_servicio[j] = v_servicio[j], v_servicio[i]


def mostrar_datos(v_servicio):
    for i in v_servicio:
        print(i)


# opcion 3
def v_contadores_op3(v_servicio):

    # tipo_s(1000, 1014)
             #1000 1001 1002 1003
    #           0  1  2  3  4  5                              14
    # v_cont = [0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    v_cont = [0] * 15

    for i in v_servicio:
        # i = T,        T,          T
        v_cont[i.tipo_s-1000] += 1

    may = 0
    ind = 0
    for i in range(len(v_cont)):
        # i = 0 1 2 3
        if v_cont[i] > 0:
            print("Del tipo de serv:", i+1000, "hay una cantidad de:", v_cont[i])

        if v_cont[i] > may:
            may = v_cont[i]
            ind = i

    # for i in range(len(v_cont)):
    #    if v_cont[i] == may:
    #        print(v_cont[i])
    #        break

    print("El Mayor tipo de serv:", ind+1000, "hay una cantidad de:", v_cont[ind])


# opcion 4
def busqueda_lineal(v_servicio, d, p):

    for i in range(len(v_servicio)):
        # i = 0  1  2  3
        if v_servicio[i].desc == d and v_servicio[i].cant_p >= p:
            return i
    return -1
