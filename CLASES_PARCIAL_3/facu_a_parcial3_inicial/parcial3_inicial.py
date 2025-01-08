

from funciones import *


def menu():
    # ctrl + d
    print("1 - Cargar Arreglo.")
    print("2 - Mostrar Arreglo.")
    print("3 - Vector de conteo o Acum.")
    print("4 - Busqueda secuencial.")
    x = int(input("Ingresar la opcion: "))  # 1
    return x        # devolver o regresar


def principal():

    # lista vector arreglo vacio
    v_teles = []

    op = -1
    while op != 0:  # mientras op sea distinto de cero, ingreso al ciclo while

        # si tengo una variable igualada a una funcion, significa que espero que la funcion me devuelva
        # algun valor
        op = menu()     # 1

        if op == 1:
            """
                1. Cargar arreglo con n teles, n se pide por teclado, 
                Cada vez que se ingrese a esta opcion debe crear el arreglo de nuevo, no conservar lo anterior
            """
            n = validar_n()         # 3

            v_teles = []
            cargar_arreglo(v_teles, n)

        elif op == 2:
            """
                2 - Mostrar datos ordenados por ID de menor a mayor.
                Solo mostrar los que superen un precio "t"
            """
            ordenar_arreglo(v_teles)

            t = float(input("Ingresar importe a superar"))
            mostrar_arreglo(v_teles, t)

        elif op == 5:
            for i in v_teles:
                print(i)


if __name__ == '__main__':
    principal()