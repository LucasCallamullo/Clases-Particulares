import os.path
import pickle
import random

from registro import *


# ===========================================================================
#                               Opcion 1
# ===========================================================================
def validar_n():

    n = int(input("Ingresar una cantidad de proyectops a cargar: "))
    while n <= 0:
        n = int(input("Ingresar una cantidad de proyectops a cargar: "))
    return n


def cargar_arreglo(v_proyectos, n):
    tupla_titulos = ("Proyecto 1.", "Proyecto 2.", "Proyecto 3.")
    tupla = (True, False)

    # codigo INT, titulo STR, importe FLOAT, cant_inv INT, laboratorio(1, 10), zona(15, 18), disponible BOOL
    for i in range(n):      #
        codigo = random.randint(1, 10)
        titulo = "Este es el " + random.choice(tupla_titulos)
        importe = round(random.uniform(0.1, 10), 2)
        cant_inv = random.randint(1, 10)
        laboratorio = random.randint(1, 10)
        zona = random.randint(15, 18)
        disponible = random.choice(tupla)

        proy = Proyecto(codigo, titulo, importe, cant_inv, laboratorio, zona, disponible)
        add_in_order(v_proyectos, proy)


def add_in_order(v_proyectos, proy):
    izq, der = 0, len(v_proyectos) - 1

    while izq <= der:

        c = (izq + der) // 2

        if v_proyectos[c].codigo == proy.codigo:
            pos = c
            break

        # la orientacion de la boca " > " determina si esta de menor a mayor o mayor  a menor
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
def mostrar_arreglo(v_proyectos, x):

    # al final del listado mostrar el acumulado de la cantidad de investigadores de los proyectos que se mostraron
    acum = 0

    # indice            0       1       2
    # v_proyectos = [   P1,   P2,     P3 ]
    for i in v_proyectos:
        # i = P1,   P2,     P3

        # solo mostrar los que superan un importe x
        if i.importe > x:
            print(i)
            acum += i.cant_inv

    print("El acum cant_inv es:", acum)


# ===========================================================================
#                               Opcion 3
# ===========================================================================
def generar_archivo_binario(v_proyectos, fd, x):
    """
    Generar un archivo binario que contenga todos los objetos que superen al importe promedio dentro del arreglo

    - primero calculo el promedio
    - genero el archivo binario en base a ese promedio
    """
    # promedio = acumulado ( de importes ) / la cantidad de veces que acumule
    acum = 0
    cont = 0

    for i in v_proyectos:
        # i = p1, p2, p3
        acum += i.importe
        cont += 1

    # calcular promedio
    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio importe es:", prom)

    #
    # guardar/generar el archivo
    m = open(fd, "wb")

    for i in v_proyectos:
        # i = P1, P2, P3
        if i.importe > prom:
            pickle.dump(i, m)

    # print("se genero el archivo")
    m.close()       # OBLIGATORIO


# ===========================================================================
#                               Opcion 4
# ===========================================================================
def mostrar_archivo_binario(fd):
    bandera = os.path.exists(fd)    # return True si existe el archivo, return False si no existe
    if bandera is False:
        print("El archivo no existe:", fd)
        return      # cortar la funcion

    m = open(fd, "rb")
    tamanio = os.path.getsize(fd)

    # calcular el promedio de los importes mostrados
    # promedio = acumulado ( de importes ) / la cantidad de veces que acumule
    acum = 0
    cont = 0

    while m.tell() < tamanio:
        proy = pickle.load(m)
        # proy = P1,    P2,     P3
        print(proy)
        acum += proy.importe
        cont += 1

    # calcular promedio
    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio importe es:", prom)

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
            print(v_proyectos[pos])
            return v_proyectos[pos].titulo

        # elif v_proyectos[c].codigo > proy.codigo:
        elif v_proyectos[c].codigo > cod:
            der = c - 1

        else:
            izq = c + 1

    cadena = "Artículo inexistente!."
    print(cadena)
    return cadena


# ===========================================================================
#                               Opcion 6
# ===========================================================================
def procesar_cadena(titulo):
    """
    #    12340120
        ¿Cuál es la cantidad de palabras de esa cadena que contienen una letra "r" en la segunda o
    en la tercera posición (en mayúsculas o minúsculas) y que además no contienen ningún dígito (numeros)?

    cantidad_palabras = 0

    cont_r_pos2_pos3 = 0
    indice = 0

    cont_digitos = 0
    """
    cantidad_palabras = 0

    cont_r_pos2_pos3 = 0
    indice = 0
    cont_digitos = 0

    print("la cadena a procesar: ", titulo)

    #
    # titulo = "Hola mundo."

    for i in titulo:
        # i = H, o, l, a,  , m, u, n,

        # estoy dentro de la palabra
        if i != " " and i != ".":

            indice += 1

            # if i.lower() == "r":
            if i in "rR" and (indice == 2 or indice == 3):
                cont_r_pos2_pos3 += 1

            # if i.isdigit():
            if i in "0123456789":
                cont_digitos += 1

        # estoy fuera de la palabra / termino una palabra
        else:

            if cont_r_pos2_pos3 > 0 and cont_digitos == 0:
                cantidad_palabras += 1

            # apagar / reiniciar banderas contadores etc
            cont_r_pos2_pos3 = 0
            indice = 0
            cont_digitos = 0

    print("cantidad de palabras cumplen:_", cantidad_palabras)


