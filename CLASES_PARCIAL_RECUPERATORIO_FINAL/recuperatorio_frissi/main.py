import os.path
import pickle
import random

from registro import *


# =============================================================================
#                   Opcion 1
# =============================================================================
def validar_n():
    n = int(input("Ingresar cantidad de proyectos a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de proyectos a cargar: "))
    return n


def cargar_arreglo(v_proyectos, n):
    tupla_proyectos = ("Proyecto 1.", "Proyecto 2.", "Proyecto 3.")
    tupla_bool = (True, False)

    # codigo INT, titulo STR "termina en .", importe FLOAT, cant_inv INT, disponibilidad BOOL,
    # laboratorio(3, 5), otro(10, 13)
    for i in range(n):
        codigo = random.randint(1, 10)                  # INT
        titulo = "Este es el " + random.choice(tupla_proyectos)     # STR
        importe = round(random.uniform(0.1, 10), 2)     # FLOAT
        cant_inv = random.randint(1, 10)
        disponibilidad = random.choice(tupla_bool)
        laboratorio = random.randint(3, 5)
        otro = random.randint(10, 13)

        proy = Proyecto(codigo, titulo, importe, cant_inv, disponibilidad, laboratorio, otro)
        add_in_order(v_proyectos, proy)


def add_in_order(v_proyectos, proy):
    izq, der = 0, len(v_proyectos) - 1

    while izq <= der:

        c = (izq + der) // 2

        # cosas para cambiar el atributo por el que te pidan ordenar
        if v_proyectos[c].codigo == proy.codigo:
            pos = c
            break

        # la orientacion de la boquita ">" determina si esta de menor a mayor O mayor a menor
        elif v_proyectos[c].codigo > proy.codigo:
            der = c - 1

        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v_proyectos[pos:pos] = [proy]


# =============================================================================
#                   Opcion 2
# =============================================================================
def mostrar_arreglo(v_proyectos, x):
    # solo mostrar los que superen un importe "x"

    # v_proyectos = [     P1,     P2,     P3]
    for i in v_proyectos:
        # i = P1, P2, P3
        if i.importe > x:
            print(i)


# =============================================================================
#                   Opcion 3
# =============================================================================
def generar_archivo_binario(v_proyectos, fd):
    # solo guardar aquellos proyectos que superen el valor promedio de los importes dentro del arreglo

    # calcular el promedio
    # prom = acumulado ( importes ) / cantidad de veces que acumule
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
    m = open(fd, "wb")

    for i in v_proyectos:
        # i = P1, P2, P3
        if i.importe > prom:
            pickle.dump(i, m)

    m.close()


# =============================================================================
#                   Opcion 4
# =============================================================================
def mostrar_archivo_binario(fd):

    bandera = os.path.exists(fd)    # retorna True sI EXISTE EL ARCHIVO, FALSE SI NO EXISTE
    if bandera is False:    # if not bandera
        print("no existe el archivo:", fd)
        return      # termina una funcion

    m = open(fd, "rb")
    tamanio = os.path.getsize(fd)

    # calcular el promedio de cant de investigadores que se mostraron del archivo
    # promedio = acumulado ( de cant_inv ) / cantidad de veces que acumule
    acum = cont = 0

    while m.tell() < tamanio:
        proy = pickle.load(m)   #
        # proy = P1,    P2,     P3,     ....
        print(proy)
        acum += proy.cant_inv
        cont += 1

    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio cant_inv es:", prom)

    m.close()


# =============================================================================
#                   Opcion 5
# =============================================================================
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


