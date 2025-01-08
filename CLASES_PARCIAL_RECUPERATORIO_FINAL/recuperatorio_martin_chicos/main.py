import os.path
import pickle
import random

from registro import *


# ===========================================================================
#                           Opcion 1
# ===========================================================================
def validar_n():
    n = int(input("Ingresar cantidad de proyectos a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de proyectos a cargar: "))
    return n


def cargar_arreglo(v_proyectos, n):
    tupla_proyectos = ("Proyecto 1.", "Proyecto 2.", "Proyecto 3.")

    # codigo INT, titulo STR ".", importe FLOAT, cant_inv INT, disponible BOOL,
    # laboratorio(3, 5), zona(15, 18)
    for i in range(n):

        codigo = random.randint(1, 10)
        titulo = "este es el " + random.choice(tupla_proyectos)
        importe = round(random.uniform(0.1, 10), 2)
        cant_inv = random.randint(1, 10)
        disponible = random.choice((False, True))
        laboratorio = random.randint(3, 5)
        zona = random.randint(15, 18)

        proy = Proyecto(codigo, titulo, importe, cant_inv, disponible, laboratorio, zona)
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

    #  Indique al final del listado la cantidad total de investigadores que trabajan entre
    #  todos los proyectos que se mostraron.

    acum = 0

    # v_proyectos = [ P1, P2, P3 ]
    for i in v_proyectos:
        # i = P1,   P2,     P3
        print(i)
        acum += i.cant_inv

    print("el total de investigadores mostrados es:", acum)


# ===========================================================================
#                           Opcion 3
# ===========================================================================
def generar_archivo_binario(v_proyectos, fd):
    """
    solo guardar en el archivo aquellos objetos que tengan un importe superior al promedio de los importes
    dentro del arreglo.
    """

    # calcular el promedio
    # prom = acumulado ( de importes ) / la cantidad de veces que acumule
    acum = 0
    cont = 0

    for i in v_proyectos:
        # i = P1, P2, P3
        acum += i.importe
        cont += 1

    prom = 0
    if cont > 0:
        prom = acum / cont

    print("El promedio de importes es:", prom)

    # guardar el archivo
    m = open(fd, "wb")

    for i in v_proyectos:
        if i.importe > prom:
            pickle.dump(i, m)

            # opcionales

    # print (genero el archivo)
    m.close()       # OBLIGATORIO


# ===========================================================================
#                           Opcion 4
# ===========================================================================
def mostrar_archivo_binario(fd):
    bandera = os.path.exists(fd)    # retorna true si existe, False si no existe

    if bandera is False:
        print("no existe el archivo:", fd)
        return      # cortar la funcion

    m = open(fd, "rb")
    tamanio = os.path.getsize(fd)

    # calcular promedio de cantidad investigadores
    # promedio = acumulado ( de cant_inv ) /  la cantidad veces qeu acumule
    acum = cont = 0

    while m.tell() < tamanio:
        proy = pickle.load(m)
        # proy = P1, P2, P3, P4

        print(proy)
        acum += proy.cant_inv
        cont += 1

    # calcular prom
    prom = 0
    if cont > 0:
        prom = acum / cont

    print("El promedio de cant_inv es:", prom)

    m.close()   # OBLIGATORIO


# ===========================================================================
#                           Opcion 5
# ===========================================================================
def busqueda_binaria(v_proyectos, cod):
    izq, der = 0, len(v_proyectos) - 1

    while izq <= der:

        c = (izq + der) // 2
        # if v_proyectos[c].codigo == proy.codigo:
        if v_proyectos[c].codigo == cod:
            pos = c
            # break
            print(v_proyectos[pos])
            return v_proyectos[pos].titulo

        # elif v_proyectos[c].codigo > proy.codigo:
        elif v_proyectos[c].codigo > cod:
            der = c - 1

        else:
            izq = c + 1

    return "Artículo inexistente!."


# ===========================================================================
#                           Opcion 6
# ===========================================================================
def analisis_cadena(titulo):
    """
    #    1234012012
        ¿Cuál es la cantidad de palabras de esa cadena que contienen una letra "r" en la segunda
    o en la tercera posición (en mayúsculas o minúsculas) y que además no contienen ningún dígito (numeros)?

    cantidad_palabras = 0

    cont_r_pos2_pos3 = 0
    indice = 0

    cont_digitos = 0
    """

    cantidad_palabras = 0

    cont_r_pos2_pos3 = 0
    indice = 0
    cont_digitos = 0

    print("El titulo a procesar es:", titulo)

    #           12340
    # titulo = "hola mundo."
    for i in titulo:
        # i = h, o, l, a,  , m,

        # dentro de la palabra
        if i != " " and i != ".":
            indice += 1

            # if i.lower() == "r":
            if i in "rR" and (indice == 2 or indice == 3):
                cont_r_pos2_pos3 += 1

            if i in "0123456789":
                cont_digitos += 1

        # fuera de la palabra / termino  una palabra
        else:
            if cont_r_pos2_pos3 > 0 and cont_digitos == 0:
                cantidad_palabras += 1

            # apagar las banderas
            cont_r_pos2_pos3 = 0
            indice = 0
            cont_digitos = 0

    print("la cantidad de palabras que cumplen:", cantidad_palabras)


