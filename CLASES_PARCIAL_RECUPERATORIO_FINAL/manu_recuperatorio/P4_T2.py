import os
import pickle
import random

from comando import *


# ========================================================================
#                                 Opcion 1
# ========================================================================
def validar_n():
    n = int(input("Ingresar cantidad de ventas a trabajar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de ventas a trabajar: "))
    return n

def cargar_arreglo(v_venta, n):
    tupla_nombre = ("Proyecto 1.", "Proyecto 2.", "Proyecto 3.")

    # codigo INT, nombre STR, tipo tupla(1, 5), origen tupla(0, 2), monto FLOAT
    for i in range(n):
        codigo = random.randint(1, 10)

        nombre = " Este es el" + random.choice(tupla_nombre)
        tipo = random.randint(1, 5)
        origen = random.randint(0, 2)
        monto = round(random.uniform(0.1, 10), 2)

        almacen = Venta(codigo, nombre, tipo, origen, monto)
        add_in_order(v_venta, almacen)

def add_in_order(v_venta, almacen):

    izq, der = 0, len(v_venta) - 1

    while izq <= der:

        c = (izq + der) // 2
        if v_venta[c].codigo == almacen.codigo:
            pos = c
            break

        elif v_venta[c].codigo > almacen.codigo:
            der = c - 1

        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v_venta[pos:pos] = [almacen]

# ========================================================================
#                                 Opcion 2
# ========================================================================
def mostrar_arreglo(v_venta):
    for i in v_venta:
        print(i)

# ========================================================================
#                                 Opcion 3
# ========================================================================
def  busqueda_binaria(v_venta, cod):
    izq, der = 0, len(v_venta) - 1

    while izq <= der:
        c = (izq + der) // 2

        if v_venta[c].codigo == cod:
            print("Datos sin cambiar:", v_venta[c])

            ori = int(input("Ingresar origen a buscar: "))
            v_venta[c].origen = ori

            print("Datos cambiados: ", v_venta[c])
            return

        elif v_venta[c].codigo > cod:
            der = c - 1
        else:
            izq = c + 1


    print("No existe.")

# ========================================================================
#                                 Opcion 4
# ========================================================================
def generar_archivo_binario(v_venta, fd):

    m = open(fd, "wb")

    for i in v_venta:

        if i.origen != 2: # o tengo q hacer if i.origen != tupla_origen[Mercosur]
            pickle.dump(i, m)

    print("Se sobre escribio el archivo binario.")
    m.close()

# ========================================================================
#                                 Opcion 5
# ========================================================================
def mostrar_archivo_binario(fd):
    if not os.path.exists(fd):
        print("El archivo no existe.")
        return
    #Mostrar el archivo generado en el punto anterior. Aquí debe mostrar también la descripción del tipo de
    #producto, y no solo el número de tipo.

    cont_origen_import = 0
    cant_total = 0

    m = open(fd, "rb")
    tam = os.path.getsize(fd)

    # Al final del listado indicar el porcentaje que representan las Ventas
    # de productos de origen Importado sobre el total de registros mostrados.
    # porc = (origen * 100)// registros mostrados
    while m.tell() < tam:
        proy = pickle.load(m)
        print(proy)
        # aqui tengo que sumar el cont
        cant_total += 1
        if proy.origen == 0:
            cont_origen_import += 1
    # aca hago lo del porcentaje
    porc = (cont_origen_import * 100) // cant_total
    print("El porcentaje de ventas sobre total registros:", porc)

    m.close()

def menu():
    print(" 1 - Cargar arreglo.")
    print(" 2 - Mostrar arreglo.")
    print(" 3 - .")
    print(" 4 - Cargar archivo binario.")
    print(" 5 - Mostrar archivo binario.")
    print(" 0 - Salir.")
    op = int(input("Ingrese opcion: "))
    return op


def principal():

    v_venta = []
    op = -1

    fd = "proyecto.dat"

    while op != 0:

        op = menu()

        if op == 1:
            n = validar_n()
            v_venta = []
            cargar_arreglo(v_venta, n)

        elif op == 2:
            if len(v_venta) == 0:
                print("El arreglo no esta cargado.")
            else:
                mostrar_arreglo(v_venta)

        elif op == 3:
            if len(v_venta) == 0:
                print("El arreglo no esta cargado.")
            else:
                """
                A partir del arreglo, buscar si existe un venta con código cod que se ingresa por teclado, 
                si lo encuentra mostrar el registro, cambiar el número de origen de dicha venta en por el 
                valor ori que se ingresa por teclado y mostrar el registro actualizado. 
                Sino existe indicar con un mensaje
                """
                cod = int(input("Ingresar codigo a buscar: "))

                busqueda_binaria(v_venta, cod)
        elif op == 4:
            if len(v_venta) == 0:
                print("El arreglo no esta cargado.")
            else:
                generar_archivo_binario(v_venta, fd)

        elif op == 5:
            if len(v_venta) == 0:
                print("El arreglo no esta cargado.")
            else:
                mostrar_archivo_binario(fd)

if __name__ == '__main__':
    principal()