import os.path
import pickle
import random
from registro import *


# ===========================================================================
#                       Opcion 1
# ===========================================================================
def validar_n():
    n = int(input("Ingresar cantidad de proyectos a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de proyectos a cargar: "))
    return n


def cargar_arreglo(v_proyectos, n):
    tupla_titulos = ("Proyecto 1.", "Proyecto 2."," Proyecto 3.")
    tupla_bools = (True, False)

    # codigo INT, titulo STR, importe FLOAT, cant_inv INT, laboratorio(5, 8), zona(10, 15), disponible BOOL
    for i in range(n):
        codigo = random.randint(1, 15)
        titulo = "Este es el " + random.choice(tupla_titulos)
        importe = round(random.uniform(0.1, 10), 2)
        cant_inv = random.randint(1, 10)

        laboratorio = random.randint(5, 8)
        zona = random.randint(10, 15)
        disponible = random.choice(tupla_bools)

        nuevo_proyecto = Proyecto(codigo, titulo, importe, cant_inv, laboratorio, zona, disponible)
        add_in_order(v_proyectos, nuevo_proyecto)


def add_in_order(v_proyectos, nuevo_proyecto):
    izq, der = 0, len(v_proyectos) - 1

    while izq <= der:

        c = (izq + der) // 2

        if v_proyectos[c].codigo == nuevo_proyecto.codigo:
            pos = c
            break

        elif v_proyectos[c].codigo > nuevo_proyecto.codigo:
            der = c - 1

        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v_proyectos[pos:pos] = [nuevo_proyecto]


# ===========================================================================
#                       Opcion 2
# ===========================================================================
def mostrar_datos(v_proyectos, x):

    # indices           0   1   2
    # v_proyectos = [   P1, P2, P3 ]

    for i in v_proyectos:
        # i = P1, P2, P3

        # solo mostrar los que tengan un importe mayor a x
        if i.importe > x:
            print(i)


# ===========================================================================
#                       Opcion 3
# ===========================================================================
def generar_archivo_binario(v_proyectos, fd):
    """
    guardar en un archivo binario todos los proyectos que superen el importe promedio dentro del arreglo de
    registros.
    """
    # calcular el promedio
    # prom = acumulado ( de importes ) / cantidad de veces que acumule
    acum = 0
    cont = 0

    for i in v_proyectos:
        # i = P1, P2, P3
        acum += i.importe
        cont += 1

    # calcular promedio
    prom = 0
    if cont > 0:
        prom = acum / cont

    print("El promedio importe es: ", prom)

    # guardar archivo
    m = open(fd, "wb")

    for i in v_proyectos:
        # i = P1, P2, P3
        if i.importe > prom:
            pickle.dump(i, m)
            # m.flush()

    # print("se genero archivop")
    m.close()   # OBLIGATORIO


# ===========================================================================
#                       Opcion 4
# ===========================================================================
def mostrar_archivo(fd):

    if os.path.exists(fd) is False:
        print("No existe el archivo:", fd)
        return          # corta la funcion directamente

    #
    m = open(fd, "rb")
    tamanio = os.path.getsize(fd)

    # calcular el promedio de cantidad de investigadores de los laboratorios 5 y 6 guardados
    # dentro del archivo
    # promedio = acumulado ( de cant_inv ) / cantidad de veces que acumule
    acum = cont = 0

    while m.tell() < tamanio:

        proy = pickle.load(m)
        # proy = P1,    P2,     P3

        print(proy)

        if proy.laboratorio == 5 or proy.laboratorio == 6:
            acum += proy.cant_inv
            cont += 1

    # calcular promedio
    prom = 0
    if cont > 0:
        prom = acum / cont

    print("El promedio cant_inv es: ", prom)

    m.close()       # OBLIGATORIO


# ===========================================================================
#                       Opcion 5
# ===========================================================================
def busqueda_binaria(v_proyectos, cod):
    izq, der = 0, len(v_proyectos) - 1

    while izq <= der:

        c = (izq + der) // 2

        # if v_proyectos[c].codigo == nuevo_proyecto.codigo:
        if v_proyectos[c].codigo == cod:
            pos = c
            # break
            print(v_proyectos[pos])         # mostrar los datos
            return v_proyectos[pos].titulo      # retornar el titulo

        # elif v_proyectos[c].codigo > nuevo_proyecto.codigo:
        elif v_proyectos[c].codigo > cod:
            der = c - 1

        else:
            izq = c + 1

    return "Artículo inexistente!."


