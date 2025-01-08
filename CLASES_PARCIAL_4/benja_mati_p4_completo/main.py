import os.path
import pickle
import random

from registro import *


# ===========================================================================
#                               Opcion 1
# ===========================================================================
def validar_n():
    n = int(input("Ingresar cantidad de piezas a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de piezas a cargar: "))
    return n


def cargar_arreglo(v_piezas, n):

    # id INT > 0 , descripcion STR, tipo(1, 3), sector, (10, 25), stock INT, importe FLOAT
    for i in range(n):
        id = random.randint(1, 10)  # INT
        descripcion = random.choice("ABCDEF")   # STR
        tipo = random.randint(1, 3)
        sector = random.randint(10, 25)
        stock = random.randint(1, 10)
        importe = round(random.uniform(0.1, 10), 2)     # FLOAT DE DOS DECIMALES

        nueva_pieza = Pieza(id, descripcion, tipo, sector, stock, importe)
        add_in_order(v_piezas, nueva_pieza)


def add_in_order(v_piezas, nueva_pieza):

    # P1.id     5
    # P2.id     3

    # indices       0
    # v_piezas = [  P1]

    izq, der = 0, len(v_piezas) - 1
    # izq = 0
    # der = -1

    while izq <= der:
        c = (izq + der) // 2    # c = centro = 0

        # el atributo por el que les pidan ordenar
        if v_piezas[c].id == nueva_pieza.id:
            pos = c
            break

        # la boquita ">" determinar si esta de menor a mayor o mayor a menor
        elif v_piezas[c].id > nueva_pieza.id:
            der = c - 1

        else:
            izq = c + 1

    if izq > der:
        pos = izq

    # indices       0       1
    # v_piezas = [  P2,     P1 ]
    # id             3       5
    v_piezas[pos:pos] = [nueva_pieza]   # el objeto VA ENTRE CORCHETES


# ===========================================================================
#                               Opcion 2
# ===========================================================================
def mostrar_datos(v_piezas, x):
    # indices       0       1
    # v_piezas = [  P1,     P2 ]

    for i in v_piezas:
        # i = P1,       P2,     P3
        print(i)

        # agregue un mensaje indicando "Stock reducido" si la cantidad en stock de la
        # pieza mostrada es inferior al valor x
        if i.stock < x:
            print("Stock reducido")


# ===========================================================================
#                               Opcion 3
# ===========================================================================
def generar_matriz(v_piezas, s1, s2):
    # crear la matriz
    f = 3  # f = filas = tipo(1, 3) = lim_superior - lim_inferior + 1 = 3 - 1 + 1 = 3
    c = 16  # c = columnas = sector(10, 25) = lim_superior - lim_inferior + 1 = 25 - 10 + 1 = 16
    matriz = [ [0] * c for i in range(f) ]

    # tipo(1, 3)       1-1     2-1     3-1
    # fila_indices      0       1       2

    # sector(10, 25)   10-10                  25
    # columna_indices   0       1       2   ... 15

    # matriz[f][c]
    # matriz = [    [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #               [0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #               [0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    ]

    #
    # rellenar la matriz
    for i in v_piezas:
        # i = P1,   P2  ,   P3
        # matriz[f][c]
        matriz[i.tipo - 1][i.sector - 10] += i.stock

    #
    # mostrar la matriz
    for f in range(len(matriz)):    # range(3)
        # f = 0, 1, 2

        for c in range(len(matriz[0])): # range(16)
            # c = 0, 1, 2, 3, ..., 15

            # Mostrar únicamente los acumuladores que sean mayores a cero.
            if matriz[f][c] > 0:
                print("Tipo de pieza:", f+1, "| Sector:", c+10, "| Stock Total:", matriz[f][c])

            # solo mostrar los sectores que estan entre el sector s1 y s2.
            if s1 <= c+10 <= s2:
                # print("Tipo de pieza:", f + 1, "| Sector:", c + 10, "| Stock Total:", matriz[f][c])
                pass


# ===========================================================================
#                               Opcion 6
# ===========================================================================
def busqueda_binaria(v_piezas, num_id):     # num_id = 10
    # indices       0       1       2
    # v_piezas = [  P1,     P2,     P3 ]
    # id            4       7       9

    izq, der = 0, len(v_piezas) - 1

    while izq <= der:
        c = (izq + der) // 2

        # if v_piezas[c].id == nueva_pieza.id:
        if v_piezas[c].id == num_id:
            pos = c
            # break
            return pos  # pos = posicion = un indice dentro del arreglo
                        # un indice donde se encuentra un objeto que cumple mi criterio
                        # de busqueda , cuando pos >= 0

        # elif v_piezas[c].id > nueva_pieza.id:
        elif v_piezas[c].id > num_id:
            der = c - 1

        else:
            izq = c + 1

    return -1   # cuando no exista un objeto que cumpla


