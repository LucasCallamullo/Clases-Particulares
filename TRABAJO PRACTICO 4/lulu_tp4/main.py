import os.path
import pickle

from envio import *


# =================================================================
#               Opcion 1
# =================================================================
def opcion1(csv, fd):

    bandera = os.path.exists(fd) # -> nos dice/nos devuelve si existe el archivo (TRUE) o si no existe (FALSE)
    if bandera:     # bandera = True
        print(" 1 - Desea crear y sobre-escribir el archivo binario nuevamente?")
        print(" 0 - Cancelar.")
        op = int(input("Ingresar opción: "))

        while op > 1 or op < 0:     # opcional
            print(" 1 - Desea crear y sobre-escribir el archivo binario nuevamente?")
            print(" 0 - Cancelar.")
            op = int(input("Ingresar opción (una opción valida): "))

        if op == 0:
            print("Ha cancelado la operacion de generar nuevamente el archivo binario.")
            return

    archivo_csv = open(csv, "r")    # r = read = leer el archivo

    m = open(fd, "wb")  # write binary -> 1 - genera el archivo si no existiera
                        #              -> 2 - Sobre escribe el archivo, perdiendo el contenido anterior

    cont = 0
    for linea in archivo_csv:
        cont += 1
        if cont >= 3:
            listita = linea.strip().split(",")
            # indices       0           1         2    3
            # listita = ['8547', 'Del $ol 456.', '4', '2']
            # codigo STR, direccion STR, tipo INT, pago INT
            codigo = listita[0]     # STR -> codigo postal
            direccion = listita[1]  # STR -> direccion postal
            tipo = int(listita[2])  # INT -> tipo de envio
            pago = int(listita[3])  # INt -> forma de pago

            env = Envio(codigo, direccion, tipo, pago)
            pickle.dump(env, m)   # recibe 2 parametros- 1-> el objeto a guardar ; 2-> el archivo donde lo guardo
            m.flush()   # opcional

    print("Se cargo el archivo binario con la cantidad de envios de:", cont-2)

    m.close()   # OBLIGATORIO
    archivo_csv.close()     # OBLIGATORIO


# =================================================================
#               Opcion 2
# =================================================================
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
    m.flush() # OPCIONAL

    print("Carga terminada")
    print()
    m.close()


# =================================================================
#               Opcion 3
# =================================================================
def opcion3(fd):

    if os.path.exists(fd) is False:      # if not -> preguntar si era False
        print("No existe el archivo:", fd)
        return      # cortaba directamente la funcion

    m = open(fd, "rb")  # read binary ; leer binario ; modo de lectura del archivo para ver su contenido

    tam = os.path.getsize(fd)   # nos devuelve el tamaño en bytes del archivo       # 1600 bytes

    # indices   0   1   2
    # vector = [E1, E2, E3]

    # archivo = [   E1            E2                  E3    ]
    # bytes     0           500             1000            1600
    # m.tell()  0           500             1000

    while m.tell() < tam:   # mientras m.tell() sea menor a tam ingreso al ciclo

        env = pickle.load(m)    # recuperar un objeto dentro del archivo binario (m)
        # env = E1
        print(env)

    m.close()   # OBLIGATORIO


# =================================================================
#               Opcion 4
# =================================================================
def opcion4(fd, cp):
    if os.path.exists(fd) is False:      # if not -> preguntar si era False
        print("No existe el archivo:", fd)
        return      # cortaba directamente la funcion

    m = open(fd, "rb")  # read binary ; leer binario ; modo de lectura del archivo para ver su contenido
    tam = os.path.getsize(fd)  # nos devuelve el tamaño en bytes del archivo       # 1600 bytes

    # archivo = [   E1            E2                  E3    ]
    # bytes     0           500             1000            1600
    # m.tell()  0           500             1000

    cont = 0
    while m.tell() < tam:  # mientras m.tell() sea menor a tam ingreso al ciclo

        env = pickle.load(m)  # recuperar un objeto dentro del archivo binario (m)
        # env = E1, E2, E3
        if env.codigo == cp:    # 8547
            print(env)
            cont += 1

    print("Se mostraron la cantidad de:", cont)

    m.close()   # OBLIGATORIO