# ===========================================================================
#                       Opcion 6
# ===========================================================================
def procesar_cadena(titulo):
    """
      1234012012
     ¿Cuál es la cantidad de palabras de esa cadena que contienen una letra "r" en la segunda o en
     la tercera posición (en mayúsculas o minúsculas) y que además no contienen ningún dígito (numeros)?

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

    #           12340123450
    # titulo = "Hola Mundo."

    for i in titulo:
        # i = H, o, l, a,  , M, u

        # estoy dentro de la palabra
        if i != " " and i != ".":

            indice += 1

            # if i.lower() == "r":
            if i in "rR" and (indice == 2 or indice == 3):
                cont_r_pos2_pos3 += 1

            # if i.isdigit():
            if i in "0123456789":            # si la i es igual a "algo de aca"
                cont_digitos += 1

            # si les pidieran vocales
            # if i in "aeiouáéíóú":

        # estoy fuera de la palabra / termino la palabra
        else:

            if cont_r_pos2_pos3 > 0 and cont_digitos == 0:
                cantidad_palabras += 1

            # apagar las banderas
            cont_r_pos2_pos3 = 0
            indice = 0
            cont_digitos = 0

    print("cantidad de palabras que cumplen:", cantidad_palabras)


# ===========================================================================
#                       Opcion 7
# ===========================================================================
def busqueda_secuencial(v_proyectos, tit):
    # buscar el titulo y mostrar todos los proyectos que tengan ese titulo
    # indique un mensaje si no existe ningun proyecto con ese titulo

    se_encontro = False

    for i in range(len(v_proyectos)):
        # i = 0, 1, 2, 3, 4
        if v_proyectos[i].titulo == tit:
            print(v_proyectos[i])
            se_encontro = True

    if se_encontro is False:        # if not se_encontro:
        print("No existe ese titulo dentro del arreglo")


def busqueda_secuencial_retorno_titulo(v_proyectos, tit):
    # buscar el titulo tit y mostrar sus datos y retornar su titulo, detenerse al primer resultado
    # retorne un mensaje "hola mundo." si no existe ningun proyecto con ese titulo

    for i in range(len(v_proyectos)):
        # i = 0, 1, 2, 3, 4
        if v_proyectos[i].titulo == tit:
            print(v_proyectos[i])       # mostramos sus datos
            return v_proyectos[i].titulo        # retorna el proyecto

    return "Hola mundo."


# ===========================================================================
#                       Opcion 8
# ===========================================================================
def generar_matriz_con_archivo(fd):
    """
    a partir del archivo binario generado, determinar y mostrar la cantidad posible por cada combinacion
    entre laboratorio y zona        # laboratorio(5, 8), zona(10, 15)
    """
    if os.path.exists(fd) is False:
        print("No existe el archivo:", fd)
        return          # corta la funcion directamente

    # generar_matriz
    f = 4    # f = laboratorio(5, 8) = 8 - 5 + 1 = 4
    c = 6    # c = zona(10, 15)
    matriz = [ [0] * c for i in range(f) ]

    # rellenar la matriz
    # for i in v_proyectos:
    #      matriz[i.laboratorio - 5][i.zona - 10] += 1

    m = open(fd, "rb")
    tamanio = os.path.getsize(fd)

    while m.tell() < tamanio:
        proy = pickle.load(m)
        # proy = P1,    P2,     P3
        matriz[proy.laboratorio - 5][proy.zona - 10] += 1

    m.close()       # OBLIGATORIO

    # mostrar la matriz
    for f in range(len(matriz)):
        for c in range(len(matriz[0])):

            # solo mostrar los laboratorios entre l1 y l2 ( ambos incluidos )
            # if l1 <= f+5 <= l2
            #    print("Laboratorio:", f+5, "- Zona:", c+10, "- Cantidad:", matriz[f][c])

            # solo mostrar los contadores mayores a cero
            if matriz[f][c] > 0:
                print("Laboratorio:", f + 5, "- Zona:", c + 10, "- Cantidad:", matriz[f][c])


# ===========================================================================
#                       Opcion 9
# ===========================================================================
def secuencial_con_archivo(fd, tit):
    """
    buscar un titulo tit en el archivo y detener la busqueda al primer resultado
    """
    if os.path.exists(fd) is False:
        print("No existe el archivo:", fd)
        return          # corta la funcion directamente

    m = open(fd, "rb")
    tamanio = os.path.getsize(fd)

    while m.tell() < tamanio:
        proy = pickle.load(m)
        # proy = P1,    P2,     P3

        if proy.titulo == tit:
            print(proy)
            break

    m.close()       # OBLIGATORIO



# ===========================================================================
#                       MENU
# ===========================================================================
def menu():
    print("1 - Cargar arreglo.")
    print("2 - Mostrar arreglo.")
    print("3 - generar archivo binario.")
    print("4 - mostrar archivo binario.")
    print("5 - busqueda binaria.")
    print("6 - procesar cadena.")

    print("0 - Salir.")

    op = int(input("Ingresar opción: "))
    return op


def principal():

    # vector/arreglo/lista de trabajo
    v_proyectos = []

    # enunciado de archivos binarios
    fd = "proyectos.dat"

    # para verificar el punto 6
    titulo = None

    op = -1
    while op != 0:
        op = menu()

        if op == 1:
            n = validar_n()
            cargar_arreglo(v_proyectos, n)

        elif op == 2:

            if len(v_proyectos) > 0:
                x = int(input("Ingresar importe a superar: "))
                mostrar_datos(v_proyectos, x)

            else:
                print("El vector no esta cargado.")

        elif op == 3:
            if len(v_proyectos) > 0:
                generar_archivo_binario(v_proyectos, fd)

            else:
                print("El vector no esta cargado.")

        elif op == 4:
            mostrar_archivo(fd)

        elif op == 5:
            if len(v_proyectos) > 0:
                c = int(input("Ingresar codigo a buscar: "))
                titulo = busqueda_binaria(v_proyectos, c)

            else:
                print("El vector no esta cargado.")

        elif op == 6:
            if titulo is None:
                print("Debe pasar primero por la op 5.")

            else:
                procesar_cadena(titulo)

        elif op == 7:
            # buscar el titulo y mostrar todos los proyectos que tengan ese titulo
            # indique un mensaje si no existe ningun proyecto
            tit = input("Ingresar titulo a buscar: ")
            busqueda_secuencial(v_proyectos, tit)

        elif op == 8:
            generar_matriz_con_archivo(fd)


if __name__ == "__main__":
    principal()