# ===========================================================================
#                           Opcion 7
# ===========================================================================
def busqueda_secuencial(v_proyectos, tit):
    pos = -1
    for i in range(len(v_proyectos)):
        # i = 0, 1, 2, 3...

        if v_proyectos[i].titulo == tit:
            pos = i
            break

    return pos      # -1 es cuando no existe, si pos es 0 o mas es porque si existe


def busqueda_secuencial_retorna_titulo(v_proyectos, tit):
    titulo = "Articulo inexistente!"
    for i in range(len(v_proyectos)):
        # i = 0, 1, 2, 3...

        if v_proyectos[i].titulo == tit:
            titulo = v_proyectos[i].titulo
            # pos = i
            break

    return titulo


def busqueda_secuencial_mas_de_un_resultado(v_proyectos, tit):
    # buscar un titulo "tit" pero debe mostrar todos los resultados posibles si existieran aumenten todos
    # los importes de los que se mostraron en un 10%, al final
    # informar si no encontro ningun resultado

    se_encontro = False

    for i in range(len(v_proyectos)):
        # i = 0, 1, 2, 3...

        if v_proyectos[i].titulo == tit:
            print(v_proyectos[i])

            v_proyectos[i].importe += v_proyectos[i].importe * 0.1

            se_encontro = True

    if se_encontro is False:     # esta en falso
        print("No se encontro ningun resultado")


# ===========================================================================
#                           Opcion 8
# ===========================================================================
def generar_vector_acum(v_proyectos):
    """
    determinar y mostrar la sumatora de importes por cada posible laboratorio
    # laboratorio(3, 5) = lim_superior - lim_inferior + 1 = 3
    """

    # generar vector acum
    # laboratorio(3, 5)    3-3      4-3      5-3
    # indices               0        1       2
    # v_acum =              [0,       0,      0]

    v_acum = [0] * 3

    #
    # rellenar el vector acum

    # v_proyectos = [P1, P2, P3]
    for i in v_proyectos:
        # i = p1, p2, p3
        v_acum[i.laboratorio - 3] += i.importe

        # v_acum[i.laboratorio] += 1        # cantidad

    #
    # mostrar el vector acum
    for i in range(len(v_acum)):
        # i =  0, 1, 2
        print("Laboratorio:", i + 3, "- acumulado de importe:", v_acum[i])


# ===========================================================================
#                           Opcion 9
# ===========================================================================
def mostrar_archvo_binario_op9(fd, tit):

    bandera = os.path.exists(fd)  # retorna true si existe, False si no existe

    if bandera is False:
        print("no existe el archivo:", fd)
        return  # cortar la funcion

    m = open(fd, "rb")
    tamanio = os.path.getsize(fd)

    #
    # buscar un titulo "tit" y solo mostrar ese archivo y termina de leer el archivo

    while m.tell() < tamanio:
        proy = pickle.load(m)
        # proy = P1, P2, P3, P4

        if proy.titulo == tit:
            print(proy)
            break

    m.close()       # OBLIGATORIO


def menu():
    print("1 - Cargar arreglo.")
    print("2 - Mostrar arreglo.")
    print("3 - generar archivo binario.")
    print("4 - mostrar archivo binario.")
    print("5 - busqueda binaria.")
    print("6 - procesar cadena.")
    print("7 - busqueda secuencial (uno solo).")
    print("8 - vector acum/conteo.")

    print("9 - archivo con busqueda")

    print("0 - Salir.")

    op = int(input("Ingresar opción: "))
    return op


def principal():

    # vector de trabajo
    v_proyectos = []

    # opcion (generar archivo)
    fd = "proyectos.dat"

    # para verificar opcion 6
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
                print("El arreglo no esta cargado.")

        elif op == 3:
            if len(v_proyectos) > 0:
                generar_archivo_binario(v_proyectos, fd)

            else:
                print("El arreglo no esta cargado.")

        elif op == 4:
            mostrar_archivo_binario(fd)

        elif op == 5:
            if len(v_proyectos) > 0:
                c = int(input("ingresar codigo a buscar: "))
                titulo = busqueda_binaria(v_proyectos, c)

            else:
                print("El arreglo no esta cargado.")

        elif op == 6:
            if titulo is None:
                print("Debe ingresar primero a la opcion 5.")

            else:
                analisis_cadena(titulo)

        elif op == 7:
            # buscar el titulo "tit" y detener la busqeuda al primer resultado y modifcar su valor
            # de importe con un descuento del 22%
            tit = input("Ingresar titulo a buscar: ")
            pos = busqueda_secuencial(v_proyectos, tit)

            # pos   2
            # indices         0   1    2
            # v_proyectos = [ P1, P2 , P3 ]

            if pos >= 0:
                print("Datos sin acutalizar:", v_proyectos[pos])

                # realizar al importe un descuento del 22%
                v_proyectos[pos].importe += v_proyectos[pos].importe * 0.22

                print("Datos acutalizados:", v_proyectos[pos])

                # solo mostrar su laboratorio
                print("laboratorio:", v_proyectos[pos].laboratorio)

            else:
                print("no existe!")

        elif op == 8:
            generar_vector_acum(v_proyectos)


        elif op == 9:
            # buscar un titulo guardado dentro del archivo y mostrar solamente ese
            tit = input("Ingresar titulo: ")
            mostrar_archvo_binario_op9(fd, tit)


if __name__ == "__main__":
    principal()










