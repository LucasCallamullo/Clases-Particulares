import os
import io

from func import *
from reg import *


def menu():
    print("-" * 115)
    print("EMPRESA DE PEAJES 4.0")
    print("-" * 115)
    print("1. Crear un archivo binario.")
    print("2. Cargar un ticket manualmente.")
    print("3. Mostrar datos.")
    print("4. Buscar una patente.")
    print("5. Buscar un código identificatorio.")
    print("6. Cantidad de tipos de vehículos por cabina.")
    print("7. Cantidad vehículos por cada tipo de vehículo, y la cantidad total de vehículos por cabina.")
    print("8. Cargar Arreglo Y Mostrar mayores al promedio.")
    print("0. Salir.")
    op = validar_entre(0, 9, validar_solo_num(input("\nIngrese opción elegida: ")))
    print("-" * 115)
    print()
    return op


def convertir_ticket(linea):
    token = linea.split(",")
    return Ticket(int(token[0]), token[1], int(token[2]), int(token[3]), int(token[4]),
                  int(token[5]), imp_final(int(token[2]), int(token[3]), imp_basico(int(token[4]))))


def crear_archivo(archivo, fd):
    if not os.path.exists(archivo):
        print("El archivo no existe.")
    else:
        m = open(archivo, "rt")
        t = open(fd, "wb")
        cont_linea = 0
        for linea in m:
            cont_linea += 1
            if cont_linea > 2:
                if linea[-1] == "\n":
                    linea = linea[:-1]
                ticket = convertir_ticket(linea)
                pickle.dump(ticket, t)

        m.close()
        t.close()
        print("ARCHIVO CARGADO.")
        print()


def buscar(archivo, fd, p):
    if not os.path.exists(archivo):
        print("El archivo", archivo, "no existe.")
        print()
        return

    m = open(fd, "rb")
    t = os.path.getsize(fd)
    fp_inicial = m.tell()
    m.seek(0, io.SEEK_SET)

    pos = -1
    cont = 0
    print("Buscando registros...")
    while m.tell() < t:
        fp = m.tell()
        ticket = pickle.load(m)
        if ticket.patente == p:
            pos = fp
            cont += 1
            print(ticket)
    print()
    if cont != 0:
        print("Se mostraron: ", cont, " registros.")
    print()
    m.seek(fp_inicial, io.SEEK_SET)
    m.close()
    return pos


def buscar_cod(archivo, fd, c):
    if not os.path.exists(archivo):
        print("El archivo", archivo, "no existe.")
        print()
        return

    m = open(fd, "rb")
    t = os.path.getsize(fd)
    fp_inicial = m.tell()
    m.seek(0, io.SEEK_SET)

    pos = -1
    print("Buscando registro...")
    print()
    while m.tell() < t:
        fp = m.tell()
        ticket = pickle.load(m)
        if ticket.codigo == c:
            pos = fp
            print(ticket)
            break
    print()
    m.seek(fp_inicial, io.SEEK_SET)
    m.close()
    return pos


def cargar_manual(archivo, fd):
    if not os.path.exists(archivo):
        print("El archivo no existe.")

    if len(fd) != 0:
        m = open(fd, "ab")
    else:
        m = open(fd, "wb")
    cod = validar_solo_num(input("Código identificador: "))
    pat = validar_pat((input("Ingrese patente: ")).upper())
    tipo = validar_entre(0, 2, validar_solo_num(input("Ingrese tipo de vehículo (0.Moto, 1.Auto, 2.Camión): ")))
    pago = validar_entre(1, 2, validar_solo_num(input("Ingrese forma de pago (1.Manual, 2.Telepeaje): ")))
    cab = validar_entre(0, 4, validar_solo_num(
        input("Ingrese número de cabina (0. Argentina, 1.Bolivia, 2.Brasil, 3.Paraguay, 4.Uruguay): ")))
    d = validar_mayor(0, validar_solo_num(input("Ingrese distancia recorrida: ")))
    imp = imp_final(tipo, pago, imp_basico(cab))
    ticket = Ticket(int(cod), pat, int(tipo), int(pago), int(cab), int(d), imp)
    pickle.dump(ticket, m)
    m.close()
    print("\nTICKET CARGADO.\n")


def mostrar_archivo(archivo, fd):
    if not os.path.exists(archivo):
        print("El archivo", archivo, "no existe.")
        print()
        return
    cont_linea = 0
    tam = os.path.getsize(fd)
    m = open(fd, "rb")
    print("Contenido del archivo", fd, "...")
    while m.tell() < tam:
        p = pickle.load(m)
        print(p)
        cont_linea += 1

    m.close()
    print()


