import random

# import clase_parcial          # clase_parcial.Taxi()
from clase_parcial import *         # Taxi()
# from clase_parcial import Taxi      # Taxi()


# =================================================================
#               Opcion 1
# =================================================================
def validar_n():
    n = int(input("Ingresar cantidad de taxis a cargar: "))     # 0
    while n <= 0:
        n = int(input("Ingresar cantidad de taxis a cargar: (DEBE SER POSITIVO) "))
    return n    # 4


def cargar_arreglo(n, v_taxis):

    for i in range(n):      # 4 vueltas cargo 4 taxis
        # num_id INT ; dni INT ; marca(1, 20) INT ; tarifa FLOAT ; nombre STR
        num_id = random.randint(1, 10)      # se genera un INT aleatorio
        dni = random.randint(1, 10)         # se genera un INT aleatorio
        marca = random.randint(1, 20)       # se genera un INT aleatorio
        tarifa = round(random.uniform(0.1, 10), 2)    # se genera un FLOAT aleatorio
        # flotante = random.uniform(0.1, 10) --> 5.123456789
        # round (flotante, 2) --> 5.12
        nombre = random.choice("ABCDEF")        # se genera un STR aleatorio

        taxi = Taxi(num_id, dni, marca, tarifa, nombre)

        v_taxis.append(taxi)
        # v_taxis = [ ]
        # v_taxis = [ T1 ]
        # v_taxis = [ T1, T2 ]
        # v_taxis = [ T1, T2, T3 ]
        # v_taxis = [ T1, T2, T3, T4 ]
    print("Se cargaron", n, "taxis")


# =================================================================
#               Opcion 2
# =================================================================
def ordenar_arreglo(v_taxis):
    # v_taxis = [ T1, T2, T3, T4 ]
    n = len(v_taxis)  # 4
    for i in range(n - 1):  # 3
        for j in range(i + 1, n):

            # la > define como esta ordenado de menor a mayor o alreves
            if v_taxis[i].num_id > v_taxis[j].num_id:
                v_taxis[i], v_taxis[j] = v_taxis[j], v_taxis[i]

"""
def ordenar_arreglo(v_taxis, ordenador_por="num_id"):
    # v_taxis = [ T1, T2, T3, T4 ]
    n = len(v_taxis)  # 4
    for i in range(n - 1):  # 3
        for j in range(i + 1, n):

            # la > define como esta ordenado de menor a mayor o alreves
            if ordenador_por == 'num_id' and v_taxis[i].num_id > v_taxis[j].num_id:
                v_taxis[i], v_taxis[j] = v_taxis[j], v_taxis[i]
                
            if ordenador_por == 'tarifa' and v_taxis[i].tarifa > v_taxis[j].tarifa:
                v_taxis[i], v_taxis[j] = v_taxis[j], v_taxis[i]
"""


def mostrar_arreglo(v_taxis):
    # Mostrar los datos de todos los taxis cuya tarifa por km esté entre los valores i1 e i2
    # (ambos incluidos) que se cargan por teclado,
    i1 = int(input("Ingresar tarifa a superar: "))
    i2 = int(input("Ingresar tarifa a ser menor: "))

    # Muestre al final una línea adicional con la cantidad de taxis mostrados en este listado.
    cont = 0

    # v_taxis = [ T1, T2, T3, T4 ]
    for i in v_taxis:
        # i = T1, T2, T3, T4

        # if i.tarifa >= i1 and i.tarifa <= i2:
        if i1 <= i.tarifa <= i2:
            print(i)
            cont += 1

    print("La cantidad de taxis mostrados es:", cont)


def mostrar_arreglo_promedio(v_taxis):
    """
        solo mostrar aquellos taxis que tengan una tarifa superior a la tarifa promedio
        de todos los taxis.

        # recorrer todos los taxis
        prom = acumlacion de tarifas / cantidad de tarifas

        # mostrar solo los que superen el promedio
    """
    acum_tarifas = 0
    cont_taxis = 0
    for i in v_taxis:
        # i = T1, T2
        # i --> como un objeto del tipo Taxi
        acum_tarifas += i.tarifa
        cont_taxis += 1

    prom = 0
    if cont_taxis > 0:
        prom = acum_tarifas / cont_taxis

    for i in v_taxis:
        # i = T1, T2

        # mostrar solo los taxis con una tarifa que superen el promedio de las tarifas dentro del arreglo
        if i.tarifa > prom:
            print(i)


