import random
from registro import *


# ==============================
# Opcion 1
def validar_n():
    n = 0
    while n <= 0:   # Si se cumple la condicion (O sea si es True) ingresa al ciclo
        n = int(input("Ingrese cantidad de arreglos a cargar: "))

    # Si no se cumple la condicion del ciclo while(o sea False) sale del ciclo
    return n


def cargar_arreglo(v_paq, n):
    descripciones = ("A", "B", "C", "D")

    for i in range(n):      # n = 5
        # i = 0 1 2 3 4
        id = random.randint(1, 10)
        # desc = random.choice(descripciones)
        desc = random.randint(1, 4)
        tipo_p = random.randint(0, 19)
        cant_dias = random.randint(1, 10)
        # Funcion para pedir randoms floats
        importe = round(random.uniform(0.1, 10), 2)
        paq = Paquete(id, desc, tipo_p, cant_dias, importe)
        v_paq.append(paq)


# ============================
# Opcion 2
def ordenar(v_paq):
    n = len(v_paq)
    for i in range(n-1):
        for j in range(i+1, n):
            if v_paq[i].cant_dias > v_paq[j].cant_dias:
                v_paq[i], v_paq[j] = v_paq[j], v_paq[i]


def mostrar_datos(v_paq, t):
    #          0  1  2  3
    # v_paq = [P, P, P, P]
    # for i in range(len(v_paq)):   # 4
    #    i = 0, 1, 2, 3
    #    print(v_paq[i])

    # v_paq = [P, P, P, P]
    for i in v_paq:
        # i = P
        if i.importe > t:
            print(i)


# ======================================
# Opcion 3
def v_contadores_op3(v_paq):
    # tipo_p(1, 20)
    # tipo_p = 1        2       3           4
    # tipo_p =  0       1        2           3           4                                           19

    # v_cont = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    v_cont = [0] * 20
    for i in v_paq:
        # v_paq = [P, P, P, P]
        # i = P
        v_cont[i.tipo_p-1] += 1

    for i in range(len(v_cont)):
        # Si te pidieran solo los contadores mayores a 0
        # x es un numero que piden por teclado
        if v_cont[i] > 0:
            print("Tipo P:", i+1, "Existen cantidad de paquetes:", v_cont[i])


# ============================================
# Opcion 4
def busqueda_secuencial(v_paq, x, t):
    for i in range(len(v_paq)):
        if v_paq[i].id == x and v_paq[i].importe >= t:
            return i
    return -1


# =================================
# Opcion 5
def calcular_mayor(v_paq):
    may = 0
    for i in v_paq:
        if i.importe > may:
            may = i.importe

    for i in v_paq:
        if i.importe == may:
            print(i)
            break
