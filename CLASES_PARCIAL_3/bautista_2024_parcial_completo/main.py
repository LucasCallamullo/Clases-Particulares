import random
from registro import *


# Opcion 1
def validar_n():
    n = int(input("Ingresar cantidad de errores a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de errores a cargar (DEBE SER POSITIVO): "))
    return n


def cargar_arreglo(v_errores, n):
    # codigo (1000, 5000) INT, error_sist (1, 3), mensaje STR, hora(1, 24), importe FLOAT
    for i in range(n):      #
        codigo = random.randint(1000, 5000)     # INT
        error_sist = random.randint(1, 3)     # INT
        mensaje = random.choice("ABCDEF")       # STR
        hora = random.randint(1, 24)    # INT
        importe = round(random.uniform(0.1, 10), 2)       # FLOAT

        e = Error(codigo, error_sist, mensaje, hora, importe)
        v_errores.append(e)
        # v_errores = [ E1, E2, E3 ]
    print("Se cargaron los", n, "errores")


# Opcion 2
def ordenar_arreglo(v_errores):
    # indices           0       1       2
    # v_errores = [     E2,     E1,     E3 ]
    # codigo            3       5       4

    n = len(v_errores)  # 3

    for i in range(n-1):    # range(2)
        # i = 0,    1

        for j in range(i+1, n):
            # j = 1,    2
            # i = 0

            # la > es la que dice si se ordena de menor a mayor o mayor a menor
            if v_errores[i].codigo > v_errores[j].codigo:

                v_errores[i], v_errores[j] = v_errores[j], v_errores[i]


def mostrar_arreglo(v_errores, h1, h2):

    # Al final del listado mostrar el promedio de los importes de los errores mostrados
    # promedio = acumulado(importes) / cantidad
    acum = 0
    cont = 0

    # indices           0       1       2
    # v_errores = [     E1,     E2,     E3 ]
    # codigo            3       5       4
    for i in v_errores:
        # i = E1 , E2 , E3
        if h1 < i.hora < h2:
            print(i)
            cont += 1
            acum += i.importe

    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio de los importes mostrados:", prom)


# Opcion 3
def generar_vector_conteo(v_errores, x):

    # generar vector de conteo
    v_conteo = [0] * 24     # hora(1, 24) 24 contadores

    #
    # hora         1-1 2-1  3   4
    # indices       0   1   2   3   4 --> los indices hacen referencia a cada posible "hora"
    # v_conteo = [  2,  1,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # rellener el vector de conteo/acum
    # indices           0       1       2
    # v_errores = [     E1,     E2,     E3 ]
    # hora              1       2       1
    for i in v_errores:
        # i = E1,   E2, E3
        v_conteo[i.hora-1] += 1
        # v_acum[i.hora-1] += i.importe

    # Al final de este listado, mostrar cual fue la hora en la
    # que se produjo la mayor cantidad de errores
    mayor = None
    hora = None

    # mostrar el vector de conteo /acum
    for i in range(len(v_conteo)):  # 24
        # i = 0, 1, 2, 3 ... --> los indices hacen referencia a cada posible "hora"

        # Solo mostrar los contadores que superen un valor de x
        if v_conteo[i] > x:
            print("Hora:", i+1, "Tiene la cantidad de errores de:", v_conteo[i])

        # Solo mostrar los contadores que superen un valor de 0
        if v_conteo[i] > 0:
            pass

        # solo mostrar las horas mayores o iguales a 3  " x"
        if i+1 >= 3:
            pass

        # Conseguir mayor y hora
        if mayor is None or v_conteo[i] > mayor:
            mayor = v_conteo[i]
            hora = i+1

    print("La hora:", hora, "tuvo la mayor cantidad de errores con:", mayor)


# Opcion 4
def busqueda_secuencial(v_errores, cod, msj):   # cod = 5
    # indices           0       1       2
    # v_errores = [     E1,     E2,     E3 ]
    # codigo            3       5       4
    pos = -1
    for i in range(len(v_errores)):
        # i = 0,    1,  2,
        if v_errores[i].codigo == cod and v_errores[i].mensaje == msj:
            pos = i
            break       # romper ciclos

    return pos  # 0 o + SI EXISTE / -1 NO EXISTE



def menu():
    # ctrl + d
    print(" 1 - Cargar Arreglo.")
    print(" 2 - Mostrar Arreglo.")
    print(" 3 - Vector de Conteo.")
    print(" 4 - Busqueda Secuencial.")
    print(" 0 - Salir.")
    op = int(input("INgresar opcion: "))    # 2
    return op   # retornar o devolver


def principal():

    # arreglo/vector/lista de trabajo
    v_errores = []      # list()

    op = -1
    while op != 0:      # mientras op sea distinto de cero, ingresa al ciclo while

        # si una variable esta igualada a funcion, significa que espera que la funcion devuelva algun valor
        op = menu()     # lo que retorne menu 2

        if op == 1:
            """ 
            1 - cargar n y validarlo, cargar el arreglo con n objetos.
            - Cada vez que se ingresa a esta opcion debe generarse nuevamente el arreglo
            """
            n = validar_n()
            v_errores = []
            cargar_arreglo(v_errores, n)

        elif op == 2:
            """
            2 - Mostrar el arreglo ordenado por codigo
            - Solo mostrar los errores que esten entre la hora "h1" y "h2", ambos que se carga por
            teclado
            """
            ordenar_arreglo(v_errores)
            h1 = int(input("Ingresar la hora a superar: "))
            h2 = int(input("Ingresar la hora a ser menor: "))
            mostrar_arreglo(v_errores, h1, h2)

        elif op == 3:
            """
            3 - determinar y mostrar la cantidad de errores por cada posible hora(1, 24)    24 contadores
            - solo mostrar los contadores que superan una cantidad "x" que se carga por teclado.
            """
            x = int(input("Ingresar cantidad a superar: "))
            generar_vector_conteo(v_errores, x)

        elif op == 4:
            """
            4 - Determinar si existe algun error cuyo codigo sea "cod" y tenga una mensaje "msj" y ambos
            se cargan por teclado.
            - si existe -
            - si no existe, informar        
            - detener la busqueda al primer resultado
            """
            cod = int(input("Ingresar codigo a buscar: "))
            msj = input("Ingresar mensaje a buscar: ")

            pos = busqueda_secuencial(v_errores, cod, msj)

            if pos >= 0:
                # Si existe, modificar su importe por un valor imp que se carga por teclado, y luego
                # mostrar su datos modificados

                print("Datos sin modificar:", v_errores[pos])

                imp = float(input("Ingresar nuevo importe: "))
                v_errores[pos].importe = imp

                print("Datos modificados:", v_errores[pos])

                # aumentar el importe 10%
                v_errores[pos].importe += v_errores[pos].importe * 0.1

                # solo mostrar la hora y su importe
                print("La hora:", v_errores[pos].hora, "y su importe:", v_errores[pos].importe)

            else:
                print("No existe.")


if __name__ == '__main__':
    principal()

