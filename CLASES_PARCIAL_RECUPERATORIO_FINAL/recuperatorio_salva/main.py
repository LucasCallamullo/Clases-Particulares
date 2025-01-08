import pickle
import random

from registro import *


# ===========================================================================
#                           Opcion 1
# ===========================================================================
def validar_n():
    n = int(input("Ingresar una opcion: "))
    while n <= 0:
        n = int(input("Ingresar una opcion: "))
    return n


def cargar_arreglo(v_proyectos, n):

    tuplas_1 = ("Proyecto1", "Proyecto2", "Proyecto3")

    for i in range(n):

        # codigo INT, titulo UNA CADENA, importe FLOAT, cantidad INT
        codigo = random.randint(1, 15)
        titulo = "Esto es " + random.choice(tuplas_1) + "."
        importe = round(random.uniform(0.1, 10), 2)
        cantidad = random.randint(1, 15)
        proy = Proyecto(codigo, titulo, importe, cantidad)
        add_in_order(v_proyectos, proy)


def add_in_order(v_proyectos, proy):
    izq, der = 0, len(v_proyectos) - 1

    while izq <= der:
        c = (izq + der) // 2

        if v_proyectos[c].codigo == proy.codigo:
            pos = c
            break

        elif v_proyectos[c].codigo > proy.codigo:
            der = c - 1

        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v_proyectos[pos:pos] = [proy]


# ===========================================================================
#                           Opcion 2
# ===========================================================================
def mostrar_datos(v_proyectos):

    # mostrar al final el acumulado de la cantidad investigadores de los proyectos msotrados
    acum = 0

    for i in v_proyectos:
        # i = P1, P2
        print(i)
        acum += i.cantidad

    print("El acumulado:", acum)



# ===========================================================================
#                           Opcion 4
# ===========================================================================
def guardar_archivo_binario(v_proyectos, fd):

    # calcular el promedio de los importes
    # promedio = acumulado ( de importes )  / la cantidad de veces que acumule
    acum = 0
    cont = 0
    for i in v_proyectos:
        acum += i.importe
        cont += 1

    prom = 0
    if cont > 0:
        prom = acum / cont

    print("El promedio es:", prom)

    #
    m = open(fd, "wb")

    for i in v_proyectos:
        # guardar los que superan el promedio
        if i.importe > prom:
            pickle.dump(i, m)
            m.flush() # opcional

    m.close()       # OBLIGATORIO


# ===========================================================================
#                           Opcion 5
# ===========================================================================
def busqueda_binaria(v_proyectos, c):
    izq, der = 0, len(v_proyectos) - 1

    while izq <= der:
        c = (izq + der) // 2

        if v_proyectos[c].codigo == c:
            titulo = v_proyectos[c].titulo
            return titulo

        elif v_proyectos[c].codigo > c:
            der = c - 1

        else:
            izq = c + 1

    return "Artículo inexistente!."


# ===========================================================================
#                           Opcion 6
# ===========================================================================
def procesar_cadena(titulo):
    """
     ¿Cuál es la cantidad de palabras de esa cadena que contienen una letra "r" en la segunda
     o en la tercera posición (en mayúsculas o minúsculas) y que además no contienen ningún dígito?

    - cont --> cantidad de palabras
    - tiene_r_2o3 --> bandera
    - indice  --> para saber la posicion de la letra dentro de la palabra
    - tiene_digito --> bandera
    """

    cont = 0
    tiene_r_2o3 = False
    indice = 0
    tiene_digito = False

    for i in titulo:
        # i = H, o, l , a

        # dentro de la palabra
        if i != " " and i != ".":

            indice += 1

            if i.lower() == "r" and (indice == 2 or indice == 3):
                tiene_r_2o3 = True

            #
            if i in "0123456789":
                tiene_digito = True

        # fuera/termino de la palabra
        else:
            if tiene_r_2o3 and not tiene_digito:
                cont += 1

            # apagar las banderas
            tiene_r_2o3 = False
            indice = 0
            tiene_digito = False

    print("La cantidad de palabras con una r en 2 o 3 es:", cont)


# ===========================================================================
#                           Opcion 7
# ===========================================================================
def busqueda_secuencial(v_proyectos, tit):

    pos = -1
    for i in range(len(v_proyectos)):
        if v_proyectos[i].titulo == tit:
            pos = i
            break

    return pos


# ===========================================================================
#                           Opcion 8
# ===========================================================================
def vector_conteo(v_proyectos):

    # un contador para la cantidad de edades(1, 10) # 10
    v_conteo = [0] * 10

    # edad         1  2  3  4  5
    # indices      0  1  2  3  4  5
    # v_conteo = [ 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in v_proyectos:
        v_conteo[i.edad-1] += 1
        # v_conteo[i.edad-1] += i.importe

    for i in range(len(v_conteo)):
        # i = 0, 1, 2, 3, ,4

        # solo mostrar los que superan un contador de 0
        if v_conteo[i] > 0:
            print("La edad:", i+1, " - cantidad:", v_conteo[i])

        # solo mostrar la edad de 3 a 5 incluidos ambos
        if 3 <= i+1 <= 5:
            pass



def menu():
    print("1 - Cargar arreglo.")
    print("2 - Mostrar arreglo.")
    print("3 - Generar Archivo binario.")
    print("4 - Mostrar Archivo binario.")
    print("5 - .")
    op = int(input("Ingresar opción: "))
    return op


def principal():

    v_proyectos = []

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
            """
            3 - Guardar en un archivo binario los registros que tengo un importe superior al promedio
            de los importes.
            """
            if len(v_proyectos) > 0:
                guardar_archivo_binario(v_proyectos, fd)

            else:
                print("el arreglo no esta cargado.")


        elif op == 4:

            pass

        elif op == 5:
            if len(v_proyectos) > 0:
                c = int(input("Codigo a buscar: "))
                titulo = busqueda_binaria(v_proyectos, c)

            else:
                print("el arreglo no esta cargado.")

        elif op == 6:

            if titulo is None:
                print("primero debe pasar por la opcion 5.")

            else:
                procesar_cadena(titulo)



if __name__ == "__main__":
    principal()