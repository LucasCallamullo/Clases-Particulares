import os.path
import pickle
import random
from ctypes.wintypes import tagMSG

from proyecto import *

# =========================================================================
#                                Opcion 1
# =========================================================================
def validar_n():
    n = int(input("Ingresar valor a cargar: "))
    while n < 0:
        n = int(input("Ingresar valor a cargar:"))
    return n

def cargar_arreglo(v_lote, n):
    for i in range(n):
        # nom_ape "ABCDEF", num_man (1, 35), num_lote (1, 20), ori_terreno (1, 4), sup_terreno, monto (1, 10)
        nom_ape = random.choice("ABCDEF")
        num_man = random.randint(1, 35)
        num_lote = random.randint(1, 20)
        ori_terreno = random.randint(1,4)
        sup_terreno = random.randint(1, 15)
        monto = round(random.uniform(0.1, 10), 2) # FLOat

        almacen = Lote(nom_ape, num_man, num_lote,ori_terreno,sup_terreno, monto)
        add_in_order(v_lote, almacen)
    print("Se cargaron: ", n, "lotes")

def add_in_order(v_lote, almacen):
    izq, der = 0, len(v_lote) - 1
    while izq <= der:
        c = (izq + der) // 2
        if v_lote[c].nom_ape == almacen.nom_ape:
            pos = c
            break
        elif v_lote[c].nom_ape > almacen.nom_ape:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq

    v_lote[pos:pos] = [almacen]

# =========================================================================
#                                Opcion 2
# =========================================================================
def mostrar_datos(v_lote):
    for i in v_lote:
        print(i)

# =========================================================================
#                                Opcion 4
# =========================================================================
def cargar_archivo_binario(v_lote, fd, l1, l2):
    m = open(fd, "wb")
    for i in v_lote:
        if l1 < i.num_lote < l2:
            pickle.dump(i, m)
            print(i)

    print("Se sobre escribio el archivo binario.")
    m.close()
# =========================================================================
#                                Opcion 5
# =========================================================================
def mostrar_archivo_binario(fd):
    if not os.path.exists(fd):
        print("El archivo no existe")
        return

    m = open(fd, "rb")      # ---> aca se abre coin "rb"
    tam = os.path.getsize(fd)
    acum = 0
    cont = 0
    while m.tell() < tam:
        almacen = pickle.load(m)

        print(almacen)
        acum += almacen.monto
        cont += 1

    prom = 0
    if cont > 0:
        prom = acum // cont
    print("El promdedio de venta: ", prom)

def menu():
    print(" 1 - Cargar arreglo.")
    print(" 2 - Mostrar arreglo.")
    print(" 3 - .")
    print(" 4 - Cargar archivo binario.")
    print(" 5 - Mostrar archivo binario.")
    print(" 0 - Salir.")
    op = int(input("Ingresar opcion: "))
    return op



def principal():
    v_lote = []
    op = -1

    fd = "terreno.dat"

    while op != 0:

        op = menu()

        if op == 1:
            n = validar_n()
            v_lote = []
            cargar_arreglo(v_lote, n)

        elif op == 2:
            if len(v_lote) == 0:
                print("El arreglo no esta cargado.")
            else:
                mostrar_datos(v_lote)

        elif op == 3:
            pass

        elif op == 4:
            if len(v_lote) == 0:
                print("El arreglo no esta cargado.")
            else:
                l1 = int(input("Ingrese valor a trabajar."))
                l2 = int(input("Ingrese valor a trabajar."))
                cargar_archivo_binario(v_lote, fd, l1, l2)

        elif op == 5:
            mostrar_archivo_binario(fd)


if __name__ == '__main__':
    principal()