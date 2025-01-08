import os.path
import pickle
import random

from registro import *


# ===========================================================================
#                                Opcion 1
# ===========================================================================
def validar_n():
    n = int(input("Ingresar cantidad de proyectos a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de proyectos a cargar: "))
    return n


def cargar_arreglo(v_proyectos, n):
    tupla_proyectos = ("Python", "Javascript", "C++")

    # codigo INT, titulo STR, importe FLOAT, cantidad_inv INT, laboratorio(3, 7), encargado(5, 12)
    for i in range(n):
        codigo = random.randint(1, 15)      # INT
        titulo = "Este es el lenguaje " + random.choice(tupla_proyectos) + "."
        importe = round(random.uniform(0.1, 10), 2)     # FLOAT
        cantidad_inv = random.randint(1, 10)
        laboratorio = random.randint(3, 7)
        encargado = random.randint(5, 12)

        proy = Proyecto(codigo, titulo, importe, cantidad_inv, laboratorio, encargado)
        add_in_order(v_proyectos, proy)


def add_in_order(v_proyectos, proy):
    izq, der = 0, len(v_proyectos) - 1

    while izq <= der:

        c = (izq + der) // 2

        # el atributo por el que te pidan ordenarlo "codigo"
        if v_proyectos[c].codigo == proy.codigo:
            pos = c
            break

        # la orientacion de de la boquita ">" determina si esta de menor a mayor o de mayor a menor
        elif v_proyectos[c].codigo > proy.codigo:
            der = c - 1

        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v_proyectos[pos:pos] = [proy]       # el objeto VA ENTRE CORCHETES


# ===========================================================================
#                                Opcion 2
# ===========================================================================
def mostrar_datos(v_proyectos):
    # indices          0    1       2
    # v_proyectos = [ P1,   P2,     P3 ]

    # Indique al final del listado la cantidad
    # total de investigadores que trabajan entre todos los proyectos que se mostraron
    acum = 0

    for i in v_proyectos:
        # i = P1, P2, P3

        print(i)
        acum += i.cantidad_inv

    print("El acumulado es:", acum)


# ===========================================================================
#                                Opcion 3
# ===========================================================================
def generar_archivo_binario(fd, v_proyectos):
    """
    3 - generar un archivo binario que contenga solo los registros que superen al importe de promedio
    de los registros del arreglo
    """
    # calcular el promedio de importes
    # promedio = acumulado ( de importes ) / la cantidad de veces qeu acumule
    acum = 0
    cont = 0

    # indices           0       1       2
    # v_proyectos = [   P1,     P2,     P3 ]
    for i in v_proyectos:
        # i = P1, P2, P3
        acum += i.importe
        cont += 1

    # calcular el promedio
    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio es:", prom)

    # guardar el archivo binario

    m = open(fd, "wb")  # primer parametro: es el nombre del archivo
                        # segundo parametro: es el modo de apertura
    # wb = write binary = generar el archivo si no existe, sobre-escribe todo el contenido del archivo
    # ab = append binary = generar el archivo si no existe, agrega contenido al final del archivo
    # conservando todo el contenido anterior

    for i in v_proyectos:
        # i = P1, P2, P3

        # superen al importe promedio
        if i.importe > prom:
            pickle.dump(i, m)   # primer parametro es que quiero guardar ( i )
                                # segundo parametro es donde lo quiero guardar ( m )

    print("Se genero el archivo.")      # opcional
    m.close()       # OBLIGATORIO


# ===========================================================================
#                                Opcion 4
# ===========================================================================
def mostrar_archivo_binario(fd):

    bandera = os.path.exists(fd)    # retorna True si existe el archivo, o FALSE si NO EXISTE

    if bandera is False:        # if not bandera
        print("NO existe el archivo:", fd)
        return          #

    m = open(fd, "rb")      # read binary
    tamanio = os.path.getsize(fd)   # nos dice el tamaño en bytes del archivo

    # Muestre al final del listado el monto asignado promedio de la cantidad de investigadores
    # de los proyectos mostrados que sean del laboratorio 3 al 5 (incluidos ambos)
    # promedio = acumulado (de cantidad de investigadores ) / cantidad de veces que acumule
    acum = 0
    cont = 0

    while m.tell() < tamanio:

        proy = pickle.load(m)   # unico parametro el archivo
        # proy = P1, P2, P3
        print(proy)

        if 3 <= proy.laboratorio <= 5:
            acum += proy.cantidad_inv
            cont += 1

    # calcular el promedio
    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio cantidad de investigadores es:", prom)

    m.close()       # OBLIGATORIO


