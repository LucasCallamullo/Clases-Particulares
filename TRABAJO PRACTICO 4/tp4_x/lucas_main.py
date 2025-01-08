from modulo_tp4 import *
import pickle
import os.path


def menu():
    print('*' * 50)
    print('MENU')
    print('-' * 10, '\n'
                    '1. Crear archivo binario \n'
                    '2. Cargar por teclado los datos de un ticket \n'
                    '3. Mostrar registros \n'
                    '4. Mostrar registros de una cierta patente \n'
                    '5. Buscar un cierto código \n'
                    '6. Mostrar cantidad de vehículos por cabina \n'
                    '7. Mostrar cantidad total de vehículos por tipo y por país de cabina \n'
                    '8. Calcular la distancia promedio \n'
                    '9. Salir')
    print('*' * 50)


def crear_achivo(archivo):
    peaje = open('peajes-tp4.csv', 'rt')
    arc = open(archivo, 'wb')
    pri = 0
    for linea in peaje:
        pri += 1
        if pri > 2:
            if linea[-1] == '\n':
                linea = linea[:-1]
            pickle.dump(crear(linea), arc)
    arc.flush()
    peaje.close()
    arc.close()


def validar(desde, hasta, msj):
    valor = int(input(msj))
    while valor < desde or valor > hasta:
        print('ERROR')
        valor = int(input(msj))
    return valor


def carga(archivo):
    codigo = int(input('ingrese el código del ticket '))
    while codigo <= 0:
        codigo = int(input('ERROR el código debe ser mayor a 0. Intente nuevamente '))
    patente = input('Ingrese la patente ')
    tipo = validar(0, 2, 'Ingrese el tipo (valor entre 0 y 2) ')
    forma_pago = validar(1, 2, 'Ingrese la forma de pago (valor entre 1 y 2) ')
    pais_cabina = validar(0, 4, 'Ingrese el país de la cabina (valor entre 0 y 4) ')
    distancia = int(input('Ingrese la distancia '))
    while distancia < 0:
        distancia = int(input('ERROR la distancia debe ser positiva. Ingrese la distancia nuevamente '))
    ticket = Ticket(codigo, patente, tipo, forma_pago, pais_cabina, distancia)
    arc = open(archivo, 'ab')
    pickle.dump(ticket, arc)
    arc.flush()
    arc.close


def pais_patente(pat):
    if len(pat) == 6:
        if pat[0:4].isalpha() and pat[4:6].isdigit():
            pais = 5

    elif pat[0:2].isalpha() and pat[2:5].isdigit() and pat[5:7].isalpha():
        pais = 0

    elif pat[0:2].isalpha() and pat[2:7].isdigit():
        pais = 1

    elif pat[0:3].isalpha() and pat[3].isdigit() and pat[4].isalpha() and pat[5:7].isdigit():
        pais = 2

    elif pat[0:4].isalpha() and pat[4:7].isdigit():
        pais = 3

    elif pat[0:3].isalpha() and pat[3:7].isdigit():
        pais = 4

    else:
        pais = 6

    return pais


def muestra(archivo):
    paises = ('Argentina', 'Bolivia', 'Brasil', 'Paraguay', 'Uruguay', 'Chile', 'Otro',)
    if os.path.exists(archivo):
        size = os.path.getsize(archivo)
        arc = open(archivo, 'rb')
        while arc.tell() < size:
            ticket = pickle.load(arc)
            pais = pais_patente(ticket.patente)
            print(ticket, ' - Pais: ', paises[pais])
    else:
        print('El archivo no existe')


def mostrar_patente(archivo):
    if os.path.exists(archivo):
        size = os.path.getsize(archivo)
        m = open(archivo, 'rb')
        pat = input('Ingrese una patente: ')
        ct = 0
        while m.tell() < size:
            ticket = pickle.load(m)
            if ticket.patente == pat:
                ct += 1
                print(ticket)
        print('Se mostraron', ct, 'registro/s')
        m.close()
    else:
        print('El archivo no existe. Cargue el archivo primero')


def busqueda(archivo):
    if os.path.exists(archivo):
        res = None
        size = os.path.getsize(archivo)
        m = open(archivo, 'rb')
        cod = int(input('Ingrese un código: '))
        while m.tell() < size:
            ticket = pickle.load(m)
            if ticket.codigo == cod:
                res = ticket
                break
        m.close()
    else:
        print('El archivo no existe. Cargue el archivo primero')

    return res


