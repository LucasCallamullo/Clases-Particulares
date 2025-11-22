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
    nombres = ("Hamburguesa", "Pollo", "Papas Fritas", "Lomito", "Helado")
    for i in range(n):
        id = random.randint(1, 25000)
        de = random.choice(nombres) + " " + str(i)
        ca = random.randint(0, 5000)
        ti = random.randint(1, 30)
        im = round(random.uniform(0, 20000), 2)
        v[i] = clase.Producto(id, de, ca, ti, im)
    print("Listo. El arreglo fue generado")
    print()
    return v


def mostrar(v):
    n = len(v)

    for i in range(n-1):
        for j in range(i+1, n):
            if v[i].calorias > v[j].calorias:
                v[i], v[j] = v[j], v[i]

    print("Listado de productos...")
    ac = 0
    for i in range(n):
        ac += v[i].calorias
        print(v[i])
    prom = ac // n
    print("Promedio de calorias entre todos los productos:", prom)
    print()


def contar(v):
    n = len(v)
    c = 30 * [0]

    for i in range(n):
        ind = v[i].tipo - 1
        c[ind] += 1

    print("Cantidad de productos por tipo (solo entre 0 y 2...")
    for k in range(30):
        if 0 <= c[k] < 3:
            print("Tipo:", k+1, "Cantidad:", c[k])
    print()


def buscar(v):
    n = len(v)
    cod = int(input("Codigo del producto a buscar: "))
    for i in range(n):
        if cod == v[i].codigo:
            print("Encontrado:")
            print("Descripcion del producto:", v[i].descripcion, " - Precio:", v[i].precio)
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
        print("3. Conteo por tipo")
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
