
import random

# Traer el modulo registro completo
from registro import *


# ================================================================================
#                           Opcion 1
# ================================================================================
def cargar_arreglo(v_paquetes, n):
    # id INT > 0, descripcion STR , tipo INT (2, 21) , cantidad INT , importe FLOAT
    descripciones = "ABCDEF"
    for i in range(n):          # 5
        id = random.randint(1, 10)
        descripcion = random.choice(descripciones)
        tipo = random.randint(2, 21)
        cantidad = random.randint(1, 10)
        importe = round(random.uniform(0.1, 10), 2)
        paquete = Paquete(id, descripcion, tipo, cantidad, importe)

        v_paquetes.append(paquete)

    print("Se cargaron la cantidad de paquetes:", n)


# ================================================================================
#                           Opcion 2
# ================================================================================
def ordenar_arreglo(v_paquetes):
    #                0   1   2   3   4
    # v_paquetes = [P1, P2, P3, P4, P5]

    # v_paquetes[i]
    n = len(v_paquetes)   # 5
    for i in range(n-1):        # 4
        # i = 0, 1, 2, 3

        for j in range(i+1, n):
            # j = 1, 2, 3, 4

            # Menor a mayor , se come a la i >
            # Mayor a menor , se come a la j >
            if v_paquetes[i].cantidad > v_paquetes[j].cantidad:
                v_paquetes[i], v_paquetes[j] = v_paquetes[j], v_paquetes[i]


def mostrar_arreglo(v_paquetes, t):
    # v_paquetes = [P1, P2, P3, P4, P5]
    """
        Solo mostrar los Paquetes que superen un importe "t" que se ingresa por teclado y ademas
        al final de listado mostrar cuantos registros se mostraron.
    """
    cont = 0

    for i in v_paquetes:
        # i = P1, P2, ... , P5
        if i.importe > t:
            print(i)
            cont += 1

    print("Se mostraron la cantidad de registros de:", cont)


# ================================================================================
#                           Opcion 3
# ================================================================================
def generar_vector_conteo(v_paquetes):
    # tipo INT (2, 21)

    # Generar el vector con 0
    v_conteo = [0] * 20

    # tipo         2-2 3-2 4-2      15  18  19  20
    # indices      0  1  2
    # v_conteo = [ 1, 0, 1, 2, ..., 1 , 0]

    # Rellenar el vector de conteo
    for i in v_paquetes:
        # i = P1, P2, P3
        v_conteo[i.tipo-2] += 1

        # que te hubieran pedido el acumulado de importes por tipo
        # v_acum[i.tipo] += i.importe

    # Mostrar el vector
    may = None
    tipo = None

    for i in range(len(v_conteo)):      # 20
        # i = 0, 1, 2, 3, 4, ..., 19

        # Solo muestres los contadores que tengan una cantidad mayor a 0
        if v_conteo[i] > 0:
            print("Del Tipo:", i+2, "Existen la cantidad de paquetes:", v_conteo[i])

        if may is None or v_conteo[i] > may:
            may = v_conteo[i]  # 2
            tipo = i+2         # 3

    print("El tipo con la mayor cantidad de paquetes es:", tipo)


# ================================================================================
#                           Opcion 4
# ================================================================================
def busqueda_secuencial(v_paquetes, x, t):
    pos = -1
    for i in range(len(v_paquetes)):        # 5
        # i = 0, 1, 2, 3, 4
        if v_paquetes[i].id == x and v_paquetes[i].importe >= t:
            pos = i
            break   # Romper ciclos

    return pos      # -1    ;  0 2 3