# ===========================================================================
#                                Opcion 5
# ===========================================================================
def busqueda_binaria(v_proyectos, center):   # c = 7
    # indices           0       1       2
    # v_proyectos = [   P1,     P2,     P3 ]
    # codigo            2       4       6

    izq, der = 0, len(v_proyectos) - 1
    # izq = 2
    # der = 2

    while izq <= der:

        c = (izq + der) // 2        # c = centro/center  = 2

        # if v_proyectos[c].codigo == proy.codigo:
        if v_proyectos[c].codigo == center:
            print(v_proyectos[c])   # mostrar sus datos
            titulo = v_proyectos[c].titulo
            return titulo

        # elif v_proyectos[c].codigo > proy.codigo:
        elif v_proyectos[c].codigo > center:
            der = c - 1

        else:
            izq = c + 1

    return "Artículo inexistente!."


# ===========================================================================
#                                Opcion 6
# ===========================================================================
def procesar_cadena(titulo):
    """
    #            12345678
     ¿Cuál es la cantidad de palabras de esa cadena que contienen una letra "r" en la segunda o
     en la tercera posición (en mayúsculas o minúsculas) y que además no contienen ningún dígito?
     El texto debe ser procesado obligatoriamente caracter a caracter, a razón de uno por vuelta de ciclo.

    cont --> cantidad de palabras
    tiene_r_pos2o3 --> bandera
    indice  --> va a indicar la posicion
    tiene_digito --> bandera
    """
    cont = 0
    tiene_r_pos2o3 = False
    indice = 0
    tiene_digito = False

    # titulo = "Artículo inexistente!."
    for i in titulo:
        # i = A, r, t, i

        # dentro de una palabra
        if i != " " and i != ".":

            indice += 1

            if i.lower() == "r" and (indice == 2 or indice == 3):
                tiene_r_pos2o3 = True

            if i in "0123456789":   # si la i esta en o es igual a alguno de esos numeros
                tiene_digito = True

        # fuera de una palabra
        else:

            if tiene_r_pos2o3 is True and tiene_digito is False:
                cont += 1

            # apagar las banderas e indices
            tiene_r_pos2o3 = False
            indice = 0
            tiene_digito = False

    print("la cantidad de palabras con r en pos 2 o 3 sin digitos es:", cont)


