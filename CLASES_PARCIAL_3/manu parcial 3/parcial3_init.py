import random

# import clase                    # clase.Producto
# from clase import Producto      # Producto
from clase import *             # Producto


# ==========================================================================
#           Opcion 1
# ==========================================================================
def validar_n():
    n = int(input("Ingresar cantidad de Productos a cargar: "))     # 5
    while n <= 0:
        n = int(input("Ingresar cantidad de Productos a cargar: "))
    return n


def cargar_arreglo(n, v_productos):

    # codigo INT ; descripcion STR ; calorias INT ; tipo (1, 30) INT ; precio FLOAT
    for i in range(n):
        codigo = random.randint(10, 99)         # INT aleatorio
        descripcion = random.choice("ABCDEF")           # STR al azar
        calorias = random.randint(1, 10)                # INT aleatorio
        tipo = random.randint(1, 30)                    # INT aleatorio
        precio = round(random.uniform(0.1, 10), 2)    # FLOAT aleatorio

        product = Producto(codigo, descripcion, calorias, tipo, precio)
        v_productos.append(product)
        # v_productos = [ P1, P2, P3, P4 ]

    print("Se cargaron", n, "Productos.")


# ==========================================================================
#           Opcion 2
# ==========================================================================
def ordenar_arreglo(v_productos):
    # v_productos = [ P1, P2, P3, P4 ]
    n = len(v_productos)        # 4

    for i in range(n - 1):      # 3
        # i = 0,            1, 2

        for j in range(i+1, n):     # 4
            # j = 1, 2,             3
            # i = 0

            # la orientacion de la boquita te indica si esta de menor a mayor O mayor a menor.

            # if 10 > 5
            if v_productos[i].calorias > v_productos[j].calorias:
                v_productos[i], v_productos[j] = v_productos[j], v_productos[i]


def mostrar_arreglo(v_productos):
    # mostrar el promedio de las calorias de los productos mostrados
    # promedio = sumatoria de las calorias // cantidad veces que sumaste
    acum = 0
    cont = 0

    # v_productos = [ P1, P2, P3, P4 ]
    for i in v_productos:
        # i = P1,   P2 ,    P3
        print(i)
        acum += i.calorias
        cont += 1

    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio de calorias es:", prom)


def mostrar_arreglo_2(v_productos):
    # mostrar al final  la sumatoria de calorias de los productos mostrados
    # que superen el precio "x" ingresado por teclado.
    acum = 0
    x = int(input("Precio a superar: "))

    # v_productos = [ P1, P2, P3, P4 ]
    for i in v_productos:
        # i = P1,   P2 ,    P3
        if i.precio > x:
            print(i)
            acum += i.calorias

    print("La Sumatoria de calorias es:", acum)


def mostrar_arreglo_3(v_productos):
    # mostrar la cantidad productos mostrados
    # que esten entre los precios "x1" y "x2" (ambos incluidos) ingresado por teclado.
    cont = 0
    x1 = int(input("Precio a superar: "))
    x2 = int(input("Precio a ser menor: "))

    # v_productos = [ P1, P2, P3, P4 ]
    for i in v_productos:
        # i = P1,   P2 ,    P3,     P4
        if x1 <= i.precio <= x2:
            print(i)
            cont += 1

    print("La cantidad de productos mostrados es:", cont)


# ==========================================================================
#           Opcion 3
# ==========================================================================
def vector_conteo(v_productos):
    """
    Determinar la cantidad de productos que hay en el arreglo por cada tipo de producto posible
    (30 contadores en total en un vector de conteo).
    Muestre solo los valores de los contadores cuyos valores finales sean mayores a cero y menores a tres.
    """
    # 1. Crear el vector de conteo/acum
    # tipo(1, 30)   = lim_superior - lim_inferior + 1 = 30 - 1 + 1 = 30
    v_conteo = [0] * 30

    # 2. Rellenar el vector
    # v_productos   = [ P1,     P2,     P3, ... ]
    # tipo          =   2       1       2

    # tipo(1, 30)      1-1     2-1     3-1  ... 30-1
    # indices           0       1       2,  ..., 29
    # v_conteo      = [ 1  ,    1   ,   0,  ... ]
    for i in v_productos:   # v_productos   = [ P1,     P2,     P3, ... ]
        # i = P1, P2, P3, ...
        v_conteo[i.tipo - 1] += 1

        # determinar el precio acumulado por cada tipo de marca
        # v_conteo[i.tipo - 1] += i.precio

    # t1 = int(input("Ingresar tipo inferior a mostrar: "))
    # t2 = int(input("Ingresar tipo superior a mostrar: "))

    # 3. Mostrar el vector
    for i in range(len(v_conteo)):  # range(30)
        # i = 0, 1, 2, 3, 4, ..., 29    --> i toma el valor de indices

        # i + 1 --> tipo
        # v_conteo[i] --> a cada contador

        # Muestre solo los valores de los contadores cuyos valores finales
        # sean mayores a cero y menores a tres.
        if 0 < v_conteo[i] < 3:
            print("Tipo:", i+1, "- Tiene la cantidad de:", v_conteo[i])
        # if v_conteo[i] > 0 and v_conteo[i] < 3:

        # Muestre solo los contadores que correspondan los tipos que esten entre t1 y t2 que
        # se cargan por teclado
        # if t1 < i+1 < t2:
            # print("Tipo:", i + 1, "- Tiene la cantidad de:", v_conteo[i])