def mat_conteo(archivo, fd):
    if not os.path.exists(archivo):
        print("El archivo", archivo, "no existe.")
        print()
        return
    cont_fila, cont_columna = 3, 5
    cant = [cont_columna * [0] for f in range(cont_fila)]
    tam = os.path.getsize(fd)
    m = open(fd, "rb")

    while m.tell() < tam:
        ticket = pickle.load(m)
        f = ticket.tipo_vehiculo
        c = ticket.cabina
        cant[f][c] += 1

    print("Cantidad de tipos de vehículos por cabina...")
    for f in range(cont_fila):
        for c in range(cont_columna):
            if cant[f][c] > 0:
                print("Tipo", TIPOS[f], " - Cabina", CABINAS[c], " - Cantidad: ", cant[f][c])

    m.close()
    return cant


# Opcion 7
def mat_total(matriz):
    acum_tot_f = 0
    for f in range(len(matriz)):
        for c in range(len(matriz[0])):
            acum_tot_f += matriz[f][c]
        print("Total acumulado por Tipo Vehiculo:", TIPOS[f], "es:", acum_tot_f)
        print()
        acum_tot_f = 0


    acum_tot_c = 0
    for c in range(len(matriz[0])):
        for f in range(len(matriz)):
            acum_tot_c += matriz[f][c]

        print("Total acumulado por Pais Cabina:", CABINAS[c], "es:", acum_tot_c)
        print()
        acum_tot_c = 0


# Opcion 8
def calcular_promedio(archivo):
    if os.path.exists(archivo):
        m = open(archivo, 'rb')
        tam = os.path.getsize(archivo)
        suma = 0
        cant = 0
        while m.tell() < tam:
            ticket = pickle.load(m)
            suma += ticket.distancia
            cant += 1

        m.close()
        if cant > 0:
            promedio = suma / cant
            print('La distancia promedio es: ', promedio)
            return promedio

    else:
        print('El archivo no existe. Cargue el archivo primero')


def generar_arreglo(archivo, prom, v):
    if os.path.exists(archivo):
        m = open(archivo, 'rb')
        tam = os.path.getsize(archivo)
        while m.tell() < tam:
            ticket = pickle.load(m)
            if ticket.distancia > prom:
                codigo = ticket.codigo
                patente = ticket.patente
                tipo_vehiculo = ticket.tipo_vehiculo
                forma_pago = ticket.forma_pago
                cabina = ticket.cabina
                distancia = ticket.distancia
                imp = imp_final(tipo_vehiculo, forma_pago, imp_basico(cabina))

                ticket = Ticket(codigo, patente, tipo_vehiculo, forma_pago, cabina, distancia, imp)
                add_in_order(v, ticket)
        m.close()


def add_in_order(v, ticket):
    n = len(v)
    # pos = n
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if v[c].distancia == ticket.distancia:
            pos = c
            break
        if v[c].distancia > ticket.distancia:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq
    # Lo marca pero logicamente siempre va a existir pos.
    v[pos:pos] = [ticket]


def mostrar_arreglo(v):
    for ticket in v:
        print(ticket)


def main():
    archivo = "peajes-tp4.csv"
    fd = "tickets.dat"
    v = []
    datos_cargados = False

    # bandera opcion 6
    ingreso_op6 = False

    op = -1
    while op != 0:
        op = int(menu())
        if op == 1:
            if not datos_cargados:
                crear_archivo(archivo, fd)
                datos_cargados = True
            if datos_cargados or len(fd) != 0:
                confirmar = validar_entre(1, 2, validar_solo_num(input("1. Sí\n2. No\n¿Eliminar datos existentes?: ")))
                if int(confirmar) == 1:
                    crear_archivo(archivo, fd)
        elif op == 2:
            cargar_manual(archivo, fd)
            datos_cargados = True
        elif op == 0:
            print()
            print("SALIENDO DEL PROGRAMA.")
        elif op == 3:
            mostrar_archivo(archivo, fd)
        elif op == 4:
            p = (input("Patente a buscar: ")).upper()
            print()
            pos = buscar(archivo, fd, p)
            if pos == -1:
                print("No se encontró esa patente.")
        elif op == 5:
            c = validar_solo_num(input("Código identificador a buscar: "))
            print()
            pos = buscar_cod(archivo, fd, int(c))
            if pos == -1:
                print("No se encontró ese código identificatorio.")
        elif op == 6:
            mat_cant = mat_conteo(archivo, fd)
            ingreso_op6 = True

        elif op == 7:
            if ingreso_op6:
                # Aparece este error pero sabemos que la bandera controla que nunca pueda entrar
                # en esta opcion excepto que haya pasado por la opcion 6 previamente
                mat_total(mat_cant)
            else:
                print("Primero debe crear la matriz en la opcion 6.")

        elif op == 8:
            prom = calcular_promedio(fd)
            generar_arreglo(fd, prom, v)
            mostrar_arreglo(v)

        else:
            print("OPCIÓN INVÁLIDA.")


if __name__ == "__main__":
    main()
