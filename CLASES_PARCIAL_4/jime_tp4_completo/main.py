import os.path
import pickle

from envio import *


# =====================================================
#               Opcion 1
# =====================================================
def opcion1(csv, fd):

    bandera = os.path.exists(fd)    # devuelve True si "fd" existe, y sino devuelve False si "fd" NO existe
    if bandera:             # significa que esta en True
        # ctrl + d
        print("1 - Si sobreeescribir")
        print("2 - Cancelar.")
        op = int(input("Elegir opcion: "))  # 3
        if op == 2:
            print("Se cancelo la operacion.")
            return      # corte de la funcion

    archivo_csv = open(csv, "r")    # primer parametro es el nombre del archivo (csv)
                                    # segundo parametro el modo de apertura ( r = read = leer)

    m = open(fd, "wb")  # write binary, crea el archivo si no existe, y sobre-escribe todo su contenido

    cont = 0

    for linea in archivo_csv:

        cont += 1

        if cont > 2:
            # PREGUNTAR SI PUEDEN HACERLO DE ESTA FORMA
            lista_linea = linea.strip().split(",")
            # indices           0       1               2        3
            # lista_linea = [ "8547", "Del $ol 456.",   "4",  "2" ]
            codigo = lista_linea[0]
            direccion = lista_linea[1]
            tipo = int(lista_linea[2])
            pago = int(lista_linea[3])

            env = Envio(codigo, direccion, tipo, pago)
            pickle.dump(env, m)     # primer parametro es el objeto a guuardar (env)
                                    # segundo parametro es donde lo quiero guardar (m)

            m.flush()   # opcional  --> guarda mejor el archivo

    print("Se genero el archivo correctamente.")    # opcional

    m.close()               # OBLIGATORIO
    archivo_csv.close()     # OBLIGATORIO


# =====================================================
#               Opcion 2
# =====================================================
def validar_rango(inf, sup, msj):
    # funcion reutilizada del tp3  --> de lo que subio de la catedra
    valor = int(input(msj))
    while sup < valor or valor < inf:
        print("El valor ingresado no es correcto. Intente nuevamente.")
        valor = int(input(msj))
    return valor


def opcion2(fd):

    m = open(fd, "ab")  # append binary, para agregar elementos al final del archivo conservando su contenido anterior
                                        # si el archivo no existe tambien lo crea
    # codigo STR, direccion STR, tipo INT, pago INT
    codigo = input("Codigo postal: ")
    direccion = input("Direccion postal: ")
    tipo = validar_rango(0, 6, "Tipo de envio (entre 0 y 6): ")
    pago = validar_rango(1, 2, "Forma de pago (entre 1 y 2): ")

    env = Envio(codigo, direccion, tipo, pago)
    pickle.dump(env, m)
    m.flush()       # opcional

    print("Se agrego el nuevo envio")
    print()
    m.close()       # OBLIGATORIO


# =====================================================
#               Opcion 3
# =====================================================
def opcion3(fd):

    if os.path.exists(fd) is False:     # if not os.path.exists(fd)
        print("El archivo no existe.")
        return      # cortar la funcion

    m = open(fd, "rb")  # read binary   # modo de lectura
    tam = os.path.getsize(fd)   # nos dice/nos devuelve el tamaño en bytes del archivo 1530 bytes

    # indices      0    1   2
    # v_lista = [ E1 , E2 , E3 ]

    #
    # archivo = [ E1        E2              E3 ]
    # bytes     0      500        1000      1530
    # m.tell()  0      500        1000      1530

    while m.tell() < tam:

        env = pickle.load(m)    # me recupera al objeto como tal a partir del byte que estoy leyendo
        # env = E1, E2,  E3


        print(env)

    m.close()       # OBLIGATORIO


# =====================================================
#               Opcion 4
# =====================================================
def opcion4(fd, cp):

    if os.path.exists(fd) is False:  # if not os.path.exists(fd)
        print("El archivo no existe.")
        return  # cortar la funcion

    m = open(fd, "rb")  # read binary   # modo de lectura
    tam = os.path.getsize(fd)  # nos dice/nos devuelve el tamaño en bytes del archivo 1530 bytes

    while m.tell() < tam:
        env = pickle.load(m)
        # env = E1, E2,  E3
        if env.codigo == cp:
            print(env)

    m.close()  # OBLIGATORIO



