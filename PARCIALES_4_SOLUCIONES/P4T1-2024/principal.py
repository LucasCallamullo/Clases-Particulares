from clase import *
import random
import pickle
import os.path


def add_in_order(e, v):
    n = len(v)
    pos = n
    izq = 0
    der = n - 1
    while izq <= der:
        c = (izq+der) // 2
        if v[c].nombre == e.nombre:
            pos = c
            break
        if v[c].nombre > e.nombre:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    v[pos:pos] = [e]


def validar():
    n = 0
    while n <= 0:
       n = int(input("Ingrese la cantidad de equipos: "))
    return n


def cargar_vector():
    v = []
    n = validar()
    for i in range(n):
        num = random.randint(1, 1000)
        nom = "Equipo " + str(num)
        edad = random.randint(12, 17)
        niv = random.randint(0, 2)
        monto = round(random.uniform(1000, 50000), 2)
        e = Equipo(num, nom, edad, niv, monto)
        add_in_order(e, v)
    return v


def mostrar_vector(v):
    for i in range(len(v)):
        print(v[i])


def validar_rango():
    e = 11
    while e < 12 or e > 17:
        e = int(input("Ingrese la edad a acumular: "))
    return e


def acumular(v):
    mat = [[0] * 3 for i in range(6)]
    for i in range(len(v)):
        fila = v[i].edad - 12
        col = v[i].nivel
        mat[fila][col] += v[i].monto
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] > 0:
                print("Edad:", i+12, " - Nivel:", j, ":$", mat[i][j])
    e = validar_rango()
    fila = e - 12
    acu = 0
    for j in range(3):
        acu += mat[fila][j]
    print("Total acumulado para la edad: $", acu)


def generar_archivo(v, i1, i2):
    arch = "inscripciones.dat"
    m = open(arch, "wb")
    for i in range(len(v)):
        if i1 <= v[i].numero <= i2:
            pickle.dump(v[i], m)
    m.close()


def mostrar_archivo():
    arch = "inscripciones.dat"
    if not os.path.exists(arch):
        print("No existe el archivo")
        return
    m = open(arch, "rb")
    tam = os.path.getsize(arch)
    acu = cont = 0
    while m.tell() < tam:
        e = pickle.load(m)
        print(e)
        acu += e.edad
        cont += 1
    if cont > 0:
        prom = acu / cont
    else:
        prom = 0
    print("Edad promedio:", prom)


def principal():
    op = 1
    v = []
    while op != 6:
        print("Menú de opciones")
        print("1-Cargar")
        print("2-Mostrar")
        print("3-Acumular")
        print("4-Generar archivo")
        print("5-Mostrar archivo")
        print("6-Salir")
        op = int(input("Ingrese su opción: "))
        if op == 1:
            v = cargar_vector()
        elif op == 5:
            mostrar_archivo()
        elif op == 6:
            print("Adiós!")
        elif len(v) == 0:
            print("Primero debe cargar el vector!")
        elif op == 2:
            mostrar_vector(v)
        elif op == 3:
            acumular(v)
        elif op == 4:
            i1 = int(input("Ingrese i1: "))
            i2 = int(input("Ingrese i2: "))
            generar_archivo(v, i1, i2)


if __name__ == "__main__":
    principal()