import os.path
import pickle
import random
from registro import *


# ========================================================================
#                               Opcion 1
# ========================================================================
def validar_n():
    n = int(input("Ingrese cantidad de productos a cargar: "))
    while n <= 0:       # mientras n sea igual o menor a 0, que entre al ciclo
        n = int(input("Ingrese cantidad de productos a cargar(debe ser positivo): "))
    return n


def cargar_arreglo(v_prod, n):
    nombres = "ABCDEF"
    # tipo (1, 4)           # marca (555, 559)
    # def __init__(self, id, nombre, marca, tipo, importe):
    for i in range(n):          # 3
        # i = 0             1       2
        id = random.randint(1, 15)          # enteros
        nombre = random.choice(nombres)     # strings
        marca = random.randint(555, 559)
        tipo = random.randint(1, 4)
        importe = round(random.uniform(0.1, 10), 2)     # flotantes
        productito = Producto(id, nombre, marca, tipo, importe)
        add_in_order(v_prod, productito)


def add_in_order(v_prod, productito):       # Primera vuelta
    izq, der = 0, len(v_prod) - 1           # len(v_prod) = 0       ;       productito.id = 5
                                            # v_prod = [ P1 ]
    while izq <= der:                       # Segunda vuelta
        c = (izq + der) // 2                # len(v_prod) = 1       ;       productito.id = 4
        if v_prod[c].id == productito.id:                                   # id = 4
            pos = c
            break
        elif v_prod[c].id > productito.id:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    #             0       1     2
    # v_prod = [  P2,    P1 ]
    v_prod[pos:pos] = [productito]


# ========================================================================
#                           Opcion 2
# ========================================================================
def mostrar_datos(v_prod, t):
    # v_prod = [ P1.id , P2, P3, P4 ]
    #            P1.importe,
    #            P1.tipo
    cont = 0
    for i in v_prod:
        if i.importe > t:
            print(i)
            cont += 1

    print("La cantidad de arreglos que se mostraron fue:", cont)


# ========================================================================
#                           Opcion 3
# ========================================================================
# tipo (1, 4)   1:Motherboard, 2: Procesador, 3:Ram, 4:Gabinete
# marca (555, 559)  555:Asus, 556: Gygabite, 557: AMD, 558:Logitech, 559:Redragon
def generar_matriz(v_prod):
    # crear la matriz en 0
    filas = 4       # tipo
    columnas = 5    # marca
    matriz = [[0] * columnas for i in range(filas)]

    # [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

    # [ [0, 1, 0, 1, 0],
    #   [2, 0, 1, 0, 0],
    #   [0, 0, 0, 0, 0],
    #   [0, 0, 0, 0, 0] ]

    # Rellenar la matriz
    for i in v_prod:
        matriz[i.tipo-1][i.marca-555] += 1
        # si nos pidiera el costo acumulado por marca y tipo
        # matriz[i.tipo-1][i.marca-555] += i.importe

    # mostrar la matriz
    marcas_str = ("Asus", "Gygabite", "AMD", "Logitech", "Redragon")
    tipos_str = ("Motherboard", "Procesador", "Cooler", "Gabinete")
    for f in range(len(matriz)):        # f = 0, 1, 2, 3
        for c in range(len(matriz[0])):     # c = 0, 1, 2, 3, 4
            if matriz[f][c] > 0 and (c+555 == 557 or c+555 == 558 or c+555 == 559):
                print("=" * 50)
                print("La cantidad por tipo:", tipos_str[f], "y marca:", marcas_str[c])
                print("La cantidad total es:", matriz[f][c])


# ========================================================================
#                           Opcion 4
# ========================================================================
def generar_archivo(fd, v_prod, x):
    m = open(fd, "wb")  # write binary , crear archivo? si, si existiera un archivo previamente lo sobreescribe
    # m = open(fd, "ab")  # append binary, crear archivo? si, si existiera un archivo previamente lo agrega al final

    cont = 0
    for i in v_prod:
        # i = P1 , P2, P3
        if i.importe > x and (i.marca == 555 or i.marca == 556):
            cont += 1
            pickle.dump(i, m)
            m.flush()       # no es necesario

    print("La cantidad de producots que se cargaron:", cont)
    m.close()   # VA SI O SI


# ========================================================================
#                           Opcion 5
# ========================================================================
def mostrar_archivo(fd):
    if os.path.exists(fd):
        m = open(fd, "rb")   # read binary, modo de lectura del archivo.
        tam = os.path.getsize(fd)       # esto va a devolver el tamaño total en 206 bytes

        # v_prod =  [ P1 , P2 , P3 ]

        # fd    = [ P1          P2 ]
        #         0       103       206

        cont = 0
        acum = 0

        while m.tell() < tam:
            prod = pickle.load(m)
            print(prod)

            if prod.tipo == 1 or prod.tipo == 2:
                cont += 1
                acum += prod.importe

        if cont > 0:
            prom = acum / cont
            print("El promedio de los precios de los motherboards y procesadores es:", prom)

        m.close()

    else:
        print("El archivo no existe, por favor ingrese primero por la opcion 4.")


# ========================================================================
#                           Opcion 6
# ========================================================================
def busqueda_binaria(v_prod, num):
    # vector = [ id id id id id ]
    izq, der = 0, len(v_prod) - 1

    while izq <= der:
        c = (izq + der) // 2
        if v_prod[c].id == num:
            return c            # 0 1   2   3   4 ...
        elif v_prod[c].id > num:
            der = c - 1
        else:
            izq = c + 1
    return -1




def menu():
    print("=" * 50)
    print(" 1 - Cargar Arreglo."
          "\n 2 - Mostrar datos."
          "\n 3 - Generar y Mostrar Matriz"
          "\n 4 - Generar Archivo Binario"
          "\n 5 - Mostrar Archivo Binario")

    return int(input("Ingresar opcion: "))


def principal():

    # arreglo / vector / lista principal
    v_prod = list()     # []


    # nombre del archivo binario
    fd = "productos.dat"        # file description = nombre del archivo


    op = -1
    while op != 0:

        op = menu()

        if op == 1:
            n = validar_n()
            cargar_arreglo(v_prod, n)

        elif op == 2:
            t = float(input("Ingrese precio a superar: "))
            mostrar_datos(v_prod, t)

        elif op == 3:
            generar_matriz(v_prod)

        elif op == 4:
            x = float(input("Ingreso precio a superar para guardar en el archivo: "))
            generar_archivo(fd, v_prod, x)

        elif op == 5:
            mostrar_archivo(fd)

        elif op == 6:
            num = int(input("Ingresar id a buscar: "))
            pos = busqueda_binaria(v_prod, num)

            if pos >= 0:
                # mostrar datos
                print(v_prod[pos])

                # modificar su precio
                val = float(input("Ingresar valor: "))
                v_prod[pos].importe = val

                # aumento del 25%
                # v_prod[pos].importe = v_prod[pos].importe + v_prod[pos].importe * 0.25

                # muestres solamente algun atributo
                # print(v_prod[pos].importe)

            else:
                print("No se encontro un producto con ese id.")





if __name__ == '__main__':
    principal()
