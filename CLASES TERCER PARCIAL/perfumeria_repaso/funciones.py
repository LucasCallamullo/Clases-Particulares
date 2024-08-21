import random
from registro import *


# ============================================================
#                   Opcion 1
# ============================================================
def cargar_arreglo(v_venta, n):
    tipo_fac = ("A", "B", "C", "E")
    apellidos = ("Mart", "Fern", "Agui", "Boseti", "Garcia")

    for i in range(n):
        num_f = random.randint(0, 50)
        # importe = random.uniform(0.1, 199999.9)
        importe = round(random.uniform(0, 10), 2)
        tipo_f = random.choice(tipo_fac)
        apellido = random.choice(apellidos)
        tipo_perf = random.randint(1, 4)
        ventita = Venta(num_f, importe, tipo_f, apellido, tipo_perf)
        v_venta.append(ventita)


# ============================================================
#                   Opcion 2
# ============================================================
def sort(v_venta):
    n = len(v_venta)
    for i in range(n-1):
        for j in range(i+1, n):
            if v_venta[i].apellido < v_venta[j].apellido:
                v_venta[i], v_venta[j] = v_venta[j], v_venta[i]


# No es necesaria
def validar_t():
    t = input("Ingrese una factura: ")
    facturas = "ABCE"
    while not t.upper() in facturas:
        print("Las facturas deben ser (A, B, C, E")
        t = input("Ingrese una factura: ")
    return t.upper()


def mostrar_datos_op2(v_venta, x, t):
    for i in v_venta:
        if i.importe > x and i.tipo_f != t:
            print(i)


# ============================================================
#                   Opcion 3
# ============================================================
def funcion_op3(v_venta, z):
    # (1, 17)    #

    # 0 1 2 3 4 ...
    v_acum = [0] * 17
    for i in v_venta:
        # i = obj1
        v_acum[i.tipo_perf-1] += i.importe

    print("El total facturado del tipo de perfume", z, "es:", round(v_acum[z-1], 2))


# ============================================================
#                   Opcion 4
# ============================================================
def funcion_op4(v_venta):
    encontramos = False
    for i in range(len(v_venta)):
        if 2 <= v_venta[i].tipo_perf <= 3 and v_venta[i].tipo_f != "C":
            print("Num Fact:", v_venta[i].num_f, "Apellido:", v_venta[i].apellido, "Importe:", v_venta[i].importe)
            encontramos = True
    if not encontramos:
        print("No se encontraron archivos")


# ============================================================
#                   Opcion 5
# ============================================================
def funcion_op5(v_venta, n, p):
    for i in range(len(v_venta)):
        # 0 1 2 3 4
        if v_venta[i].num_f == n and v_venta[i].importe < p:
            return i
    return -1
