import os.path
import pickle
import random
from registro import *


# ===================================================================
#                       Opcion 1
# ===================================================================
def validar_n():
    n = int(input("Ingresar cantidad de consumos a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de consumos a cargar: "))  # 5
    return n


def cargar_arreglo(v_consumos, n):

    # num_tel STR, hora(0, 23) INT, tipo(1, 3), importe FLOAT, titular STR
    for i in range(n):  # 5
        num_tel = str(random.randint(1000, 9000))    # STR
        hora = random.randint(0, 23)    # INT
        tipo = random.randint(1, 3)    # INT
        importe = round(random.uniform(0.1, 10), 2)   # FLOAT
        titular = random.choice("ABCDEF")   # STR

        nuevo_consumo = Consumo(num_tel, hora, tipo, importe, titular)
        # c1, c2
        add_in_order(v_consumos, nuevo_consumo)


def add_in_order(v_consumos, nuevo_consumo):
    # C1.num_tel        5

    # indices           0
    # v_consumos = [     ]

    izq, der = 0, len(v_consumos) - 1
    # izq = 0
    # der = -1

    while izq <= der:
        c = (izq + der) // 2

        # lo unico que cambia es el atributo por el que te pidan ordenar
        if v_consumos[c].num_tel == nuevo_consumo.num_tel:
            pos = c
            break

        # la boquita ">" determina si esta de menor a mayor, o de mayor a menor
        elif v_consumos[c].num_tel > nuevo_consumo.num_tel:
            der = c - 1

        else:
            izq = c + 1

    if izq > der:
        pos = izq

    # indices           0
    # v_consumos = [    C1 ]
    v_consumos[pos:pos] = [nuevo_consumo]   # el objeto va ENTRE CORCHETES [ ]


# ===================================================================
#                       Opcion 2
# ===================================================================
def mostrar_datos(v_consumos):

    # indices           0       1       2
    # v_consumos = [    C1,     C2 ,    C3 ]

    for consumo in v_consumos:
        # consumo = C1,   C2,     C3
        # consumo.nombre consumo.codigo consumo.importe
        print(consumo)


# ===================================================================
#                       Opcion 3
# ===================================================================
def generar_matriz(v_consumos, h1, h2):

    # crear la matriz
    f = 3   # f = filas = tipo(1, 3) = lim_superior - lim_inferior + 1 = 3 - 1 + 1 = 3
    c = 24  # c = columnas = hora(0, 23) = lim_superior - lim_inferior + 1 = 23 - 0 + 1 = 24
    matriz = [ [0] * c for i in range(f) ]

    # tipo(1, 3)       1-1       2       3
    # fila_indices      0       1       2

    # hora(0, 23)       0   1   2   3       23
    # columnas_indices  0   1   2   3   ... 23

    # matriz[f][c]
    # matriz = [    [0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #               [0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    ]

    #
    # rellenar la matriz:
    for i in v_consumos:
        # i = C1, C2, C3
        # matriz[f][c]
        matriz[i.tipo - 1][i.hora] += i.importe

    #
    # mostrar la matriz
    for f in range(len(matriz)):    # range(3)
        # f = 0, 1, 2

        for c in range(len(matriz[0])):  # range(24=
            # c = 0, 1, 2, ..., 23

            # Muestre únicamente aquellos acumulados que correspondan al horario entre las h1 y las h2 hs
            if h1 <= c <= h2:
                print("Hora:", c, "| Tipo de Consumo:", f+1, "| Importe acumulado:", matriz[f][c])

            # solo mostrar el tipo de consumos SMS -->
            # if 1 == f+1:
            #    print("Hora:", c, "| Tipo de Consumo:", f+1, "| Importe acumulado:", matriz[f][c])

            # solo mostrar los contadores/Acumuladores mayores a 0
            # if matriz[f][c] > 0:
            #    print("Hora:", c, "| Tipo de Consumo:", f+1, "| Importe acumulado:", matriz[f][c])


# ===================================================================
#                       Opcion 4
# ===================================================================
def generar_archivo_binario(v_consumos, fd, t):
    """
    A partir del arreglo genere un archivo binario que contenga todos los consumos
    correspondientes a llamadas y mensajes tipo SMS realizados por el número de teléfono
    t (que se carga por teclado).
    """
    m = open(fd, "wb")  # primer parametro: nombre del archivo ( fd )
    #           # segundo parametro: modo de apertura( "wb" )
    # wb --> crea el archivo si no existe, sobre escribe todo el contenido
    # ab (append binary) --> crea el archivo si no existe, agrega contenido al final del
    # archivo conservando todo su contenido anterior

    for i in v_consumos:
        # i = C1, C2, C3
        if i.tipo == 1 and i.num_tel == t:
            pickle.dump(i, m)   # primer parametro: lo que quiero guardar ( i )
                                # segundo parametro: donde lo quierop guardar ( m )

    print("Se genero el archivo.")  # opcional
    m.close()   # OBLIGATORIO


