import pickle
import random
import os

from clases import *


def mostrar_menu():
    print('PROYECTOS')
    print('1. Cargar vector')
    print('2. Mostrar vector')
    print('3. Buscar proyecto')
    print('4. Generar archivo')
    print('5. Mostrar archivo')
    print('0. Salir')
    opcion = int(input('Ingrese opción: '))
    return opcion


def validar_mayor_que(x, mensaje):
    num = int(input(mensaje))
    while num <= x:
        num = int(input('Error!' + mensaje))
    return num


def add_in_order(v, x):
    n = len(v)
    pos = n
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if v[c].numero == x.numero:
            pos = c
            break
        if x.numero < v[c].numero:
            der = c - 1
        else:
            izq = c + 1
    # Agregar nuevo objeto
    if izq > der:
        pos = izq
    v[pos:pos] = [x]


def cargar_vector(v, n):
    for i in range(n):
        numero = random.randint(100, 999)
        nombre = 'Proyecto' + str(i)
        cliente = 'Cliente' + str(i)
        lenguaje = random.randint(1, 5)
        horas = random.randint(10, 50)
        x = Proyecto(numero, nombre, cliente, lenguaje, horas)
        add_in_order(v, x)


def mostrar_vector(v):
    for i in range(len(v)):
        print(v[i])


def buscar_por_numero(v, num):
    n = len(v)
    pos = -1
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if v[c].numero == num:
            pos = c
            break
        if num < v[c].numero:
            der = c - 1
        else:
            izq = c + 1
    return pos


def crear_archivo(v, fd):
    n = len(v)
    ach = 0
    for proyecto in v:
        ach += proyecto.horas
    promedio = ach / n

    m = open(fd, "wb")
    for proyecto in v:
        if proyecto.horas > promedio:
            pickle.dump(proyecto, m)
    m.close()
    print("Archivo creado...")


def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("Error: el archivo", fd, "no existe...")
        return

    t = os.path.getsize(fd)
    m = open(fd, "rb")
    print("Listado del proyectos contenidos en el archivo", fd)
    c = 0
    while m.tell() < t:
        p = pickle.load(m)
        print(p)
        c += 1
    m.close()
    print("Cantidad de proyectos mostrados:", c)


def principal():
    fd = "proyectos.dat"
    v = []
    opcion = -1
    while opcion != 0:
        opcion = mostrar_menu()
        if opcion == 1:
            n = validar_mayor_que(0, 'Ingrese n: ')
            cargar_vector(v, n)

        elif opcion == 2:
            if len(v) == 0:
                print('Debe cargar el vector')
            else:
                mostrar_vector(v)

        elif opcion == 3:
            if len(v) == 0:
                print('Debe cargar el vector')
            else:
                num = int(input('Ingrese numero de proyecto: '))
                pos = buscar_por_numero(v, num)
                if pos == -1:
                    print('Proyecto inexistente!')
                else:
                    print('Encontrado:', v[pos])
                    if v[pos].lenguaje == 4:
                        v[pos].horas += v[pos].horas * 8 / 100
                        print('Modificado:', v[pos])

        elif opcion == 4:
            if len(v) == 0:
                print('Debe cargar el vector')
            else:
                crear_archivo(v, fd)

        elif opcion == 5:
            mostrar_archivo(fd)


if __name__ == '__main__':
    principal()
