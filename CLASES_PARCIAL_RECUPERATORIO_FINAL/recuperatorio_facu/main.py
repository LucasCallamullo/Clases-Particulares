import os.path
import pickle
import random

# from registro import *
import registro


# ===========================================================================
#                                   Opcion 1
# ===========================================================================
def validar_n():

    n = int(input("Ingresar cantidad de proyectos a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de proyectos a cargar: "))
    return n


def cargar_arreglo(v_proyectos, n):
    titulos = ("Titulo 1", "Titulo 2", "Titulo 3")

    # codigo INT, titulo STR que termina ".", importe FLOAT, cantidad INT, laboratorio(3, 5), calle(10, 15)
    for i in range(n):
        codigo = random.randint(1, 10)
        titulo = "Este es el " + random.choice(titulos) + "."
        importe = round(random.uniform(0.1, 10), 2)     # FLOAT con 2 decimales
        cantidad = random.randint(1, 10)
        laboratorio = random.randint(3, 5)
        calle = random.randint(10, 15)

        proy = registro.Proyecto(codigo, titulo, importe, cantidad, laboratorio, calle)
        add_in_order(v_proyectos, proy)


def add_in_order(v_proyectos, proy):
    izq, der = 0, len(v_proyectos) - 1

    while izq <= der:

        c = (izq + der) // 2

        # te pueden cambiar el atributo por el que te piden ordenar
        if v_proyectos[c].codigo == proy.codigo:
            pos = c
            break

        # la boquita ">" indica si esta ordenador de menor a mayor o mayor a menor
        elif v_proyectos[c].codigo > proy.codigo:
            der = c - 1

        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v_proyectos[pos:pos] = [proy]


# ===========================================================================
#                                   Opcion 2
# ===========================================================================
def mostrar_datos(v_proyectos):

    # Indique al final del listado la cantidad promedio de investigadores que trabajan entre
    # todos los proyectos que se mostraron.

    # promedio = acumulado (de cantidad) /   cantidad de veces que acumule
    acum = 0
    cant = 0

    # v_proyectos = [   P1,     P2,     P3]
    for i in v_proyectos:
        # i = P1, P2

        print(i)

        acum += i.cantidad
        cant += 1

    # calcular el promedio
    prom = 0
    if cant > 0:
        prom = acum / cant

    print("el promedio de investigadores es:", prom)


# ===========================================================================
#                                   Opcion 3
# ===========================================================================
def generar_archivo_binario(fd, v_proyectos):
    """
    3 - generar un archivo binario donde solo se guarden los proyectos que superen el importe
    promedio dentro del arreglo
    """
    # promedio = acumulado ( de importes ) / la cantidad de veces que acumule
    acum = cont = 0

    for i in v_proyectos:
        # i = P1, P2, P3
        acum += i.importe
        cont += 1

    # calcular el promedio
    prom = 0
    if cont > 0:
        prom = acum / cont

    print("el promedio de importe es:", prom)

    # punto 4 generico
    m = open(fd, "wb")
    # "wb" = write binary = crea el archivo si no existe, borra todo el contenido y crea nuevo contenido
    # "ab" = append binary = crea el archivo si no existe, agrega contenido al final del archivo

    for i in v_proyectos:
        # i = p1, p2, p3

        if i.importe > prom:
            pickle.dump(i, m)

    m.close()       # OBLIGATORIO


# ===========================================================================
#                                   Opcion 4
# ===========================================================================
def mostrar_archivo_binario(fd, l1, l2):

    bandera = os.path.exists(fd)    # si existe el archivo retorna TRUE, si no existe FALSE
    if bandera is False:        # if not bandera
        print("no existe el archivo:", fd)
        return      # cortar la funcion

    m = open(fd, "rb")
    tam = os.path.getsize(fd)

    while m.tell() < tam:

        proy = pickle.load(m)
        # proy = P1, P2, P3

        # si esta entre l1 y l2 (laboratorios) lo printeo
        if l1 <= proy.laboratorio <= l2:
            print(proy)

    m.close()       # OBLIGATORIO


# ===========================================================================
#                                   Opcion 5
# ===========================================================================
def busqueda_binaria(v_proyectos, codigo):      # codigo = 6

    # indices           0       1       2
    # v_proyectos = [   P1,     P2,     P3 ]
    # codigo            2       4       6

    izq, der = 0, len(v_proyectos) - 1
    # izq = 2
    # der = 2

    while izq <= der:

        c = (izq + der) // 2        # centro , center   c = 2

        # if v_proyectos[c].codigo == proy.codigo:
        if v_proyectos[c].codigo == codigo:
            # pos = c     # c = pos = 2
            # break
            print(v_proyectos[c])
            return v_proyectos[c].titulo        # retornar el titulo

        # elif v_proyectos[c].codigo > proy.codigo:
        elif v_proyectos[c].codigo > codigo:
            der = c - 1

        else:
            izq = c + 1

    return "Artículo inexistente!."     # retorna str


