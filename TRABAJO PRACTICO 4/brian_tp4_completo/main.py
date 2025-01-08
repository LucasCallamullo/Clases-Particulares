import os.path
import pickle

from envio import *


# ==========================================================
#                   Opcion 1
# ==========================================================
def opcion1(csv, fd):

    if os.path.exists(fd):
        print("1 - crear nuevamente.")
        print("0 - cancelar.")
        op = int(input("Ingresar opcion: "))

        if op == 0:
            print("Se cancelo la creacion del nuevo archivo")
            return      # corto la funcion

    file_csv = open(csv, "r")   # read solo lectura
    m = open(fd, "wb")

    cont = 0

    for linea in file_csv:
        cont += 1
        if cont > 2:

            data = linea.strip().split(",")
            # indices   0           1           2    3
            # data = [ "8547", "Del $ol 456.", "4", "2" ]

            # codigo, direccion, tipo, pago)
            codigo = data[0]
            direccion = data[1]
            tipo = int(data[2])
            pago = int(data[3])

            env = Envio(codigo, direccion, tipo, pago)
            pickle.dump(env, m)
            m.flush()       # opcional

    m.close()           # OBLIGATORIO
    file_csv.close()    # OBLIGATORIO


# ==========================================================
#                   Opcion 2
# ==========================================================
def validar_rango(inf, sup, msj):
    # funcion reutilizada del tp3
    valor = int(input(msj))
    while sup < valor or valor < inf:
        print("El valor ingresado no es correcto. Intente nuevamente.")
        valor = int(input(msj))
    return valor


def opcion2(fd):

    m = open(fd, "ab")  # append binary, para agregar elementos al final del archivo conservando su contenido anterior

    # codigo STR, direccion STR, tipo INT, pago INT
    codigo = input("Codigo postal: ")
    direccion = input("Direccion postal: ")
    tipo = validar_rango(0, 6, "Tipo de envio (entre 0 y 6): ")
    pago = validar_rango(1, 2, "Forma de pago (entre 1 y 2): ")
    env = Envio(codigo, direccion, tipo, pago)
    pickle.dump(env, m)

    print("Carga terminada")
    print()
    m.close()


# ==========================================================
#                   Opcion 3
# ==========================================================
def opcion3(fd):

    if os.path.exists(fd) is False:
        print("El archivo no existe.")
        return

    m = open(fd, "rb")  # read binary
    tam = os.path.getsize(fd)

    while m.tell() < tam:
        env = pickle.load(m)

        print(env)

    m.close()


# ==========================================================
#                   Opcion 6
# ==========================================================
def opcion6(fd):

    if os.path.exists(fd) is False:
        print("El archivo no existe. Pase por la opcion 1")
        return

    # crear la matriz
    f = 7   # f = fila = tipo(0, 6) = lim_superior - lim_inferior + 1 = 6 - 0 + 1 = 7
    c = 2   # c = columna = pago(1, 2)
    matriz = [[0] * c for i in range(f)]

    # rellenar la matriz
    m = open(fd, "rb")  # read binary
    tam = os.path.getsize(fd)

    while m.tell() < tam:
        env = pickle.load(m)

        # matriz[f][c]
        matriz[env.tipo][env.pago - 1] += 1

    m.close()

    # mostrar la matriz
    for f in range(len(matriz)):
        # f = 0, 1, 2, 3, 4, 5, 6
        for c in range(len(matriz[0])):
            # c = 0, 1

            if matriz[f][c] > 0:
                print(f"Tipo de Envio: {f} | Forma de Pago: {c+1} | Cantidad: {matriz[f][c]}")
                # print("Tipo de Envio:", f, "| Forma de Pago: {c+1} | Cantidad: {matriz[f][c]}")

    return matriz


# ==========================================================
#                   Opcion 7
# ==========================================================
def opcion7(matriz):
    """
    Tipo de Envio: 1 | Forma de Pago: 1 | Cantidad: 3
    Tipo de Envio: 1 | Forma de Pago: 2 | Cantidad: 2
    Tipo de Envio: 2 | Forma de Pago: 1 | Cantidad: 1
    Tipo de Envio: 2 | Forma de Pago: 2 | Cantidad: 1
    Tipo de Envio: 4 | Forma de Pago: 2 | Cantidad: 1
    Tipo de Envio: 5 | Forma de Pago: 1 | Cantidad: 4
    Tipo de Envio: 6 | Forma de Pago: 1 | Cantidad: 1
    Tipo de Envio: 6 | Forma de Pago: 2 | Cantidad: 2
    """
    # totalizar filas
    for f in range(len(matriz)):
        # f = 0,  1, 2, 3, 4, 5, 6

        acum = 0

        for c in range(len(matriz[0])):
            # c = 0, 1
            # f = 1
            acum += matriz[f][c]    # 5

        print("Tipo de envio:", f, "tiene el total de:", acum)

    # totalizar columnas
    for c in range(len(matriz[0])):
        # f = 0,  1
        acum = 0
        for f in range(len(matriz)):
            # f = 0, 1, 2, 3, 4, 5, 6
            # c = 0
            acum += matriz[f][c]  # 5

        print("Forma de pago:", c+1, "tiene el total de:", acum)












def menu():
    print()
    print("1 - Generar Archivo.")
    print("2 - Agregar Archivo.")
    print("3 - Mostrar Archivo.")
    print("4 - Buscar por Código Postal.")
    print("5 - Buscar por Dirección Postal.")
    print("6 - Generar Matriz.")
    print("7 - Mostrar Matriz.")
    print("8 - Generar Arreglo.")
    print("0 - Salir.")
    op = int(input("Ingresar opcion: "))
    return op


def principal():

    # crear el nombre de nuestro archivo binario principal
    fd = "envios.dat"       # file description , nombre del archivo

    # nombre de nuestro archivo csv a leer
    # csv = "envios-tp4.csv"
    csv = "envios-muestra.csv"

    # opcion 7
    matriz = None

    op = -1
    while op != 0:

        op = menu()

        if op == 1:
            opcion1(csv, fd)

        elif op == 2:
            opcion2(fd)

        elif op == 3:
            opcion3(fd)


        elif op == 6:
            matriz = opcion6(fd)

        elif op == 7:
            if matriz is None:
                print("Debe ingresar primero a la opcion 6")
            else:
                opcion7(matriz)




if __name__ == '__main__':
    principal()
