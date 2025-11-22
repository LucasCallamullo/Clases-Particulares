import random

from registro import *


# ==================================================================
#                   Opcion 1
# ==================================================================
def validar_n():
    n = int(input("Ingresar cantidad de figuritas a cargar: "))
    while n <= 0:   # mientras n sea igual o menor a cero ingresar al ciclo while
        n = int(input("Ingresar cantidad de figuritas a cargar (TIENE QUE SER UN POSITIVO): "))
    return n        # 5


def cargar_arreglo(v_figuritas, n):
    # pais (1, 32), num_jug (1, 19), nombre STR, posicion (0, 3), importe FLOAT
    for i in range(n):  # range(5)
        pais = random.randint(1, 32)        # generar INT
        num_jug = random.randint(1, 19)
        nombre = random.choice("ABCDEF")            # generar STR
        posicion = random.randint(0, 3)
        importe = round(random.uniform(1, 10), 2)    # generar FLOAT

        figu = Figurita(pais, num_jug, nombre, posicion, importe)

        v_figuritas.append(figu)

    print("se cargaron", n, "figuritas al arreglo.")


# ==================================================================
#                   Opcion 2
# ==================================================================
def ordenar_arreglo(v_figuritas):
    n = len(v_figuritas)        # 5
    for i in range(n-1):        # 4
        # i = 0,       1, 2, 3

        for j in range(i+1, n):     #  5
            # cuando i = 0 ;   j = 1, 2, 3, 4
            # cuando i = 1 ;   j = 2, 3, 4

            # te pueden pedir de mayor a menor o menor a mayor
            if v_figuritas[i].nombre > v_figuritas[j].nombre:
            # if    A     >     D
                v_figuritas[i], v_figuritas[j] = v_figuritas[j], v_figuritas[i]


def mostrar_arreglo(v_figuritas, v):
    # al final del listado mostremos el promedio de los importes de las figuritas se mostraron
    # prom = sumatoria de importes de las figuritas que se mostraron / cantidad de veces que sume
    prom_acum = 0
    prom_cont = 0

    # al final del listado mostremos cuantas figuritas se mostraron
    cont = 0

    # solo lo estas mostrando / leyendo
    # v_figuritas = [ F1, F2, F3, F4, ... ]
    for i in v_figuritas:
        # i = F1,    F2,    F3,     F4

        # solo mostrar los que superen el importe "v"
        if i.importe > v:
            print(i)
            cont += 1

            prom_acum += i.importe
            prom_cont += 1

    # al final del listado --> despues del for
    print("se mostraron la cantidad de", cont, "figuritas.")

    # calcular promedio - fuera del for
    prom = 0
    if prom_cont > 0:
        prom = prom_acum / prom_cont

    print("El promedio es:", round(prom, 2))


# ==================================================================
#                   Opcion 3
# ==================================================================
def generar_vector_conteo(v_figuritas, c):
    # determinar la cantidad de figuritas por cada posible el pais
    # mostrar solo los que tengan un contador mayor a "c" que se carga por teclado

    # pais(1, 32) = lim_superior - lim_inferior + 1 = 32 - 1 + 1 = 32

    #
    # generar el vector
    v_conteo = [0] * 32

    # pais       1-1 2-1 3-1
    # indice      0  1  2
    # v_conteo = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    #
    # rellenar el vector
    # v_figuritas = [ F1, F2, F3, F4 ]
    for i in v_figuritas:
        # i = F1, F2, F3, F4

        v_conteo[i.pais-1] += 1       # vector de conteo
        # v_acum += i.importe  # vector acum - si te pidieran determinar la sumatoria de importe por cada posible pais

    #
    # mostrar el vector
    for i in range(len(v_conteo)):
        # i = 0,        1, 2, 3, ..., 31

        # i = indice, debería corresponder con el atributo "pais", DEBO sumarle lo que le reste
        # en el anterior paso
        # i + 1  = Pais

        # mostrar solo los paises del 1 al 16 (ambos incluidos )
        # if 1 <= i+1 <= 16:
        # if i+1 >= 1 and i+1 <= 16:
            # print(v_conteo[i])

        # mostrar solo los que tengan un contador mayor a "c" que se carga por teclado
        if v_conteo[i] > c:
            print("Pais:", i+1, "- Cantidad:", v_conteo[i])