# ==========================================================================
#           Opcion 4
# ==========================================================================
def busqueda_secuencial(v_productos):
    """
    Determinar si existe un producto cuyo código sea igual cod, siendo cod un valor que se carga por teclado.
    Si existe, mostrar solo su descripción y su precio. Si no existe, informar con un mensaje.
    Si existe más de un registro que coincida con esos parámetros de búsqueda, debe mostrar sólo el
    primero que encuentre. La búsqueda debe detenerse al encontrar el primer objeto que coincida con
    el criterio pedido.
    """
    cod = int(input("Ingrese codigo a buscar: "))   # 3

    # indices         0   1   2   3
    # v_productos = [ P1, P2, P3, P4 ]
    # codigo           5   4  3   8
    for i in range(len(v_productos)):
        # i = 0, 1, 2, ....

        # producto = v_productos[i]
        #
        if v_productos[i].codigo == cod:

            # Si existe, aumentar se precio por un 25%, mostrar los cambios antes y despues
            print("Datos viejos: ", v_productos[i])

            # v_productos[i].precio = v_productos[i].precio + ( v_productos[i].precio * 25 / 100 )
            v_productos[i].precio += v_productos[i].precio * 0.25   # aumenta el 25%
            print("Datos nuevos: ", v_productos[i])

            # si existe cargar un nuevo precio por teclado
            # v_productos[i].precio = float(input("Ingrese un nuevo precio: "))

            # Si existe, mostrar solo su descripción y su precio.
            print("Descripcion:", v_productos[i].descripcion, "- Precio:", v_productos[i].precio)
            return      # para terminar la funcion, termina el ciclo

    print("No existe")
    # for i in v_productos:
    #    pass


# punto 2 alternativo
def mostrar_datos_promedio(v_productos):
    """
        Solo mostrar los productos del arreglo, que tengan un precio mayor al precio promedio de los precios
        de los productos dentro del arreglo.
        1. Calcular promedio
        2. muestro los que superen el promedio

        prom = acumulado de precios / la cantidad veces sumamos
    """
    # calcular promedio
    acum = 0
    cont = 0
    for i in v_productos:
        acum += i.precio
        cont += 1
    prom = 0
    if cont > 0:
        prom = acum / cont

    # mostramos datos
    for i in v_productos:
        # i = P1, P2, P#
        if i.precio > prom:
            print(i)


def menu():
    # ctrl + d
    print("1 - Cargar Arreglo.")
    print("2 - Mostrar Arreglo.")
    print("3 - Vector de conteo.")
    print("4 - Busqueda secuencial.")
    print("0 - Salir.")
    x = int(input("Ingresar opcion: "))        # 3
    return x   # 3


def principal():

    # lista - arreglo - array - vector
    v_productos = []            # [ P1, P2 ]

    op = -1
    while op != 0:

        op = menu()         # op = el retorno

        if op == 1:
            n = validar_n()
            cargar_arreglo(n, v_productos)

        elif op == 2:
            # if v_productos:
            if len(v_productos) > 0:
                ordenar_arreglo(v_productos)
                mostrar_arreglo(v_productos)
            else:
                print("No se cargo el arreglo...")

        elif op == 3:
            if len(v_productos) > 0:
                vector_conteo(v_productos)
            else:
                print("No se cargo el arreglo...")

        elif op == 4:
            if len(v_productos) > 0:
                busqueda_secuencial(v_productos)
            else:
                print("No se cargo el arreglo...")

        elif op == 0:
            print("Termino el programa.")


if __name__ == '__main__':
    principal()