# ===========================================================================
#                               Opcion 7
# ===========================================================================
def busqueda_secuencial(v_proyectos, tit):

    # este es el caso si solo les pide buscar uno y/o detenerse al primer resultado
    for i in range(len(v_proyectos)):
        # i = 0, 1, 2, 3, ...
        if v_proyectos[i].titulo == tit:
            pos = i
            return pos      # existe porque pos es mayor o igual a cero ( valores de indice )

    return -1       # no existe


def busqueda_secuencial_retornar_titulo(v_proyectos, tit):
    # mostrar los datos y retornar titulo

    for i in range(len(v_proyectos)):
        # i = 0, 1, 2, 3, ...
        if v_proyectos[i].titulo == tit:
            print(v_proyectos[i])
            return v_proyectos[i].titulo  # existe porque pos es mayor o igual a cero ( valores de indice )

    mensaje = "No existe!"
    print(mensaje)
    return mensaje  # no existe


def busqueda_secuencial_muchos(v_proyectos, tit):
    # este es el caso si te piden mostrar todos los resultados que coincidan e informar si no existe
    se_encontro = False

    for i in range(len(v_proyectos)):
        # i = 0, 1, 2, 3, ...
        if v_proyectos[i].titulo == tit:
            print(v_proyectos[i])
            se_encontro = True

    if se_encontro is False:
        print("No se encontraron resultados")


# ===========================================================================
#                               Opcion 8
# ===========================================================================
def generar_matriz_con_archivo_binario(fd):

    bandera = os.path.exists(fd)  # return True si existe el archivo, return False si no existe
    if bandera is False:
        print("El archivo no existe:", fd)
        return  # cortar la funcion

    # crear la matriz
    f = 10   # f = laboratorio(1, 10)    = 10 - 1 + 1 = 10
    c = 4    # c = zona(15, 18)          = 18 - 15 + 1 = 4   (15 16 17 18
    matriz = [ [0] * c for i in range(f) ]

    # rellenar la matriz
    m = open(fd, "rb")
    tamanio = os.path.getsize(fd)

    while m.tell() < tamanio:
        proy = pickle.load(m)
        # proy = P1,    P2,     P3
        matriz[proy.laboratorio - 1][proy.zona - 15] += 1       # determinar cantidad
        # matriz[proy.laboratorio - 1][proy.zona - 15] += proy.importe      # determinar sumatoria de importes

    m.close()  # OBLIGATORIO

    # mostrar la matriz
    for f in range(len(matriz)):
        for c in range(len(matriz[0])):
            print("Laboratorio: ", f, "- Zona:", c, "- Cantidad:", matriz[f][c])


def busqueda_secuencial_con_archivo_binario(fd, tit):

    bandera = os.path.exists(fd)  # return True si existe el archivo, return False si no existe
    if bandera is False:
        print("El archivo no existe:", fd)
        return  # cortar la funcion

    m = open(fd, "rb")
    tamanio = os.path.getsize(fd)

    while m.tell() < tamanio:
        proy = pickle.load(m)
        # proy = P1,    P2,     P3
        if proy.titulo == tit:
            print(proy)
            break   # se detenga al primer resultado

    m.close()  # OBLIGATORIO



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

    # opcion 1
    v_proyectos = []

    # para puntos de archivos binarios
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
                # solo mostrar los que superen un importe "x"
                x = float(input("Ingresar importe a superar: "))
                mostrar_arreglo(v_proyectos, x)

            else:
                print("El arreglo no esta cargado.")

        elif op == 3:
            if len(v_proyectos) > 0:
                # solo guardar los que superen un importe "x"
                x = float(input("Ingresar importe a superar: "))
                generar_archivo_binario(v_proyectos, fd, x)

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
                print("Debe pasar primerop por la op 5.")

            else:
                procesar_cadena(titulo)

        elif op == 7:
            # buscar un titulo
            tit = input("Titulo a buscar: ")
            pos = busqueda_secuencial(v_proyectos, tit)

            if pos >= 0:
                # mostrar sus datos antes  ydespues del cambio y modifcar su importe con un aumento del 10%
                print("DAtos sin acatualizar")

                v_proyectos[pos].importe += v_proyectos[pos].importe * 0.1

                print("DAtos acatualizados")

            else:
                print("No existe.")


if __name__ == "__main__":
    principal()