# =================================================================
#               Opcion 3
# =================================================================
def vector_conteo(v_taxis):
    """
    Determinar cuántos taxis hay para cada una de las marcas de la flota (20 contadores).
    Mostrar todos los conteos que sean diferentes de cero.
    """
    # crear el vector
    # marca(1, 20)  --> ¿cuantas marcas hay del 1 - 20?
    # lim_superior - lim_inferior + 1 = 20 - 1 + 1 = 20
    v_conteo = [0] * 20

    #
    # marca(1, 20)         1-1 2-1 3-1 4  5-1  ...                                      20-1
    # indices               0   1   2     4  5                                        19
    # v_conteo          = [ 2,  1,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #
    # rellenar el vector
    # v_taxis = [ T1, T2,   T3, ... ]
    # marca        1   2    1
    # tarifa       15  25.5 30
    for i in v_taxis:
        # i = T1, T2,  T3
        v_conteo[i.marca-1] += 1
        # determinar cual es la tarifa acumulada por cada tipo de marca
        # v_conteo[i.marca-1] += i.tarifa

    #
    # mostrar el vector
    x1 = int(input("Ingresar contador a superar: "))
    x2 = int(input("Ingresar contador a ser menor: "))

    n = len(v_conteo)   # 20
    for i in range(n):
        # i = 0,        1, 2, ..., 19
        # Mostrar todos los conteos que sean mayores que una cantidad "x" que se carga por teclado.
        if x1 <= v_conteo[i] <= x2:
            print("Marca: ", i+1, " - Cantidad: ", v_conteo[i])
            # "Marca: ", 1, " - Cantidad: ", 2)

        # mostrar solo la cantidad de taxis de la marca 3 y 10:
        # if 3 <= i+1 <= 10:
        #    print("Marca: ", i+1, " - Cantidad: ", v_conteo[i])


# =================================================================
#               Opcion 4
# =================================================================
def busqueda_secuencial(v_taxis):
    """
    Determinar si existe un taxi cuyo conductor tenga el DNI d (cargar d por teclado). Si lo encuentra, aplique un
    15% de descuento a la tarifa, y muestre todos los datos de ese objeto modificado. Si no lo encuentra, informe
    con un mensaje que no existe. Debe detener la búsqueda en el primero que encuentre (sin importar si hay más
    de un objeto que cumpla el criterio pedido).
    """
    dni = int(input("Ingrese dni a buscar: "))

    for i in range(len(v_taxis)):
        # i = 0, 1, 2, ...
        # v_taxis[i]    --> para acceder al elemento
        if v_taxis[i].dni == dni:
            # aplique un 15% de descuento a la tarifa, y muestre todos los
            # datos de ese objeto modificado.
            print("Datos viejos - ", v_taxis[i])
            # v_taxis[i].tarifa = v_taxis[i].tarifa - v_taxis[i].tarifa * 15 / 100
            v_taxis[i].tarifa -= v_taxis[i].tarifa * 0.15
            # v_taxis[i].tarifa = round(v_taxis[i].tarifa, 2)
            print("Datos nuevos - ", v_taxis[i])

            #
            # Mostrar solo su num identificacion y su tarifa
            # print("Num Id:", v_taxis[i].num_id, " - Tarifa:", v_taxis[i].tarifa)

            #
            # ingresar una nueva tarifa por teclado
            x = float(input("Ingresar flotante: "))
            v_taxis[i].tarifa = round(x, 2)     # 5.12

            return      # termina la funcion

    # Si no lo encuentra, informe con un mensaje que "no existe ese taxi".
    print("no existe ese taxi")

    # for i in v_taxis:
    #    if i.dni == dni:
    #        pass


def menu():
    print("1 - Cargar arreglo.")
    print("2 - Mostrar arreglo.")
    print("3 - Vector de conteo.")
    print("4 - Busqueda secuencial.")
    print("0 - Salir")
    op = int(input("Ingresar opcion: "))  # str  1
    return op


def principal():

    # vector de trabajo inicial
    v_taxis = []        # el tamaño es 0

    op = -1
    while op != 0:  # mientras op sea distinto de cero ingreso al ciclo

        op = menu()

        if op == 1:
            n = validar_n()
            cargar_arreglo(n, v_taxis)

        elif op == 2:
            # if v_taxis:
            if len(v_taxis) > 0:
                ordenar_arreglo(v_taxis)    # []
                mostrar_arreglo(v_taxis)
            else:
                print("Pasar por la opcion 1.")

        elif op == 3:
            if len(v_taxis) > 0:
                vector_conteo(v_taxis)
            else:
                print("Pasar por la opcion 1.")

        elif op == 4:
            if len(v_taxis) > 0:
                busqueda_secuencial(v_taxis)
            else:
                print("Pasar por la opcion 1.")


if __name__ == '__main__':
    principal()