# ===================================================================
#                       Opcion 5
# ===================================================================
def mostrar_archivo_binario(fd):
    """
    5 - Mostrar el archivo generado en el punto anterior y luego de mostrarlo agregue una
    línea que informe la cantidad de registros que se mostraron en el listado.
    """
    bandera = os.path.exists(fd)    # retorna True si el archivo existe, FALSE si NO existe
    if bandera is False:        # if not bandera
        print("El archivo no existe.")
        return      # cortar la funcion

    m = open(fd, "rb")  # read binary, modo de lectura
    tam = os.path.getsize(fd)   # nos devuelve el tamaño del archivo en bytes = 300

    # archivo = [   C1          C2               C3 ]
    # bytes     0       100         200            300
    # m.tell()  0       100

    # al final indicar el promedio de los importes que se mostraron
    # prom = acum (de  importes ) / cantidad d eveces que acumule
    acum = 0
    cont = 0

    while m.tell() < tam:
        consu = pickle.load(m)  # unico parametro el archivo ( m )
        # consu = C1    C2      C3
        print(consu)
        acum += consu.importe
        cont += 1

    # calcular promedio
    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio es:", prom)

    m.close()   # OBLIGATORIO


# ===================================================================
#                       Opcion 6
# ===================================================================
def busqueda_binaria(v_consumos, num):
    # v_consumos [ C1,  c2, C3 ]

    izq, der = 0, len(v_consumos) - 1

    while izq <= der:
        c = (izq + der) // 2

        # if v_consumos[c].num_tel == nuevo_consumo.num_tel:
        if v_consumos[c].num_tel == num:
            pos = c
            # break
            return pos  # 0 o +, si existe el registro

        # elif v_consumos[c].num_tel > nuevo_consumo.num_tel:
        elif v_consumos[c].num_tel > num:
            der = c - 1

        else:
            izq = c + 1

    return -1   # NO EXISTE


def menu():
    # ctrl + d
    print("1 - Cargar Arreglo. ")
    print("2 - Mostrar Arreglo. ")
    print("3 - Generar Matriz. ")
    print("4 - Generar Archivo Binario. ")
    print("5 - Mostrar Archivo Binario. ")
    print("6 - Busqueda Binaria. ")
    print("0 - Salir.")
    op = int(input("Ingresar opcion: "))
    return op


def principal():

    # arreglo / vector / lista de trabajo
    v_consumos = []

    # Nombre del archivo
    fd = "consumos.dat"   # file description ; nombre del archivo

    op = -1
    while op != 0:      #

        op = menu()

        if op == 1:
            n = validar_n()
            # Cada vez que se ingrese en esta opción, el arreglo debe ser creado desde cero y
            # todo contenido anterior debe ser eliminado
            v_consumos = []
            cargar_arreglo(v_consumos, n)

        elif op == 2:
            if len(v_consumos) > 0:
                mostrar_datos(v_consumos)
            else:
                print("Debe cargar el arreglo.")

        elif op == 3:
            # Muestre únicamente aquellos acumulados que correspondan al horario entre las h1 y las h2 hs
            h1 = int(input("Ingresar hora a superar: "))
            h2 = int(input("Ingresar hora a ser menor: "))
            generar_matriz(v_consumos, h1, h2)

        elif op == 4:
            # S realizados por el número de teléfono t (que se carga por teclado).
            t = input("Ingresar num_tel a guardar: ")
            generar_archivo_binario(v_consumos, fd, t)

        elif op == 5:
            mostrar_archivo_binario(fd)

        elif op == 6:
            """ 
            6 - buscar num_tel "num" que se carga por teclado
            Si existe y su tipo de consumos era llamadas o sms hacer un descuento del 22% mostrar
            sus datos antes y despues del cambio.
            Si no existe informar con el mensaje "no existe ese num_tel <num>
            """
            num = input("Ingresar num_tel a buscar: ")
            pos = busqueda_binaria(v_consumos, num)

            if pos >= 0:
                print("datos sin actualizar:", v_consumos[pos])

                if v_consumos[pos].tipo == 1 or v_consumos[pos].tipo == 2:
                    # descuento del 22%
                    v_consumos[pos].importe -= v_consumos[pos].importe * 0.22

                print("datos actualizados:", v_consumos[pos])

            else:   # pos = -1
                print("No existe ese num_tel:", num)


if __name__ == '__main__':
    principal()

