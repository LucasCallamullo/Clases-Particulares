import os.path
import pickle

from envio import *

def opcion1(csv, fd):
    file_csv = open(csv, "r")
    cont = 0

    m = open(fd, "wb")

    for linea in file_csv:
        cont += 1

        if cont >= 3:
            d = linea.strip().split(",")
            codigo = d[0]
            direccion = d[1]
            tipo = int(d[2])
            pago = int(d[3])
            env = Envio(codigo, direccion, tipo, pago)
            pickle.dump(env, m)
            m.flush()

    m.close()
    file_csv.close()


# Opcion 2
def validar_rango(inf, sup, msj):
    # funcion reutilizada del tp3
    valor = int(input(msj))
    while sup < valor or valor < inf:
        print("El valor ingresado no es correcto. Intente nuevamente.")
        valor = int(input(msj))
    return valor


def opcion2(fd):
    m = open(fd, "ab")  # append binary, para agregar elementos al final del archivo conservando su contenido anterior

    codigo = input("Codigo postal: ")
    direccion = input("Direccion postal: ")
    tipo = validar_rango(0, 6, "Tipo de envio (entre 0 y 6): ")
    pago = validar_rango(1, 2, "Forma de pago (entre 1 y 2): ")
    env = Envio(codigo, direccion, tipo, pago)
    pickle.dump(env, m)

    m.close()


# opcion 3
def opcion3(fd):

    if os.path.exists(fd) is False:
        print("El archivo no existe.")
        return      # corta la funcion

    m = open(fd, "rb")  # modo e lectura
    tam = os.path.getsize(fd)   #

    while m.tell() < tam:

        env = pickle.load(m)
        # env = E1, E2, E3
        # env.codigo env.pago env.tipo

        print(env)

    m.close()


# opcion 6      tipo(0, 6)  , pago(1, 2)
def opcion6(fd):

    if os.path.exists(fd) is False:
        print("El archivo no existe.")
        return      # corta la funcion

    m = open(fd, "rb")  # modo e lectura
    tam = os.path.getsize(fd)   #

    # rellenar la matriz
    while m.tell() < tam:

        env = pickle.load(m)
        # env = E1, E2, E3
        # matriz[env.pago - 1][env.tipo] += 1

        print(env)

    m.close()


# opcion 8
def calcular_prom_op8(fd):

    if os.path.exists(fd) is False:
        print("El archivo no existe.")
        return      # corta la funcion

    m = open(fd, "rb")
    tam = os.path.getsize(fd)

    # calcular promedio de importes
    # promedio = acumulado ( de importes ) / la cantidad de veces que acumulamos
    acum = 0
    cont = 0

    while m.tell() < tam:

        env = pickle.load(m)
        # env = E1, E2, E3
        importe = env.calcular_importe()
        acum += importe
        cont += 1

    # calcular promedio
    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio es:", prom)

    m.close()

    return prom


def opcion8(fd, prom):
    if os.path.exists(fd) is False:
        print("El archivo no existe.")
        return

    m = open(fd, "rb")
    tam = os.path.getsize(fd)

    # crear un vector
    v = []

    while m.tell() < tam:

        env = pickle.load(m)
        # env = E1, E2, E3
        importe = env.calcular_importe()
        if importe > prom:
            add_in_order(v, env)

    m.close()

    # mostrar vector
    for i in v:
        # i = E1, E2, E3
        print(i)


def add_in_order(v_envios, env):
    izq, der = 0, len(v_envios) - 1
    pos = 0

    while izq <= der:
        c = (izq + der) // 2
        if v_envios[c].codigo == env.codigo:
            pos = c
            break
        elif v_envios[c].codigo > env.codigo:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v_envios[pos:pos] = [env]


def menu():
    print()
    print("1 - Generar Archivo.")
    print("2 - Agregar Archivo.")
    print("3 - Mostrar Archivo.")
    print("4 - Buscar en el archivo por Código Postal.")
    print("5 - Buscar en el archivo por Dirección Postal.")
    print("6 - Generar Matriz.")
    print("7 - Mostrar Matriz.")
    print("8 - Generar Arreglo.")
    print("0 - Salir.")
    op = int(input("Ingresar opcion: "))
    return op


def principal():

    # nombre de nuestro archivo .csv
    csv = "envios-tp4.csv"
    # csv = "envios-muestra.csv"

    # crear nuestro nombre del archivo
    fd = "envios.dat"

    op = -1
    while op != 0:

        op = menu()

        if op == 1:
            opcion1(csv, fd)

        elif op == 2:
            opcion2(fd)

        elif op == 3:
            opcion3(fd)

        elif op == 8:
            prom = calcular_prom_op8(fd)
            opcion8(fd, prom)



if __name__ == '__main__':
    principal()