# ===========================================================================
#                                   Opcion 6
# ===========================================================================
def analisis_cadena(titulo):
    """
    ¿Cuál es la cantidad de palabras de esa cadena que contienen una letra "r" en la segunda o
    en la tercera posición (en mayúsculas o minúsculas) y que además no contienen ningún dígito (numero)?

    # 123456012340
    # titulo hola.

    cant = 0

    indice = 0
    cont_r_pos2_pos3 = 0
    cont_digitos = 0
    """

    # titulo = "Artículo inexistente!."
    print("el titulo a a analizar es:", titulo)

    cant = 0

    indice = 0
    cont_r_pos2_pos3 = 0
    cont_digitos = 0

    for i in titulo:
        #     1  2  3
        # i = A, r, t, i, c, u, l, o,  , i,

        # dentro de la palabra
        if i != " " and i != ".":

            indice += 1

            if i.lower() == "r" and (indice == 2 or indice == 3):
                cont_r_pos2_pos3 += 1

            if i in "0123456789":
                cont_digitos += 1

        # fuera de la palabra / termino una palabra
        else:

            if cont_r_pos2_pos3 > 0 and cont_digitos == 0:
                cant += 1

            # apagar banderas / contadores
            indice = 0
            cont_r_pos2_pos3 = 0
            cont_digitos = 0

    print("las palabras que cumplen:", cant)


# ===========================================================================
#                                   Opcion 7
# ===========================================================================
def busqueda_secuencial(v_proyectos, tit):

    pos = -1
    for i in range(len(v_proyectos)):
        # i = 0, 1 , 2 , 3 ...

        if v_proyectos[i].titulo == tit:
            pos = i
            break

    return pos  # retorna 0 o más es porque existe el objeto
    # retorna -1 no existe objeto que cumpla


# ===========================================================================
#                                   Opcion 8
# ===========================================================================
def vector_de_acum(v_proyectos, x):
    # determinar el acumulado total de investigadores por cada posible laboratorio
    # solo mostrar los que superan un acumulado "x"

    #
    # crear vector acum
    # cantidad de laboratorios ( 3, 5 ) = lim_superior - lim_inferior + 1 = 5 - 3 + 1 = 3
    v_acum = [0] * 3

    # laboratorio(3, 5)    3-3       4       5
    # indices               0      1       2
    # v_acum            = [ 0,     0,      0 ]

    # rellenas el vector
    for i in v_proyectos:
        v_acum[i.laboratorio - 3] += i.cantidad

    # mostrar_la matriz
    for i in range(len(v_acum)):
        # i = 0, 1, 2

        # solo mostrar los que superan un acumulado "x"
        if v_acum[i] > x:
            print("Laboratorio:", i+3, "- Acumulado investigadores:", v_acum[i])


# ===========================================================================
#                                   MENU
# ===========================================================================
def menu():
    print("1 - Cargar arreglo.")
    print("2 - Mostrar arreglo.")
    print("3 - crear archivo binario.")
    print("4 - mostrar archivo binario.")
    print("5 - busqueda binario.")
    print("6 - analisis cadena.")

    op = int(input("Ingresar opción: "))
    return op


def principal():

    # vector lista arreglo
    v_proyectos = []

    # nombre del archivo
    fd = "proyectos.dat"        # .dat o .bin

    # opcion 6
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
                print("el vector no esta cargado.")

        elif op == 3:
            if len(v_proyectos) > 0:
                generar_archivo_binario(fd, v_proyectos)
            else:
                print("el vector no esta cargado.")

        elif op == 4:
            # solo mostrar los proyectos que estan entre los laboratorios l1 y l2 inbcluidos ambos
            l1 = int(input("Ingresar laboratorio a superar: "))
            l2 = int(input("Ingresar laboratorio a ser menor: "))
            mostrar_archivo_binario(fd, l1, l2)

        elif op == 5:
            if len(v_proyectos) > 0:
                c = int(input("Codigo a buscar: "))
                titulo = busqueda_binaria(v_proyectos, c)
            else:
                print("el vector no esta cargado.")

        elif op == 6:
            if titulo is None:
                print("Pase por la opcion 5.")

            else:
                analisis_cadena(titulo)

        elif op == 7:
            """ 
            buscar por titulo "tit", detener la busqueda al primer resultado
            
            si existe mostrar sus datos antes y despues de actualizar su valor de importe por
            un descuento del 22 por ciento....
            
            si no existe informar
            """
            tit = input("Titulo a buscar: ")
            pos = busqueda_secuencial(v_proyectos, tit)

            if pos >= 0:
                print("datos sin actualizar", v_proyectos[pos])

                v_proyectos[pos].importe -= v_proyectos[pos].importe * 0.22

                print("datos actualizados", v_proyectos[pos])

                #
                # cambiar su importe por un valor x que se carga por teclado
                x = float(input("Ingresar nuevo importe: "))
                v_proyectos[pos].importe = x

                #
                # solo mostrar su titulo y su laboratorio
                print("Titulo:", v_proyectos[pos].titulo, "y su laboratorio:", v_proyectos[pos].laboratorio)

            else:       # cuandop pos  =  -1
                print("No existe!")

        elif op == 8:
            # determinar el acumulado total de investigadores por cada posible laboratorio
            # solo mostrar los que superan un acumulado "x"
            x = int(input("Ingresar acumulado a superar: "))
            vector_de_acum(v_proyectos, x)


if __name__ == "__main__":
    principal()
