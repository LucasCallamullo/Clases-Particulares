import os.path
import pickle
import random

from registro import *


# ===========================================================================
#                           Opcion 1
# ===========================================================================
def validar_n():
    n = int(input("Ingresar cantidad de vehiculos a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de vehiculos a cargar: "))
    return n


def cargar_arreglo(v_autos, n):
    # id INT > 0, tamanio(1, 4), tipo(0, 5), importe FLOAT, marca(3, 7), anio(2000, 2020)

    for i in range(n):
        id = random.randint(1, 10)
        tamanio = random.randint(1, 4)
        tipo = random.randint(0, 4)
        importe = round(random.uniform(0.1, 10), 2)
        marca = random.randint(3, 7)
        anio = random.randint(2000, 2020)

        nuevo_auto = Vehiculo(id, tamanio, tipo, importe, marca, anio)
        add_in_order(v_autos, nuevo_auto)


def add_in_order(v_autos, nuevo_auto):

    izq, der = 0, len(v_autos) - 1

    while izq <= der:

        c = (izq + der) // 2        # 0

        # el atributo por el que les pidan ordenarlo
        if v_autos[c].id == nuevo_auto.id:
            pos = c
            break

        # la boquita ">" determina si esta de menor a mayor o mayor a menor
        elif v_autos[c].id > nuevo_auto.id:
            der = c - 1

        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v_autos[pos:pos] = [nuevo_auto]     # el objeto va ENTRE CORCHETES


# ===========================================================================
#                           Opcion 2
# ===========================================================================
def mostrar_datos(v_autos):
    # indices      0   1  2
    # v_autos = [ A1, A2, A3 ]
    for i in v_autos:
        # i = A1, A2, A3
        print(i)


# ===========================================================================
#                           Opcion 3
# ===========================================================================
def busqueda_binaria(v_autos, identi):
    izq, der = 0, len(v_autos) - 1
    # v_autos [ A1 A2 A3 A4 a5 ]
    while izq <= der:

        c = (izq + der) // 2  # 0

        # if v_autos[c].id == nuevo_auto.id:
        if v_autos[c].id == identi:
            pos = c
            # break
            return pos  # pos que retorna un valor de indice 0 o +

        # elif v_autos[c].id > nuevo_auto.id:
        elif v_autos[c].id > identi:
            der = c - 1

        else:
            izq = c + 1

    return -1   # no existe un objeto que cumpla


# ===========================================================================
#                           Opcion 4
# ===========================================================================
def generar_archivo_binario(v_autos, fd, x1, x2):

    m = open(fd, "wb")  # primer parametro es el nombre del archivo ( fd )
                        # segundo parametro es el modo de apertura ( "wb" )
    # wb = write binary = crea el archivo si no existe, sobre escribe todo su cotenido
    # ab = append binary = crea el archivo si no existe, agrega contenido al final del archiv
    # conservando todo su contenido anterior

    for i in v_autos:
        # i = A1, A2, A3

        #  guardar todos los vehículos medianos o grandes que la empresa tiene en su flota.
        #  Y que ademas esten entre un importe x1 y x2
        if (i.tamanio == 3 or i.tamanio == 4) and x1 <= i.importe <= x2:
            pickle.dump(i, m)   # primer parametro que quiero guardar ( i )
                               # segundo parametro es donde lo quiero guardar ( m )

    print("Se sobre escribio el archivo")   # opcional
    m.close()   # OBLIGATORIO


# ===========================================================================
#                           Opcion 5
# ===========================================================================
def mostrar_archivo_binario(fd):
    bandera = os.path.exists(fd)    # retorna TRUE si existe el archivo, retorna FALSE si NO existe
    if bandera is False:        # if not bandera
        print("El archivo no existe.")
        return      # corta la funcion y dejo de leer

    m = open(fd, "rb")  # read binary -> modo de lectura
    tam = os.path.getsize(fd)   # nos dice el tamaño en bytes del archivo = 300 bytes

    # archivo = [   A1      A2      A3 ]
    # bytes     0       100     200     300
    # m.tell()  0       100     200

    # al final, cuál es el costo promedio de alquiler de los autos eléctricos que
    # se encontraban en el archivo
    # promedio = acumulado ( de importes ) / la cantidad de veces que acumulamos
    acum = 0
    cont = 0

    while m.tell() < tam:

        auto = pickle.load(m)   # unico parametro el archivo ( m )
        # auto = A1, A2
        print(auto)

        if auto.tipo == 3:
            acum += auto.importe
            cont += 1

    # calcular el promedio
    prom = 0
    if cont > 0:
        prom = acum/cont
    print("El promedio es:", prom)

    m.close()   # OBLIGATORIO


