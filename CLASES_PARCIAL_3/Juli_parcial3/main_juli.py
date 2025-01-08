

# pedimos importar todas las funciones del modulo funciones
from funciones import *


def menu():
    # ctrl + d
    print()
    print("1 - Cargar Arreglo.")
    print("2 - Mostrar el Arreglo.")
    print("3 - Vector de conteo o acumulacion.")
    print("4 - Busqueda secuencial o binaria.")
    print("0 - Salir.")
    print()
    op = int(input("Ingresar la opcion: "))     # 3
    return op


def principal():

    v_teles = []        # list()

    op = -1
    while op != 0:      # mientras op sea distinto de cero ejecuto el ciclo while

        op = menu()     # 3

        if op == 1:
            n = validar_n()
            cargar_arreglo(n, v_teles)

        elif op == 2:
            t = int(input("Ingresar ID a superar para msotrar: "))
            ordenar_arreglo(v_teles)
            mostrar_datos(v_teles, t)

        elif op == 3:
            pass
        elif op == 4:
            print("alguna cosa 2")
        elif op == 5:
            print("alguna cosa 2")

        elif op == 0:
            print("gracioas por usar el programa ")

    print("Termino el programa")


if __name__ == '__main__':
    principal()
