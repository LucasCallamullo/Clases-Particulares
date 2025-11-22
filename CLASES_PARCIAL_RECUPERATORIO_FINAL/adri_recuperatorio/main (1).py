import os.path
import pickle
import random
import clase


def add_in_order(v, alquiler):
    n = len(v)
    pos = n
    izq, der = 0, n-1
    while izq <= der:
        c = (izq + der) // 2
        if alquiler.nombre == v[c].nombre:
            pos = c
            break
        else:
            if alquiler.nombre < v[c].nombre:
                der = c - 1
            else:
                izq = c + 1
    if izq > der:
        pos = izq
    v[pos:pos] = [alquiler]


def validar(inf):
    n = int(input("Ingresar un valor mayor a " + str(inf) + ", por favor: "))
    while n <= inf:
        n = int(input("Error! El valor debe ser mayor a " + str(inf) + ". Intente de nuevo: "))
    return n


def cargar():

    v = []
    n = validar(0)

    nombre1 = ("CoD", "Fortnite", "Among Us", "LoL", "Minecraft")
    persona1 = "ABCDEF"
    for i in range(n):
        nombre = random.choice(nombre1)
        persona = random.choice(persona1)
        tipo = random.randint(0, 4)
        mes = random.randint(1, 12)
        monto = round(random.uniform(0.1, 1000))
        alquiler = clase.Alquiler(nombre, persona, tipo, mes, monto)
        add_in_order(v, alquiler)
    print("Arreglo cargado exitosamente")
    return v


def acumular(v):
    n = len(v)
    ac = [[0] * 4 for i in range(12)]
    for i in range(n):
        pass


def mostrar(v):
    n = len(v)
    print("Lista de Juegos...")
    for i in range(n):
        print(v[i])
    print()


def generar_archivo(v, fd, mes):
    n = len(v)
    m = open(fd,"wb")
    x = int(input("Mes de publicación: "))
    for i in range(12):
        if x > v[i].mes:
            pickle.dump(v[i].mes)

    m.close()
    print("Arreglo cargado.")


def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("No exixte el archivo ", fd, "...")
        return
    print("Listado de ...")
    c = ac = 0
    m = open(fd, "rb")
    t = os.path.getsize(fd)
    while m.tell() < t:
        r = pickle.load(m)
        c += 1
        ac += r.mes
        print(r)
    m.close()


def principal():
    v = []
    fd = ".dat"
    op = -1

    while op != 6:
        print("1-Cargar arreglo.")
        print("2-Mostrar arreglo por tipo de juego y mes de publicacion.")
        print("3-Buscar juego (nombre).")
        print("4-Generar archivo.")
        print("5-Mostrar archivo.")
        print("6-Salir")
        op = int(input("Ingrese una opcion: "))
        print()
        if op == 1:
            v = cargar()

        elif op == 2:
            if v:
                mostrar(v)
            else:
                print("El vector no se cargó.")
        elif op == 6:
            print("Esta saliendo del programa, nos vemos...")
            print()


if __name__ == "__main__":
    principal()
