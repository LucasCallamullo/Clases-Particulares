
import random
from registro import *


# ==============================================================
#                   Opcion 1
# ==============================================================
def validar_n():
    n = int(input("Ingresar cantidad de celulares a cargar: ")) # 3
    while n <= 0:       # mientras n sea igual o menor a cero ingrese al ciclo
        n = int(input("Ingresar cantidad de celulares a cargar (DEBE SER POSITIVO): "))

    return n


def cargar_arreglo(v_celus, n):
    # marca = (1: Samsung, 2: Xiaomi, 3: Hauwei)
    # id > 0, descripcion, marca(1, 3), pulgadas(5, 13), importe > 0
    tupla_marcas = ("Samsung", "Motorola", "Xiaomi")

    for i in range(n):  # 3
        id = random.randint(1, 10)      # INT
        descripcion = random.choice("ABCDEF")      # STR
        marca = random.randint(1, 3)       # INT
        pulgadas = random.randint(5, 13)       # INT
        importe = round(random.uniform(0.1, 10), 2)   # Float

        celu = Celular(id, descripcion, marca, pulgadas, importe)
        v_celus.append(celu)
        # v_celus = [C1, C2, C3,

    print(f"Se cargaron la cantidad de {n} celulares.")


# ==============================================================
#                   Opcion 2
# ==============================================================
def ordenar_arreglo(v_celus):

    n = len(v_celus)

    for i in range(n-1):
        for j in range(i+1, n):

            # la boquita determina si esta de menor a mayor o mayor a menor
            if v_celus[i].id > v_celus[j].id:
                v_celus[i], v_celus[j] = v_celus[j], v_celus[i]


def mostrar_datos(v_celus, x):

    # Al final del listado indique cuantos celulares se mostraron
    cont = 0

    # Al final del listado mostrar el promedio de los importes de los celualres que se mostraron
    # promedio = acumulado(de importes) / cantidad
    cont = 0
    acum = 0

    # indices     0     1       2
    # v_celus = [C1,    C2,     C3]
    for i in v_celus:
        # i = C1, C2, C3

        if i.pulgadas > x:
            print(i)
            cont += 1
            acum += i.importe

    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio de los importes que se mostraron:", prom)

    print("La cantidad de celulares que se mostro fue:", cont)