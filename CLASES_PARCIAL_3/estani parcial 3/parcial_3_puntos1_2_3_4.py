import random
from clase import *


# ==============================================================================
#           Punto 1
# ==============================================================================
def validar_n():
    """ Validar que n sea mayor que cero """
    n = int(input("Cantidad de empleos a cargar: "))
    while n <= 0:       # mientras n sea igual o menor que cero, ingresa al while
        n = int(input("Cantidad de empleos a cargar (DEBE SER U NUMERO POSITIVO): "))       # 3
    return n        # 3


def cargar_arreglo(v_empleos, n):

    # num_id INT ; descripcion STR ; tipo INT (0, 39) ; sueldo FLOAT > 0
    for i in range(n):      # 5
        # i = 0, 1, 2, 3, 4
        num_id = random.randint(1000, 9999)     # Int
        descripcion = random.choice("ABCDEF")       # Str
        tipo = random.randint(13, 18)    # int
        sueldo = round(random.uniform(0.1, 9), 2)     # float   5.25

        emp = Empleo(num_id, descripcion, tipo, sueldo)

        v_empleos.append(emp)
        # v_empleos = [ E1, E2, E3, E4 ]

    print("Se cargaron la cantidad de empleos de:", n)


# ==============================================================================
#           Punto 2
# ==============================================================================
def ordenar_datos(v_empleos):
    n = len(v_empleos)          # 5

    # indices       0       1       2       3
    # v_empleos = [ E2,     E1,    E3,    E4 ]
    # descipcion    A       D       C       B
    n = len(v_empleos)      # 4

    for i in range(n-1):        # range(3)
        # i = 0,  1,        2

        for j in range(i+1, n):     # range(4)
            # j = 1,  2,  3

            # >   ---> de menor a mayor
            # <   ---> de mayor a menor
            if v_empleos[i].descripcion > v_empleos[j].descripcion:
                v_empleos[i], v_empleos[j] = v_empleos[j], v_empleos[i]


def mostrar_datos(v_empleos):
    # 2.bis - solo mostrar los empleos cuyo sueldo sea superior a una variable "salario",
    # ademas que su descripcion sea distinta de "desc" que se carga por teclado
    # que se ingresa por teclado, indicar al final cuantos empleos se mostraron
    salario = int(input("Ingresar sueldo a superar: "))         # 5.0
    desc = input("Ingresar descripcion: ")

    cont_empleos_mostrados = 0

    for i in v_empleos:
        # i = E1,   E2,     E3,     E4
        if i.sueldo > salario and i.descripcion != desc:
            print(i)
            cont_empleos_mostrados += 1

    print("Se mostraron:", cont_empleos_mostrados)


def mostrar_datos_2(v_empleos):
    # Al final del listado indique la suma de los sueldos a pagar por todos
    # los empleos que se mostraron
    acum_sueldos = 0

    for i in v_empleos:
        # i = E1,   E2,     E3,     E4
        acum_sueldos += i.sueldo

    print("El acumulado de los sueldos fue: ", acum_sueldos)


def mostrar_datos_3(v_empleos):
    # Mostrar los datos de todos los empleos cuyo sueldo esté entre los valores i1 e i2
    # (ambos incluidos) que se cargan por teclado.
    i1 = int(input("Valor a superar: "))
    i2 = int(input("Valor a ser menor: "))

    for i in v_empleos:
        # i = E1,   E2,     E3,     E4
        # if i.sueldo >= i1 and i.sueldo <= i2:
        if i1 <= i.sueldo <= i2:
            print(i)


def mostrar_datos_4(v_empleos):
    # Mostrar los datos de todos los empleos y al final en una linea extra
    # mostrar el promedio de sus sueldos
    # promedio = sumatoria de cosas / la cantidad que sume
    acum = 0
    cont = 0

    for i in v_empleos:
        # i = E1,   E2,     E3,     E4
        print(i)
        acum += i.sueldo
        cont += 1

    # calculo el promedio
    prom = 0
    if cont > 0:
        prom = acum // cont
    print("El promedio es:", prom)