def matriz_conteo(archivo, mat):
    if os.path.exists(archivo):
        m = open(archivo, 'rb')
        size = os.path.getsize(archivo)
        while m.tell() < size:
            ticket = pickle.load(m)
            fila = ticket.tipo
            col = ticket.pais_cabina
            mat[fila][col] += 1
        mostrar_matriz(mat)
        m.close()
    else:
        print('El archivo no existe. Cargue el archivo primero')


def mostrar_matriz(mat):
    m = len(mat)
    n = len(mat[0])
    for i in range(m):
        for j in range(n):
            if mat[i][j] != 0:
                print('Tipo: ' + str(i) + ' -  País de cabina: ' + str(j) + ' - Cantidad: ', mat[i][j])


def cant_total(mat):
    m = len(mat)
    n = len(mat[0])
    total_fila = [0] * m
    total_columna = [0] * n
    for i in range(m):
        for j in range(n):
            total_fila[i] += mat[i][j]
    for j in range(n):
        for i in range(m):
            total_columna[j] += mat[i][j]

    mostrar_totales(total_fila, total_columna)


def mostrar_totales(total_fila, total_columna):
    for i in range(len(total_fila)):
        print('Total para el tipo', str(i) + ': ' + str(total_fila[i]))
    for j in range(len(total_columna)):
        print('Total para el país de cabina', str(j) + ': ' + str(total_columna[j]))


def calcular_promedio(archivo):
    if os.path.exists(archivo):
        m = open(archivo, 'rb')
        size = os.path.getsize(archivo)
        suma = 0
        ct = 0
        while m.tell() < size:
            peaje = pickle.load(m)
            suma += peaje.distancia
            ct += 1
        promedio = suma / ct
        print('La distancia promedio es: ', promedio)
        m.close()
        return promedio

    else:
        print('El archivo no existe. Cargue el archivo primero')


def crear_arreglo(archivo, prom, vec):
    if os.path.exists(archivo):
        m = open(archivo, 'rb')
        size = os.path.getsize(archivo)
        while m.tell() < size:
            peaje = pickle.load(m)
            if peaje.distancia > prom:
                codigo = peaje.codigo
                patente = peaje.patente
                tipo_vehiculo = peaje.tipo
                forma_pago = peaje.forma_pago
                cabina = peaje.pais_cabina
                distancia = peaje.distancia

                vec.append(Ticket(codigo, patente, tipo_vehiculo, forma_pago, cabina, distancia))

        m.close()



def shellsort(vec):
    n = len(vec)
    h = n // 2
    while h > 0:
        for j in range(h, n):
            # y = vec[j].distancia
            y = vec[j]
            k = j - h
            while k >= 0 and y.distancia < vec[k].distancia:
                vec[k + h] = vec[k]
                k -= h
            vec[k + h] = y
        h //= 2


def mostrar_arreglo(vec):
    for ticket in vec:
        # print(ticket.distancia)
        print(ticket)


def main():
    archivo = 'ticket.dat'
    print('BIENVENIDO!')
    menu()
    op = int(input('Elija una opción '))
    op6 = False

    vec = []

    while op != 9:
        if op == 1:
            if os.path.exists(archivo):
                existe = int(input(
                    'Usted ya ha creado el archivo, si quiere borrar y volver a reescribir presione 1 (sino cualquier otro número) '))
                if existe == 1:
                    crear_achivo(archivo)
                    print('El archivo fue creado con exito!')
            else:
                crear_achivo(archivo)
                print('El archivo fue creado con exito!')

        elif op == 2:
            carga(archivo)
            print('Cargado con exito!')

        elif op == 3:
            muestra(archivo)

        elif op == 4:
            mostrar_patente(archivo)

        elif op == 5:
            busq = busqueda(archivo)
            if busq == None:
                print('No se encontró')
            else:
                print('Se encontró.', busq)

        elif op == 6:
            op6 = True
            mat = [[0] * 5 for i in range(3)]
            matriz_conteo(archivo, mat)

        elif op == 7:
            if op6:
                cant_total(mat)
            else:
                print('Debe cargar la matriz primero')

        elif op == 8:

            prom = calcular_promedio(archivo)
            crear_arreglo(archivo, prom, vec)
            shellsort(vec)
            mostrar_arreglo(vec)

        menu()
        op = int(input('Elija una opción '))

    if op == 9:
        print('ADIÓS!!!')


if __name__ == '__main__':
    main()
