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
    for i in range(n):
        cod = random.randint(1, 2000)
        tip = random.randint(1, 10)
        met = random.randint(1, 20)
        pre = round(random.uniform(0, 20000), 2)
        v[i] = clase.Pintura(cod, tip, met, pre)
    print("Listo. El arreglo fue generado")
    print()
    return v


def mostrar(v):
    n = len(v)

    for i in range(n-1):
        for j in range(i+1, n):
            if v[i].precio > v[j].precio:
                v[i], v[j] = v[j], v[i]

    c = 0
    pm = float(input("Precio a filtrar (se mostrarán las pinturas con precio menor a este): "))
    rm = float(input("Metros a filtrar (se mostrarán las pinturas con rinde mayor a este): "))
    print("Listado de las pinturas solicitadas:" )
    for i in range(n):
        if v[i].precio < pm and v[i].metros > rm:
            c += 1
            print(v[i])
    print("Cantidad de pinturas mostradas:", c)
    print()


def contar(v):
    n = len(v)
    ct = 10 * [0]

    for i in range(n):
        ind = v[i].tipo - 1
        ct[ind] += 1

    c = int(input("Cantidad a filtrar (se mostrarán los contadores con valor mayor a este): "))
    print("Cantidad de pinturas por tipo:")
    for k in range(10):
        if ct[k] > c:
            print("Tipo de pintura:", k+1, "Cantidad:", ct[k])
    print()


def buscar(v):
    n = len(v)
    c = int(input("Codigo de la pintura a buscar: "))
    for i in range(n):
        if c == v[i].codigo:
            print("Encontrado - Datos actuales:")
            print(v[i])
            np = float(input("Nuevo precio a asignar: "))
            v[i].precio = round(np, 2)
            print("Datos con el precio actualizado:")
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
        print("3. Contar por tipo")
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
