

import os.path
import pickle
import random


from registro import *


# ====== Opcion 1
def validar_n():
    n = int(input("Ingresar cantidad de consumos a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de consumos a cargar: "))
    return n


def cargar_arreglo(v_consumos, n):

    num_fake = "+54 351 54376"
    numeros = "0123456789"

    # num_tel STR, hora (0, 23), tipo(1, 3), importe FLOAT > 0
    for i in range(n):      # 3
        #           "+54 351 54376" +  5   + 7  = "+54 351 5437657"
        num_tel = num_fake + random.choice(numeros) + random.choice(numeros)      # STR
        hora = random.randint(1, 24)                    # INT
        tipo = random.randint(1, 3)                     # INT
        importe = round(random.uniform(0.1, 10), 2)     # FLOAT

        cons = Consumo(num_tel, hora, tipo, importe)    # C3
        add_in_order(v_consumos, cons)


def add_in_order(v_consumos, cons):
    # C1.num_tel    3
    # C2.num_tel    1
    # C3.num_tel    2

    # indices        0          1
    # v_consumos = [ C2,        C1 ]
    # num_tel        1          3
    izq, der = 0, len(v_consumos) - 1

    # izq = 1
    # der = 1
    while izq <= der:           # mientras izq sea igual o menor a derecha
        c = (izq + der) // 2    # c = centro = center
        # c = 0
        if v_consumos[c].num_tel == cons.num_tel:
            pos = c
            break
        elif v_consumos[c].num_tel > cons.num_tel:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq       # = 0
    # indices        0   1
    # v_consumos = [ C2, C1 ]
    # num_tel        1    3
    v_consumos[pos:pos] = [cons]        # [cons] --> si o si los corchetes


# ====== Opcion 2
def mostrar_arreglo(v_consumos, x):
    # indices        0   1
    # v_consumos = [ C1, C2

    for i in v_consumos:
        # i = C1, C2, C3
        if i.importe > x:
            print(i)


# ====== Opcion 3
def generar_matriz(v_consumos, h1, h2):

    # crear la matriz
    f = 3   # filas = tipo (1, 3) --> lim_superior - lim_inferior + 1 =  3
    c = 24  # columnas = hora (500, 524) --> lim_superior - lim_inferior + 1 = 24 - 1 + 1 = 24
    matriz = [[0] * c for i in range(f)]

    # tipo(1, 3) -->  1-1   2   3
    # indices           0   1   2

    # hora(1, 24) -->   1-1
    # indices           0

    # [ [0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    ,
    #   [0, 0, 0, 0, 5, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    ,
    #   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    ]

    # rellenar la matriz
    for i in v_consumos:
        # i = C1, C2, C3, C4 ...
        # matriz[f][c] +=
        matriz[i.tipo - 1][i.hora - 1] += i.importe
        # matriz[i.tipo - 1][i.hora - 1] += 1

    # mostrar la matriz
    for f in range(len(matriz)):        # range(3)
        # f = 0, 1, 2

        for c in range(len(matriz[0])):     # range (24)
            # f = 0
            # c = 0, 1, 2, ..., 23

            # Muestre únicamente aquellos acumulados que correspondan al horario entre las "h1" y las "h2" hs
            if h1 <= c+1 <= h2:
                print("Para el tipo de consumo:", f+1, "y la hora:", c+1)
                print("Tiene el importe acumulado de:", matriz[f][c])
                print()

            # Solo mostrar los que tengan un contador/acumulador mayor a cero
            if matriz[f][c] > 0:
                pass        # hacer prints

            # solo mostrar los acumuladores mayores a "x" y que sean del tipo de consumo SMS
            # if matriz[f][c] > "x" and f+1 == 1:
            #    pass   # hacer prints


# ====== Opcion 4
def generar_archivo_binario(v_consumos, fd, t):
    m = open(fd, "wb")      # primer parametro: nombre del archivo (fd), segundo parametro: modo de apertura ("wb")
    # v_consumos = [ C1, C2, C3 ]

    for i in v_consumos:
        # i = C1, C2, C3

        # Solo guardar los tipo de consumos SMS y Llamada y que correspondan al numero de telefono "t"
        if (i.tipo == 1 or i.tipo == 2) and i.num_tel == t:

            pickle.dump(i, m)   # primer parametro = lo que quiero guardar, (i) es el objeto C1, C2, C3
                                # segundo parametro = el archivo donde lo queremos guardar (m)

            m.flush()      # opcional

    m.close()   # OBLIGATORIO


