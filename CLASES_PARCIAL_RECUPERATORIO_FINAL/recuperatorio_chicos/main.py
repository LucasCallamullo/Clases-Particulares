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
        titulo = "Este es el " + random.choice(tupla_titulos)
        importe = round(random.uniform(0.1, 10), 2)
        cant_inv = random.randint(1, 10)
        disponible = random.choice(tupla)
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
def busqueda_binaria(v_proyectos, cod):
    izq, der = 0, len(v_proyectos) - 1

    while izq <= der:

        c = (izq + der) // 2
        # if v_proyectos[c].codigo == proy.codigo:
        if v_proyectos[c].codigo == cod:
            pos = c
            # break
            print(v_proyectos[pos])     # para mostrar los datos del proyecto que se encontro
            return v_proyectos[pos].titulo      # para retornar el titulo como tal

        # la boquita ">" determina si esta de menor a mayor o mayor a menor
        # elif v_proyectos[c].codigo > proy.codigo:
        elif v_proyectos[c].codigo > cod:
            der = c - 1

        else:
            izq = c + 1

    return "Articulo Inexistente!."


# ===========================================================================
#                               Opcion 6
# ===========================================================================
def procesar_cadena(titulo):
    """
    # indice     123401
                ¿Cuál es la cantidad de palabras de esa cadena que contienen una letra "r" en la segunda
    o en la tercera posición (en mayúsculas o minúsculas) y que además no contienen ningún dígito?

    cantidad_palabras = 0

    cont_r_pos2_pos3 = 0
    indice = 0

    cont_digitos = 0
    """
    cantidad_palabras = 0

    cont_r_pos2_pos3 = 0
    indice = 0

    cont_digitos = 0

    print("cadena a analizar:", titulo)

    # procesar cadena

    # titulo = "hola mundo."
    for i in titulo:
        # i = h, o, l, a,  , m, ...

        # dentro de la palabra
        if i != " " and i != ".":
            indice += 1

            # if i.lower() == "r"
            if i in "rR" and (indice == 2 or indice == 3):
                cont_r_pos2_pos3 += 1

            if i in "0123456789":
                cont_digitos += 1

        # fuera de la palabra/ termino una palabra
        else:

            if cont_r_pos2_pos3 > 0 and cont_digitos == 0:
                cantidad_palabras += 1

            # apagar la banderas
            cont_r_pos2_pos3 = 0
            indice = 0
            cont_digitos = 0

    print("la cantidad de palabras que cumplen:", cantidad_palabras)


# ===========================================================================
#                               Opcion 7
# ===========================================================================
def busqueda_secuencial(v_proyectos, tit):

    pos = -1
    for i in range(len(v_proyectos)):
        # i = 0, 1, 2, 3,
        if v_proyectos[i].titulo == tit:
            pos = i
            break       # poara que se detenga al primer resultado

    return pos      # -1 es cuando no existe, pos >= 0 significa que encontro resultado


def busqueda_secuencial_retornas_titulo(v_proyectos, tit):
    titulo = "Articulo Inexistente!."
    for i in range(len(v_proyectos)):
        # i = 0, 1, 2, 3,
        if v_proyectos[i].titulo == tit:
            titulo = v_proyectos[i].titulo
            break  # poara que se detenga al primer resultado

    return titulo  # -1 es cuando no existe, pos >= 0 significa que encontro resultado


def busqueda_secuencial_mostrar_varios_resultados(v_proyectos, tit):
    # buscar y mostrar todos los proyectos que tengan un titulo tit y si no existe ninguno informar

    se_encontro = False

    for i in range(len(v_proyectos)):
        # i = 0, 1, 2, 3,
        if v_proyectos[i].titulo == tit:
            print(v_proyectos[i])
            se_encontro = True

    if se_encontro is False:
        print("No se encontro ningun titulo con ese tit.")


# ===========================================================================
#                               Opcion 8
# ===========================================================================
def generar_vector_conteo(v_proyectos, x1, x2):

    # generar vector conteo
    # zona(10, 15) = lim_superior - lim_inferior + 1 = 15 - 10 + 1 = 6

    v_conteo = [0] * 6       # se multiplica por la cantidad posibles de zona

    # zona       10-10 11 12
    # indices      0  1   2 ...
    # v_conteo = [ 0, 0 , 0, , 0

    # rellenar el vector
    for i in v_proyectos:
        # i = P1, P2, P3
        v_conteo[i.zona - 10] += 1      # cantidad
        # v_conteo[i.zona - 10] += i.importe      # sumatoria importes

    # mostrar el vector
    for i in range(len(v_conteo)):
        # i = 0, 1, 2, 3, 4, 5

        # solo mostrar los contadores que estan entre x1 y x2
        if x1 <= v_conteo[i] <= x2:
            print("Zona:", i + 10, "- Cantidad:", v_conteo[i])

        # solo mostrar la zona 15 o más
        # if i+10 >= 15:
        #    print("Zona:", i + 10, "- Cantidad:", v_conteo[i])



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
            if len(v_proyectos) > 0:
                c = int(input("ingresar codigo a buscar: "))
                titulo = busqueda_binaria(v_proyectos, c)

            else:
                print("El arreglo no esta cargado.")

        elif op == 6:
            if titulo is None:
                print("Debe pasar primero por la op 5.")
            else:
                procesar_cadena(titulo)

        elif op == 7:
            # buscar un titulo "tit" dentro del arreglo detenerse al primer resultado
            # y si existe modificar su importe por un nuevo
            # valor "x" que se carga por teclado, mostrar el proyecto antes y despues del cambio
            tit = input("Ingresar titulo a buscar: ")
            pos = busqueda_secuencial(v_proyectos, tit)

            if pos >= 0:
                print("Datos sin actualizar: ", v_proyectos[pos])

                x = float(input("ingresar nuevo importe: "))
                v_proyectos[pos].importe = x

                print("Datos actualizados: ", v_proyectos[pos])

                # realizar un descuento del 28%
                v_proyectos[pos].importe -= v_proyectos[pos].importe * 0.28

            else:
                print("No existe!")

        elif op == 8:
            if len(v_proyectos) > 0:
                # determinar y mostrar la cantidad de proyectos por cada zona posible
                # solo mostrar los contadores que estan entre x1 y x2
                x1 = int(input("Ingresar cantidad de proyectos a superar: "))
                x2 = int(input("Ingresar cantidad de proyectos a ser menor: "))
                generar_vector_conteo(v_proyectos, x1, x2)

            else:
                print("El arreglo no esta cargado.")


if __name__ == "__main__":
    principal()
