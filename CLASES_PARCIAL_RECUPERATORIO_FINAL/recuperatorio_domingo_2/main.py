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
    # codigo INT, titulo STR, importe FLOAT, cant_inv INT, laboratorio(3, 5), zona(10, 15), disponible BOOL

    tupla_titulos = ("Proyecto 1.", "Proyecto 2.", "Proyecto 3.")
    tupla_bool = (True, False)

    for i in range(n):      #
        codigo = random.randint(1, 10)
        titulo = "Este es el " + random.choice(tupla_titulos)
        importe = round(random.uniform(0.1, 10), 2)
        cant_inv = random.randint(1, 10)
        laboratorio = random.randint(3, 5)
        zona = random.randint(10, 15)
        disponible = random.choice(tupla_bool)

        proy = Proyecto(codigo, titulo, importe, cant_inv, laboratorio, zona, disponible)
        add_in_order(v_proyectos, proy)


def add_in_order(v_proyectos, proy):
    izq, der = 0, len(v_proyectos) - 1

    while izq <= der:

        c = ( izq + der ) // 2
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
#                       Opcion 2
# ===========================================================================
def mostrar_arreglo(v_proyectos, x):

    # al final del listado  mostrar cual fue el acumulado de la cantidad de investigadores que se mostraron
    acum = 0

    # v_proyectos = [ P1 , P2 , P3 ]
    for i in v_proyectos:
        # i = P1,   P2,     P3

        # solo mostrar los que superan un importe x
        if i.importe > x:
            print(i)
            acum += i.cant_inv

    print("El acum cant_inv es:", acum)


# ===========================================================================
#                       Opcion 3
# ===========================================================================
def generar_archivo_binario(v_proyectos, fd):
    """
    generar un archivo binario que solo se guarden los proyectos que tengan un importe superior al importe
    promedio dentro del arreglo

    - primero recorro mi arreglo y calculo mi importe promedio
    - guardo los proyectos del archivo a partir del promedio que calcule
    """
    # calcular un promedio
    # promedio = acumulado ( de importes ) / la cantidad de veces que acumule
    acum = 0
    cont = 0

    for i in v_proyectos:
        # i = P1, P2, P3
        acum += i.importe
        cont += 1

    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio importe es:", prom)

    #
    # guardar en el archivo
    m = open(fd, "wb")

    for i in v_proyectos:
        if i.importe > prom:
            pickle.dump(i, m)
            # m.flush()

    m.close()       # OBLIGATORIO


# ===========================================================================
#                       Opcion 4
# ===========================================================================
def mostrar_archivo_binario(fd):

    if os.path.exists(fd) is False:
        print("No existe el archivo:", fd)
        return

    m = open(fd, "rb")
    tam = os.path.getsize(fd)

    # calcular un promedio
    # promedio = acumulado ( de importes ) / la cantidad de veces que acumule
    acum = 0
    cont = 0

    while m.tell() < tam:
        proy = pickle.load(m)
        # proy = P1,    P2,     P3
        print(proy)

        acum += proy.importe
        cont += 1

    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio importe es:", prom)

    m.close()


# ===========================================================================
#                       Opcion 5
# ===========================================================================
def busqueda_binaria(v_proyectos, cod):
    """
    Esta busqueda solo se utiliza si me piden buscar un atributo que casualmente es el mismo atributo por el que esta
    ordenado en el punto 1

    :param v_proyectos:
    :param c:
    :return:
    """
    izq, der = 0, len(v_proyectos) - 1

    while izq <= der:

        c = (izq + der) // 2
        # if v_proyectos[c].codigo == proy.codigo:
        if v_proyectos[c].codigo == cod:
            pos = c
            # break
            print(v_proyectos[pos])     # Mostrar datos
            return v_proyectos[pos].titulo      # retornar el titulo

        # elif v_proyectos[c].codigo > proy.codigo:
        elif v_proyectos[c].codigo > cod:
            der = c - 1

        else:
            izq = c + 1

    mensaje = "Articulo Inexistente!."
    print(mensaje)
    return mensaje


# ===========================================================================
#                       Opcion 6
# ===========================================================================
def procesar_cadena(titulo):
    """

    #   123
        Cuál es la cantidad de palabras de esa cadena que contienen una letra "r" en la segunda o
    en la tercera posición (en mayúsculas o minúsculas) y que además no contienen ningún dígito?

    cantidad_palabras = 0

    cont_r_pos2_pos3 = 0
    indice = 0

    cont_digitos = 0
    """
    cantidad_palabras = 0

    cont_r_pos2_pos3 = 0
    indice = 0

    cont_digitos = 0

    # si nos hubieran pedido que el titulo en realidad fuera el titulo de la posicion 0
    # titulo = v_proyectos[0].titulo

    print("Ingresar cadena a procesar: ", titulo)

    #           1
    # titulo = "Hola mundo."
    for i in titulo:
        # i = H, o, l, a,  , m, ...

        # dentro de la palabra
        if i != " " and i != ".":

            indice += 1

            # if i.lower() == "r" and (indice == 2 or indice == 3):
            if i in "rR" and (indice == 2 or indice == 3):
                cont_r_pos2_pos3 += 1

            if i in "0123456789":
                cont_digitos += 1

        # fuera de la palabra
        else:

            if cont_r_pos2_pos3 > 0 and cont_digitos == 0:
                cantidad_palabras += 1

            # apagar las banderas / reiniciar contadores
            cont_r_pos2_pos3 = 0
            indice = 0
            cont_digitos = 0

    print("La cantidad de palabras que cummple:", cantidad_palabras)