# ==============================================================================
#           Punto 3
# ==============================================================================
def vector_conteo(v_empleos):
    """
    Determinar cuántos Empleos hay para cada uno de los tipos de empleo (del 13 al 18).
    Mostrar todos los conteos que sean diferentes de cero.
    """
    # Crear el vector de conteo
    # tipo(13, 18) = lim_superior - lim_inferior + 1 = 18 - 13 + 1 = 6
    # tipo(1, 20) = lim_superior - lim_inferior + 1 = 20 - 1 + 1 = 20
    v_conteo = [0] * 6

    # tipo        13-13   14-13   15-13    16      17      18
    # indices   =   0       1       2       3       4       5
    # v_conteo  =  [2,      0,      1,      0,      0,      0]
    # Rellenar el vector
    for i in v_empleos:
        # i = E1, E2, E3
        v_conteo[i.tipo - 13] += 1

        # determinar el sueldo acumulado por cada tipo de empleo
        # v_conteo[i.tipo - 13] += i.sueldo

    # si te pidieran mostrar los contadores mayores a una variable mayor a cero
    cantidad_a_superar = int(input("Cantidad a superar: "))

    # Mostrar el vector de conteo
    n = len(v_conteo)
    for i in range(n):
        # i = 0,   1,   2,   3,  4,   5

        # v_conteo[i]   -->     contador, acumulador, a la cantidad, o al acumulado de algo
        # i+13          -->     al tipo de empleo
        if v_conteo[i] > cantidad_a_superar:
            print("El tipo de empleo:", i+13, "tiene la cantidad de empleados de", v_conteo[i])

        # solo muestres los tipo entre t1 y t2
        # if t1 <= i+13 <= t2:
        #    print("El tipo de empleo:", i + 13, "tiene la cantidad de empleados de", v_conteo[i])


# ==============================================================================
#           Punto 4
# ==============================================================================
def busqueda_secuencial(v_empleos):
    """
    Determinar si existe un empleado cuyo num identifacion sea igual a cod.
    - Si existe alguno, modificar su sueldo por una variable s1 ingresada por teclado,
    y mostrar los datos de ese empleado antes y después del cambio.
    - Si no existe, informar con un mensaje.
    - Debe mostrar los datos del primer empleado que encuentre, y detener la búsqueda en
    la primera que encuentre (sin importar si hay más de un objeto que cumpla el
    criterio pedido)
    """
    n = len(v_empleos)
    cod = int(input("Ingresar num_id a buscar: "))
    # nombre = input("Ingresar nombre a buscar: ")        # porque es str

    # indice        0   1   2
    # v_empleos = [E1, E2, E3]

    for i in range(n):
        # i = 0, 1, 2, 3, ...
        emp = v_empleos[i]      # --> E1, E2, E3

        if emp.num_id == cod:
            print("Datos viejos:", emp)

            # pido por teclado el nuevo sueldo
            s1 = int(input("Ingresar nuevo sueldo: "))
            emp.sueldo = s1

            print("Datos actualizados:", emp)

            return      # corta la funcion

    print("No existe ese empleado con num_id:", cod)


def busqueda_secuencial_2(v_empleos):
    n = len(v_empleos)
    nombre = input("Ingresar nombre a buscar: ")        # porque es str

    for i in range(n):
        # i = 0, 1, 2, 3, ...
        emp = v_empleos[i]  # --> E1, E2, E3

        if emp.nombre == nombre:
            # Solo mostrar sueldo y nombre
            print("Datos viejos: Sueldo:", emp.sueldo, " | Nombre:", emp.nombre)

            # realizar un descuento del 25% sobre el sueldo
            emp.sueldo -= emp.sueldo * 0.25

            # sueldo_a_restar = emp.sueldo * 25 / 100
            # emp.sueldo -= sueldo_a_restar
            print("Datos actualizados: Sueldo:", emp.sueldo, " | Nombre:", emp.nombre)
            return  # corta la funcion

    print("No existe ese empleado con nombre:", nombre)



def menu():
    print()
    print("1 - Cargar Arreglo.")
    print("2 - Mostrar Arreglo.")
    print("3 - Vector de conteo o acumulación.")
    print("4 - Búsqueda secuencial.")
    op = int(input("Ingresar opción: "))        # 3
    return op       # 3


def principal():

    # arreglo / vector de trabajo
    v_empleos = []      # list()

    op = -1
    while op != 0:

        op = menu()

        if op == 1:
            n = validar_n()
            cargar_arreglo(v_empleos, n)

        elif op == 2:
            # if len(v_empleos) == 0:
            if v_empleos:
                ordenar_datos(v_empleos)
                mostrar_datos(v_empleos)
            else:
                print("Debe pasar primero por la opción 1...")

        elif op == 3:
            if v_empleos:
                vector_conteo(v_empleos)
            else:
                print("Debe pasar primero por la opción 1...")

        elif op == 4:
            if v_empleos:
                busqueda_secuencial(v_empleos)
            else:
                print("Debe pasar primero por la opción 1...")


if __name__ == '__main__':
    principal()
