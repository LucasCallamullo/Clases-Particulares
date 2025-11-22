import os.path
import pickle
import random
from registro import *


# ===========================================================================
#                               Opcion 1
# ===========================================================================
def validar_n():
    n = int(input("ingresar cantida de proyectos a cargaR: "))
    while n <= 0:
        n = int(input("ingresar cantida de proyectos a cargaR: "))
    return n


def cargar_arreglo(v_proyectos, n):
    tupla_titulos = ("Proyecto 1.", "Proyecto 2.", "Proyecto 3.")

    tupla = (True, False)

    # codigo INT, titulo STR, importe FLOAT, cant_inv INT, disponible BOOL
    # laboratorio (3, 5), zona(10, 15)
    for i in range(n):      # NO SE OLVIDEN

        codigo = random.randint(1, 10)

        # titulo = random.choice("ABCDEF")
        titulo = "Este es el " + random.choice(tupla_titulos)       # a partir de ahora los str se hacen como oraciones

        importe = round(random.uniform(0.1, 10), 2)
        cant_inv = random.randint(1, 10)
        disponible = random.choice(tupla)                       # bool
        laboratorio = random.randint(3, 5)
        zona = random.randint(10, 15)

        proy = Proyecto(codigo, titulo, importe, cant_inv, disponible, laboratorio, zona)

        add_in_order(v_proyectos, proy)


def add_in_order(v_proyectos, proy):
    izq, der = 0, len(v_proyectos) - 1

    while izq <= der:

        c = (izq + der) // 2
        if v_proyectos[c].codigo == proy.codigo:
            pos = c
            break

        # la boquita ">" determina si esta de menor a mayor o mayor a menor
        elif v_proyectos[c].codigo > proy.codigo:
            der = c - 1

        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v_proyectos[pos:pos] = [proy]


# ===========================================================================
#                               Opcion 2
# ===========================================================================
def mostrar_datos(v_proyectos):

    # Indique al final del listado la cantidad total de investigadores que trabajan entre
    # todos los proyectos que se mostraron
    acum = 0

    # indices           0       1       2
    # v_proyectos = [   P1,   P2,     P3 ]
    for i in v_proyectos:
        # i = P1,       P2,     P3
        print(i)
        acum += i.cant_inv

    print("el acumulado cant_inv es:", acum)


# ===========================================================================
#                               Opcion 3
# ===========================================================================
def generar_archivo_binario(v_proyectos, fd):
    """
    generar un archivo binario que contenga todos aquellos proyectos que superen el importe promedio
    de los importes de los proyectos dentro del arreglo

    paso 1: calcular el importe promedio
    paso 2: generar archivo binario comparando con el promedio
    """
    # calcular el importe
    # prom = acumulado ( de importes ) / cantidad de veces que acumule
    acum = 0
    cont = 0

    for i in v_proyectos:
        # i = P1, P2, P3
        acum += i.importe
        cont += 1

    # calcular el promedio
    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio es:", prom)

    # guardar el archivo
    m = open(fd, "wb")

    for i in v_proyectos:
        if i.importe > prom:
            pickle.dump(i, m)

    m.close()


# ===========================================================================
#                               Opcion 4
# ===========================================================================
def mostrar_archivo_binario(fd):
    bandera = os.path.exists(fd)    # retorna true si existe el arhcivo, FALSE si no eixste
    if bandera is False:
        print("El archivo no existe:", fd)
        return      # cortar la funcion

    m = open(fd, "rb")
    tamanio = os.path.getsize(fd)

    # calcular promedio de los importes mostrados
    # prom = acumulado ( de importes ) / cantidad de veces qe acumule
    acum = cont = 0

    while m.tell() < tamanio:
        proy = pickle.load(m)
        # proy = P1, P2, P3
        print(proy)

        acum += proy.importe
        cont += 1

    # calcular el promedio
    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio es:", prom)

    m.close()       # OBLIGATORIO