# ===========================================================================
#                       Opcion 7
# ===========================================================================
def busqueda_secuencial(v_proyectos, tit):
    # buscar por titulo "tit" y detenerse al primer resutlado que encuentre

    for i in range(len(v_proyectos)):
        # i = 0, 1, 2, 3
        if v_proyectos[i].titulo == tit:
            pos = i
            return pos      # cuando existe es cero o mas

    return -1       # no existe


def busqueda_secuencial_retorna_titulo(v_proyectos, tit):
    # buscar por titulo "tit" y detenerse al primer resultado que encuentre
    # mostrar sus datos y retornar el titulo del mismo y si no se encuentr
    # retornar un mensaje uqe "hola mundo."

    for i in range(len(v_proyectos)):
        # i = 0, 1, 2, 3
        if v_proyectos[i].titulo == tit:
            pos = i
            print(v_proyectos[pos])
            return v_proyectos[pos].titulo

    mensaje = "Hola mundo."
    print(mensaje)
    return mensaje  # no existe


def busqueda_secuencial_mostrar_muchos(v_proyectos, tit):
    # buscar por titulo "tit" y mostrar todos los reesultados posibles pero informar con no existe si no encuentra
    # resultados

    se_encontro = False

    for i in range(len(v_proyectos)):
        # i = 0, 1, 2, 3
        if v_proyectos[i].titulo == tit:
            pos = i
            print(v_proyectos[pos])
            se_encontro = True

    if se_encontro is False:
        print("No existe.")


# ===========================================================================
#                       Opcion 8
# ===========================================================================
def generar_matriz_con_el_archivo_binario(fd):
    """
    determinar y mostrar la cantidad de proyectos posibles por cada combinacion entre laboratorio y zona

    :param fd:
    :return:
    """
    if os.path.exists(fd) is False:
        print("No existe el archivo:", fd)
        return

    # generar matriz
    f = 3    # f = laboratorio ( 3, 5 ) = 5-3+1 = 3
    c = 6    # c = zona(10, 15) = 15 - 10 + 1 = 6
    matriz = [ [0] * c for i in range(f) ]

    #
    # rellenor de la  matriz
    # for i in v_proyectos:
    #   # i = P1, P2, P3
    #   matriz[i.laboratorio-3][i.zona-10] += 1

    #
    m = open(fd, "rb")
    tam = os.path.getsize(fd)

    while m.tell() < tam:
        proy = pickle.load(m)
        # proy = P1,    P2,     P3
        matriz[proy.laboratorio - 3][proy.zona - 10] += 1

    m.close()

    #
    # mostrar la matriz
    for f in range(len(matriz)):

        for c in range(len(matriz[0])):

            # solo mostrar aquellos contadores que sean mayores a cero:
            if matriz[f][c] > 0:
                print("Laboratorio:", f+3, "- Zona:", c+10, "- Cantidad:", matriz[f][c])

            # solo mostrar las zonas entre z1 y z2
            # if z1 < c+10 < z2:
            #    print("Laboratorio:", f + 3, "- Zona:", c + 10, "- Cantidad:", matriz[f][c])


def busqueda_secuencial_con_el_archivo_binario(fd, tit):
    """
    determinar y mostrar un proyecto cuyo titulo sea tit y detenerse al primer resultado
    si no eixste informar
    """
    if os.path.exists(fd) is False:
        print("No existe el archivo:", fd)
        return

    m = open(fd, "rb")
    tam = os.path.getsize(fd)

    se_encontro = False

    while m.tell() < tam:
        proy = pickle.load(m)
        # proy = P1,    P2,     P3

        if proy.titulo == tit:
            print(proy)
            se_encontro = True
            break       # deterse al primer resultado

    if se_encontro is False:
        print("no existe.")

    m.close()



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

    # vector /arreglo de trabajo
    v_proyectos = []

    # puntos de archivos binarios
    fd = "proyectos.dat"

    # para verificar op 6
    titulo = None

    op = -1
    while op != 0:
        op = menu()

        if op == 1:
            n = validar_n()
            cargar_arreglo(v_proyectos, n)

        elif op == 2:
            if len(v_proyectos) > 0:
                # solo mostrar los que superen un importe x
                x = float(input("Ingresar importe a superar: "))
                mostrar_arreglo(v_proyectos, x)

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
                c = int(input("Ingresar codigo a buscar: "))
                titulo = busqueda_binaria(v_proyectos, c)

            else:
                print("El arreglo no esta cargado.")

        elif op == 6:
            if titulo is None:
                print("Primero debe pasar por la op 5")

            else:
                procesar_cadena(titulo)

        elif op == 7:
            tit = input("Ingresar titulo a buscar: ")
            pos = busqueda_secuencial(v_proyectos, tit)

            if pos >= 0:
                # mostrar los datos antes y despues de realizar un cambio en su importe que sea un descuento del 10%
                print("Datos viejos:", v_proyectos[pos])

                v_proyectos[pos].importe -= v_proyectos[pos].importe * 0.1

                print("Datos nuevos:", v_proyectos[pos])

            else:
                print("No existe.")


if __name__ == "__main__":
    principal()
