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
        co = random.randint(1, 10000)
        di = random.randint(1, 40)
        ti = random.randint(1, 20)
        gr = random.randint(1, 200)
        ig = round(random.randint(1, 2))
        v[i] = clase.Tubo(co, di, ti, gr, ig)
    print("Listo. El arreglo fue generado")
    print()
    return v


def mostrar(v):
    n = len(v)

    for i in range(n-1):
        for j in range(i+1, n):
            if v[i].diametro < v[j].diametro:
                v[i], v[j] = v[j], v[i]

    ac = 0
    print("Listado de tubos IGNIFUGOS de PVC disponibles:")
    for i in range(n):
        if v[i].ignifugo == 1:
            print(v[i])
            ac += v[i].gramos
    prom = ac // n
    print("Promedio de gramos de PVC usados entre todos los tubos:", prom)
    print()


def contar(v):
    n = len(v)
    c = 20 * [0]

    for i in range(n):
        ind = v[i].tipo - 1
        c[ind] += 1

    a = int(input("Valor (se mostrarán los contadores mayores a este valor): "))
    print("Cantidades de tubos con valor mayor a", a, ":")
    for k in range(20):
        if c[k] > a:
            print("Codigo:", k+1, "Cantidad disponible:", c[k])
    print()


def buscar(v):
    n = len(v)
    id = int(input("Codigo de producto del tubo a buscar: "))
    for i in range(n):
        if id == v[i].codigo:
            print("Encontrado:")
            print("Tipo de aplicacion:", v[i].tipo, " - Diametro:", v[i].diametro)
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
