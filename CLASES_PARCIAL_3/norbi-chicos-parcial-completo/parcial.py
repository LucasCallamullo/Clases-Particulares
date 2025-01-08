import random

from registro import *


# ===============================================================
#                               Opcion 1
# ===============================================================
def validar_n():
    n = int(input("Ingresar cantidad de figuritas a cargar: "))     # 0
    while n <= 0:
        n = int(input("Ingresar cantidad de figuritas a cargar: "))     # 3
    return n


def cargar_arreglo(v_figus, n):

    # pais (1, 32), num_jug(1, 19), nombre STR, posicion(1, 4), importe > 0 FLOAT
    for i in range(n):  # 3 vueltas
        pais = random.randint(1, 32)    # INT
        num_jug = random.randint(1, 19)    # INT
        nombre = random.choice("ABCDEF")        # STR
        posicion = random.randint(1, 4)    # INT
        importe = round(random.uniform(0.1, 10), 2)   # FLOAT

        figu = Figurita(pais, num_jug, nombre, posicion, importe)
        v_figus.append(figu)
        # v_figus = [F1, F2, F3]
    print("Se cargo el arreglo.")


# ===============================================================
#                               Opcion 2
# ===============================================================
def ordenar_arreglo(v_figus):
    n = len(v_figus)
    for i in range(n-1):
        for j in range(i+1, n):

            # la > es lo que determina de menor a mayor o mayor a menor
            if v_figus[i].nombre > v_figus[j].nombre:
                v_figus[i], v_figus[j] = v_figus[j], v_figus[i]


def mostrar_arreglo(v_figus, p):
    # Al final del listado mostrar el promedio de los importes que se mostraron
    # promedio = acumulado(de los imports) / cantidad
    acum = 0
    cont = 0

    # indices       0       1       2
    # v_figus = [   F1,     F2,     F3  ]
    for i in v_figus:
        # i = F1,   F2,   F3

        if i.pais > p:
            print(i)
            acum += i.importe
            cont += 1

    prom = 0
    if cont > 0:
        prom = acum / cont

    print("El promedio de los importes mostrados es:", prom)


# ===============================================================
#                               Opcion 3
# ===============================================================
def generar_vector_conteo(v_figus, x):
    # generar vector de conteo/acum
    v_conteo = [0] * 32     # pais(1, 32) 32 contadores

    # pais         1-1 2-1  3   4   5
    # indices       0   1   2   3   4   5  --> los indices referencian a cada posible pais                            31
    # v_conteo = [  2,  1,  0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # rellenar el vector de conteo
    # indices       0       1       2
    # v_figus = [   F1,     F2,     F3  ]
    # pais          1       2       1
    for i in v_figus:
        # i = F1 ,  F2  , F3
        v_conteo[i.pais-1] += 1
        # v_acum[i.pais-1] += i.importe

    # mostrar el vector de conteo
    for i in range(len(v_conteo)):  # range(32)
        # i = 0,    1, 2, 3, 4.., 31 --> los indices hacen referencia a cada posible pais.

        # solo mostrar los contadores que superen un valor "x"
        if v_conteo[i] > x:
            print("Pais:", i+1, "tiene la cantidad de:", v_conteo[i])

        # solo mostrar los contadores que superen un valor 0
        if v_conteo[i] > 0:
            pass

        # Solo mostrar los paises que son mayores o iguales a 3.  "p"
        if i+1 >= 3:
            pass


# ===============================================================
#                               Opcion 4
# ===============================================================
def busqueda_secuencial(v_figus, nom, j):   # nom = B
    # indices       0       1       2
    # v_figus = [   F1,     F2,     F3  ]
    # nombre        A       B       D
    pos = -1
    for i in range(len(v_figus)):
        # i = 0, 1, 2
        if v_figus[i].nombre == nom and v_figus[i].num_jug == j:
            pos = i
            break   # romper ciclos

    return pos  # 0 o + SI EXISTE       / -1  NO EXISTE


def menu():
    # ctrl + d
    print("1 - Cargar Arreglo.")
    print("2 - Mostrar Arreglo.")
    print("3 - Vector de Conteo/Acum.")
    print("4 - Busqueda Secuencial.")
    print("0 - Salir.")
    op = int(input("Ingresar una opcion: "))    # 3

    return op   # devolver o retornar algun valor


def principal():

    # vector-arreglo-lista-array de trabajo
    v_figus = []

    op = -1
    while op != 0:  # mientras op sea distinto de cero, ingreso al ciclo

        # si una variable esta igualada a una funcion es porque espero que la funcino devuelva algo
        op = menu()     # lo que retorna menu es un 3

        if op == 1:
            """
            1 - pedir n y validar_n, cargar el arreglo con "n" objetos
            -
            """
            n = validar_n()
            cargar_arreglo(v_figus, n)

        elif op == 2:
            """
            2 - Mostrar El arreglo ordenado por nombre de menor a mayor
            - Solo mostrar los que superen el pais "p" que se carga por teclado
            -
            """
            if len(v_figus) > 0:
                ordenar_arreglo(v_figus)

                p = int(input("Ingresar pais a superar: "))
                mostrar_arreglo(v_figus, p)

            else:
                print("El arreglo no esta cargado.")

        elif op == 3:
            """
            3 - Determinar y mostrar la cantidad de figuritas que hay por cada posible pais
            (1, 32) de 32 contadores
            - solo mostrar los contadores que superen una cantidad "x" que se carga por teclado
            """
            if len(v_figus) > 0:
                x = int(input("Ingresar cantidad a superar: "))
                generar_vector_conteo(v_figus, x)

            else:
                print("El arreglo no esta cargado.")

        elif op == 4:
            """
            4 - Determinar si existe una figurita cuyo nombre sea igual a "nom" y tenga un 
            num_jug igual a "j" ambos valores se cargan por teclado
            - Si existe - - -
            - Si no existe, informar -> si no existe o informar "No existe una figurita asi"
            - detener la busqeuda al primer resultad
            """
            nom = input("Ingresar nombre a buscar: ")
            j = int(input("Ingresar num jug a buscar: "))
            pos = busqueda_secuencial(v_figus, nom, j)

            if pos >= 0:

                # Si existe modificar su importe por un valor  "imp" que se carga por teclado y luego
                # mostrar los datos modificados

                print("Datos sin modificar:", v_figus[pos])

                imp = float(input("Ingresar nuevo importe: "))
                v_figus[pos].importe = imp

                print("Datos modificados:", v_figus[pos])

                # aumentar un 10% su importe
                v_figus[pos].importe += v_figus[pos].importe * 0.1

                # Solo mostrar su pais y su importe
                print("Pais:", v_figus[pos].pais, "y su importe:", v_figus[pos].importe)

                # si existe mostrar todos sus datos
                print(v_figus[pos])

            else:
                print("No existe una figurita asi")



if __name__ == '__main__':
    principal()