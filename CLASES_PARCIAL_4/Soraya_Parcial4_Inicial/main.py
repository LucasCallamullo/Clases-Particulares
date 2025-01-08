import os.path
import pickle
import random
from registro import *


# ======================================================================
#           Opcion 1
# ======================================================================
def validar_n():
    n = int(input("Ingresar cantidad de lotes a cargar: "))     # 0
    while n <= 0:
        n = int(input("Ingresar cantidad de lotes a cargar: "))     # 3
    return n


def cargar_arreglo(v_lotes, n):
    # nombre STR, manzana(1, 35), lote (1, 20),
    # orientacion(1, 4)  (1: Norte, 2: Sur, 3: Este, 4:Oeste), superficie INT, importe FLOAT
    for i in range(n):
        nombre = random.choice("ABCDEF")        # STR
        manzana = random.randint(1, 35)
        lote = random.randint(1, 20)            # INT
        orientacion = random.randint(1, 4)
        superficie = random.randint(1, 10)      # INT
        importe = round(random.uniform(0.1, 10), 2)     # FLOAT

        nuevo_lote = Lote(nombre, manzana, lote, orientacion, superficie, importe)
        add_in_order(v_lotes, nuevo_lote)


def add_in_order(v_lotes, nuevo_lote):
    izq, der = 0, len(v_lotes) - 1
    # lotes =   L2 L1
    # nombre    A  B

    while izq <= der:
        c = (izq + der) // 2
        # el atributo por el que ordenas
        if v_lotes[c].nombre == nuevo_lote.nombre:
            pos = c
            break
        # lo que te indice si esta ordenado de menor a mayor o mayor a menor es  la ">"
        elif v_lotes[c].nombre > nuevo_lote.nombre:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    # indices  0    1
    # v_lotes [L2, L1]
    # nombre    A   B
    v_lotes[pos:pos] = [nuevo_lote]     # Aca el nuevo_lote va si o si entre corchetes


# ======================================================================
#           Opcion 2
# ======================================================================
def mostrar_datos(v_lotes, t1, t2):

    # indices   0   1   2
    # v_lotes [ L1, L2, L3]
    for i in v_lotes:
        # i = L1,     L2, L3        --> la i vale como cada elemento de la lista
        if t1 <= i.importe <= t2:
            print(i)


# ======================================================================
#           Opcion 4
# ======================================================================
def generar_archivo_binario(v_lotes, fd, l1, l2):

    m = open(fd, "wb")  # recibe dos parametros, primer parametro = nombre del archivo (fd)
                                        # segundo parametro = modo de apertura ("wb")
    # wb = write binary, generar un archivo binario si no existiera, sobre-escribe tod0 su contenido

    # si te dijeran que el archivo debe conservar su contenido cada vez que se ingrese a la opcion "ab"
    # ab = append binary, generar un archivo binario si no existiera, agrega el contenido al final del archivo,
    # conservando su contenido anterior

    for i in v_lotes:
        # i = L1,     L2, L3        --> la i vale como cada elemento de la lista
        if l1 <= i.lote <= l2:
            pickle.dump(i, m)   # -> recibe dos parametros, el primero = lo que quiero guardar ( i )
                                                    #   el segundo = donde lo quiero guardar ( m )
            m.flush()  # opcional

    m.close()  # OBLIGATORIO


# ======================================================================
#           Opcion 5
# ======================================================================
def mostrar_archivo_binario(fd):

    if os.path.exists(fd) is False:
        print("El archivo NO existe.")
        return

    m = open(fd, "rb")  # read binary -> leer el archivo binario
    tam = os.path.getsize(fd)   # nos dice o nos devuelve el tamaño en bytes del archivo    # tam = 620

    # este es el recorrido para leer un archivo binario

    # indices   0   1   2
    # v_lotes [ L1, L2, L3]

    #
    # archivo =     [ L1           L2                 L3 ]
    # bytes         0       200             400           620
    # m.tell()      0       200             400

    # mostrar al final en una linea el calculo del promedio de los importes de los lotes dentro
    # del archivo que tengan una orientacion hacia el norte o el sur.
    # promedio = acumulador (de importes) / cantidad
    acum = 0
    cont = 0

    while m.tell() < tam:
        lotecito = pickle.load(m)

        print(lotecito)
        if lotecito.orientacion == 1 or lotecito.orientacion == 2:
            acum += lotecito.importe
            cont += 1

    # calcular promedio
    prom = 0
    if cont > 0:
        prom = acum / cont

    print("El promedio de los lotes mostrados de orientacion norte y sur es:", prom)

    m.close()   # OBLIGATORIO





def menu():
    print("1 - Cargar Arreglo.")
    print("2 - Mostrar Arreglo.")
    print("3 - Matriz con el Arreglo.")
    print("4 - Generar archivo binario con el Arreglo.")
    print("5 - Mostrar archivo binario con el Arreglo.")
    op = int(input("Ingresar opcion: "))
    return op


def principal():

    # arreglo/vector/lista de trabajo
    v_lotes = []

    # el nombre de tu archivo binario de trabajo
    fd = "lotes.dat"       # -> file description ; nombre del archivo

    op = -1
    while op != 0:
        op = menu()

        if op == 1:

            n = validar_n()
            # Cada vez que se ingrese en esta opción, el arreglo debe ser creado desde cero y
            # tod0 contenido anterior debe ser eliminado.
            v_lotes = []
            cargar_arreglo(v_lotes, n)

        elif op == 2:
            """
            - solo mostrar los lotes que tengan un importe que esta entre un importe t1 y t2 que se cargar por teclado
            """
            t1 = float(input("Importe a superar: "))
            t2 = float(input("Importe a ser menor: "))
            mostrar_datos(v_lotes, t1, t2)

        elif op == 3:
            pass

        elif op == 4:
            """
             4 - A partir del arreglo, genere un archivo binario que contenga los datos de todos 
             los lotes cuyo número de lote esté comprendido entre l1 y l2, siendo estos valores 
             que se ingresan por teclado.
            """
            l1 = int(input("Ingreesar numero de lote a superar: "))
            l2 = int(input("Ingreesar numero de lote a ser inferior: "))
            generar_archivo_binario(v_lotes, fd, l1, l2)

        elif op == 5:
            """
            5 - Mostrar el archivo generado en el punto anterior y luego de mostrarlo agregue 
            una línea que informe el valor promedio de venta de los lotes contenidos en el archivo.
            """
            mostrar_archivo_binario(fd)



if __name__ == '__main__':
    principal()