# =====================================================
#               Opcion 6
# =====================================================
def opcion6(fd):

    if os.path.exists(fd) is False:  # if not os.path.exists(fd)
        print("El archivo no existe.")
        return  # cortar la funcion

    #
    # crear la matriz
    f = 2    # f = filas = pago(1, 2)  --> 2
    c = 7    # c = columnas = tipo(0, 6) -> lim_superior - lim_inferior + 1 = 6 - 0 + 1 = 7
    matriz = [ [0] * c for i in range(f) ]

    # pago(1, 2)      1-1   2-1
    # fila_indices =    0,  1

    # tipo(0, 6)        0   1   2   3   4   5   6
    # columnas_indices  0   1   2   3   4   5   6

    # matriz = [    [2, 1, 0, 0, 0, 0, 0],
    #               [0, 0, 0, 0, 0, 0, 0]       ]

    #
    # rellenar la matriz
    m = open(fd, "rb")  # read binary   # modo de lectura
    tam = os.path.getsize(fd)  # nos dice/nos devuelve el tamaño en bytes del archivo 1530 bytes

    while m.tell() < tam:
        env = pickle.load(m)
        # env = E1, E2,  E3
        # matriz[f][c]
        matriz[env.pago - 1][env.tipo] += 1
        # matriz[env.pago - 1][env.tipo] += env.importe

    m.close()  # OBLIGATORIO

    #
    # mostrar la matriz
    for f in range(len(matriz)):    # range(2)
        # f = 0, 1

        for c in range(len(matriz[0])):     # range( 7 )
            # c = 0, 1, ..., 6

            # solo mostrar los contadores/acumuladores sean distinto de cero
            if matriz[f][c] > 0:
                print("Tipo de Envio:", c, "| Forma de Pago:", f+1, "| Cantidad:", matriz[f][c])

            # solamente muestre la forma de pago que sea igual a 1
            # if f+1 == 1:

    return matriz


# =====================================================
#               Opcion 8
# =====================================================
def opcion8_promedio(fd):
    if os.path.exists(fd) is False:  # if not os.path.exists(fd)
        print("El archivo no existe.")
        return  # cortar la funcion

    m = open(fd, "rb")  # read binary   # modo de lectura
    tam = os.path.getsize(fd)  # nos dice/nos devuelve el tamaño en bytes del archivo 1530 bytes

    # calcular promedio = acumulado ( de importes ) / cantidad de veces qeu acumule
    acum = 0
    cont = 0

    while m.tell() < tam:
        env = pickle.load(m)
        # env = E1, E2,  E3

        importe = env.calcular_importe()
        acum += importe
        cont += 1

    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio es:", prom)

    m.close()  # OBLIGATORIO

    return prom


def opcion8(fd, promedio):
    if os.path.exists(fd) is False:  # if not os.path.exists(fd)
        print("El archivo no existe.")
        return  # cortar la funcion

    m = open(fd, "rb")  # read binary   # modo de lectura
    tam = os.path.getsize(fd)  # nos dice/nos devuelve el tamaño en bytes del archivo 1530 bytes

    # nuestro arreglo de trabajo
    v_envios = []

    while m.tell() < tam:
        env = pickle.load(m)
        # env = E1, E2,  E3
        importe = env.calcular_importe()

        if importe > promedio:
            v_envios.append(env)

    # shellsort
    shell_sort(v_envios)

    # mostrar
    for i in v_envios:
        # i = E1, E2
        print(i)


def shell_sort(v):
    n = len(v)
    h = 1

    # Determinar el valor inicial de h según el tamaño de la lista
    while h <= n // 9:
        h = 3 * h + 1

    # Ejecutar el proceso de Shell Sort
    while h > 0:
        for j in range(h, n):
            temp = v[j]  # Guardar el objeto completo
            k = j - h

            # Comparar los atributos 'codigo' y ordenar el objeto completo
            while k >= 0 and temp.codigo < v[k].codigo:
                v[k + h] = v[k]  # Mover el objeto completo
                k -= h

            v[k + h] = temp  # Colocar el objeto completo en la posición correcta

        h //= 3  # Reducir h para la siguiente pasada


def menu():
    print()
    print("1 - Generar Archivo.")
    print("2 - Agregar Archivo.")
    print("3 - Mostrar Archivo.")
    print("4 - Buscar por Código Postal.")
    print("5 - Buscar por Dirección Postal.")
    print("6 - Generar Matriz.")
    print("7 - Mostrar Matriz.")
    print("8 - Generar Arreglo.")
    print("0 - Salir.")
    op = int(input("Ingresar opcion: "))
    return op


def principal():

    # v_envios = [E1, E2, E3]
    # archivo = [ E1        E2          E3 ]

    # crear el nombre de nuestro archivo binario principal
    fd = "envios.dat"       # file description , nombre del archivo

    # nombre de nuestro archivo csv a leer
    # csv = "envios-tp4.csv"
    csv = "envios-muestra.csv"

    op = -1
    while op != 0:  # mientras op sea distinto de cero, ingreso al ciclo while

        op = menu()

        if op == 1:
            opcion1(csv, fd)

        elif op == 2:
            opcion2(fd)

        elif op == 3:
            opcion3(fd)

        elif op == 4:
            cp = input("Codigo postal a buscar: ")
            opcion4(fd, cp)

        elif op == 6:
            matriz = opcion6(fd)

        elif op == 7:
            # opcion7(matriz)
            pass

        elif op == 8:
            # si una variable esta igualada a una funcion es pórque espera que la funcion devuelva algo
            promedio = opcion8_promedio(fd)
            opcion8(fd, promedio)



if __name__ == '__main__':
    principal()
