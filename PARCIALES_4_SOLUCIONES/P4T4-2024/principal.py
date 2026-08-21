import os
import pickle
import registro


def menu():
    cadena = "Menu de Opciones\n"
    cadena += f'{"-" * 70}\n'
    cadena += '1 ---- Cargar Seguros\n'
    cadena += '2 ---- Mostrar Seguros\n'
    cadena += '3 ---- Buscar Seguros por Nombr\n'
    cadena += '4 ---- Generar Archivo de Seguros\n'
    cadena += '5 ---- Mostrar Archivo de Seguros\n'
    cadena += '0 ---- Salir\n'
    cadena += 'Ingrese su opcion: '
    return int(input(cadena))


def validar_mayor_que(inf, mensaje='Ingrese un valor: '):
    num = inf
    while num <= inf:
        num = int(input(mensaje))
        if num <= inf:
            print(f'{num} debe ser mayor que {inf}')
    return num


def add_in_order(seguros, seguro):
    tam = len(seguros)
    izq, der = 0, tam - 1
    pos = -1

    while izq <= der:
        med = (izq + der) // 2
        if seguros[med].nombre == seguro.nombre:
            pos = med
            break

        if seguro.nombre < seguros[med].nombre:
            der = med - 1
        else:
            izq = med + 1

    if izq > der:
        pos = izq

    seguros[pos:pos] = [seguro]


def cargar_arreglo(seguros, n):
    for i in range(n):
        seguro = registro.crear_seguro()
        add_in_order(seguros, seguro)


def mostrar(seguros):
    print('Listado de Seguros:')
    print('=' * 80)
    for seguro in seguros:
        print(seguro)


def buscar(seguros, nom):
    tam = len(seguros)
    izq, der = 0, tam - 1

    while izq <= der:
        med = (izq + der) // 2
        if seguros[med].nombre == nom:
            if seguros[med].es_propietario:
                seguros[med].monto -= seguros[med].monto * 0.10
            else:
                seguros[med].monto -= seguros[med].monto * 0.15
            print(seguros[med])
            return

        if nom < seguros[med].nombre:
            der = med - 1
        else:
            izq = med + 1
    print(f'No existe un seguro para el nombre {nom}')


def generar_archivo(FD, seguros, t):
    m = open(FD, 'wb')
    for seguro in seguros:
        if seguro.tipo == t:
            pickle.dump(seguro, m)
    m.close()


def mostrar_archivo(FD):
    if not os.path.exists(FD):
        print(f'No existe el archivo {FD}')
        return

    m = open(FD, 'rb')
    size = os.path.getsize(FD)
    print('Listado de Seguros:')
    print('=' * 80)
    cont = acum = 0
    while m.tell() < size:
        seguro = pickle.load(m)
        cont += 1
        acum += seguro.monto
        print(seguro)

    m.close()

    prom = 0
    if cont > 0:
        prom = acum / cont

    print(f'El monto promedio de los seguros es: ${prom:>10.2f}')


def principal():
    opcion = -1
    seguros = []
    FD = "seguros.dat"

    while opcion != 0:
        opcion = menu()
        if opcion == 1:
            n = validar_mayor_que(0, 'Ingrese la cantidad de Seguros a cargar: ')
            cargar_arreglo(seguros, n)

        if len(seguros) > 0:
            if opcion == 2:
                mostrar(seguros)

            elif opcion == 3:
                nom = input('Ingrese el nombre del asegurado: ')
                buscar(seguros, nom)

            elif opcion == 4:
                t = int(input('Ingrese el tipo de vivienda: '))
                generar_archivo(FD, seguros, t)
            elif opcion == 5:
                mostrar_archivo(FD)
        else:
            print('Primero debe cargar el arreglo con los datos')
        print()


if __name__ == '__main__':
    principal()
