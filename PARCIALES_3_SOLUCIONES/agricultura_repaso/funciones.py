import random
from registro import *


# Opcion 1
def cargar_vector(v_t, n):
    nombres = ("Juan", "María", "Luis", "Ana", "Pedro", "Sofía", "Carlos", "Laura", "Miguel", "Isabel",
               "Antonio", "Elena", "José", "Ana", "Fernando")
    for i in range(n):
        id = random.randint(0, 19)
        desc = random.choice(nombres)
        personas = random.randint(0, 19)
        importe = random.randint(0, 500)
        tipo = random.randint(0, 19)
        trabajo = Trabajo(id, desc, tipo, importe, personas)
        v_t.append(trabajo)


def mostrar_datos(v_t):
    # [ TRABAJO, TRABAJO, TRABJO, TRABJO ]
    # for i in range(len(v_t)):
    #    print("=" * 50)
    #    print(v_t[i])


    for i in v_t:
        print("=" * 50)
        print(i)


# Opcion 4:
def calcular_promedio(v_t):
    acum = 0
    cont = 0
    for i in v_t:
        acum += i.importe
        cont += 1

    prom = acum / cont
    return prom


def mostrar_datos_op4(v_t, prom):
    for i in v_t:
        if i.importe > prom:
            print(i)


# Opcion 2
def sort(v_t):
    n = len(v_t)
    for i in range(n-1):
        for j in range(i+1, n):
            if v_t[i].tipo < v_t[j].tipo:
                v_t[i], v_t[j] = v_t[j], v_t[i]


def cant_personas(v_t, num):
    for i in v_t:
        if i.cant_personas > num:
            print(i)


# opcion 3
def contador_trabajos(v_t):
    v_cont = [0] * 20
    # 0 19        ,   2000 2019
    for i in v_t:
        v_cont[i.tipo] += 1
    return v_cont
