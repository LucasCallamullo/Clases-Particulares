import os.path
import pickle
import random

from registro import *


# =====================================================================
#                   Opcion 1
# =====================================================================
def validar_n():
    n = int(input("Ingresar cantidad de lotes a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de lotes a cargar: "))
    return n


def cargar_arreglo(v_lotes, n):
    # nombre STR, manzana(1, 35), num_lote(1, 20), orientacion (1, 4), superficie FLOAT, importe FLOAT
    for i in range(n):  # range(3)
        # i = 0, 1,         2
        nombre = random.choice("ABCDEF")    # STR
        manzana = random.randint(1, 35)     # INT
        num_lote = random.randint(1, 20)
        orientacion = random.randint(1, 4)
        superficie = round(random.uniform(0.1, 10), 2)  # FLOAT
        importe = round(random.uniform(0.1, 10), 2)  # FLOAT

        nuevo_lote = Lote(nombre, manzana, num_lote, orientacion, superficie, importe)
        add_in_order(v_lotes, nuevo_lote)


def add_in_order(v_lotes, nuevo_lote):
    # L1.nombre     C
    # L2.nombre     B

    # indices       0
    # v_lotes = [   L1  ]

    izq, der = 0, len(v_lotes) - 1

    # izq = 0
    # der = -1

    while izq <= der:   # mientras izq sea menor o igual a derecha ingresamos al ciclo
        c = (izq + der) // 2
        # c = 0

        # lo unico que cambia es el atributo por el que les piden ordenar
        if v_lotes[c].nombre == nuevo_lote.nombre:
            pos = c
            break
        # lo unico que determina si esta ordenado de menor a mayor o mayor a menor es ">"
        elif v_lotes[c].nombre > nuevo_lote.nombre:
            der = c - 1

        else:
            izq = c + 1

    if izq > der:
        pos = izq
    # pos = 0

    # indices       0       1       2
    # v_lotes =   [ L2  ,   L1 ]
    # nombres       B       C
    v_lotes[pos:pos] = [nuevo_lote]     # esto va con corchetes "nuevo_lote"


# =====================================================================
#                   Opcion 2
# =====================================================================
def mostrar_datos(v_lotes):
    # indices       0       1       2
    # v_lotes =   [ L1  ,   L2,     L3 ]
    for i in v_lotes:
        # i = L1,   L2,     L3      --> la "i" toma el valor de cada elemento de la lista
        print(i)

    # for i in range(len(v_lotes)):   # range(3)
        # i = 0, 1, 2           --> la "i" vale como valores de indices


# =====================================================================
#                   Opcion 3
# =====================================================================
def generar_matriz(v_lotes, m):

    # crear la matriz
    f = 4     # f = filas = orientacion(1, 4) = lim_superior - lim_inferio + 1 = 4 - 1 + 1 = 4
    c = 35    # c = columnas = manzana(1, 35) = lim_superior - lim_inferio + 1 = 35 - 1 + 1 = 35
    matriz = [ [0] * c for i in range(f) ]

    # orientacion      1-1 2-1  3-1  4-1
    # indices de filas  0   1   2   3

    # manzana(1, 35)   1-1 2-1   ...     34     35
    # indices columnas  0   1   2   ...     34

    # [ [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   ]

    # rellenar la matriz
    # v_lotes = [ L1    ,   L2  ,   L3]
    # orientacion   1       2       1
    # manzana       1       2       1
    # superficie    5       4       3
    for i in v_lotes:
        # i = L1,   L2, L3
        # matriz[f][c] +=
        matriz[i.orientacion - 1][i.manzana - 1] += i.superficie
        # matriz[i.orientacion - 1][i.manzana - 1] += 1

    #
    # Mostrar, además, la superficie total vendida para una manzana m
    acum = 0
    tupla_orientaciones = ("Norte", "Sur", "Este", "Oeste")

    # mostrar la matriz
    for f in range(len(matriz)):        # range(4)
        # f = 0, 1, 2, 3

        for c in range(len(matriz[0])):     # range(35)
            # c = 0, 1, 2, 3, ..., 34

            # Solo mostrar los que tengan un valor mayor a cero
            if matriz[f][c] > 0:
                # print("Manzana:", c + 1, "| Orientacion:", f + 1, "| Superficie vendida:", matriz[f][c])
                print("Manzana:", c + 1, "| Orientacion:", tupla_orientaciones[f], "| Superficie vendida:", matriz[f][c])

            # Mostrar, además, la superficie total vendida para una manzana m
            if m == c+1:
                acum += matriz[f][c]

    print("El acumulado total de la manazana:", m, "es:", acum)


# =====================================================================
#                   Opcion 4
# =====================================================================
def generar_archivo_binario(v_lotes, fd, l1, l2):

    m = open(fd, "wb")  # primer parametro es el nombre del archivo ( fd )
                        # segundo parametro es el modo de apertura ( "wb" o "ab" )

    # wb = write binary = genera el archivo si no existe, sobre escribe tod0 su contenido
    # ab = append binary = genera el archivo si no existe, agrega tod0 el contenido al final del archivo, conservando
    # tod0 su contenido

    for i in v_lotes:
        # i = L1, L2, L3
        # lo unico que cambia esw la condicion
        if l1 <= i.num_lote <= l2:

            pickle.dump(i, m)   # primer parametro lo que quiero guardar (i)
                            # segundo parametro: donde lo quiero guardar (m)
            m.flush()   # OPCIONAL -- Guarda mejor el archivo

    print("Se genero el archivo binario.")  # Opcional
    m.close()   # OBLIGATORIO


