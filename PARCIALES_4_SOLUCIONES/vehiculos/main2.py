


import os.path
import pickle
import random
from registro import *


# =================================================================
#                   Opcion 1
# =================================================================
def validar_n():
    n = int(input("Ingresar la cantidad de vehiculos a cargar: "))
    while n <= 0:
        n = int(input("Ingresar la cantidad de vehiculos a cargar: "))
    return n


def cargar_arreglo(v_vehiculos, n):
    # marca STR , id INT > 0, tam (1, 4), tipo(0, 4), importe FLOAT

    for i in range(n):  # n = 3
        # i = 0, 1
        marca = random.choice("ABCDEF")
        id = random.randint(1, 10)
        tam = random.randint(1, 4)
        tipo = random.randint(5, 9)
        importe = round(random.uniform(0.1, 10), 2)

        auto = Vehiculo(marca, id, tam, tipo, importe)
        add_in_order(v_vehiculos, auto)


def add_in_order(v_vehiculos, auto):
    """
    Este algoritmo es siempre igual solo cambia el atributo por el que comparas
    y la "<" define si esta de menor a mayor o mayor a menor
    """

    # A1.id         3
    # A2.id         2

    # indices        0
    # v_vehiculos = [A1]
    # id             3
    izq, der = 0, len(v_vehiculos) - 1

    # izq = 0
    # der = -1

    while izq <= der:       # mientrass izq sea menor o igual a cero , ingreso al ciclo

        c = (izq + der) // 2        # c = centro
        # c = 0
        if v_vehiculos[c].id == auto.id:
            pos = c
            break
        elif v_vehiculos[c].id > auto.id:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    # indices           0   1
    # v_vehiculos = [   A2, A1]
    # id                2   3
    v_vehiculos[pos:pos] = [auto]       # no te olvides los corchetes en el objeto


# =================================================================
#                   Opcion 2
# =================================================================
def mostrar_arreglo(v_vehiculos, s1, s2):

    for i in v_vehiculos:
        # i = V1, V2, V3
        if s1 <= i.importe <= s2:
            print(i)


# =================================================================
#                   Opcion 4
# =================================================================
def generar_archivo_binario(v_vehiculos, fd, t):
    """
    # recibe dos parametros, el primero es el nombre del archivo (fd), y el segundo el modo de apertura
    # write binary, escribir en binario, sobre-escribe tod0 el contenido del archivo, y lo crea si no existiera
    # "ab" append binary, agrega contenido al final del archivo, conserva su contenido anterior, y tambien lo crea si no existe
    """
    m = open(fd, "wb")

    for i in v_vehiculos:
        # i = V1, V2, V3
        if i.importe > t and (i.tam == 3 or i.tam == 4):
            pickle.dump(i, m)   # recibir dos parametros, el primero es "m", y el segundo lo que queremos guardar(i)
            m.flush()    # opcional

    m.close()   # OBLIGATORIO


# =================================================================
#                   Opcion 5
# =================================================================
def mostrar_archivo_binario(fd):

    if os.path.exists(fd):

        m = open(fd, "rb")  # read binary, leer el archivo
        size = os.path.getsize(fd)      # nos devuelve el tamaño en bytes del archivo

        # indices   0   1   2
        # listas = [V1, V2, V3]

        # archivo = [ V1        V2          V3       V4]
        #           0     100        200       300       396

        # calcular el promedio de alquileres ( importe )
        # promedio = acumulador ( importes ) / cantidad
        acum = 0
        cont = 0

        while m.tell() < size:
            # auto = v1, v2
            auto = pickle.load(m)   # nos devuelve un objeto a la vez y mueve el puntero (tell)

            print(auto)

            if auto.tipo == 8 or auto.tipo == 9:
                acum += auto.importe
                cont += 1

        prom = 0
        if cont > 0:
            prom = acum / cont
        print("El promedio de los importes del tipo hidrogeno y electrico es:", round(prom, 2))

        m.close()   # no te lo olvides

    # No existe el archivo creado
    else:
        print("No existe el archivo:", fd)


