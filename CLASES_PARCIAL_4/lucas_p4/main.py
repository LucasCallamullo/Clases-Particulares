import random

from clase_zapato import *

# import clase_zapato
# clase_zapato.Zapato()


# =========================================================================
#           Opcion 1
# =========================================================================
def validar_n():
    n = int(input("Ingresar cantidad de zapatos a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de zapatos a cargar: "))
    return n


def cargar_arreglo(n, v_zapatos):
    # tupla_nombres = ("Lucas", "Agos")

    # codigo INT > 0, nombre STR, talle INT (35, 45), ancho (0, 2), disponible BOOL, precio FLOAT
    for i in range(n):
        codigo = random.randint(1, 15)
        nombre = random.choice("ABCDEF")
        # nombre = random.choice(tupla_nombres)
        talle = random.randint(35, 45)
        ancho = random.randint(0, 2)
        disponible = random.choice((True, False))       # bool
        precio = round(random.uniform(0.1, 10), 2)

        zapatito = Zapato(codigo, nombre, talle, ancho, disponible, precio)

        add_in_order(v_zapatos, zapatito)

    print("Se cargaron", n, "zapatos.")


def add_in_order(v_zapatos, zapatito):
    # indice        0       1       2       3       4       5
    # v_zapatos = [ Z2,     Z1,     Z3,     Z6,     Z5,     Z4 ]
    # codigo        3       5       7       8       9       11

    # Z1   --> Z1.codigo = 5
    # Z2   --> Z2.codigo = 3
    # Z6   --> Z6.codigo = 8

    izq, der = 0, len(v_zapatos) - 1
    # izq = 3
    # der = 2

    while izq <= der:
        c = (izq + der) // 2        # c (centro) --> 3

        # lo unico que varía es el atributo que te piden a comparar
        if v_zapatos[c].codigo == zapatito.codigo:
            pos = c
            break

        # la boquita define como esta ordenado ascendente o descendete ">"
        elif v_zapatos[c].codigo > zapatito.codigo:
            der = c - 1

        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v_zapatos[pos:pos] = [zapatito]


# =========================================================================
#           Opcion 2
# =========================================================================
def mostrar_arreglo(v_zapatos):
    for i in v_zapatos:
        # i = z1, Z2
        print(i)


# =========================================================================
#           Opcion 3
# =========================================================================
def generar_matriz(v_zapatos):

    #
    # generar matriz
    f = 3   # fila = ancho(0, 2)    # lim_superior - lim_inferior + 1 = 2 - 0 + 1 = 3
    c = 11   # columna = talle(35, 45)  # lim_superior - lim_inferior + 1 = 45 - 35 + 1 = 11
    matriz = [ [0] * c for i in range(f) ]
    # matriz = [ [0] * f for i in range(c) ]

    # ancho (0, 2)      0       1       2
    # filas             0,      1,      2

    # talle(35, 45)   35-35,     36,     37, ...,    45
    # columnas          0,      1,      2,  ...,    10

    # [ [0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   ]

    #
    # rellenar la matriz
    for i in v_zapatos:
        # i = z1, Z2, Z3

        """ Determinar la cantidad de zapatos por cada posible combinacion de ancho y talle """
        matriz[i.ancho][i.talle-35] += 1        # matriz de conteo

        """ Determinar cuál es el stock disponible por cada combinación de talle y ancho. """
        # matriz[i.ancho][i.talle - 35] += i.stock     # matriz de acumulacion

    #
    # mostrar la matriz
    """ mostrar aquellos contadores que superen la cantidad de 'u' zapatos que se carga por teclado """
    # u = int(input("Ingresar cantidad de zapatos por combinacion a superar: "))      # 0

    """ Solo mostrar la cantidades combinadas para un talle 't' que se carga por teclado """
    t = int(input("Ingresar talle a mostrar: "))

    n = len(matriz)

    # tupla_anchos = ("Delgado", "Normal", "Extra ancho")

    for f in range(n):        # 3
        # f = 0, 1, 2       --> f = filas = ancho(0, 2)

        for c in range(len(matriz[0])):     # 11
            # c = 0, 1, 2, 3, ..., 10   --> c = columnas --> c+35 = talle(35, 45)

            # if matriz[f][c] > u:
            if c+35 == t:
                print("Ancho:", f, " - Talle:", c+35, "- Cantidad:", matriz[f][c])
                # print("Ancho:", tupla_anchos[f], " - Talle:", c+35, "- Cantidad:", matriz[f][c])








def menu():
    print("1 - Cargar arreglo.")
    print("2 - Mostrar arreglo.")
    print("3 - Generar matriz.")

    print("4 - Generar archivo binario.")
    print("5 - Mostrar archivo binario.")
    print("0 - Salir.")
    op = int(input("Ingresar opcion: "))
    return op


def principal():

    v_zapatos = []

    op = -1
    while op != 0:

        op = menu()

        if op == 1:
            n = validar_n()
            v_zapatos = []
            cargar_arreglo(n, v_zapatos)

        elif op == 2:
            # if v_zapatos:
            if len(v_zapatos) > 0:
                mostrar_arreglo(v_zapatos)
            else:
                print("Debe pasar primero por la opcion 1")

        elif op == 3:
            generar_matriz(v_zapatos)

        elif op == 4:
            pass
        elif op == 5:
            pass


if __name__ == '__main__':
    principal()




