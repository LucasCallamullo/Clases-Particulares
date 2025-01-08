import os.path
import pickle
import random

from soporte import *

import soporte


# ============================================================================
#                       Opcion 1
# ============================================================================
def validar_n():
    n = int(input("Ingresar cantidad de internos a cargar: "))
    while n <= 0:   # mientras n sea igual o menor pido de nuevo n
        n = int(input("Ingresar cantidad de internos a cargar: "))
    return n


def cargar_arreglo(v, n):
    # dni INT, nombre STR, tipo (0, 14), pago (0, 4), edad INT, importe FLOAT
    for i in range(n):          # la cantidad de "n" vueltas

        dni = random.randint(1, 10)
        nombre = random.choice("ABCDEF")            # STR
        tipo = random.randint(0, 14)
        pago = random.randint(0, 4)
        edad = random.randint(1, 10)            # INT
        importe = round(random.uniform(0.1, 10), 2)     # FLOAT

        inter = Interno(dni, nombre, tipo, pago, edad, importe)     # from soporte import *
        # inter = soporte.Interno(dni, nombre, tipo, pago, edad, importe)     # import soporte

        add_in_order(v, inter)


def add_in_order(v, inter):
    izq, der = 0, len(v) - 1

    while izq <= der:

        c = (izq + der) // 2

        # el atributo por el que te pídan ordenar
        if v[c].nombre == inter.nombre:
            pos = c
            break

        # la orientacion de la boca indica si esta de menor a mayor o mayor a menor
        elif v[c].nombre > inter.nombre:
            der = c - 1

        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v[pos:pos] = [inter]


# ============================================================================
#                       Opcion 2
# ============================================================================
def mostrar_datos(v):
    # calcular el promedio de importes de los internos mostrados
    # promedio = sumatoria de IMPORTEs / la cantidad de veces que acumule
    acum = 0
    cont = 0

    # indices       0    1      2       3
    # v         = [ I1,  I2,   I3,     I4]
    for i in v:
        # i = I1,   I2,     I3,     I4

        # solo mostrar los importes que superen el valor de cero
        if i.importe > 0:
            print(i)

            acum += i.importe
            cont += 1

    # calcular promedio
    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio de importes es:", prom)


# ============================================================================
#                       Opcion 6
# ============================================================================
def generar_archivo_binario(v, fd, mon):
    """
    Grabar en un archivo binario los datos de los registros del arreglo generado en el punto 1 que correspondan a
internos cuyo tipo de servicio sea mayor a 3 y tengan un monto pagado superior al valor mon que se carga por
teclado. [Máximo 4 puntos].
    """
    m = open(fd, "wb")      # primer parametro nombre del archivo
                            # segundo parametro modo de apertura
    # wb = write binary = crea el archivo y borra todo el contenido anterior y sobreescribe el nuevo
    # ab = append binary = crea el archivo, agregar contenido al final, conservando todo lo anterior

    # indices       0    1      2       3
    # v         = [ I1,  I2,   I3,     I4]
    for i in v:
        # i = I1,   I2,     I3,     I4

        # internos cuyo tipo de servicio sea mayor a 3 y tengan un monto pagado superior al valor mon
        if i.tipo > 3 and i.importe > mon:

            pickle.dump(i, m)   # primer parametro: lo que quiero guardar ( i )
                                # segundo parametro: donde lo queres guardar ( m )

    print("Se cargo correctamente el archivo binario.") # opcional
    m.close()       # OBLIGATORIO


def generar_archivo_binario_promedio(v, fd):
    """
    guardes en un archivo binario solo los internos que superen el importe promedio del arreglo

    # primero obtengo el importe promedio
    # despues guardo los que superen el importe promedio
    """
    # calcular el promedio
    # prom = acum ( de importes ) / cantidad veces que acumule
    acum = 0
    cont = 0

    for i in v:
        acum += i.importe
        cont += 1

    prom = acum / cont
    print("el promediop es:", prom)

    # segundo paso
    m = open(fd, "wb")
    for i in v:
        # i = I1,   I2,     I3,     I4
        if i.importe > prom:
            pickle.dump(i, m)

    print("Se cargo correctamente el archivo binario.")
    m.close()