# ===========================================================================
#                               Opcion 5
# ===========================================================================
def busqueda_binaria(v_proyectos, c):
    """
    Busqueda binaria es cuando te piden buscar por el mismo atributo por el que esta ordenado

    Ejemplo en el punto 1 esta ordenado por "codigo", y en el punto que te pide buscar te piden buscar
    ese mismo atributo "codigo"
    """
    izq, der = 0, len(v_proyectos) - 1

    while izq <= der:

        c = (izq + der) // 2
        # if v_proyectos[c].codigo == proy.codigo:
        if v_proyectos[c].codigo == c:      # aca es cuando se encuentra un objeto que cumple
            # pos = c
            # break

            # caso: mostrar datos
            print(v_proyectos[c])       # referencia al objeto completo es: v_proyectos[c]

            # caso: mostrar solo el titulo
            # print("Titulo:", v_proyectos[c].titulo)

            # retornar el título del mismo para utilizar luego en el ítem 6
            return v_proyectos[c].titulo

        # elif v_proyectos[c].codigo > proy.codigo:
        elif v_proyectos[c].codigo > c:
            der = c - 1

        else:
            izq = c + 1

    # fuera del while es cuando no se encuentra el objeto como tal
    mensaje = "Artículo inexistente!."
    print(mensaje)

    # y retornar ese mismo mensaje para ser usado en el punto 6
    return mensaje


# ===========================================================================
#                               Opcion 6
# ===========================================================================
def procesar_cadena(titulo):
    """
    #12340120120123456780
    ¿Cuál es la cantidad de palabras de esa cadena que contienen una letra "r" en la segunda o
    en la tercera posición (en mayúsculas o minúsculas) y que además no contienen ningún dígito?
    """
    # titulo = "Artículo inexistente!."
    r1 = 0      # la cantidad de palabras que cumplen
    indice = 0
    # cont_r_pos2_pos3 = 0
    tiene_r_pos2_pos3 = False
    tiene_digito = False

    for i in titulo:
        # i = A, r, t, i, c, ...

        # dentro de la palabra
        if i != " " and i != ".":
            indice += 1

            # si la posicion es la 2 o la 3
            if (indice == 2 or indice == 3) and i.lower() == "r":
                tiene_r_pos2_pos3 = True

            # además no contienen ningún dígito
            if i in "0123456789":   # si la "i" esta en..
                tiene_digito = True

        # fuera de la palabra
        else:
            # tiene r en pos 2 o 3, y no tiene digito
            # if tiene_r_pos2_pos3 and not tiene_digito:
            if tiene_r_pos2_pos3 is True and tiene_digito is False:
                r1 += 1

            # reinicar contadores / banderas
            indice = 0
            # cont_r_pos2_pos3 = 0
            tiene_r_pos2_pos3 = False
            tiene_digito = False


# ===========================================================================
#                               Opcion 7
# ===========================================================================
def busqueda_secuencial(v_proyectos, tit, s):

    for i in range(len(v_proyectos)):
        # i = 0, 1, 2, 3
        # v_proyectos[i] --> referencia al objeto en este tipo de ciclo for

        if v_proyectos[i].titulo == tit and v_proyectos[i].cant_inv > s:
            # si existe modificar su importe por un nuevo valor "x" que se carga por teclado,
            # mostrar los datos del proyecto antes y despues del cambio

            # mostrar datos antes del cambio
            print("Sin cambios: ", v_proyectos[i])

            # modificar por un nuevo valor "x" que se carga por teclado
            x = int(input("Ingresar nuevo importe: "))
            v_proyectos[i].importe = x

            # aumentar un 25% el valor del importe
            # v_proyectos[i].importe += v_proyectos[i].importe * 0.25

            # descontar un 25% el valor del importe
            # v_proyectos[i].importe -= v_proyectos[i].importe * 0.25

            # mostrar datos despues del cambio
            print("Con cambios: ", v_proyectos[i])

            return  # detener la busqueda

    # no existe cuando sale del ciclo for
    print("No existe.")


