
import os.path
import pickle

from envio import *


def validar_opcion(mensaje):
    print(" 1 - " + mensaje)
    print(" 0 - Cancelar.")
    op = int(input("Ingresar opción: "))
    while op > 1 or op < 0:
        print(" 1 - " + mensaje)
        print(" 0 - Cancelar.")
        op = int(input("Ingresar opción (una opción valida): "))
    return op


def opcion1(fdt, fd):

    if os.path.exists(fd):
        mensaje = "Desea crear y sobre-escribir el archivo binario nuevamente?"
        op = validar_opcion(mensaje)
        if op == 0:
            print("Ha cancelado la operacion de generar nuevamente el archivo binario.")
            return

    archivo_csv = open(fdt, "r")   # read csv para recuperar los datos
    m = open(fd, "wb")  # write binary, crea el archivo, y sobreescribe el contenido

    cont = 0
    for linea in archivo_csv:
        cont += 1
        if cont >= 3:
            lista_linea = linea.strip().split(",")
            # lista_linea = ['8547', 'Del $ol 456.', '4', '2']
            # codigo STR, direccion STR, tipo INT, pago INT
            codigo = lista_linea[0]
            direccion = lista_linea[1]
            tipo = int(lista_linea[2])
            pago = int(lista_linea[3])

            env = Envio(codigo, direccion, tipo, pago)
            pickle.dump(env, m)     # env = objeto a guardar, m = archivo donde guardar


    print(f"Se cargo el archivo binario con {cont-2} registros")
    archivo_csv.close()
    m.close()


# --------------------------------------------------------------
#                   Opcion 2
# --------------------------------------------------------------
def validar_rango(inf, sup, msj):
    # funcion reutilizada del tp3
    valor = int(input(msj))
    while sup < valor or valor < inf:
        print("El valor ingresado no es correcto. Intente nuevamente.")
        valor = int(input(msj))
    return valor


def opcion2(fd):

    m = open(fd, "ab")
    codigo = input("Codigo postal: ")
    direccion = input("Direccion postal: ")
    tipo = validar_rango(0, 6, "Tipo de envio (entre 0 y 6): ")
    pago = validar_rango(1, 2, "Forma de pago (entre 1 y 2): ")
    env = Envio(codigo, direccion, tipo, pago)
    pickle.dump(env, m)

    print("Carga terminada")
    print()
    m.close()


def opcion3(fd):

    if not os.path.exists(fd):
        print(f"No existe el archivo: {fd}"
              f"\nIngrese primero algún registro con la opción 1 o 2.")
        return

    m = open(fd, "rb")  # read binary, porque solo nos interesa leer el contenido del archivo
    tam = os.path.getsize(fd)

    while m.tell() < tam:
        env = pickle.load(m)        # env = E1, E2, E3
        #
        print(env)

    m.close()


def principal():

    # nombre de nuestro archivo .csv
    fdt = "envios-muestra.csv"

    # crear nuestro nombre del archivo
    fd = "envios.dat"