# ===========================================================================
#                               Opcion 4
# ===========================================================================
def generar_archivo_binario(v_piezas, fd, t):

    m = open(fd, "wb")  # primer parametro: nombre del archivo ( fd )
                        # segundo parametro: el modo de apertura ( "wb" )
    # wb = write binary = CREA EL ARCHIVO SI NO EXISTE, sobre escribe todo el contenido del archivo
    # ab = append binary = CREA EL ARCHIVO SI NO EXISTE, agrega contenido al final del archivo
    # conservando todo su contenido anterior

    for i in v_piezas:
        # i = P1,   P2,     P3

        # guardar los datos de todas las piezas cuyo sector de almacenamiento
        # sea mayor a 15 y que no supere un importe "t"
        if i.sector > 15 and i.importe < t:
            pickle.dump(i, m)   # primer parametro que quiero guardar ( i )
                            # segundo parametro es donde lo quiero guardar ( m )

    print("Se sobre escribio el archivo binario.")      # OPCIONAL

    m.close()   # OBLIGATORIO


# ===========================================================================
#                               Opcion 5
# ===========================================================================
def mostrar_archivo_binario(fd):

    bandera = os.path.exists(fd)    # retornar TRUE si existe el archivo, FALSE si NO existe
    if bandera is False:    # if not bandera:
        print("El archivo no existe.")
        return      # cortar la funcion aca

    m = open(fd, "rb")  # read binary = modo de lectura
    tamanio = os.path.getsize(fd)   # nos dice el tamaño en bytes del archivo = 300

    # archivo = [   P1      P2      P3  ]
    # bytes     0       100     200     300
    # m.tell()  0       100     200

    # indicando además al final una línea extra con la cantidad en
    # stock promedio de todas las piezas mostradas.
    # promedio = acumulado ( de stock ) / la cantidad de veces que acumule
    acum = 0
    cont = 0

    while m.tell() < tamanio:

        piezita = pickle.load(m)    # unico parametro el archivo (m)
        # piezita = P1,         P2,
        print(piezita)

        acum += piezita.stock
        cont += 1

    # calcular promedio
    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio stock es:", prom)

    m.close()       # OBLIGATORIO


# ===========================================================================
#                             PRINCIPAL
# ===========================================================================
def menu():
    print("1 - Cargar arreglo.")
    print("2 - Mostrar arreglo.")
    print("3 - Generar matriz.")
    print("4 - Generar archivo binario.")
    print("5 - Mostrar archivo binario.")
    print("6 - Busqueda binaria.")
    op = int(input("Ingresar opción: "))
    return op


def principal():

    # vector / arreglo / lista de trabajo
    v_piezas = []

    # nombre del archivo binario
    fd = "piezas.dat"   #

    op = -1
    while op != 0:
        op = menu()

        if op == 1:
            n = validar_n()
            """ 
            Cada vez que se ingrese en esta opción, el arreglo debe ser creado desde 
            cero y todo contenido anterior debe ser eliminado.
            """
            v_piezas = []
            cargar_arreglo(v_piezas, n)

        elif op == 2:
            if len(v_piezas) > 0:
                x = int(input("Ingresar stock a superar: "))
                mostrar_datos(v_piezas, x)
            else:
                print("El arreglo no esta cargado.")

        elif op == 3:
            """
            3 - Determinar el valor acumulado en stock por tipo de pieza y 
            sector de almacenamiento
            - solo mostrar los que estan entre el sector s1 y s2 que se carga por teclado
            """
            if len(v_piezas) > 0:
                s1 = int(input("Ingresar sector a superar: "))
                s2 = int(input("Ingresar sector a ser menor: "))
                generar_matriz(v_piezas, s1, s2)

            else:
                print("El arreglo no esta cargado.")

        elif op == 4:
            """
            4 - A partir del arreglo generar un archivo binario donde se incluyan 
            los datos de todas las piezas cuyo sector de almacenamiento sea mayor a 15 y 
            que no supere un importe "t".
            """
            if len(v_piezas) > 0:
                t = float(input("Ingresar importe a no superar: "))
                generar_archivo_binario(v_piezas, fd, t)

            else:
                print("El arreglo no esta cargado.")

        elif op == 5:
            """
            5 - . Mostrar el archivo generado en el punto anterior, a razón de un 
            registro por línea en la pantalla, indicando
            además al final una línea extra con la cantidad en stock promedio 
            de todas las piezas mostradas.
            """
            mostrar_archivo_binario(fd)

        elif op == 6:
            """
            6 - buscar una pieza con el id "num_id" y si existe mostrar sus datos y 
            si era del TIPO2 o TIPO3 realizar un descuento del 22% en su importe y mostrar
            los datos actualizados, 
            pero si no existe 
            informar con el mensaje "no existe ese <num_id> y bla bla bla"
            """
            num_id = int(input("Ingresar ID a buscar: "))
            pos = busqueda_binaria(v_piezas, num_id)
            if pos >= 0:
                print(v_piezas[pos])

                # si era del TIPO2 o TIPO3 realizar un descuento del 22% en su importe
                if v_piezas[pos].tipo == 2 or v_piezas[pos].tipo == 3:
                    # porcentaje
                    # importe total         --- 100%
                    # importe total * 22 / 100  --- 22%
                    v_piezas[pos].importe -= v_piezas[pos].importe * 0.22

                    print("Datos acutalizados:", v_piezas[pos])

                    # modifcar el importe por un valor que se carga por teclado
                    v_piezas[pos].importe = float(input("ingresar nuevo importe: "))

            else:       # cuando pos es -1
                print("no existe ese", num_id, "y bla bla bla")


if __name__ == "__main__":
    principal()
