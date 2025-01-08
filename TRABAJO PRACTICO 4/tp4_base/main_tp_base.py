import os.path
import pickle

from envio import *


# Opcion 1
def opcion1(fdt, fdb):

    bandera = os.path.exists(fdb)   # retorna TRUE si existe el archivo, y si no FALSE si NO existe
    if bandera is True:     # if bandera:
        print("1 - Sobre escribir el archivo")
        print("2 - cancelar.")
        op = int(input("Ingresar opcion: "))

        if op == 2:
            print("Se cancelo la operación.")
            return      # corta una funcion

    m_csv = open(fdt, "r")  # r = read ) modo de lectura
    m = open(fdb, "wb")  # primer parametro es el nombre del archivo ( fdb )
                # segundo parametro modo de apertura ( "wb" )
    # wb = write binary = crea el archivo si no existe, sobre escribe todo el contenido
    # ab = append binary = crea el archivo si no existe, agrega contenido al final conservando todo lo anterior

    cont = 0
    for linea in m_csv:
        cont += 1
        if cont >= 3:
            datos = linea.strip().split(",")
            codigo = datos[0]
            direccion = datos[1]
            tipo = int(datos[2])
            pago = int(datos[3])

            env = Envio(codigo, direccion, tipo, pago)
            pickle.dump(env, m)   # primer parametro es que quiero guardar ( env )
                                 # segundo parametro es el archivo ( m )

    m.close()   # OBLIGATORIO
    m_csv.close()   # OBLIGATORIO


# opcion 2
def validar_rango(inf, sup, msj):
    # funcion reutilizada del tp3
    valor = int(input(msj))
    while sup < valor or valor < inf:
        print("El valor ingresado no es correcto. Intente nuevamente.")
        valor = int(input(msj))
    return valor


def opcion2(fdb):
    m = open(fdb, "ab")  # append binary, para agregar elementos al final del archivo conservando su contenido anterior

    # codigo STR, direccion STR, tipo INT, pago INT
    codigo = input("Codigo postal: ")
    direccion = input("Direccion postal: ")
    tipo = validar_rango(0, 6, "Tipo de envio (entre 0 y 6): ")
    pago = validar_rango(1, 2, "Forma de pago (entre 1 y 2): ")
    env = Envio(codigo, direccion, tipo, pago)
    pickle.dump(env, m)

    print("Carga terminada..")
    print()
    m.close()


# opcion 3
def opcion3(fdb):
    if os.path.exists(fdb) is False:
        print("El archivo no existe:", fdb)
        return      # cortar la funcion

    m = open(fdb, "rb")     # rb = read binary = modo de lectura
    tam = os.path.getsize(fdb)  # nos dice el tamaño en bytes del archivo = 300 bytes

    # archivo = [   E1       E2       E3 ]
    # bytes     0       100     200     300
    # m.tell()  0       100

    while m.tell() < tam:
        env = pickle.load(m)    # unico parametro el archivo
        # env = E1,      E2,         E3
        print(env)

    m.close()


# Opcion 6
def opcion6(fdb):
    if os.path.exists(fdb) is False:
        print("El archivo no existe:", fdb)
        return      # cortar la funcion

    # crear la matriz
    f = 2    # f = filas = pago(1, 2) = lim_superior - lim_inferior + 1 = 2 - 1 + 1 = 2
    c = 7    # c = columnas = tipo(0, 6) = 6 - 0 + 1 = 7
    matriz = [ [0] * c for i in range(f) ]

    # pago(1, 2)       1-1 2-1
    # fila_indices      0   1

    # tipo(0, 6)        0   1   2   3   4   5   6
    # columnas_indices  0   1   2   3   4   5   6

    # matriz[f][c]
    # matriz = [    [0, 5, 5, 0, 3, 0, 0],
    #               [0, 2, 0, 0, 0, 0, 0]    ]

    # rellenar la matriz
    m = open(fdb, "rb")  # rb = read binary = modo de lectura
    tam = os.path.getsize(fdb)  # nos dice el tamaño en bytes del archivo = 300 bytes

    while m.tell() < tam:
        env = pickle.load(m)  # unico parametro el archivo
        # env = E1,      E2,         E3
        # matriz[f][c]

        matriz[env.pago - 1][env.tipo] += 1

    m.close()

    # Mostrar la matriz
    for f in range(len(matriz)):    # range(2)
        # f = 0, 1
        for c in range(len(matriz[0])): # range(7)
            # c = 0, 1, 2, 3, 4, 5, 6

            if matriz[f][c] != 0:
                print("Tipo de envío:", c, "| Forma de Pago:", f+1, "| Cantidad:", matriz[f][c])

    return matriz


