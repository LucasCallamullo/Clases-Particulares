import os.path
import random
import pickle
from cañete_clase import *

#===================================   PUNTO 1 =========================
def validar_n():
    n = int(input("Ingresar la cantidad de arreglos a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de arreglos a cargar mayor a 0: "))
    return n

def cargar_arreglo(v_alquiler, n):
    ## nombrejuego (str), nombrecliente(str), tipo(int(0,4), mes (int(1,12), monto(float)
    for i in range(n):
        nombre = random.choice("ABCDEFG")
        cliente = random.choice("ABCDEFGHI")
        tipo = random.randint(0, 4)
        mes = random.randint(1, 12)
        monto = random.uniform(0.1, 10)
        nuevo_alquiler = Alquiler(cliente,nombre,tipo,mes, monto)
        add_in_order(v_alquiler, nuevo_alquiler)

def add_in_order(v_alquiler, nuevo_alquiler):
    izq, der = 0, len(v_alquiler) - 1

    while izq <= der:
        c = (izq + der) // 2

        if v_alquiler[c].nombre == nuevo_alquiler.nombre:
            pos = c
            break

        elif v_alquiler[c].nombre > nuevo_alquiler.nombre:
            der = c - 1

        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v_alquiler[pos:pos] = [nuevo_alquiler]


#=============================== PUNTO 2 =====================
def mostrar_arreglo(v_alquiler):
    for i in v_alquiler:
        acum = 0 * 60
        if i.mes and i.tipo:
            acum += i.monto
            if acum > 0:
                print(i)


#======================= PUNTO 4 =========================
def generar_archivo_binario(v_alquiler, fd, x):

    m = open(fd, "wb")

    for i in v_alquiler:
        if i.mes < x:
            pickle.dump(i,m)

    m.close()

#=========================  PUNTO 5 =========================

def mostrar_archivo_binario(fd):
    if not os.path.exists(fd):
        print("El archivo no existe", fd)
        return

    m = open(fd, "rb")
    tam = os.path.getsize(fd)

    acum = 0
    cont = 0

    while m.tell() < tam:
        alquilercito = pickle.load(m)
        print(alquilercito)
        cont += 1
        acum += alquilercito

    if cont > 0:
        prom = acum // cont
        print("El promedio de los archivos mostrados es: ", prom)

    m.close()

#===================================================================

def menu():
    print(" 1- Cargar arreglo ")
    print(" 2- Mostrar arreglo")
    print(" 3- Buaqueda binaria ")
    print(" 4- Generar archivo bbinario ")
    print(" 5- Mostrar archivo binario ")
    print(" 0- Salir ")
    op = int(input("Ingresar la opcionn que desee: "))
    return op

def principal():

    v_alquiler = []
    op = - 1
    fd = "alqui.dat"

    while op != 0:
        op = menu()

        if op == 1:

            n = validar_n()
            v_alquiler = []
            cargar_arreglo(v_alquiler, n)

        elif op == 2:

            if len(v_alquiler) > 0:

                mostrar_arreglo(v_alquiler)

            else:
                print("El arreglo no esta cargado en el punto 1")

        elif op == 3:
            pass

        elif op == 4:

            if len(v_alquiler) > 0:
                x = int(input("Ingresar valor menor: "))
                generar_archivo_binario(v_alquiler, fd, x)

            else:
                print("El arreglo en el punto 1 no esta cargado")

        elif op == 5:

            if len(v_alquiler) > 0:
                mostrar_archivo_binario(fd)
            else:
                print("El arreglo no esta cargado en el punto 1.")

if __name__ == '__main__':
    principal()


