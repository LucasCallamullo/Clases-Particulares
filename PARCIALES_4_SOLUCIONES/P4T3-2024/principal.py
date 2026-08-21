from zapato import *
import pickle
import os


def menu():
    print("\n========= Menú de opciones =========")
    print("1) Cargar zapatos")
    print("2) Mostrar con descripción")
    print("3) Stock por talle y ancho")
    print("4) Generar archivo")
    print("5) Mostrar archivo con promedio")
    return int(input("Ingrese una opción: "))


def add_in_order(v, reg):
    izq, der = 0, len(v) - 1
    pos = 0
    while izq <= der:
        med = (izq + der) // 2
        if v[med].codigo == reg.codigo:
            pos = med
            break

        if reg.codigo < v[med].codigo:
            der = med - 1
        else:
            izq = med + 1

    if izq > der:
        pos = izq
    v[pos:pos] = [reg]


def cargar_zapatos(n):
    v = []
    for _ in range(n):
        zapato = generar_zapato()
        add_in_order(v, zapato)
    return v


def mostrar(v):
    for zapato in v:
        print(zapato)


def promedio(cantidad, total):
    prom = 0
    if cantidad > 0:
        prom = total / cantidad

    return prom


def generar_matriz(v):
    m = [[0] * 11 for i in range(3)]
    n = len(v)
    for i in range(n):
        f = v[i].ancho
        c = v[i].talle - 35
        m[f][c] += v[i].stock

    return m


def generar_archivo(nombre, v, t):
    n = len(v)
    m = open(nombre, "wb")
    for i in range(n):
        if v[i].stock > 0 and v[i].talle == t:
            pickle.dump(v[i], m)
    m.close()


def mostrar_archivo(nombre):
    if not os.path.exists(nombre):
        print("No existe el archivo...")
        return

    size = os.path.getsize(nombre)
    m = open(nombre, "rb")
    acu = cont = 0
    while m.tell() < size:
        zapato = pickle.load(m)
        acu += zapato.stock
        cont += 1
        print(zapato)

    m.close()
    prom = promedio(cont, acu)
    print("El promedio de stock es:", round(prom, 2), "unidades")


def mostrar_matriz(m, u):
    anchos = ("Delgado", "Normal", "Extra ancho")
    for f in range(len(m)):
        for c in range(len(m[f])):
            if m[f][c] > u:
                print("Talle:", c + 35, " Ancho:", anchos[f], " Stock:", m[f][c])


def principal():
    v = []
    nombre_archivo = "zapatos.dat"
    op = -1
    while op != 0:
        op = menu()
        if op == 1:
            n = int(input("Ingrese la cantidad de zapatos a cargar: "))
            v = cargar_zapatos(n)
        elif len(v) > 0:
            if op == 2:
                mostrar(v)
            elif op == 3:
                m = generar_matriz(v)
                u = int(input("Ingrese el valor mínimo a mostrar: "))
                mostrar_matriz(m, u)
            elif op == 4:
                t = int(input("Ingrese el talle: "))
                generar_archivo(nombre_archivo, v, t)
            elif op == 5:
                mostrar_archivo(nombre_archivo)
        else:
            print("\nPrimero debe cargar los zapatos...\n")


if __name__ == "__main__":
    principal()