# ===========================================================================
#                                Opcion 7
# ===========================================================================
def generar_matriz(v_proyectos):
    """
    7 - determinar y mostrar la cantidad de proyectos por cada posible combinacion entre
    laboratorios y encargados
    """

    # generar la matriz
    f = 5    # f = filas = laboratorio(3, 7) = lim_superior - lim_inferior + 1 = 7 - 3 + 1 = 5
    c = 8    # c = columnas = encargado(5, 12) = lim_superior - lim_inferior + 1 = 12 - 5 + 1 = 8
    matriz = [ [0] * c for i in range(f) ]

    # laboratorio(3, 7)        3-3 4-3 5-3 6   7
    # fila_indices =            0,  1,  2,  3,  4

    #
    # encargado(5, 12)        5-5   6   7   8   9   10  11  12
    # columna_indices   =       0   1   2   3   4   5   6   7

    # matriz[f][c]  --> el acceso es al reves a como lo creaste
    # matriz =  [   [1, 0, 0, 0, 0, 0, 0, 0],
    #               [0, 0, 5, 0, 0, 0, 0, 0],
    #               [0, 1, 0, 0, 0, 0, 0, 0],
    #               [0, 0, 0, 0, 0, 0, 0, 0],
    #               [0, 0, 0, 0, 0, 0, 0, 0]    ]

    #
    # rellenar la matriz
    for i in v_proyectos:
        # i = P1, P2, P3
        # matriz[f][c]
        matriz[i.laboratorio - 3][i.encargado - 5] += 1

        # si te pidiera el acumulado/sumatora de importes
        # matriz[i.laboratorio - 3][i.encargado - 5] += i.importe

    #
    # mostrar la matriz

    for f in range(len(matriz)):    # range(5)
        # f = 0, 1, 2, 3, 4

        for c in range(len(matriz[0])):     # range(8)
            # c = 0, 1, 2, 3, ..., 7

            # solo mostrar aquellos contadores que tengan un valor mayor a 0
            if matriz[f][c] > 0:
                print("Laboratorio:", f+3, "- Encargado:", c+5, "- cantidad:", matriz[f][c])

            # solo mostrar los laboratorios entre l1 y l2 (ambos incluidos) que se cargan por teclado
            # if l1 <= f+3 <= l2:
            #    print("Laboratorio:", f+3, "- Encargado:", c+5, "- cantidad:", matriz[f][c])


# ===========================================================================
#                                Opcion 8
# ===========================================================================
def busqueda_secuencial(v_proyectos, tit):

    pos = -1
    for i in range(len(v_proyectos)):
        # i = 0, 1, 2, ...
        if v_proyectos[i].titulo == tit:
            pos = i
            break

    return pos




def menu():
    print("1 - Cargar arreglo.")
    print("2 - Mostrar arreglo.")
    print("3 - Generar archivo binario.")
    print("4 - Mostrar archivo binario.")
    print("5 - busqueda binaria.")
    print("6 - analisis de cadena.")
    print("7 - matriz.")

    print("5 - busqueda binaria.")
    op = int(input("Ingresar opción: "))
    return op


def principal():

    # vector / arreglo / lista de trabajo
    v_proyectos = []

    # fd = file description
    fd = "proyectos.dat"

    titulo = None

    op = -1
    while op != 0:
        op = menu()

        if op == 1:
            n = validar_n()
            cargar_arreglo(v_proyectos, n)

        elif op == 2:
            if len(v_proyectos) > 0:
                mostrar_datos(v_proyectos)
            else:
                print("el arreglo no esta cargado.")

        elif op == 3:
            if len(v_proyectos) > 0:
                generar_archivo_binario(fd, v_proyectos)
            else:
                print("el arreglo no esta cargado.")

        elif op == 4:
            mostrar_archivo_binario(fd)

        elif op == 5:
            if len(v_proyectos) > 0:
                c = int(input("Ingresar codigo a buscar: "))
                # si una variable esta igualada a una funcion es porque espera que retorne algun resultado
                titulo = busqueda_binaria(v_proyectos, c)
            else:
                print("el arreglo no esta cargado.")

        elif op == 6:
            if titulo is None:
                print("primero debe pasar por la opcion 5")

            else:
                procesar_cadena(titulo)

        elif op == 7:
            generar_matriz(v_proyectos)

        elif op == 8:
            tit = input("Buscar titulo: ")
            pos = busqueda_secuencial(v_proyectos, tit)

            if pos >= 0:
                # mostrar sus datos antes y despues de la actualizacion, si existe hacer un descuento sobre
                # su importe del 22%

                print("Datos sin actualizar:", v_proyectos[pos])

                # realizar descuento del 22% en el importe
                v_proyectos[pos].importe -= v_proyectos[pos].importe * 0.22

                # cambiar su importe por un valor que se carga por teclado
                # v_proyectos[pos].importe = float(input("Ingresar nuevo improte: "))

                print("Datos actualizados:", v_proyectos[pos])

                # solo mostrar su laboratorio y encargado
                print("laboratorio:", v_proyectos[pos].laboratorio, "y su encargado es:", v_proyectos[pos].encargado)

            else:
                print("No existe.")


if __name__ == "__main__":
    principal()
