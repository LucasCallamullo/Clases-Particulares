import random
import clase


# carga y retorna un número, validando que sea mayor al valor inf que entra como parámetro.
def validar(inf):
    n = int(input('Valor (mayor a ' + str(inf) + ' por favor): '))
    while n <= inf:
        n = int(input('Error... Se pidio mayor a ' + str(inf) + '... Cargue de nuevo: '))
    return n


def cargar():
    n = validar(0)
    v = n * [None]
    nombres = ("Mesa", "Silla", "Placard", "Florero", "Repisa")
    for i in range(n):
        cod = random.randint(1, 2000)
        des = random.choice(nombres) + " " + str(i)
        sec = random.randint(1, 55)
        vol = random.randint(1, 30)
        pre = round(random.uniform(0, 30000), 2)
        v[i] = clase.Articulo(cod, des, sec, vol, pre)
    print("Listo. El arreglo fue generado")
    print()
    return v


def mostrar(v):
    n = len(v)

    for i in range(n-1):
        for j in range(i+1, n):
            if v[i].codigo > v[j].codigo:
                v[i], v[j] = v[j], v[i]

    c = 0
    pm = float(input("Precio a filtrar (se mostrarán los articulos con precio mayor a este): "))
    print("Listado de las articulos solicitados:" )
    for i in range(n):
        if v[i].precio > pm:
            print(v[i])
    print()


def contar(v):
    n = len(v)
    ct = 55 * [0]

    for i in range(n):
        ind = v[i].seccion - 1
        ct[ind] += 1

    x = int(input("Cantidad a filtrar (se mostrarán los contadores con valor mayor a este): "))
    print("Cantidad de articulos por tipo:")
    for k in range(55):
        if ct[k] > x:
            print("Seccion:", k+1, "Cantidad:", ct[k])
    print()


def buscar(v):
    n = len(v)
    desc = input("Descripcion del articulo a buscar: ")
    p = float(input("Precio maximo del articulo a buscar: "))
    for i in range(n):
        if desc == v[i].descripcion and v[i].precio < p:
            print("Encontrado - Datos actuales:")
            print(v[i])
            print()
            return
    print("No estaba...")
    print()


def principal():
    v = []
    op = -1
    while op != 5:
        print("1. Cargar arreglo")
        print("2. Mostrar ordenado")
        print("3. Contar por seccion")
        print("4. Buscar")
        print("5. Salir")
        op = int(input("Ingrese número de opción: "))

        if op == 1:
            v = cargar()

        elif op == 2:
            if v:
                mostrar(v)
            else:
                print("el vector no fue cargado todavía...")
                print()

        elif op == 3:
            if v:
                contar(v)
            else:
                print("el vector no fue cargado todavía...")
                print()

        elif op == 4:
            if v:
                buscar(v)
            else:
                print("el vector no fue cargado todavía...")
                print()

        elif op == 5:
            print("Programa terminado... Hasta la vista baby...")
            print()


if __name__ == "__main__":
    principal()
