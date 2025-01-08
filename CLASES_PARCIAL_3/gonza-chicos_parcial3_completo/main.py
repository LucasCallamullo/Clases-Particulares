import random


from registro import *


# Opcion 1
def validar_n():
    n = int(input("Ingresar cantidad de figuritas a cargar: ")) # 3
    while n <= 0:
        n = int(input("Ingresar cantidad de figuritas a cargar: ")) #
    return n


def cargar_arreglo(v_figus, n):
    # pais(1, 32) INT, num_jug(1, 19) INT, nombre STR, posicion(1, 4), importe > 0 FLOAT
    for i in range(n):  # range(3)
        # i = 0, 1, 2
        pais = random.randint(1, 32)    # INT
        num_jug = random.randint(1, 19)    # INT
        nombre = random.choice("ABCDEF")        # STR
        posicion = random.randint(1, 4)     # INT
        importe = round(random.uniform(0.1, 10), 2)   # FLOAT

        figu = Figurita(pais, num_jug, nombre, posicion, importe)
        v_figus.append(figu)
        # v_figus = [F1, F2, F3]
    print("Se cargaron las", n, "figuritas.")


# Opcion 2
def ordenar_arreglo(v_figus):
    n = len(v_figus)    # 3
    # indices       0       1       2
    # v_figus = [   F2,     F1,     F3]
    # nombre        A       X       S

    for i in range(n-1):    # range(2)
        # i = 0,    1

        for j in range(i+1, n):
            # j = 2
            # i = 1

            # la > nos indica si es de menor a mayor o mayor a menor
            if v_figus[i].nombre > v_figus[j].nombre:

                v_figus[i], v_figus[j] = v_figus[j], v_figus[i]


def mostrar_arreglo(v_figus, p):

    # Al final de listado mostrar la sumatoria de los importes de las figuritas mostradas
    acum = 0

    # indices       0       1       2
    # v_figus = [   F1,     F2,     F3]
    # pais          1       5       1

    for i in v_figus:
        # i = F1, F2, F3

        if i.pais > p:
            print(i)
            acum += i.importe

    print("La sumatoria de los importes mostrados:", round(acum, 2))


# Opcion 3
def generar_vector_conteo(v_figus, m):

    # generar vector de conteo/acum
    v_conteo = [0] * 32     # pais(1, 32)   * 32 contadores

    # pais(1,32)   1-1 2-1 3-1  4   5
    # indices       0   1   2   3   4   5   --> los indices hacen referencia a cada posible pais
    # v_conteo = [  2,  1,  0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # rellenar el vector
    # indices       0       1       2
    # v_figus = [   F1,     F2,     F3]
    # pais          1       2       1
    for i in v_figus:
        # i = F1,   F2, F3
        v_conteo[i.pais-1] += 1
        # v_acum[i.pais-1] += i.importe

    # mostrar el vector de conteo / acum
    for i in range(len(v_conteo)):
        # i = 0,    1, 2, 3, ..., --> los indices hacen referencia a cada posible pais

        # solo mostrar los contadores que superen "m"
        if v_conteo[i] > m:     # 0
            print("Pais:", i+1, "Tiene la cantidad de figuritas:", v_conteo[i])

        # solo mostrar los paises mayores o iguales  a 3:
        if i+1 >= 3:
            pass


# Opcion 4:
def busqueda_secuencial(v_figus, nom):  # nom = S
    pos = -1
    # indices       0       1       2
    # v_figus = [   F1,     F2,     F3]
    # nombre        X       S       A
    for i in range(len(v_figus)):
        # i = 0, 1, 2
        if v_figus[i].nombre == nom and (v_figus[i].posicion == 1 or v_figus[i].posicion == 2):
            pos = i     # 1
            break   # romper ciclos
    return pos  # 0 o +    SI EXISTE       / -1     NO EXISTE


def menu():
    # ctrl + d
    print("1 - Cargar Arreglo.")
    print("2 - Mostrar Arreglo.")
    print("3 - Vector Conteo/Acum.")
    print("4 - Busqueda Secuencial.")
    print("0 - Salir.")
    op = int(input("Ingresar una opcion: "))    # 3
    return op


def principal():

    # lista - arreglo - array- vector de trabajo
    v_figus = []        # list()

    op = -1
    while op != 0:  # mientras op sea distinto de cero, ingresar al ciclo

        op = menu()     # 3

        if op == 1:
            n = validar_n()
            """
            1 - 
            Cada vez que se ingrese a estar opcion generar nuevamente el arreglo
            """
            v_figus = []
            cargar_arreglo(v_figus, n)

        elif op == 2:
            """
            2 - Mostrar el arreglo ordenado por nombre de menor a mayor
            - Solo mostrar los valores que superen a un pais "p" que se carga por teclado
            """
            ordenar_arreglo(v_figus)

            p = int(input("Pais a superar: "))
            mostrar_arreglo(v_figus, p)

        elif op == 3:
            """
            3 - Determinar y Mostrar la cantidad de figuritas por cada posible pais(1, 32) 32 contadores
            - Solo mostrar los contadores que superen un valor "m" que se carga por teclado
            """
            m = int(input("Ingresar una cantidad a superar: "))
            generar_vector_conteo(v_figus, m)

        elif op == 4:
            """
            4 - Determinar si existe alguna figurita cuyo nombre sea igual "nom" y juegen en la posicion
            de "Arquero" o "Defensor"
            - Si existe modificar su importe por un valor "imp" que se carga por teclado despues mostrar
            los datos modificados
            - Si No existe, informar
            - Debe detenerse al primer resultado
            """
            nom = input("Ingresar nombre a buscar: ")
            pos = busqueda_secuencial(v_figus, nom)

            if pos >= 0:
                print("Datos Sin Modificar:", v_figus[pos])

                imp = float(input("Ingresar nuevo importe: "))
                v_figus[pos].importe = imp

                print("Datos Modificados:", v_figus[pos])

                # aumentar su importe un 10%
                v_figus[pos].importe += v_figus[pos].importe * 0.1

                # Mostrar solo su pais , y su numero de jugador
                print("Pais:", v_figus[pos].pais, "Y su num jug:", v_figus[pos].num_jug)

            else:
                print("No existe.")


if __name__ == '__main__':
    principal()

