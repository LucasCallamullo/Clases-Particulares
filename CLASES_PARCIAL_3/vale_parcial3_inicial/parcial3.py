import random

from registro import *


# Opcion 1
def validar_n():
    n = int(input("Ingresar cantidad de teles a cargar: ")) # -1
    while n <= 0:       # mientras n sea menor o igual a cero
        n = int(input("Ingresar cantidad de teles a cargar: (DEBE SER POSITIVO)"))

    return n


def cargar_arreglo(v_teles, n):
    #                 1               2             3
    # depositos = ("Deposito A", "Deposito B", "Deposito C")

    # id > 0, marca STR, pulgadas(32, 50), importe > 0, deposito(1, 3)

    marcas = ("Hitachi", "LG", "samsung")

    for i in range(n):      # 5
        id = random.randint(1, 10)      # INT
        marca = random.choice("ABCDEF")         # STR
        pulgadas = random.randint(32, 50)   # INt
        importe = round(random.uniform(0.1, 10), 2)       # Float
        deposito = random.randint(1, 3)

        tv = Tele(id, marca, pulgadas, importe, deposito)
        v_teles.append(tv)
        # v_teles = [T1, T2, T3]
    print("Se ingresaron", n, "teles.")


# opcion 2
def ordenar_arreglo(v_teles):
    # indices     0     1       2
    # v_teles = [T2,    T1,     T3]
    # id          3     5      7

    n = len(v_teles)        # 3

    for i in range(n-1):    # range(2)
        # i = 0,        1

        for j in range(i+1, n):
            # j = 2
            # i = 1

            # la condicion es lo unico que cambia
            if v_teles[i].id > v_teles[j].id:

                v_teles[i], v_teles[j] = v_teles[j], v_teles[i]


def mostrar_arreglo(v_teles, t):

    # Indique al final cuantas se mostaron
    cont = 0

    # Indique al final el promedio de los importes de las teles que se mostraron
    # promedio = Acumulado / contador
    cont = 0
    acum = 0

    # indices     0     1       2
    # v_teles = [T1,    T2,     T3]
    for i in v_teles:
        # i = T1, T2, T3

        if i.importe > t:
            print(i)
            cont += 1
            acum += i.importe

    if cont > 0:
        prom = acum / cont
        print("EL promedio es:", prom)

    print("Se mostraron:", cont)


# Opcion 3
def generar_vector_conteo(v_teles, x):
    # generar vector de conteo
    v_conteo = [0] * 19         # pulgadas(32, 50)  19 contadores

    # pulgadas    32-32 33-32  34                                              50
    # indices       0   1   2   3 --> los indices hacen referencia a cada "pulgadas"
    # v_conteo = [  2,  1,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # rellenar el vector
    # indices       0       1       2
    # v_teles = [   T1,     T2,     T3]
    # pulgadas      32      33      32
    for i in v_teles:
        # i = T1,    T2, T3
        v_conteo[i.pulgadas-32] += 1
        # v_acum[i.pulgadas-32] += i.importe

    # mostrar el vector d conteo/acum
    for i in range(len(v_conteo)):      # range(19)
        # i = 0,    1, 2, ..., 18 --> los indices hacen referencia a cada "pulgadas"

        # Solo mostrar los contadores que superan a "x"
        if v_conteo[i] > x:
            print("La Pulgada:", i+32, "Tiene la cantidad de:", v_conteo[i])

        # Solo mostrar los contadores que superan a 0
        if v_conteo[i] > 0:
            pass

        # Solo mostrar las pulgadas mayores o iguales a 33 >=
        if i+32 >= 33:
            pass


# Opcion 4
def busqueda_secuencial(v_teles, p, m):
    # indices       0       1       2
    # v_teles = [   T1,     T2,     T3]
    # pulgadas      32      33      33
    for i in range(len(v_teles)):
        # i = 0, 1, 2
        if v_teles[i].pulgadas == p and v_teles[i].marca == m:

            # Si existe modifcar su importe por un valor "imp" que se carga por teclado, y luego
            # mostrar sus datos actualizados
            print("Datos sin actualizar:", v_teles[i])

            imp = float(input("Ingresar nuevo importe: "))
            v_teles[i].importe = imp

            print("Datos actualizados:", v_teles[i])

            # aumentar un 10% el importe
            v_teles[i].importe += v_teles[i].importe * 0.1

            # mostrar solo su id y su importe
            print("ID:", v_teles[i].id, "y su importe:", v_teles[i].importe)

            # Solo mostrar su datos
            print(v_teles[i])

            return      # el return solito corta la funcion como tal

    # Si no existe
    print("No Existe.")



def menu():
    # ctrl + d
    print("1 - Cargar Arreglo")
    print("2 - Mostrar Arreglo.")
    print("3 - Vector de conteo / acum")
    print("4 - Busqueda Secuencial")
    print("0 - Salir.")
    op = int(input("Ingresar opcion: "))        # 2
    return op       # 2


def principal():

    # vector / lista / arreglo
    v_teles = []

    op = -1
    while op != 0:      # mientras op sea distinto de cero

        # que si una variable esta igualada a una funcion es porque espero que esa funcion me devuelva algo
        op = menu()     # 2

        if op == 1:
            n = validar_n()
            cargar_arreglo(v_teles, n)

        elif op == 2:
            """
                2 - Mostrar el arreglo ordenado por ID de menor a mayor
                - Solo mostrar las teles que superen un importe "t" que se ingresa por teclado
            """
            if len(v_teles) > 0:
                ordenar_arreglo(v_teles)

                t = float(input("Ingrese el importe a superar: "))
                mostrar_arreglo(v_teles, t)

            else:
                print("Ingresa primero a la opcion 1")

        elif op == 3:
            """
            3 - determinar y mostrar la cantidad de teles por cada posible pulgada(32, 50) 19 contadores
            - Solo mostrar los contadores que tengan una cantidad mayor a "x"
            """


            x = int(input("Ingresar cantidad a superar: "))
            generar_vector_conteo(v_teles, x)

        elif op == 4:
            """
            Determinar si existe una tele que tenga una cantidad de pulgadas sea igual a "p" y una marca
            igual a "m" ambos se cargan por teclado
            Si existe ---
            Si no existe, informar
            Detener la busqueda al primero
            """
            p = int(input("Ingresar cantidad de pulgadas: "))
            m = input("Ingresar marca a buscar: ")
            busqueda_secuencial(v_teles, p, m)


if __name__ == '__main__':
    principal()
