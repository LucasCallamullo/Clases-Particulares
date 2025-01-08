import random

from registro import *


# ===============================================================
#               OPCION 1
# ===============================================================
def validar_n():
    n = int(input("Ingresar cantidad de empleos a generar: "))  # 3
    while n <= 0:
        n = int(input("Ingresar cantidad de empleos a generar: "))
    return n


def cargar_arreglo(v, n):
    # id > 0 INT, descripcion STR, tipo(11, 20), importe > 0 FLOAT
    for i in range(n):  # 3
        id = random.randint(1, 10)  # INT
        descripcion = random.choice("ABCDEF")       # STR
        tipo = random.randint(11, 20)       # ITN
        importe = round(random.uniform(0.1, 10), 2)   # FLOAT

        e = Empleo(id, descripcion, tipo, importe)
        v.append(e)
        # v = [ E1,     E2,     E3 ]
        # id    3       1       2
        # desc  A       B       C
        # tipó
    print("Se cargo el arreglo.")


# ===============================================================
#               OPCION 2
# ===============================================================
def ordenar_arreglo(v):
    # indices   0       1       2
    # v = [     E2,     E1,     E3 ]
    # id        1       3       2

    n = len(v)  # 3

    for i in range(n-1):    # range(2)
        # i = 0,    1

        for j in range(i+1, n):
            # j = 1,    2
            # i = 0

            # la > define si esta de menor a mayor o mayor a menor
            if v[i].id > v[j].id:

                v[i], v[j] = v[j], v[i]


def mostrar_arreglo(v, t):

    # Al final del listado mostrar el promedio de los importes que se mostraron
    # promedio = acumulado(importes) / cantidad
    acum = 0
    cont = 0

    # indices   0       1       2
    # v = [     E1,     E2,     E3 ]
    for i in v:
        # i = E1, E2, E3
        if i.tipo > t:
            print(i)
            acum += i.importe
            cont += 1

    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio de los importes mostrados es:", prom)

    # for i in range(len(v)):
    #    print(v[i])


# ===============================================================
#               OPCION 3
# ===============================================================
def generar_vector_conteo(v, x):
    # generar vector conteo /acum
    v_conteo = [0] * 10     # tipo(11, 20)  10 contadores

    #
    # tipo       11-11 12-11  13  14
    # indices       0   1   2   3   4 --> los indices referencia a cada "tipo de empleo" posible
    # v_conteo = [  2,  1,  0,  0,  0, 0, 0, 0, 0, 0]

    # rellenar el vector de conteo/acum
    # indices   0       1       2
    # v = [     E1,     E2,     E3 ]
    # tipo      11       12     11
    for i in v:
        # i = E1,   E2 , E3
        v_conteo[i.tipo-11] += 1
        # v_acum[i.tipo-11] += i.importe

    # Mostrar el vector de conteo/acum
    for i in range(len(v_conteo)):  # 10
        # i = 0,    1, 2, 3, ..., 9 --> los indices referencia a cada "tipo de empleo" posible

        # Solo mostrar los contadores que superan una cantidad "x"
        if v_conteo[i] > x:
            print("Tipo de empleo:", i+11, "tiene la cantidad de:", v_conteo[i])

        # Solo mostrar los contadores que superan una cantidad 0
        if v_conteo[i] > 0:
            pass

        # Solo mostrar tipo de empleos que superen o igualen un empleo 15
        if i+11 >= 15:
            pass


# ===============================================================
#               OPCION 4
# ===============================================================
def busqueda_secuencial(v, num, desc):  # num = 15
    # indices   0       1       2
    # v = [     E1,     E2,     E3 ]
    # id        10       15     2
    pos = -1
    for i in range(len(v)): # range(3)
        # i = 0, 1, 2
        if v[i].id == num and v[i].descripcion == desc:
            pos = i
            break   # romper ciclos

    return pos  # 0 o + SI EXISTE / -1 NO EXISTE


def menu():
    # ctrl + d
    print(" 1 - Cargar Arreglo.")
    print(" 2 - Mostrar Arreglo.")
    print(" 3 - Vector de conteo/acum.")
    print(" 4 - Busqueda Secuencial.")
    print(" 0 - Salir.")
    op = int(input("Ingresar opcion: "))    # 3
    return op   # nos devuelve algun valor


def principal():

    # arreglo / lista / vector de trbajo
    v = []

    op = -1
    while op != 0:      # mientras op sea distinto de cero, ingresar al ciclo

        # si una variable esta igualada a una funcion , singifica que espera que la funcion devuelva algo
        op = menu()     # vale lo que retorna menu

        if op == 1:
            """
            1 - carguen n y validen n, cargar arreglo con "n" cantidad de objetos
            - cada vez que se carga este arreglo debe generar nuevamente el arreglo
            """
            n = validar_n()
            v = []
            cargar_arreglo(v, n)

        elif op == 2:
            """
            2 - mostrar el arreglo ordenado por ID de menor a mayor
            - solo mostrar los tipos de empleos superiores a "t" que se carga por teclado
            - 
            """
            ordenar_arreglo(v)

            t = int(input("Ingresar tipo de empleo a superar: "))
            mostrar_arreglo(v, t)

        elif op == 3:
            """
            3 - Determinar y mostrar la cantidad de empleos por cada posible tipo(11, 20) 10 contadores
            - solo mostrar los contadores que superen una cantidad "x" que se carga por teclado
            """
            x = int(input("Ingresar cantidad a superar: "))
            generar_vector_conteo(v, x)

        elif op == 4:
            """
            4 - Determinar si existe un empleo cuyo ID sea igual "num" y tenga una descripcion
            igual a "desc"
            - Si Existe ---
            - Si No Existe, Informar    si no existe que informe "No existe el empleo."
            - Detener la busqueda al primer resultado
            """
            num = int(input("Ingresar ID a buscar: "))
            desc = input("Ingresar descripcion a buscar: ")
            pos = busqueda_secuencial(v, num, desc)

            # pos       1
            # v = [ E1, E2, E3 ]
            if pos >= 0:
                # Si existe modifcar su importe por un valor "imp" que se carga por teclado, y
                # despues mostrar todos sus datos modificados

                print("Datos Sin Modificar:", v[pos])

                imp = float(input("Ingresar nuevo importe: "))
                v[pos].importe = imp

                print("Datos Modificados:", v[pos])

                # aumentar su importe un 10%
                v[pos].importe += v[pos].importe * 0.1

                # Solo mostrar su id y su importe
                print("ID:", v[pos].id, "y su importe:", v[pos].importe)

            else:
                print("No existe el empleo.")


if __name__ == '__main__':
    principal()