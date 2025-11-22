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
        id = random.randint(1, 50000)
        dn = random.randint(1, 99999999)
        mr = random.randint(1, 20)
        ta = round(random.uniform(0, 3000), 2)
        v[i] = clase.Taxi(id, dn, mr, ta)
    print("Listo. El arreglo fue generado")
    print()
    return v


def mostrar(v):
    n = len(v)

    for i in range(n-1):
        for j in range(i+1, n):
            if v[i].codigo > v[j].codigo:
                v[i], v[j] = v[j], v[i]

    cs = 0
    i1 = int(input("Primer importe a filtrar: "))
    i2 = int(input("Segundo importe a filtrar: "))
    print("Listado de taxis con tarifa por kilometro entre", i1, "y", i2, ":" )
    for i in range(n):
        if i1 <= v[i].tarifa <= i2:
            cs += 1
            print(v[i])
    print("Cantidad de taxis mostrados:", cs)
    print()


def contar(v):
    n = len(v)
    c = 20 * [0]

    for i in range(n):
        ind = v[i].marca - 1
        c[ind] += 1

    print("Cantidad de taxis por marca:")
    for k in range(10):
        if c[k] > 0:
            print("Marca:", k+1, "Cantidad:", c[k])
    print()


def buscar(v):
    n = len(v)
    dni = int(input("DNI del chofer a buscar: "))
    for i in range(n):
        if dni == v[i].dni:
            print("Encontrado - Datos actuales:")
            print(v[i])
            d = v[i].tarifa * 0.15
            v[i].tarifa -= d
            print("Datos con el importe actualizado:")
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
        print("3. Contar por marca")
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
