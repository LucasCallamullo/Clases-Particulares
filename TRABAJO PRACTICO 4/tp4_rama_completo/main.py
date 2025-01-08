import os.path
import pickle

from envio import *


def opcion1(fd_csv, fd_dat):

    if os.path.exists(fd_dat):
        print("1 - Crear de nuevo y borrar el anterior.")
        print("2 - Cancelar.")
        op = int(input("Elegir una opcion: "))
        if op == 2:
            print("Se cancelo la operacion.")
            return

    file_csv = open(fd_csv, "r")
    m = open(fd_dat, "wb")

    cont = 0
    for linea in file_csv:
        cont += 1
        if cont >= 3:
            datos = linea.split(",")
            codigo = datos[0]
            direccion = datos[1]
            tipo = int(datos[2])
            pago = int(datos[3])

            env = Envio(codigo, direccion, tipo, pago)
            pickle.dump(env, m)

    m.close()
    file_csv.close()


def validar_rango(inf, sup, msj):
    valor = int(input(msj))
    while sup < valor or valor < inf:
        print("El valor ingresado no es correcto. Intente nuevamente.")
        valor = int(input(msj))
    return valor


def opcion2(fd_dat):
    m = open(fd_dat, "ab")

    codigo = input("Codigo postal: ")
    direccion = input("Direccion postal: ")
    tipo = validar_rango(0, 6, "Tipo de envio (entre 0 y 6): ")
    pago = validar_rango(1, 2, "Forma de pago (entre 1 y 2): ")

    env = Envio(codigo, direccion, tipo, pago)
    pickle.dump(env, m)

    print("Carga terminada de 1 registro.")
    print()
    m.close()


def opcion3(fd_dat):

    if os.path.exists(fd_dat) is False:
        print("El archivo no existe.")
        return

    m = open(fd_dat, "rb")
    tam = os.path.getsize(fd_dat)

    while m.tell() < tam:
        env = pickle.load(m)
        print(env)

    m.close()


def opcion4(fd_dat, cp):
    if os.path.exists(fd_dat) is False:
        print("El archivo no existe.")
        return

    m = open(fd_dat, "rb")
    tam = os.path.getsize(fd_dat)

    cont = 0

    while m.tell() < tam:
        env = pickle.load(m)

        if env.codigo == cp:
            print(env)
            cont += 1

    print("Envios mostrados:", cont)

    m.close()


def opcion5(fd_dat, d):
    if os.path.exists(fd_dat) is False:
        print("El archivo no existe.")
        return

    m = open(fd_dat, "rb")
    tam = os.path.getsize(fd_dat)

    bandera = False

    while m.tell() < tam:
        env = pickle.load(m)

        if env.direccion == d:
            print(env)
            bandera = True
            break

    if bandera is False:
        print("No existe un envío con la direccion posta:", d)

    m.close()


def opcion6(fd_dat):
    if os.path.exists(fd_dat) is False:
        print("El archivo no existe.")
        return

    f = 2   # f = fila = pago(1, 2)
    c = 7   # c = columna = tipo(0, 6)
    matriz = [ [0] * c for i in range(f) ]

    m = open(fd_dat, "rb")
    tam = os.path.getsize(fd_dat)
    while m.tell() < tam:
        env = pickle.load(m)
        matriz[env.pago - 1][env.tipo] += 1
    m.close()

    for f in range(len(matriz)):
        for c in range(len(matriz[0])):
            if matriz[f][c] > 0:
                print("Forma de pago:", f+1, "| Tipo de envío:", c, "| Cantidad:", matriz[f][c])

    return matriz


def opcion7(matriz):
    for f in range(len(matriz)):

        total_envios = 0
        for c in range(len(matriz[0])):
            total_envios += matriz[f][c]

        print("Forma de pago:", f+1, "Tiene total de envios:", total_envios)

    for c in range(len(matriz[0])):
        total_envios = 0

        for f in range(len(matriz)):
            total_envios += matriz[f][c]

        print("Tipo de envio:", c, "Tiene total de envios:", total_envios)


def calcular_promedio(fd_dat):
    if os.path.exists(fd_dat) is False:
        print("El archivo no existe.")
        return

    m = open(fd_dat, "rb")
    tam = os.path.getsize(fd_dat)

    acum = 0
    cont = 0
    while m.tell() < tam:
        env = pickle.load(m)

        importe = env.calcular_importe()
        acum += importe
        cont += 1
    m.close()

    prom = 0
    if cont > 0:
        prom = acum/cont

    print("el promedio es:", prom)
    return prom


def opcion8(fd_dat, prom):
    if os.path.exists(fd_dat) is False:
        print("El archivo no existe.")
        return

    m = open(fd_dat, "rb")
    tam = os.path.getsize(fd_dat)

    v = []

    while m.tell() < tam:
        env = pickle.load(m)
        importe = env.calcular_importe()
        if importe > prom:
            add_in_order(v, env)

    m.close()

    for i in v:
        print(i)


def add_in_order(v, env):

    izq, der = 0, len(v) - 1
    pos = 0

    while izq <= der:
        c = (izq + der) // 2
        if v[c].codigo == env.codigo:
            pos = c
            break
        elif v[c].codigo > env.codigo:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v[pos:pos] = [env]


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

    fd_csv = "envios-tp4.csv"
    fd_dat = "envios.dat"

    matriz = None

    op = -1
    while op != 0:

        op = menu()

        if op == 1:
            opcion1(fd_csv, fd_dat)

        elif op == 2:
            opcion2(fd_dat)

        elif op == 3:
            opcion3(fd_dat)

        elif op == 4:
            cp = input("Ingresar codigo postal a buscar: ")
            opcion4(fd_dat, cp)

        elif op == 5:
            d = input("Ingresar direccion postal a buscar: ")
            opcion5(fd_dat, d)

        elif op == 6:
            matriz = opcion6(fd_dat)

        elif op == 7:
            if matriz is None:
                print("Primero debe ingresar opcion 6.")
            else:
                opcion7(matriz)

        elif op == 8:
            prom = calcular_promedio(fd_dat)
            opcion8(fd_dat, prom)

        else:
            print("Elija una opcion correcta.")



if __name__ == '__main__':
    principal()