# ==================================================================
#                   Opcion 4
# ==================================================================
def busqueda_secuencial(v_figuritas, nom, j):
    # buscar un jugador por nombre "nom" y numero de jugador "j", determinar si existe

    # si existe reemplazar su valor de importe por un nuevo valor "mon" ingresado por teclado, debes mostrar
    # sus datos antes y despues de la modificacion, debe detenerse la busqueda a la primera coincidencia
    # si no existe informar con un mensaje.

    for i in range(len(v_figuritas)):
        # i = 0,    1, 2, 3

        # buscar un jugador por nombre "nom" y numero de jugador "j"
        if v_figuritas[i].nombre == nom and v_figuritas[i].num_jug == j:

            # mostrar datos, antes de la modificacion
            print(v_figuritas[i])

            # reemplazar su valor de importe por "mon" ingresado por teclado
            mon = float(input("Ingresar nuevo importe: "))
            v_figuritas[i].importe = mon

            # mostrar datos, despues de la modificacion
            print(v_figuritas[i])

            return      # para cumplir lo de detenerse al primer resultado

    # fuera del for
    # informar que no existe
    print("No existe.")


# ==================================================================
#                   Opcion 4
# ==================================================================
def busqueda_secuencial2(v_figuritas, nom, j):
    # buscar un jugador por nombre "nom" y numero de jugador "j", determinar si existe

    # si existe realizar un descuento del 25% en su importe, debes mostrar
    # sus datos antes y despues de la modificacion, debe detenerse la busqueda a la primera coincidencia
    # si no existe informar con un mensaje.

    for i in range(len(v_figuritas)):
        # i = 0,    1, 2, 3

        # buscar un jugador por nombre "nom" y numero de jugador "j"
        if v_figuritas[i].nombre == nom and v_figuritas[i].num_jug == j:
            # mostrar datos, antes de la modificacion
            print(v_figuritas[i])

            # realizar un aumento del 10% en su importe
            v_figuritas[i].importe += v_figuritas[i].importe * 0.10

            # realizar un descuento del 25% en su importe
            v_figuritas[i].importe -= v_figuritas[i].importe * 0.25

            # mostrar datos, despues de la modificacion
            print(v_figuritas[i])

            return  # para cumplir lo de detenerse al primer resultado

    # fuera del for
    # informar que no existe
    print("No existe.")


def menu():
    print("1 - Cargar arreglo.")
    print("2 - Ordenar y Mostrar arreglo.")
    print("3 - Vector de conteo o acum.")
    print("4 - Busqueda secuencial.")
    print("0 - Salir.")
    op = int(input("Ingresar una opcion: "))        # 3
    return op       # 3


def principal():

    # arreglo - vector - lista
    v_figuritas = []

    op = -1

    while op != 0:      # mientras "op" sea distinto de cero, ingresar al ciclo while

        op = menu()     # 3

        if op == 1:
            n = validar_n()     # 5
            cargar_arreglo(v_figuritas, n)

        elif op == 2:
            if len(v_figuritas) == 0:
                print("El vector esta vacío")

            else:
                ordenar_arreglo(v_figuritas)
                # porque pedimos un importe
                v = float(input("Importe a superar para mostrar: "))    # STR
                mostrar_arreglo(v_figuritas, v)

        elif op == 3:
            if len(v_figuritas) == 0:
                print("El vector esta vacío")
            else:
                # trabajas la opcion 3

                # determinar la cantidad de figuritas por cada posible el pais
                # mostrar solo los que tengan un contador mayor a "c" que se carga por teclado
                c = int(input("Ingresar cantidad a superar: "))
                generar_vector_conteo(v_figuritas, c)

        elif op == 4:
            if len(v_figuritas) == 0:
                print("El vector esta vacío")

            else:
                # buscar un jugador por nombre "nom" y numero de jugador "j", determinar si existe
                nom = input("Ingresar nombre a buscar: ")
                j = int(input("Ingresar numero del jugador: "))
                busqueda_secuencial(v_figuritas, nom, j)


if __name__ == '__main__':
    principal()
