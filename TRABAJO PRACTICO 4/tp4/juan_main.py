import os.path
import pickle
from registro import *


# =================================================================================
#                                       OPCIÓN 1
# =================================================================================
def generar_archivo(fd, f_csv):
    if os.path.exists(fd):
        res = pregunta_op1()
        if res == "N":
            print("No se sobreescribio el archivo: ", fd)
            return
        else:
            print("Se sobreescribio el archivo: ", fd)

    csv, m = open(f_csv, 'rt'), open(fd, "wb")
    cont, lineas = 0, csv.readlines()

    for i in lineas:
        cont += 1
        if cont > 2:
            token = ["861043680", "RCO0099", "0", "2", "3", "170"]
            token = i.split(",")
            # utilizamos funcion del registro para obtener al pais al que pertenece la patente

            codigo = int(token[0])
            patente = token[1]


            pais_patente = pais_patente_identificado(token[1])
            #                   codigo          patente   tipo_veh     forma_pago      pais_cabina     km_recorridos
            new_ticket = Ticket(int(token[0]), token[1], int(token[2]), int(token[3]), int(token[4]), int(token[5]), pais_patente)
            pickle.dump(new_ticket, m)
            m.flush()

    print("Se cargaron un total de:", cont-2, "en el archivo:", fd)
    m.close()
    csv.close()


def pregunta_op1():
    res = input("¿Desea generar un nuevo archivo? S/N: ").upper()
    while res != "S" and res != "N":
        res = input("¿Desea generar un nuevo archivo? S/N (debe ingresar S o N): ").upper()
    return res


# =================================================================================
#                                       OPCIÓN 2
# =================================================================================
def cargar_ticket_individual(fd):
    nuevo_archivo = False
    if not os.path.exists(fd):
        nuevo_archivo = True

    m = open(fd, "ab")
    codigo = validar_datos(1, -1, "Ingresar el código del ticket(Num. Positivo): ")
    patente = input("Ingresar la patente del vehículo: ")
    tipo = validar_datos(0, 2, "Ingresar el tipo de vehiculo (0, 1 o 2) : ")
    forma_de_pago = validar_datos(1, 2, "Ingresar la forma de pago (1 o 2): ")
    pais_cabina = validar_datos(0, 4, "Ingresar el pais de la cabina (entre 0 y 4): ")
    km_recorridos = validar_datos(0, -1, "Ingresar la cantidad de kilometros recorridos: ")
    # utilizamos funcion del registro para obtener al pais al que pertenece la patente
    pais_patente = pais_patente_identificado(patente)
    new_ticket = Ticket(codigo, patente, tipo, forma_de_pago, pais_cabina, km_recorridos, pais_patente)
    pickle.dump(new_ticket, m)
    m.flush()
    m.close()

    if nuevo_archivo:
        print("Se genero correctamente un nuevo archivo con el Ticket generado.")
    else:
        print("Se agrego al final del archivo el Ticket generado.")


def validar_datos(inf, sup, msj):
    valor = int(input(msj))
    if sup != -1:
        while not inf <= valor <= sup:
            print("El valor ingresado no es correcto. Intente nuevamente.")
            valor = int(input(msj))
    else:
        #           1 <=    0
        while not inf <= valor:     # 0
            print("El valor ingresado no es correcto. Intente nuevamente.")
            valor = int(input(msj))

    return valor


# =================================================================================
#                                       OPCIÓN 3
# =================================================================================
def mostrar_archivo(fd):
    m = open(fd, "rb")
    size = os.path.getsize(fd)
    #   vector = [ T, T, T ]
    #   fd =     [ T            T               T ]
    #            0     25           50            70
    while m.tell() < size:
        tick = pickle.load(m)
        print(tick)
    m.close()


# =================================================================================
#                                       OPCIÓN 4
# =================================================================================
def busqueda_lineal_op4(fd, p):
    m = open(fd, "rb")
    cont, size = 0, os.path.getsize(fd)
    while m.tell() < size:
        tick = pickle.load(m)
        if tick.patente == p:
            print(tick)
            cont += 1
    print("Se mostraron un total de:", cont, "Tickets.")
    m.close()


# =================================================================================
#                                       OPCIÓN 5
# =================================================================================
def busqueda_lineal_op5(fd, c):
    m = open(fd, "rb")
    size = os.path.getsize(fd)
    codigo_encontrado = False
    while m.tell() < size:
        tick = pickle.load(m)
        if tick.codigo == c:
            print(tick)
            codigo_encontrado = True
            break

    if not codigo_encontrado:
        print("No se encontro un Ticket con el codigo:", c)
    m.close()


