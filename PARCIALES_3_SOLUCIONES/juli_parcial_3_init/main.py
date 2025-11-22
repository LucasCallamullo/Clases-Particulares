import random

from registro import *


# ==============================================================================
#           Opcion 1
# ==============================================================================
def validar_n():
    n = int(input("Cantidad de taxis a cargar: "))
    while n <= 0:
        n = int(input("Cantidad de taxis a cargar: "))
    return n        # 3


def cargar_arreglo(v_taxis, n):
    # id INT, nombre STR, marca (1, 20) INT, importe FLOAT

    for i in range(n):      # 3 - 1 = 2
        # i = 0, 1, 2

        id = random.randint(1, 10)    # INT
        nombre = random.choice("ABCDEF")    # str
        marca = random.randint(1, 3)   # INT - pueden tocar el limete inferior y superior estan incluidos
        importe = round(random.uniform(0.1, 10), 2)     # Float

        taxi_objeto = Taxi(id, nombre, marca, importe)      # se crea un objeto del tipo Taxi
        v_taxis.append(taxi_objeto)     # agregar el objeto al final de la lista

    print("se cargaron los", n, "taxis en el arreglo.")


# ==============================================================================
#           Opcion 2
# ==============================================================================
def ordernar_datos(v_taxis):

    n = len(v_taxis)    # 4
    for i in range(n-1):
        # i = 0,    1, 2

        for j in range(i+1, n):
            # i = 0
            # j = 1,    2, 3

            # , y ordenados de menor a mayor por número de identificación
            #       3    >   2

            # la boquita te dice si esta ordenado de menor a mayor o mayor a menor
            if v_taxis[i].id > v_taxis[j].id:
                v_taxis[i], v_taxis[j] = v_taxis[j], v_taxis[i]


def mostrar_datos(v_taxis, i1, i2):

    # Muestre al final una línea adicional con la cantidad de taxis mostrados en este listado
    cont = 0

    # Muestre al final una línea adicional con el promedio de las tarifa de taxis mostrados en este listado
    # prom = acumulador de importes / contador
    cont = 0
    acum = 0

    for i in v_taxis:
        # i = T1, T2, T3, T4

        # Mostrar los datos de todos los taxis cuya tarifa por km esté entre los valores i1 e i2 (ambos incluidos)
        # if i1 <= i.importe <= i2:
        if i.importe >= i1 and i.importe <= i2:
            print(i)
            cont += 1
            acum += i.importe

    print("Se mostraron la cantidad de taxis de:", cont)

    # calcular promedio
    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio es:", prom)


# ==============================================================================
#           Opcion 3
# ==============================================================================
def generar_vector_conteo(v_taxis, x):

    # generar vector
    # marcas(1 , 3) = lim_superior - lim_inferior + 1 = 3 - 1 + 1 = 3
    v_conteo = [0] * 3

    #
    # marcas(1, 3) 1-1     2-1     3-1
    # indices       0       1       2
    # v_conteo = [  2,      1,      0]

    #
    # rellenar el vector
    for i in v_taxis:
        # i = T1, T2, T3
        v_conteo[i.marca - 1] += 1
        # v_acum[i.marca - 1 ] += i.importe

    #
    # mostrar el vector
    for i in range(len(v_conteo)):
        # i = 0, 1, 2

        # Mostrar todos los contadores que sean mayores a "x".
        if v_conteo[i] > x:
            print("Marca:", i+1, " - cantidad:", v_conteo[i])

        # Mostrar todos los contadores que sean distintos de 0.
        if v_conteo[i] != 0:
            pass

        # Mostrar todas las marcas que sean igual a "Citroen"  ( marca 2 )
        if i+1 == 2:
            pass    # printeas


# ==============================================================================
#           Opcion 4
# ==============================================================================
def busqueda_secuencial(v_taxis, d):
    # Si lo encuentra, aplique un 15% de descuento a la tarifa, y muestre todos los datos de ese objeto modificado.
    # Si no lo encuentra, informe con un mensaje que no existe  "no existe ese taxi".
    # Debe detener la búsqueda en el primero que encuentre (sin importar si hay más
    # de un objeto que cumpla el criterio pedido).

    for i in range(len(v_taxis)):
        # i = 0, 1, 2, ...

        # buscar el id y de la marca "2"
        if v_taxis[i].id == d and v_taxis[i].marca == 2:

            # mostrar los datos previos a la modificacion
            print("Sin modificar:", v_taxis[i])

            # aplique un 15% de descuento a la tarifa
            v_taxis[i].importe -= v_taxis[i].importe * 0.15

            # aplique un aumento del 25% de a la tarifa
            # v_taxis[i].importe += v_taxis[i].importe * 0.25

            # modificar su tarifa por un valor "mon" qeu se carga por tecladop
            # mon = float(input("Ingresar nueva tarifa: "))
            # v_taxis[i].importe = mon

            # mostrar los datos posterior a la modificacion
            print("Modificados:", v_taxis[i])

            # mostrar su dni y su nombre
            print("nombre:", v_taxis[i].nombre, "dni:", v_taxis[i].id)

            return  # Debe detener la búsqueda en el primero que encuentre

    # Si no lo encuentra, informe con un mensaje que no existe.
    print("no existe ese taxi.")


def menu():
    print("1 - Cargar Arreglo.")
    print("2 - Ordenar y mostrar arreglo.")
    print("3 - Vector conteo o acum.")
    print("4 - Busqueda secuencial.")
    print("0 - Salir")
    op = int(input("Ingresar opcion: "))
    return op


def principal():

    #
    v_taxis = []            # crea una lista vacía    list()

    op = -1

    while op != 0:

        op = menu()

        if op == 1:
            n = validar_n()

            # cada vez que se ingrese a esta opcion debe cargar nuevamente el arreglo
            # v_taxis = []
            cargar_arreglo(v_taxis, n)

        elif op == 2:

            if len(v_taxis) == 0:
                print("El vector no esta cargaddo.")

            else:
                ordernar_datos(v_taxis)

                # mostrar los que tengan tarifas entre i1 e i2
                i1 = float(input("Ingresar importe a superar: "))
                i2 = float(input("Ingresar importe a ser menor: "))

                mostrar_datos(v_taxis, i1, i2)

        elif op == 3:
            if len(v_taxis) == 0:
                print("El vector no esta cargaddo.")

            else:
                # mostrar todos los contadores mayores que "x"
                x = int(input("Ingresar cantidad a superar: "))
                generar_vector_conteo(v_taxis, x)

        elif op == 4:
            if len(v_taxis) == 0:
                print("El vector no esta cargaddo.")

            else:
                # Determinar si existe un taxi cuyo conductor tenga el ID d (cargar d por teclado).
                d = int(input("Ingresar ID a buscar: "))
                busqueda_secuencial(v_taxis, d)


if __name__ == '__main__':
    principal()