# ===========================================================================
#                               Opcion 8
# ===========================================================================
def generar_vector_conteo(v_proyectos, x1, x2):
    # determinar y mostrar la cantidad de proyectos por cada zona posible
    # solo mostrar los contadores que estan entre x1 y x2

    # generar el vector
    # cantidad de "zona" posible ( zona ( 10, 15 ) = 15 - 10 + 1 = 6

    # zona(10, 15)  10  11 12 13 14 15
    # indices        0  1  2  3  4  5
    # v_conteo =    [0, 0, 0, 0, 0, 0]
    v_conteo = [0] * 6

    # rellenar el vector
    for i in v_proyectos:
        # i --> hace referencia al objeto
        # i = p1, p2, p3

        # determinar y mostrar la cantidad de proyectos por cada zona posible
        v_conteo[i.zona - 10] += 1

        # determinar y mostrar la acumulacion de importes de los proyectos por cada zona posible
        # v_conteo[i.zona - 10] += i.importe

    # mostrar el vector
    for i in range(len(v_conteo)):
        # i = 0, 1, 2, 3
        # la i esta haciendo referencia a los indices del vector
        # pero los indices hacen referencia a la "zona"

        # v_conteo[i] --> al contador

        # mostrar los contadores que estan entre x1 y x2
        if x1 < v_conteo[i] < x2:
            print("Zona:", i+10, " - Cantidad:", v_conteo[i])

        # mostrar solamente la zona 13 y 14
        if i+10 == 13 or i+10 == 14:
            print("Zona:", i + 10, " - Cantidad:", v_conteo[i])



def menu():
    print("1 - Cargar arreglo.")
    print("2 - Mostrar arreglo.")
    print("3 - generar archivo binario.")
    print("4 - mostrar archivo binario.")
    print("5 - busqueda binaria.")
    print("6 - procesar cadena.")
    print("7 - busqueda secuencial.")

    print("0 - Salir.")

    op = int(input("Ingresar opción: "))
    return op


def principal():

    # vector de trabajo
    v_proyectos = []

    # punto de archivos binarios
    fd = "proyectos.dat"

    # para verificar si pase por la op 5
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
            if len(v_proyectos) == 0:
                print("El arreglo no esta cargado.")

            else:
                # el input solo es un STR
                # el int(input(  para pedir un INT  - entero - integer
                c = int(input("ingresar codigo a buscar: "))

                # que si una variable esta igualada a un funcion es porque espera que la funcion retorne algo
                titulo = busqueda_binaria(v_proyectos, c)

        elif op == 6:
            if titulo is None:
                print("Debe pasar primero por la op 5.")
            else:
                procesar_cadena(titulo)
                # la parte de pasar el parametro a analizar la cadena

                # analizar (algun atributo siempre) "titulo" del primer objeto del arreglo
                # titulo = v_proyectos[0].titulo
                # procesar_cadena(titulo)

                # analizar (algun atributo siempre) "titulo" del ultimo objeto del arreglo
                # ultimo = len(v_proyectos) - 1
                # titulo = v_proyectos[ultimo].titulo
                # procesar_cadena(titulo)

                # analizar (algun atributo siempre) "titulo" del objeto central del arreglo
                # centro = len(v_proyectos) // 2
                # titulo = v_proyectos[centro].titulo
                # procesar_cadena(titulo)

        elif op == 7:
            if len(v_proyectos) == 0:
                print("El arreglo no esta cargado.")

            else:
                # buscar un titulo "tit" y que ademas tenga un cant_inv mayor "s"
                # dentro del arreglo detenerse al primer resultado
                # y si existe modificar su importe por un nuevo
                # valor "x" que se carga por teclado, mostrar el proyecto antes y despues del cambio
                tit = input("Ingresar titulo a buscar: ")   # STR
                s = int(input("Ingresar cant_inventario: "))
                busqueda_secuencial(v_proyectos, tit, s)


        elif op == 8:
            if len(v_proyectos) == 0:
                print("El arreglo no esta cargado.")

            else:
                # determinar y mostrar la cantidad de proyectos por cada zona posible
                # solo mostrar los contadores que estan entre x1 y x2
                x1 = int(input("Ingresar cantidad de proyectos a superar: "))
                x2 = int(input("Ingresar cantidad de proyectos a ser menor: "))
                generar_vector_conteo(v_proyectos, x1, x2)


if __name__ == "__main__":
    principal()