# =================================================================================
#                                       OPCIÓN 6
# =================================================================================
def generar_matriz(fd):
    filas, columnas = 3, 5
    matriz = [[0] * columnas for i in range(filas)]

    m = open(fd, "rb")
    size = os.path.getsize(fd)
    while m.tell() < size:
        i = pickle.load(m)
        f = i.tipo
        c = i.pais_cabina
        matriz[f][c] += 1

    m.close()
    return matriz


def mostrar_matriz(matriz):
    for f in range(len(matriz)):
        for c in range(len(matriz[0])):
            if matriz[f][c] > 0:
                print("=" * 50)
                # Reutilizo las funciones del registro para cambiar los numeros segun corresponda.
                print("Tipo Vehiculo:", vehiculo_to_str(f), "| Pais Cabina:", cabina_to_str(c))
                print("La Cantidad total es:", matriz[f][c])


# =================================================================================
#                                       OPCIÓN 7
# =================================================================================
def totalidades_matriz(matriz):
    linea = "=" * 50
    print("", linea,
          "\n           TIPO VEHICULO "
          "\n", linea, "\n")

    for f in range(len(matriz)):
        acum = 0
        for c in range(len(matriz[0])):
            acum += matriz[f][c]
        # Reutilizo las funciones del registro para cambiar los numeros segun corresponda.
        print("El acumulado total por Tipo Vehiculo:", vehiculo_to_str(f), "es:", acum)
        print()

    print("", linea,
          "\n           PAIS CABINA "
          "\n", linea, "\n")
    for c in range(len(matriz[0])):
        acum = 0
        for f in range(len(matriz)):
            acum += matriz[f][c]
        # Reutilizo las funciones del registro para cambiar los numeros segun corresponda.
        print("El acumulado total del Pais Cabina", cabina_to_str(c), "es:", acum)
        print()


# =================================================================================
#                                       OPCIÓN 8
# =================================================================================
def calcular_promedio(fd):
    m = open(fd, "rb")
    size = os.path.getsize(fd)
    cont, acum, prom = 0, 0, 0
    while m.tell() < size:
        i = pickle.load(m)
        cont += 1
        acum += i.km_recorridos

    if cont > 0:
        prom = acum / cont
        print("El promedio de los km recorridos es:", round(prom, 2))
    return prom


def cargar_archivo(fd, v_ticket, prom):
    m = open(fd, "rb")
    size = os.path.getsize(fd)
    while m.tell() < size:
        i = pickle.load(m)
        if i.km_recorridos > prom:
            add_in_order(v_ticket, i)


def add_in_order(v_ticket, ticket):          # len(v) = 0         ;        T1 = 500
    izq, der = 0, len(v_ticket) - 1         # len(v) = 1        ;           T2 = 490
    while izq <= der:
        c = (izq + der) // 2
        if v_ticket[c].km_recorridos == ticket.km_recorridos:
            pos = c
            break
        elif v_ticket[c].km_recorridos > ticket.km_recorridos:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq
    # este warning aparece pero nosotros sabemos que logicamente este algoritmo siempre nos devolvera un pos.
    #               0   1
    # v_ticket = [ T2,  T1 ]
    v_ticket[pos:pos] = [ticket]


def mostrar_vector(v_ticket):
    for i in v_ticket:
        print(i)


def main():
    # opcion 1, 2
    f_csv = "peajes-tp4.csv"
    fd = "tickets.dat"


    # opcion 6
    validar_op6 = False

    # opcion 8
    v_ticket = list()       # []

    op = -1
    while op != 0:
        op = menu()

        if op == 0:
            print(" Programa Finalizado."
                  "\n Gracias por utilizar el programa.")
            break

        elif op == 1:
            generar_archivo(fd, f_csv)

        elif op == 2:
            cargar_ticket_individual(fd)

        else:
            if not os.path.exists(fd):
                print("Primero debe crear el archivo:", fd, "pasando primero por la opcion 1 o 2.")
            else:
                if op == 3:
                    mostrar_archivo(fd)

                elif op == 4:
                    p = input("Ingresar una patente a buscar: ")
                    busqueda_lineal_op4(fd, p)

                elif op == 5:
                    c = int(input("Ingresar un codigo a buscar: "))
                    busqueda_lineal_op5(fd, c)

                elif op == 6:
                    matriz = generar_matriz(fd)
                    mostrar_matriz(matriz)
                    validar_op6 = True

                elif op == 7:
                    if validar_op6:
                        # este warning nos aparece pero nosotros sabemos que logicamente solo puede entrar si previamente creo la matriz
                        totalidades_matriz(matriz)
                    else:
                        print("Debe primero crear la matriz en la opcion 6.")

                elif op == 8:
                    prom = calcular_promedio(fd)
                    cargar_archivo(fd, v_ticket, prom)
                    mostrar_vector(v_ticket)

                else:
                    print("Por favor ingrese una opcion correcta.")


if __name__ == '__main__':
    main()