# =============================================================================
#                   Opcion 6
# =============================================================================
def analisis_cadena(titulo):
    """
    # 12340120120
     ¿Cuál es la cantidad de palabras de esa cadena que contienen una letra "r" en la segunda
     o en la tercera posición (en mayúsculas o minúsculas) y que además no contienen ningún dígito?

    cantidad_palabras = 0

    indice = 0
    cont_r_pos2_pos3 = 0

    cont_digitos = 0
    """

    cantidad_palabras = 0

    indice = 0
    cont_r_pos2_pos3 = 0
    cont_digitos = 0

    print("titulo: ", titulo)

    # analisis de cadena
    # titulo = "Hola mundo."
    for i in titulo:
        # i = H, 3, l, a,  , m,

        # dentro de la palabra
        if i != " " and ".":
            indice += 1

            if i in "rR" and (indice == 2 or indice == 3):
                cont_r_pos2_pos3 += 1

            if i in "0123456789":
                cont_digitos += 1

        # fuera de la palabra
        else:
            if cont_r_pos2_pos3 > 0 and cont_digitos == 0:
                cantidad_palabras += 1

            # apagar las banderas
            indice = 0
            cont_r_pos2_pos3 = 0
            cont_digitos = 0

    print("la cantidad de palabras que cumplen:", cantidad_palabras)


# =============================================================================
#                   Opcion 7
# =============================================================================
def busqueda_secuencial(v_proyectos, tit):

    pos = -1        # EL CASO CUANDO NO EXISTE
    for i in range(len(v_proyectos)):
        # i = 0, 1, 2, 3, ...
        if v_proyectos[i].titulo == tit:
            pos = i
            break

    return pos  # -1 si no existe , 0 o mas cuando existe


# =============================================================================
#                   Opcion 7 - otro caso
# =============================================================================
def busqueda_secuencial_bis(v_proyectos, tit):

    # mostrar todos los que tengan ese titulo y al final mostrar cuantos se mostraron,
    # pero si no existe informar
    existe = False

    cont = 0

    for i in range(len(v_proyectos)):
        # i = 0, 1, 2, 3, ...
        if v_proyectos[i].titulo == tit:
            print(v_proyectos[i])
            cont += 1
            existe = True

    print("Se mostraron la cntidad de:", cont)

    if existe is False:     # if not existe
        print("No existe ese titulo en el arreglo.")


# =============================================================================
#                   Opcion 8
# =============================================================================
def generar_matriz(v_proyectos, l1, l2):

    # generar la matriz
    f = 3    # f = filas = laboratorio(3, 5) = lim_superior - lim_inferior + 1 = 5 - 3 + 1 = 3
    c = 4    # c = columnas = otro(10, 13) = lim_superior - lim_inferior + 1 = 13 - 10 + 1 = 4
    matriz = [ [0] * c for i in range(f) ]

    # laboratorio(3, 5)    3-3     4-3     5-3
    # fila_indices          0       1       2

    # otro(10, 13)            10-10      11       12      13
    # columndas_indices         0       1       2       3

    # matriz =  [   [0, 0, 0, 0],
    #               [0, 0, 0, 0],
    #               [0, 0, 0, 0]    ]

    #
    # rellenar la matriz
    for i in v_proyectos:
        # i = P1, P2, P3
        # matriz[f][c]      # al reves a como lo creaste

        # la cantidad de proyectos por cada posible combinacion de laboratorio y otro
        matriz[i.laboratorio - 3][i.otro - 10] += 1

        # la sumatoria de importes de proyectos por cada posible combinacion de laboratorio y otro
        # matriz[i.laboratorio - 3][i.otro - 10] += i.importe

    #
    # mostrar la matriz
    for f in range(len(matriz)):        # range(3)
        # f = 0, 1, 2

        for c in range(len(matriz[0])):     # range(4)
            # c = 0, 1, 2, 3

            # solo mostrar los laboratorios entre l1 y l2 ambos incluidos
            if l1 <= f+3 <= l2:
                print("Laboratorio:", f+3, "- Otro:", c+10, "- Cantidad:", matriz[f][c])

            # solo mostrar los contadores/acumuladores mayores a 0
            # if matriz[f][c] > 0:
            #    print("Laboratorio:", f + 3, "- Otro:", c + 10, "- Cantidad:", matriz[f][c])