# ============================================================================
#                       Opcion 7
# ============================================================================
def mostrar_archivo_binario(fd):
    """
    Mostrar el archivo generado en el punto 6. Muestre al final una línea extra indicando la cantidad de registros que
se mostraron. [Máximo 4 puntos].
    """

    bandera = os.path.exists(fd)        # si existe retorn TRUE, si no existe return FALSE
    if bandera is False:
        print("El archivo no existe.")
        return          # cortar funciones

    m = open(fd, "rb")      # read binary, leer el archivo

    tamanio = os.path.getsize(fd)       # nos dice el tamaño del archivo en bytes

    #
    # bytes                 0                                         150
    # archivo       =       [       I1             I2             I3  ]
    # m.tell()              0              50             100

    #
    # Muestre al final una línea extra indicando la cantidad de registros que se mostraron, solo mostrar los que
    # van del tipo de servicio 3 al 10 (ambos incluidos).
    cont = 0

    # si 50 es menor que 150
    while m.tell() < tamanio:
        inter = pickle.load(m)      # recibe unico parametro el archivo ( m )
        # inter = I1,       I2

        # if 3 <= inter.tipo <= 10:
        print(inter)
        cont += 1

    print("Se mostraron la cantidad de", cont, "registros.")

    m.close()


# ============================================================================
#                       Opcion 3
# ============================================================================
def busqueda_secuencial(v, num):            # num 99
    """
    cortar al primer resultado.
    """
    # indices       0       1           2
    # v         = [ I1,     I2  ,       I3 ]
    # dni           6       4           5

    for i in range(len(v)):
        # i = 0,    1,       2
        if v[i].dni == num:
            # i = 1
            return i
    return -1


def busqueda_secuencial_mas_de_uno(v, num):            # num 99
    """
    todos los resultados posibles, no es comun
    """
    cont = 0

    for i in range(len(v)):
        # i = 0,    1,       2
        if v[i].dni == num:
            print(v[i])
            cont += 1

    if cont == 0:
        print("No existe.")


# ============================================================================
#                       Opcion 5
# ============================================================================
def busqueda_binaria(v, nom):
    izq, der = 0, len(v) - 1

    while izq <= der:

        c = (izq + der) // 2

        # if v[c].nombre == inter.nombre:
        if v[c].nombre == nom:
            pos = c
            return pos
            # break

        # elif v[c].nombre > inter.nombre:
        elif v[c].nombre > nom:
            der = c - 1

        else:
            izq = c + 1

    return -1


# ============================================================================
#                       Menu
# ============================================================================
def menu():
    # ctrl + d
    print("1 - Cargar arreglo.")
    print("2 - mostrar arreglo.")
    print("3 - busqueda secuencial.")
    print("4 - busqueda binaria.")

    print("6 - generar archivo binario.")
    print("7 - mostrar archivo binario.")

    op = int(input("Ingresar una opcion: "))
    return op


def principal():

    v = []      # list()

    # puntos de archivo de binario
    fd = "internos.dat"     # .dat o .bin

    op = -1
    while op != 0:      # mientras op sea distinto de cero ingreso al ciclo

        op = menu()

        if op == 1:
            n = validar_n()
            cargar_arreglo(v, n)

        elif op == 2:
            # if len(v) > 0:        # si el tamaño es mayor que cero
            if v:
                mostrar_datos(v)

            else:
                print("No se cargo el arreglo.")

        elif op == 3:
            if v:
                num = int(input("Ingresar dni a buscar: "))
                pos = busqueda_secuencial(v, num)

                if pos >= 0:
                    # ---------------------------------------------------
                    # Si existe modificar su importe con un incremento del 10%, y muestres sus datos antes
                    # y despues del cambio
                    print("datos viejos:", v[pos])

                    v[pos].importe += v[pos].importe * 0.1

                    # decrementar un 25%
                    # v[pos].importe -= v[pos].importe * 0.25

                    print("datos actualizados:", v[pos])

                    # ---------------------------------------------------
                    # Si existe, muestre solo su nombre y edad.
                    print("Nombre:", v[pos].nombre, "y Edad:", v[pos].edad)

                    # print(v[pos])       # mi resultado de la busqueda ( todos los datos )

                    # ---------------------------------------------------
                    # cargar nuevo importe por teclado
                    print("datos viejos:", v[pos])
                    v[pos].importe = float(input("Ingresar nuevo importe: "))
                    print("datos actualizados:", v[pos])

                else:
                    print("no existe.")

            else:
                print("No se cargo el arreglo.")

        elif op == 5:
            if v:
                nom = input("INgresar nombre a buscar: ")
                pos = busqueda_binaria(v, nom)

                if pos >= 0:
                    # Si existe mostrar solo todos sus datos
                    print(v[pos])
                else:
                    print("No existe.")

            else:
                print("No se cargo el arreglo.")

        elif op == 6:

            if v:       # si el arreglo existe
                mon = float(input("Ingresar importe a superar: "))
                generar_archivo_binario(v, fd, mon)

            else:
                print("No se cargo el arreglo.")

        elif op == 7:
            if v:
                mostrar_archivo_binario(fd)

            else:
                print("No se cargo el arreglo.")


if __name__ == '__main__':
    principal()