# =====================================================================
#                   Opcion 5
# =====================================================================
def mostrar_archivo_binario(fd):

    if os.path.exists(fd) is False:     # if not os.path.exists(fd)
        print("El archivo binario no existe.")
        return      # detiene la funcion aca

    m = open(fd, "rb")  # read binary, leer el contenido del archivo sin modificarlo
    tam = os.path.getsize(fd)   # tam = el tamaño en bytes del archivo      # 540

    # indices       0       1       2
    # v_lotes =   [ L1  ,   L2,     L3 ]

    # archivo =     [ L1            L2              L3 ]
    # bytes         0       150             300         540
    # m.tell()      0       150             300

    #
    # luego de mostrarlo agregue una línea al final que informe el valor
    # promedio de venta de los lotes con orientacion al Oeste contenidos en el archivo.
    # promedio = acumulador ( de importes ) // cantidad de veces que acumulamos
    acum = 0
    cont = 0

    while m.tell() < tam:

        lotecito = pickle.load(m)   # L1,   L2,     L3
        print(lotecito)

        if lotecito.orientacion == 4:
            acum += lotecito.importe
            cont += 1

    # calcular promedio
    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio es:", prom)

    m.close()   # OBLIGATORIO


# =====================================================================
#                   Opcion 6
# =====================================================================
def busqueda_binaria(v_lotes, nom):

    #               0   1   2   3   4
    # v_lotes = [ L1 , L2, L3 ,L4, L5 ]
    #

    izq, der = 0, len(v_lotes) - 1

    while izq <= der:
        c = (izq + der) // 2

        # if v_lotes[c].nombre == nuevo_lote.nombre:
        if v_lotes[c].nombre == nom:
            pos = c
            # break
            return pos  # posicion donde encontre el objeto que cumple con mi criterio de busqueda

        # elif v_lotes[c].nombre > nuevo_lote.nombre:
        elif v_lotes[c].nombre > nom:
            der = c - 1

        else:
            izq = c + 1

    return -1



def menu():
    # ctrl + d
    print("1 - Cargar Arreglo.")
    print("2 - Mostrar Arreglo.")
    print("3 - Generar Matriz")
    print("4 - Generar Archivo Binario")
    print("5 - Mostrar Archivo Binario")
    print("6 - Busqueda Binaria.")
    print("0 - Salir.")
    op = int(input("Ingresar opcion: "))    # 3
    return op   # 3


def principal():

    # arreglo / lista / vector de trabajo
    v_lotes = []        # list()

    # variable con el nombre del archivo binario
    fd = "lotes.dat"       # file description ; nombre del archivo

    op = -1
    while op != 0:  # mientras op sea distinto de cero, ingreso al ciclo

        # si una variable esta igualada a una funcion es porque espera que la funcion devuelva algun valor
        op = menu()     # 3

        if op == 1:
            n = validar_n()
            """
            Cada vez que se ingrese en esta opción, el arreglo debe ser creado desde cero y todo 
            contenido anterior debe ser eliminado.
            """
            v_lotes = []
            cargar_arreglo(v_lotes, n)

        elif op == 2:
            if len(v_lotes) > 0:
                mostrar_datos(v_lotes)
            else:
                print("El arreglo no esta cargado.")

        elif op == 3:
            """
            3 - A partir del arreglo generado en el punto 1, acumular y mostrar la superficie total vendida por cada manzana
posible combinada con cada orientación posible. Mostrar, además, la superficie total vendida para una
manzana m (siendo m un valor que se ingresa por teclado).
            """
            if len(v_lotes) > 0:
                m = int(input("Ingresar manzana a buscar su superficie total vendida: "))
                generar_matriz(v_lotes, m)
            else:
                print("El arreglo no esta cargado.")

        elif op == 4:
            """
            4 - A partir del arreglo, genere un archivo binario que contenga los datos de todos los 
lotes cuyo número de lote esté comprendido entre l1 y l2, siendo estos valores que se ingresan por 
teclado.
            """
            if len(v_lotes) > 0:
                l1 = int(input("Ingresar num_lote a superar: "))
                l2 = int(input("Ingresar num_lote a ser inferior: "))
                generar_archivo_binario(v_lotes, fd, l1, l2)

            else:
                print("El arreglo no esta cargado.")

        elif op == 5:
            """
            5 - Mostrar el archivo generado en el punto anterior y luego de mostrarlo agregue una 
línea que informe el valor promedio de venta de los lotes contenidos en el archivo.
            """
            mostrar_archivo_binario(fd)

        elif op == 6:
            """
            6 - Buscar un Lote por nombre "nom". Si existe mostrar todos sus datos y si, además, 
            la orientacion era Norte o Sur realizar un descuento del 22% sobre su precio de venta, 
            mostrando los datos del lote antes y después de la actualización. 
            Si el lote no existe informar con el mensaje “No contamos con el lote del propietario <NOMBRE> 
            pero no deje de visitar nuestra sección de ofertas!”
            """
            if len(v_lotes) > 0:

                nom = input("Ingresar nombre a buscar: ")
                pos = busqueda_binaria(v_lotes, nom)

                if pos >= 0:    # valor de indice o sea que existe el objeto que cumple

                    print("Datos sin actualizar:", v_lotes[pos])

                    if v_lotes[pos].orientacion == 1 or v_lotes[pos].orientacion == 2:
                        # descuento 22%
                        v_lotes[pos].importe -= v_lotes[pos].importe * 0.22

                    print("Datos actualizados:", v_lotes[pos])

                    # solo mostrasr el nombre
                    print("Nombre:", v_lotes[pos].nombre)

                else:       # pos = -1 , no existe el objeto
                    print("No contamos con el lote del propietario", nom)

            else:
                print("El arreglo no esta cargado.")



if __name__ == '__main__':
    principal()
