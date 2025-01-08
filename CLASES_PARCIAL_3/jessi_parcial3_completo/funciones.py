
import random
from registro import *


# ====================================================================
#                   Opcion 1
# ====================================================================
def validar_n():
    n = int(input("Ingresar la cantidad de parlantes a cargar en el arreglo: "))    # 3
    while n <= 0:       # mientras n sea igual o menor a cero
        n = int(input("Ingresar la cantidad de parlantes a cargar en el arreglo: (DEBE SER POSITIVO) "))

    return n


def cargar_arreglo(v_parlantes, n):
    # id > 0, descripcion, marca(1, 5), peso(200, 250), importe > 0,

    for i in range(n):      #
        id = random.randint(1, 10)      # INT
        descripcion = random.choice("ABCDEF")   # STR
        marca = random.randint(1, 5)        # INT
        peso = random.randint(1, 20)        # INT
        importe = round(random.uniform(0.1, 10), 2)      # FLOAT

        parlantito = Parlante(id, descripcion, marca, peso, importe)
        v_parlantes.append(parlantito)
        # v_parlantes = [P1, P2, P3

    print("Se cargaron los", n, "parlantes.")


# ====================================================================
#                   Opcion 2
# ====================================================================
def ordenar_arreglo(v_parlantes):
    n = len(v_parlantes)
    for i in range(n-1):
        for j in range(i+1, n):
            # esta condicion lo que cambia es el atributo por el que rodenamos
            if v_parlantes[i].id > v_parlantes[j].id:
                v_parlantes[i], v_parlantes[j] = v_parlantes[j], v_parlantes[i]


def mostrar_arreglo(v_parlantes, t1, t2):

    # Al final del listado mostrado, decir cuantos parlantes se mostraron
    cont = 0

    # Al final del listado mostrado, decir la suma de los importes de parlantes se mostraron
    acum = 0

    # indices         0     1       2
    # v_parlantes = [P1,    P2,     P3]
    for i in v_parlantes:
        # i = P1,   P2,     P3

        if t1 <= i.importe <= t2:
            print(i)
            cont += 1
            acum += i.importe

    print("La cantidad de parlantes mostrados fue:", cont)
    print("La suma de los importes de parlantes mostrados fue:", acum)