# =================================================================
#                   Opcion 3
# =================================================================
def generar_matriz(v_vehiculos):
    """
    el primer valor hace referencia a las columnas "c" y el segundo a las filas "f"
    """
    # crear la matriz
    c = 5   # c = tipo(5, 9)        # lim_superior - lim_inferior + 1 = 5
    f = 4   # f = tam(1, 4)
    matriz = [ [0] * c for i in range(f) ]

    # c     --> tipo   5-5, 6-5, 7,  8,  9
    # indices           0   1   2   3   4

    # f     --> tam     1-1 2   3   4
    # indices           0   1   2   3

    # [ [0, 0, 0, 0, 0],
    #   [0, 0, 0, 0, 0],
    #   [0, 0, 0, 0, 0],
    #   [0, 0, 0, 0, 0] ]

    # rellenar la matriz
    # v1 tam = 2, tipo 5
    for i in v_vehiculos:
        # i = V1, V2, V3
        # matriz[f][c]      # los indices son al reves a como lo creamos
        matriz[i.tam-1][i.tipo-5] += i.importe
        # matriz[i.tam-1][i.tipo-5] += 1

    # mostrar la matriz
    tupla_tams = ("Subcompacto", "Compacto", "Mediano", "Grande")
    tuplas_tipo = ("Nafta", "Gasoil", "GNC", "Eléctrico", "Hidrógeno")

    for f in range(len(matriz)):    # esta dado por la cantidad de filas, 4, porque tiene 4 listas
        # f = 0, 1, 2, 3

        for c in range(len(matriz[0])): # range(5), esta dado por la cantidad de columnas 5
            # c = 0, 1, 2, 3, 4

            # solo mostrar los tipo de motores 5, 6, 7 ( Nafta, Gasoil, GNC )
            if 5 <= c+5 <= 7:
                # print("Para el tamaño:", f+1, "y el tipo de motor:", c+5)
                print("Para el tamaño:", tupla_tams[f], "y el tipo de motor:", tuplas_tipo[c])
                print("Tiene el acumulado de:", matriz[f][c])
                print()

            # Solo mostrar los que tengo un contador/acumulador que sea superior a 0 o "letra"
            if matriz[f][c] > 0:        # if matriz[f][c] > "letra":
                pass


# =================================================================
#                   Opcion 6
# =================================================================
def busqueda_binaria(v_vehiculos, x):   # x = 5
    # indices           0   1   2   3   4
    # v_vehiculos = [   V1, V2, V3, V4, V5 ]
    # id                2   3   4   5   6

    izq, der = 0, len(v_vehiculos) - 1
    # izq = 3
    # der = 4

    while izq <= der:       # mientrass izq sea menor o igual a cero , ingreso al ciclo

        c = (izq + der) // 2        # c = centro    = 2, 3

        # if v_vehiculos[c].id == auto.id:
        if v_vehiculos[c].id == x:
            # pos = c
            # break
            return c    # 3
        # elif v_vehiculos[c].id > auto.id:
        elif v_vehiculos[c].id > x:
            der = c - 1
        else:
            izq = c + 1

    return -1


def menu():
    print("1 - Cargar Arreglo.")
    print("2 - Mostrar arreglo.")
    print("3 - Generar Matriz.")
    print("4 - Generar Archivo Binario.")
    print("5 - Mostrar Archivo Binario.")
    print("6 - Busqueda Binaria.")
    print("0 - Salir.")
    return int(input("Ingresar una opcion: "))


def main():

    # vector/arreglo/lista de trabajo
    v_vehiculos = []

    # nombre del archivo binario
    fd = "vehiculos.dat"           # file description, nombre del archivo

    op = -1
    while op != 0:

        op = menu()

        if op == 1:
            """
            1 - cargar arReglo bla BLA
            - cada vez que se ingresa a esta opcion debe crear nuevamente el arreglo
            """
            n = validar_n()
            v_vehiculos = []
            cargar_arreglo(v_vehiculos, n)

        elif op == 2:
            """
            2 - solo mostrar los que tengan importes entre "s1" y "s2"
            """
            if len(v_vehiculos) > 0:
                s1 = float(input("Importe a superar: "))
                s2 = float(input("Importe a ser menor: "))
                mostrar_arreglo(v_vehiculos, s1, s2)
            else:
                print("El arreglo no esta cargado, ingrese a la opcion 1")

        elif op == 3:
            """
            3 - Generar Matriz
            Calcular los importes acumulados por cada tamaño de vehiculo y tipo de motor posible
            - 
            """
            if len(v_vehiculos) > 0:
                generar_matriz(v_vehiculos)
            else:
                print("El arreglo no esta cargado, ingrese a la opcion 1")

        elif op == 4:
            """
            4 - solo guardar los que superan un importe "t"
            """
            if len(v_vehiculos) > 0:
                t = float(input("Ingresar importe a superar para guardar: "))
                generar_archivo_binario(v_vehiculos, fd, t)

            else:
                print("El arreglo no esta cargado, ingrese a la opcion 1")

        elif op == 5:
            """
            5 - Mostrar archivo binario
            """
            mostrar_archivo_binario(fd)

        elif op == 6:
            """
            Buscar un vehículo por identificador. Si existe mostrar todos sus datos y si, además, 
            el tipo de motor es GNC, Eléctrico o Hidrógeno entonces mostrar el mensaje “Opción ecológica!”. 
            Si el vehículo no existe informar con
            un mensaje
            """
            if len(v_vehiculos) > 0:
                x = int(input("Ingresar numero id a buscar: "))
                pos = busqueda_binaria(v_vehiculos, x)
                if pos >= 0:
                    print(v_vehiculos[pos])

                    if 7 <= v_vehiculos[pos].tipo <= 9:
                        print("Opcion Ecologica!")

                else:
                    print("No existe.")
            else:
                print("El arreglo no esta cargado, ingrese a la opcion 1")


if __name__ == '__main__':
    main()