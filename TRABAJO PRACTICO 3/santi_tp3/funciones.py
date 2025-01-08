

import os.path
from envio import *


def validar_rango(inf, sup, msj):
    valor = int(input(msj))
    while sup < valor or valor < inf:
        print("El valor ingresado no es correcto. Intente nuevamente.")
        valor = int(input(msj))
    return valor


def validar_mayor(inf, msj):
    valor = int(input(msj))
    while valor <= inf:
        print("El valor ingresado no es correcto. Intente nuevamente.")
        valor = int(input(msj))
    return valor


def cargar_desde_archivo(v, tc, fd):
    if not os.path.exists(fd):
        print('El archivo', fd, 'no existe...')
        print('Revise..')
        return

    pr = True
    m = open(fd, "rt")
    for line in m:
        if pr is True:
            if "SC" in line:
                tc = "SC"
            pr = False

        else:
            cp = line[0:9].strip().upper()
            direccion = line[9:29].strip()
            tipo = int(line[29])
            pago = int(line[30])

            env = Envio(cp, direccion, tipo, pago)
            v.append(env)

    m.close()
    return tc


def opcion1(v, tc, fd):
    if len(v) != 0:
        r = int(input("¿Desea borrar los datos previos? (1: Si - 2: No (volver al menu): "))
        if r == 1:
            v = []
            tc = cargar_desde_archivo(v, tc, fd)
            print("Carga terminada...")
        else:
            print("Carga cancelada... El arreglo mantiene los datos que contenia...")
    else:
        tc = cargar_desde_archivo(v, tc, fd)
        print("Carga terminada...")

    print()
    return v, tc


def opcion2(v):
    m = validar_mayor(0, "Cuantos registros quiere agregar al arreglo (al menos 1)?: ")

    for i in range(m):
        cod = input("Codigo postal: ")
        dp = input("Direccion postal: ")
        tip = validar_rango(0, 6, "Tipo de envio (entre 0 y 6): ")
        fp = validar_rango(1, 2, "Forma de pago (entre 1 y 2): ")

        env = Envio(cod, dp, tip, fp)
        v.append(env)

    print("Carga terminada")
    print()


def ordenar(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].codigo > v[j].codigo:
                v[i], v[j] = v[j], v[i]


def opcion3(v):
    n = len(v)
    ordenar(v)
    print("Hay", n, "registros en el arreglo")
    m = validar_rango(1, n, "Cantidad a mostrar (al menos 1 y no mas de " + str(n) + ")?: ")
    print("Listado de envios ordenados por codigo postal...")
    for i in range(m):
        print(v[i])

    print()


# opcion 5
def opcion5(v_envios, cp):
    pos = -1
    for i in range(len(v_envios)):
        if v_envios[i].codigo == cp:
            pos = i
            break
    return pos


# Opcion 6
def opcion6(v_envios, tc):
    v_conteo = [0] * 7

    for i in v_envios:
        if tc == "HC":
            if i.check_dir():
                v_conteo[i.tipo] += 1

        else:
            v_conteo[i.tipo] += 1

    for i in range(len(v_conteo)):
        print("Tipo de envio:", i, "Tiene cantidad de envios:", v_conteo[i])


# Opcion 7
def opcion7(v_envios, tc):

    v_acum = [0] * 7

    for i in v_envios:
        if tc == "HC":
            if i.check_dir():
                importe = i.calcular_importe_final()
                v_acum[i.tipo] += importe

        else:
            importe = i.calcular_importe_final()
            v_acum[i.tipo] += importe

    for i in range(len(v_acum)):
        print("Tipo de envio:", i, "Tiene un acumulado por importes de:", v_acum[i])

    return v_acum


# opcion 8
def opcion8(v_acum_opcion7):

    acum_total = 0
    may = None
    tipo = None
    for i in range(len(v_acum_opcion7)):

        acum_total += v_acum_opcion7[i]

        if may is None or v_acum_opcion7[i] > may:
            may = v_acum_opcion7[i]
            tipo = i

    print("El mayor importe acumulado es para el tipo de envio:", tipo, "con un monto de:", may)

    porc = 100 * may / acum_total
    print("El porcentaje que representa el monto mayor por sobre el acumulado total es:", porc)


# opcion 9
def calcular_promedio_opcion9(v_envios):
    acum = 0
    cont = 0
    for i in v_envios:
        importe = i.calcular_importe_final()
        acum += importe
        cont += 1

    if cont > 0:
        prom = acum / cont
    else:
        prom = 0

    print("El promedio de los importes finales de los envios del arreglo es:", prom)
    return prom


def opcion9(v_envios, prom):
    cont = 0
    for i in v_envios:
        importe = i.calcular_importe_final()

        if importe < prom:
            cont += 1

    print("La cantidad de envios con un importe menor al promedio es:", cont)