# ===========================================================================
#                           Opcion 6
# ===========================================================================
def generar_matriz(v_autos, z):
    # crear la matriz
    f = 5   # f = filas = marca(3, 7) = lim_superior - lim_inferior + 1 = 7 - 3 + 1 = 5
    c = 21  # c = columnas = anio(2000, 2020) = lim_superior - lim_inferior + 1 = 2020 - 2000 + 1 = 21
    matriz = [ [0] * c for i in range(f) ]

    # marca(3, 7)      3-3 4-3 5-3   6   7
    # fila_indices      0   1   2   3   4

    # anio(2000, 2020) 2000-2000
    # columna_indices   0   1   2   3 ... 20

    # matriz[f][c]  # al reves a como lo creamos
    # matriz = [    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]     ]

    #
    # rellenar la matriz
    for i in v_autos:
        # i = A1, A2, A3
        # matriz[f][c]
        matriz[i.marca - 3][i.anio - 2000] += 1
        # matriz[i.marca - 3][i.anio - 2000] += i.importe

    #
    # mostrar la matriz
    for f in range(len(matriz)):    # range(5)
        # f = 0, 1, 2, 3, 4

        for c in range(len(matriz[0])):     # range(21)
            # c = 0, 1, 2, ... 20

            # que las cantidades sean mayores a z
            if matriz[f][c] > z:
                print("Marca:", f+3, "| Año:", c+2000, "| Cantidad:", matriz[f][c])

            # solo mostrar las marcas 3 y 4
            if f+3 == 3 or f+3 == 4:
                # print("Marca:", f + 3, "| Año:", c + 2000, "| Cantidad:", matriz[f][c])
                pass


# def busqueda_secuencial(v_autos, buscar):
#    for i in range(len(v_autos))


def menu():
    print("1 - Cargar arreglo.")
    print("2 - Mostrar arreglo.")
    print("3 - Generar matriz.")
    print("4 - Generar archivo binario.")
    print("5 - Mostrar archivo binario.")
    print("6 - Busqueda binaria.")
    op = int(input("Ingresar opción: "))
    return op


def principal():

    # arreglo de trabajo
    v_autos = []

    # nombre del archivo binario
    fd = "vehiculos.dat"

    op = -1
    while op != 0:
        op = menu()

        if op == 1:
            n = validar_n()
            # Cada vez que se ingrese en esta opción, el arreglo debe ser creado
            # desde cero y todo contenido anterior debe ser eliminado.
            v_autos = []
            cargar_arreglo(v_autos, n)

        elif op == 2:
            if len(v_autos) > 0:
                mostrar_datos(v_autos)
            else:
                print("El arreglo no esta cargado")

        elif op == 3:
            """
            3 - determinar la cantidad de vehiculos por cada posible combinacion entre 
            cada posible marca y cada posible año
            - solo mostrar las cantidades que sea superior a "z"
            """
            if len(v_autos) > 0:
                z = int(input("Ingresar cantidad a superar: "))
                generar_matriz(v_autos, z)
            else:
                print("El arreglo no esta cargado")

        elif op == 6:
            """
            6 - Buscar un vehículo por identificador. Si existe mostrar todos sus 
            datos y si, además, el tipo de motor es GNC, Eléctrico o Hidrógeno entonces 
            mostrar el mensaje “Opción ecológica!”. Si el vehículo no existe informar con
            un mensaje.
            """
            identi = int(input("Ingresar ID a buscar: "))
            pos = busqueda_binaria(v_autos, identi)

            if pos >= 0:
                print(v_autos[pos])

                if 2 <= v_autos[pos].tipo <= 4:
                    print("Opción ecológica!")

                    # realizar descuento del 22%
                    v_autos[pos].importe -= v_autos[pos].importe * 0.22

                print("Datos actualizados:", v_autos[pos])

            else:  # pos = -1
                print("No existe")

        elif op == 4:
            """
            4 - A partir del arreglo genere un archivo binario que contenga los 
            datos de todos los vehículos medianos o grandes que la empresa tiene en su flota.
            Y que ademas esten entre un importe x1 y x2
            """
            x1 = float(input("Ingresar importe a superar: "))
            x2 = float(input("Ingresar importe a ser menor: "))
            generar_archivo_binario(v_autos, fd, x1, x2)

        elif op == 5:
            """
            5 - Mostrar el archivo generado en el punto anterior indicando, 
            al final, cuál es el costo promedio de alquiler de
            los autos eléctricos que se encontraban en el archivo.
            """
            mostrar_archivo_binario(fd)


if __name__ == "__main__":
    principal()