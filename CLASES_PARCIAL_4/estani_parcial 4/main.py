import os.path
import pickle
import random

from registro import *


# =====================================================================
#           Opcion 1
# =====================================================================
def validar_n():
    n = int(input("Ingresar cantidad de equipos a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de equipos a cargar: "))
    return n


def cargar_arreglo(v_equipos, n):
    nombres = ("Boca", "River", "Belgrano")

    # numero_insc INT, nombre STR, edad INT (12, 17), nivel INT (0,2), monto FLOAT
    for i in range(n):
        numero_insc = random.randint(1, 15)
        nombre = random.choice(nombres)
        edad = random.randint(12, 17)
        nivel = random.randint(0, 2)
        monto = round(random.uniform(0.1, 10))
        campeon = random.choice((True, False))      # bool

        equipito = Equipo(numero_insc, nombre, edad, nivel, monto, campeon)
        add_in_order(v_equipos, equipito)


def add_in_order(v_equipos, equipito):
    # indice        0       1       2       3       4
    # v_equipos = [ E1,     E5,     E2   ,  E3,     E4 ]
    # equipito --> E1       --> .nombre      Boca
    # equipito --> E2       --> .nombre      Doca
    # equipito --> E3       --> .nombre      Eno
    # equipito --> E4       --> .nombre      River
    # equipito --> E5       --> .nombre      Coca
    der = len(v_equipos) - 1        # 0
    izq = 0     # 1

    while izq <= der:
        c = (izq + der) // 2        # centro -> 0

        if v_equipos[c].nombre == equipito.nombre:
            pos = c
            break

        # lo unico que cambio el ordenamiento de menor a mayor o mayor a menor es la boquita ">"
        elif v_equipos[c].nombre > equipito.nombre:
            der = c - 1

        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v_equipos[pos:pos] = [equipito]


# =====================================================================
#           Opcion 2
# =====================================================================
def mostrar_arreglo(v_equipos):
    for equipo in v_equipos:
        # i = E1, E2, E3, ...
        print(equipo)


# =====================================================================
#           Opcion 4
# =====================================================================
def generar_archivo_binario(v_equipos, fd):
    # open() --> primer parametro el nombre del archivo -> fd
    #       --> segundo parametro el modo de apertura -> "wb"

    m = open(fd, "wb")      # write binary      # ab -> append binary
    # wb --> si no existe lo crea al archivo. sobre escribe el contenido
    # ab --> si no existe lo crea al archivo. agrega al final conservando el contenido

    i1 = int(input("Ingresar numero de inscripcion menor a guardar: "))
    i2 = int(input("Ingresar numero de inscripcion mayor a guardar: "))

    for i in v_equipos:
        # i = E1, E2, E3

        # contenga los datos de todos los equipos cuyo número de inscripción esté comprendido entre i1 e i2
        if i1 <= i.numero_insc <= i2:
            pickle.dump(i, m)       # primer parametro es el objeto a guardar -> (i)
            #                       # segundo parametro es donde lo quiero guardar -> osea el archivo (m)

    print("Se genero el archivo correctamente.")
    m.close()       # OBLIGATORIO


def generar_archivo_binario_promedio(v_equipos, fd):
    """
        solo guardar los que tengan un monto superior al monto promedio del arreglo
        - primero calculo el promedio
        - despues guardo los que superen el promedio
    """
    # calcular el promedio
    cont = 0
    acum = 0
    for i in v_equipos:
        acum += i.monto
        cont += 1

    prom = 0
    if cont > 0:
        prom = acum / cont

    m = open(fd, "wb")
    for i in v_equipos:
        if i.monto > prom:
            pickle.dump(i, m)
    m.close()


# =====================================================================
#           Opcion 5
# =====================================================================
def mostrar_archivo_binario(fd):

    existe = os.path.exists(fd)     # si existe el archivo devuelve True, si NO existe devuelve False
    if not existe:
        print("No existe el archivo binario:", fd)
        return      # cortaba la funcion

    # indices     0     1       2
    # listas = [ E1,    E2 ,    E3 ]

    # bytes                     0        130          260       415
    # puntero interno           0        130          260
    # archivo binario =         [   E1          E2          E3 ]
    m = open(fd, "rb")      # read binary   --> modo de lectura solo para ver el contenido
    tamanio = os.path.getsize(fd)       # 415 bytes

    # luego de mostrarlo agregue una línea que informe el valor
    # promedio de edad de los equipos contenidos en el archivo que sean del nivel avanzado.
    acum = 0
    cont = 0

    # muestres cuantos equipos se mostraron
    cont_2 = 0

    while m.tell() < tamanio:
        equi = pickle.load(m)   # recupera un objeto distinto cada vuelta
        # equi = E1, E2

        if equi.nivel == 2:
            print(equi)
            acum += equi.edad
            cont += 1

            cont_2 += 1

    # calcular el promedio
    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio de edad de los equipos es:", prom)

    # cuantos equipos se recuperaron
    print("Se mostraron la cantidad de:", cont_2)

    m.close()       # OBLIGATORIO


def menu():
    print("1 - Cargar arreglo.")
    print("2 - Mostrar arreglo.")
    print("3 - Matriz.")
    print("4 - Guardar archivo binario.")
    print("5 - Mostrar archivo binario.")
    print("6 - Busqueda binaria.")
    print("7 - Busqueda secuencial.")
    op = int(input("Ingresa numero: "))
    return op


def main():

    v_equipos = []
    fd = "equipos.dat"       # file description --> nombre del archivo

    op = -1
    while op != 0:

        op = menu()
        if op == 1:
            n = validar_n()
            # Cada vez que se ingrese en esta opción, el arreglo debe ser creado desde cero y
            # todoo contenido anterior debe ser eliminado.
            v_equipos = []
            cargar_arreglo(v_equipos, n)

        elif op == 2:
            if v_equipos:
                mostrar_arreglo(v_equipos)
            else:
                print("Ingrese por la opcion 1.")

        elif op == 4:
            if v_equipos:
                generar_archivo_binario(v_equipos, fd)
            else:
                print("Ingrese por la opcion 1.")

        elif op == 5:
            mostrar_archivo_binario(fd)


if __name__ == '__main__':
    main()