def opcion7(matriz):

    for f in range(len(matriz)):    # range(2)
        # f = 0,    1
        total_envios = 0

        for c in range(len(matriz[0])): # range(7)
            # c = 0, 1, 2, 3, 4, 5, 6
            # f = 0
            total_envios += matriz[f][c]

        print("Forma de Pago:", f+1, "Total envios:", total_envios)

    for c in range(len(matriz[0])):  # range(7)
        # c = 0, 1, 2, 3, 4, 5, 6
        total_envios = 0

        for f in range(len(matriz)):  # range(2)
            # c = 0
            # f = 0 1
            total_envios += matriz[f][c]

        print("Tipo de Envio:", c, "Total envios:", total_envios)



# opcion 8
def opcion8_calc_prom(fdb):
    if os.path.exists(fdb) is False:
        print("El archivo no existe:", fdb)
        return

    m = open(fdb, "rb")
    tam = os.path.getsize(fdb)

    # promedio de importes
    # prom = acumulado ( de importes ) / la cantidad de veces que acumule
    acum = 0
    cont = 0

    while m.tell() < tam:

        env = pickle.load(m)
        # env = E1,      E2,         E3
        importe = env.calcular_importe()
        acum += importe
        cont += 1

    # calcular el promedio
    prom = 0
    if cont > 0:
        prom = acum / cont

    print("El promedio es:", prom)
    m.close()
    return prom


def opcion8(fdb, promedio):
    if os.path.exists(fdb) is False:
        print("El archivo no existe:", fdb)
        return

    m = open(fdb, "rb")
    tam = os.path.getsize(fdb)

    # creemos un arreglo que solo contenga los objetos con importes mayores al promedio
    v = []

    while m.tell() < tam:

        env = pickle.load(m)
        # env = E1,      E2,         E3
        importe = env.calcular_importe()
        if importe > promedio:
            add_in_order(v, env)
            # v.append(env)

    m.close()
    # shell_sort(v)

    # mostrar arreglo
    for i in v:
        print(i)


def shell_sort(v):
    n = len(v)
    h = 1
    # Determinar el valor inicial de h
    while h <= n // 9:
        h = 3 * h + 1

    # Comenzar el ordenamiento
    while h > 0:
        for j in range(h, n):
            # Guardar el objeto completo
            temp = v[j]
            k = j - h

            # Comparar y mover objetos completos en lugar de solo el atributo codigo_postal
            while k >= 0 and temp.codigo < v[k].codigo:
                v[k + h] = v[k]
                k -= h

            # Asignar el objeto en la posición correcta
            v[k + h] = temp

        # Reducir h
        h //= 3


def add_in_order(v, env):

    izq, der = 0, len(v) - 1

    while izq <= der:
        c = (izq + der) // 2

        # lo que cambia es el atributo que te pidan ordenar
        if v[c].codigo == env.codigo:
            pos = c
            break

        # la boquita ">" determina si esta de menor a mayor o mayor a menor
        elif v[c].codigo > env.codigo:
            der = c - 1

        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v[pos:pos] = [env]      # el objeto va ENTRE CORCHETES


def menu():
    print()
    print("1 - Generar Archivo.")
    print("2 - Agregar Archivo.")
    print("3 - Mostrar Archivo.")
    print("4 - Buscar Código Postal.")
    print("5 - Buscar Dirección Postal.")
    print("6 - Generar Matriz.")
    print("7 - Mostrar Matriz.")
    print("8 - Generar Arreglo.")
    print("0 - Salir.")
    op = int(input("Ingresar opcion: "))
    return op


def principal():

    # nombre del archivo csv
    fdt = "envios-tp4.csv"

    # nombre del archivo binario
    # fdb = "envios-tp4.dat"   # file description
    fdb = "envios.dat"   # file description

    matriz = None

    op = -1
    while op != 0:

        op = menu()

        if op == 1:

            opcion1(fdt, fdb)

        elif op == 2:
            opcion2(fdb)

        elif op == 3:
            opcion3(fdb)

        elif op == 6:
            matriz = opcion6(fdb)

        elif op == 7:
            if matriz is None:
                print("Debe pasar primero por la opcion 6.")
            else:
                opcion7(matriz)


        elif op == 8:
            promedio = opcion8_calc_prom(fdb)
            opcion8(fdb, promedio)


if __name__ == '__main__':
    principal()