# =============================================================================
#                   Opcion 9
# =============================================================================
def vector_acum(v_proyectos, x):

    # generar vector acum/cont
    # laboratorio(3, 5) = lim_superior - lim_inferior + 1 = 5 - 3 + 1 = 3
    v_acum = [0] * 3

    #          3-3  4-3 5-3
    # indices   0   1   2
    # v_acum = [ 0, 0, 0 ]

    # rellenar el vector
    for i in v_proyectos:
        v_acum[i.laboratorio - 3] += i.importe

    # mostrar el vector
    for i in range(len(v_acum)):
        # i = 0, 1,  2

        # solo mostrar los acumuladores que superen un valor "x".
        if v_acum[i] > x:
            print("Laboratorio:", i+3, "- acumulado de importes:", v_acum[i])



# =============================================================================
#                   Menu
# =============================================================================
def menu():
    # ctrl + d
    print("1 - cargar arreglo.")
    print("2 - mostrar arreglo.")
    print("3 - generar archivo binario.")
    print("4 - mostrar archivo binario.")
    print("5 - busqueda binaria.")
    print("6 - analisis de cadena.")
    print("7 - busqeuda secuencial.")
    print("8 - matriz.")
    print("9 - vector_acum_conteo.")

    print("0 - Salir.")

    op = int(input("Ingresar opcion: "))
    return op


def principal():

    # vector
    v_proyectos = []

    # oopcion 3 ( archivo binario)
    fd = "proyectos.dat"

    # para verificar opp 6
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
                mostrar_arreglo(v_proyectos, x)

            else:
                print("No esta cargado el arreglo.")


        elif op == 3:
            if len(v_proyectos) > 0:
                generar_archivo_binario(v_proyectos, fd)

            else:
                print("No esta cargado el arreglo.")


        elif op == 4:
            mostrar_archivo_binario(fd)

        elif op == 5:
            if len(v_proyectos) > 0:
                c = int(input("Ingresar un codigo a buscar: "))
                titulo = busqueda_binaria(v_proyectos, c)

            else:
                print("No esta cargado el arreglo.")

        elif op == 6:
            if titulo is None:
                print("debe ingresar primero a la opcion 5.")

            else:
                analisis_cadena(titulo)

        elif op == 7:
            # nos pidan buscar un titulo "tit" deternse al primer resultado
            # mostrar sus datos antes y despues del cambio y
            # realizar un descuento en su importe por un 22%
            tit = input("Ingresar titulo a buscar: ")
            pos = busqueda_secuencial(v_proyectos, tit)

            if pos >= 0:
                print("Datos sin actualizar: ", v_proyectos[pos])

                # realizar un descuento en su importe por un 22%
                v_proyectos[pos].importe -= v_proyectos[pos].importe * 0.22

                # modificar su importe por un valor ingresado por teclado "x"
                x = float(input("Ingresar importe nuevo: "))
                v_proyectos[pos].importe = x

                print("Datos actualizados: ", v_proyectos[pos])

            else:       # cuando pos es -1
                print("No existe!")


        elif op == 8:
            # determinar y mostrar la cantidad de proyectos por cada posible combinacion de
            # laboratorio y otro, solo mostrar los laboratorios entre l1 y l2 ambos incluidos
            l1 = int(input("Ingresar laboratorio a superar: "))
            l2 = int(input("Ingresar laboratorio a ser menor: "))
            generar_matriz(v_proyectos, l1, l2)


        elif op == 9:
            # determinar mostrar la sumatoria de importes por cada posible laboratorio,
            # solo mostrar los acumuladores que superen un valor "x".
            x = int(input("Ingresar importe a superar: "))
            vector_acum(v_proyectos, x)


        elif op == 0:
            print("Chau valerio.")



if __name__ == '__main__':
    principal()




