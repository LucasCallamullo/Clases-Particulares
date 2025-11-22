import os.path
import pickle
import random
from equipo import Equipo


def generar_aleatorio():
    nombres = (
        "Alpha Strike", "Crimson Vipers", "Shadow Core", "Echo Squad", "Team Hydra", "Nova Aim",
        "Valor Kings", "Phoenix Rising", "Oblivion", "Recoil Nation", "Blue Fang", "Silent Storm",
        "Tactical Edge", "Ghost Ops", "Pulse Unit", "Astra Elite", "Prime Strike", "Midnight Crew",
        "Iron Wolves", "Nemesis", "Chaos Unit", "Rogue Line", "Delta Force", "Spectre", "Zero Hour"
    )

    nombre = random.choice(nombres)
    jugadores = random.randint(5, 8)
    rango = random.randint(1, 8)
    puntaje = random.randint(100, 1000)
    region = random.randint(1, 4)

    return Equipo(nombre, jugadores, rango, puntaje, region)


# ===========================================================
# Opcion 1
# ===========================================================
def cargar_arreglo(vector, n):
    for i in range(n):
        # equui va a valer lo que retorne la funcion generar_aleatorio()
        e = generar_aleatorio()     # vale como un objeto
        add_in_order(vector, e)
        add_in_order(vector, 1)


def add_in_order(v, equipo):
    der = len(v) - 1
    izq = 0
    while izq <= der:
        c = (izq + der) // 2
        if v[c].nombre == equipo.nombre:
            pos = c
            break
        elif v[c].nombre > equipo.nombre:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v[pos:pos] = [equipo]


# =================================================================
#           Punto 2
# ================================================================
def mostrar_arreglo(v):

    r1 = int(input("Ingresar rango promedio a contar (1-8): "))
    cont = 0

    # v_equipo = [ E1, E2, E3,
    for i in v:
        # i = E1, E2, E3
        if i.rango == r1:
            cont += 1

        print(i)

    print("Ingreso la cantidad de: ", cont)


# =================================================================
#           Punto 5
# ================================================================
def mostrar_archivo_binario(fd):
    """
        Calcular el porcentaje de los rangos diamante
        sobre el total de equipos

        porcentaje = cantidad_a_calcular * 100 // cantidad_total

        # cantidad_a_calcular --> rangos diamante
        # cantidad_total --> total de equipos dentro del arreglo
    """
    m = open(fd, "rb")
    tamanio = os.path.getsize(fd)

    cont_rangos_diamante = 0
    cont_total = 0

    while m.tell() < tamanio:

        eq = pickle.load(m)     # esto devuelve el objeto guardado en el archivo
        print(eq)

        if eq.rango == 6:
            cont_rangos_diamante += 1

        cont_total += 1

    # porcentaje
    porc = 0
    if cont_total > 0:
        porc = cont_rangos_diamante * 100 // cont_total

    print("el porcentaje:", porc)
    m.close()


# =================================================================
#           Punto 6
# ================================================================
def busqueda_secuencial(vector):
    x = int(input())
    for i in range(len(vector)):
        if vector[i].algo == x:
            break