# =================================================================
#               Opcion 6
# =================================================================
def opcion6(fd):
    if os.path.exists(fd) is False:      # if not -> preguntar si era False
        print("No existe el archivo:", fd)
        return      # cortaba directamente la funcion

    # crear la matriz
    f = 7   # fila = tipo_envio -> tipo(0, 6) -> 7 posibilidades -> lim_superior - lim_inferior + 1 = 6 - 0 + 1 = 7
    c = 2   # columna = forma de pago -> pago(1, 2) -> 2 posibilidades    -> 2 - 1 + 1 = 2
    matriz = [[0] * c for i in range(f)]

    # pago(1, 2)       1-1  2-1
    # columna indices   0,  1

    #    0   1
    # [ [0, 0],     -> matriz[f][c] -> accedemos a los indices de forma al reves a como creamos la matriz
    #   [0, 0],
    #   [0, 0],
    #   [1, 0],
    #   [2, 0],
    #   [0, 0],
    #   [0, 0]  ]

    # rellenar la matriz
    m = open(fd, "rb")  # read binary ; leer binario ; modo de lectura del archivo para ver su contenido
    tam = os.path.getsize(fd)  # nos devuelve el tamaño en bytes del archivo       # 1600 bytes

    while m.tell() < tam:  # mientras m.tell() sea menor a tam ingreso al ciclo
        env = pickle.load(m)  # recuperar un objeto dentro del archivo binario (m)
        # env = E1, E2, E3
        matriz[env.tipo][env.pago - 1] += 1

    m.close()  # OBLIGATORIO

    # mostrar la matriz
    for f in range(len(matriz)):    # range(7)
        # f = filas = 0, 1, ..., 6

        for c in range(len(matriz[0])):     # range(2)
            # c = columnas = 0, 1
            if matriz[f][c] > 0:
                print("Tipo de envio:", f, "| Forma de pago:", c+1, "| Tiene la cantidad de:", matriz[f][c])

    return matriz


# =================================================================
#               Opcion 7
# =================================================================
def opcion7(matriz):
    # [ [2, 3],     -> matriz[f][c] -> accedemos a los indices de forma al reves a como creamos la matriz
    #   [0, 0],
    #   [0, 0],
    #   [1, 0],
    #   [2, 0],
    #   [0, 0],
    #   [0, 0]  ]

    # totalizar por tipo de envio
    for f in range(len(matriz)):  # range(7)
        # f = filas = 0,    1,  ..., 6

        # f = 1
        total_por_tipo_envio = 0

        for c in range(len(matriz[0])):  # range(2)
            # f = 1
            # c = 0,             1
            total_por_tipo_envio += matriz[f][c]

        print("El tipo de envio:", f, "tiene la cantidad de:", total_por_tipo_envio)

    # totalizar por forma de pago
    print()
    for c in range(len(matriz[0])):  # range(2)
        # c = 0,             1

        total_por_forma_pago = 0
        for f in range(len(matriz)):  # range(7)
            # f = 0,    1,  ..., 6
            total_por_forma_pago += matriz[f][c]

        print("El Forma de Pago:", c+1, "tiene la cantidad de:", total_por_forma_pago)


# =================================================================
#               Opcion 8
# =================================================================
def opcion8_promedio(fd):
    m = open(fd, "rb")  # read binary ; leer binario ; modo de lectura del archivo para ver su contenido
    tam = os.path.getsize(fd)  # nos devuelve el tamaño en bytes del archivo       # 1600 bytes

    # archivo = [   E1            E2                  E3    ]
    # bytes     0           500             1000            1600
    # m.tell()  0           500             1000

    # promedio = acumulado ( de importes ) / cantidad
    acum, cont = 0, 0

    while m.tell() < tam:  # mientras m.tell() sea menor a tam ingreso al ciclo
        env = pickle.load(m)  # recuperar un objeto dentro del archivo binario (m)
        # env = E1, E2, E3
        importe = env.calcular_importe()      # accedo al metodo calcular_importe para que nos devuelva el importe final
        acum += importe
        cont += 1

    m.close()  # OBLIGATORIO

    # calcular promedio
    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio de los importes es:", prom)

    return prom


def opcion8(fd, promedio):
    m = open(fd, "rb")  # read binary ; leer binario ; modo de lectura del archivo para ver su contenido
    tam = os.path.getsize(fd)  # nos devuelve el tamaño en bytes del archivo       # 1600 bytes

    v_envios = []       # crear lista o arreglo vacio

    while m.tell() < tam:  # mientras m.tell() sea menor a tam ingreso al ciclo
        env = pickle.load(m)  # recuperar un objeto dentro del archivo binario (m)
        # env = E1, E2, E3
        importe = env.calcular_importe()  # accedo al metodo calcular_importe para que nos devuelva el importe final

        if importe > promedio:
            add_in_order(v_envios, env)
            # v_envios.append(env)

    # shellsort(v_envios)

    # mostrar el arreglo
    for i in v_envios:
        # i = E1, E2, E3
        print(i)

    m.close()  # OBLIGATORIO


def add_in_order(v_envios, env):

    izq, der = 0, len(v_envios) - 1

    while izq <= der:
        c = (izq + der) // 2
        # el atributo por el que lo ordenas
        if v_envios[c].codigo == env.codigo:
            pos = c
            break
        # la orientacion de esta boquita determina si esta de menor a mayor o mayor a menor
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

    # validar_opcion6
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

        elif op == 4:
            cp = input("Ingresar codigo posta a buscar: ")
            opcion4(fd, cp)

        elif op == 5:
            pass

        elif op == 6:
            matriz = opcion6(fd)

        elif op == 7:
            if matriz is None:
                print("Primero debe pasar por la opcion 6.")
            else:
                opcion7(matriz)

        elif op == 8:
            if os.path.exists(fd):
                promedio = opcion8_promedio(fd)
                opcion8(fd, promedio)

            else:
                print("No existe el archivo.")




if __name__ == '__main__':
    principal()
