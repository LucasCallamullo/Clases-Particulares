

import os.path
import pickle
import random


def opcion6(fd):    # nombre del archivo

    bandera = os.path.exists(fd)
    if bandera is False:
        print("No existe el archivo.")
        return

    m = open(fd, "rb")
    tam = os.path.getsize(fd)

    f = 2  # f = filas = pago(1, 2)
    c = 7  # c = columnas = tipo(0, 6)
    matriz = [[0] * c for i in range(f)]

    while m.tell() < tam:
        env = pickle.load(m)
        matriz[env.pago - 1][env.tipo] += 1
    m.close()

    for f in range(len(matriz)):
        for c in range(len(matriz[0])):

            if matriz[f][c] > 0:
                print("Forma de Pago:", f + 1, "| Tipo de Envio:", c, "| Cantidad:", matriz[f][c])

    return matriz


def opcion7(matriz):
    # totalizar filas
    for f in range(len(matriz)):
        suma = 0

        for c in range(len(matriz[0])):
            suma += matriz[f][c]

        print("Forma de Pago:", f + 1, "| Cantidad:", suma)

    # totalizar columnas
    for c in range(len(matriz[0])):
        suma = 0

        for f in range(len(matriz)):
            suma += matriz[1][0]

        print("Tipo de Envio:", c, "| Cantidad:", suma)



def calc_prom_op8(fd):
    bandera = os.path.exists(fd)
    if bandera is False:
        print("No existe el archivo.")
        return

    m = open(fd, "rb")
    tam = os.path.getsize(fd)

    acum, cont = 0, 0

    while m.tell() < tam:
        env = pickle.load(m)
        # env = E1, E2
        importe = env.calcular_importe()    # retorna el importe final de ese objeto de esa vuelta ciclo
        acum += importe
        cont += 1

    prom = 0
    if cont > 0:
        prom = acum / cont

    m.close()

    return prom


def opcion8(fd, prom):
    bandera = os.path.exists(fd)
    if bandera is False:
        print("No existe el archivo.")
        return

    m = open(fd, "rb")
    tam = os.path.getsize(fd)

    v_envios = []

    while m.tell() < tam:
        env = pickle.load(m)
        # env = E1, E2
        importe = env.calcular_importe()  # retorna el importe final de ese objeto de esa vuelta ciclo

        if importe > prom:
            add_in_order(v_envios, env)

    m.close()

    for i in v_envios:
        print(i)


def add_in_order(v_envios, env):
    izq, der = 0, len(v_envios) - 1
    pos = 0

    while izq <= der:
        c = (izq + der) // 2
        if v_envios[c].codigo == env.codigo:
            pos = c
            break
        elif v_envios[c].codigo >= env.codigo:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v_envios[pos:pos] = [env]


def main():

    fd = "archivo.dat"

    matriz = None

    op = -1
    while op != 0:
        op = 5

        if op == 1:
            pass

        elif op == 6:
            matriz = opcion6(fd)

        elif op == 7:
            if matriz is None:
                print("Ingrese a la op6")
            else:
                opcion7(matriz)

        elif op == 8:
            prom = calc_prom_op8(fd)
            opcion8(fd, prom)