# ====== Opcion 5
def mostrar_archivo_binario(fd):

    if os.path.exists(fd):          # devuelve True si el archivo existe, False si no existe

        m = open(fd, "rb")          # read binary, leer archivo
        tamanio = os.path.getsize(fd)   # devolver el tamaño en bytes del archivo  = 108

        # indices        0   1   2
        # v_consumos = [ C1, C2, C3 ]

        #
        # consumos.dat = [ C2                    C3  ]
        # bytes          0           54             108
        # m.tell()       0           54             108

        #
        # - al final del listado mostrar el promedio de los importes de los tipo de consumos que eran SMS
        # promedio = acumulado ( de los importes) / cantidad
        acum = 0
        cont = 0

        while m.tell() < tamanio:

            consu = pickle.load(m)  # recibe como parametro (m) o el archivo
                                    # recupera al objeto completo como tal
            # consu = C2
            if consu.tipo == 1:
                print(consu)
                cont += 1
                acum += consu.importe

        # calcular promedio
        prom = 0
        if cont > 0:
            prom = acum / cont
        print("El promedio de los importes del tipo SMS es:", prom)

        m.close()

    # No existe el archivo
    else:
        print("El archivo no existe, ingrese a la opcion 4.")


# ====== Opcion 6
def busqueda_binaria(v_consumos, num):
    izq, der = 0, len(v_consumos) - 1

    while izq <= der:  # mientras izq sea igual o menor a derecha
        c = (izq + der) // 2  # c = centro = center
        # c = 0
        # if v_consumos[c].num_tel == cons.num_tel:
        if v_consumos[c].num_tel == num:
            # pos = c
            # break
            return c
        elif v_consumos[c].num_tel > num:
            der = c - 1
        else:
            izq = c + 1
    # agregamos
    return -1


# ======================================================
#           Principal
# ======================================================
def menu():
    print(" 1 - Cargar Arreglo.")
    print(" 2 - Mostrar Arreglo.")
    print(" 3 - Generar Matriz.")
    print(" 4 - Generar Archivo binario.")
    print(" 5 - Mostrar archivo binario")
    print(" 0 - Salir.")
    return int(input("Ingresar opcion: "))


def main():  # principal()

    # Lista, arreglo, vector de trabajo
    v_consumos = []

    # fd = file description = nombre del archivo
    fd = "consumos.dat"

    op = -1
    while op != 0:

        op = menu()

        if op == 1:
            """
            1 - cada vez que se ingrese a la opcion 1 debe construir nuevamente el arreglo
            
            """
            n = validar_n()
            v_consumos = []
            cargar_arreglo(v_consumos, n)

        elif op == 2:
            """
            2 - Mostrar arreglo, pero solo los que importe "x"
            """
            if len(v_consumos) > 0:
                x = int(input("Importe a superar: "))
                mostrar_arreglo(v_consumos, x)
            else:
                print("Primero debe pasar por la opcion 1")

        elif op == 3:
            """
            3 - A partir del arreglo generado en el punto 1, calcular el monto total acumulado por 
            hora del día y por tipo de consumo. Muestre únicamente aquellos acumulados que correspondan 
            al horario entre las "h1" y las "h2" hs
            """
            if len(v_consumos) > 0:
                h1 = int(input("Ingresar hora a superar: "))
                h2 = int(input("Ingresar hora a ser menor: "))
                generar_matriz(v_consumos, h1, h2)
            else:
                print("Primero debe pasar por la opcion 1")

        elif op == 4:
            """
            4 - Generar archivo binario, debe conservar su contenido y agregar lo nuevo al final "ab"; 
            "ab" --> crea un archivo nuevo, agrega contenido al final y conserva lo anterior
            "wb" --> crea un archivo nuevo, sobreescribe todo su contenido cada vez que usamos esta opcion 4
            
            Solo guardar los tipo de consumos SMS y Llamada y que correspondan al numero de telefono "t"
            """
            if len(v_consumos) > 0:
                t = input("numero de telefono a guardar: ")
                generar_archivo_binario(v_consumos, fd, t)
            else:
                print("Primero debe pasar por la opcion 1")

        elif op == 5:
            """
            5 - Mostrar Archivo binario generado
            - al final del listado mostrar el promedio de los importes de los tipo de consumos que eran SMS
            """
            mostrar_archivo_binario(fd)

        elif op == 6:
            """ 
            6 - Busqueda binaria:
            buscar por "num" que va a ser un numero de telefoon, si existe mostrar datos, si no existe informar
            
            """
            num = input("Buscar num_tel: ")
            pos = busqueda_binaria(v_consumos, num)

            if pos >= 0:
                pass

            else:
                print("No existe")


if __name__ == '__main__':
    main()

