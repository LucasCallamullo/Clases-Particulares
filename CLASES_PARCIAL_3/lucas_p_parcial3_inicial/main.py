

from funciones import *


def menu():
    # ctrl + d
    print("1 - Cargar Arreglo.")
    print("2 - Mostrar Arreglo.")
    print("3 - Vector de conteo/acum.")
    print("4 - Busqueda Secuencial.")
    print("0 - Salir.")
    op = int(input("Ingrese una opcion: ")) # 3
    return op


def principal():

    # vector/lista/arreglo de trabajo
    v_paquetes = []

    op = -1
    while op != 0:  # mientras op sea distinto de cero, ingresar al ciclo while

        # si una variable esta igualada a una funcion es porque espero que la funcion me devuelva algun valor.
        op = menu() # 3

        if op == 1:
            n = validar_n()
            """
            1 - cada vez que se elija esta opcion debe crear el arreglo nuevamente
            """
            v_paquetes = []
            cargar_arreglo(v_paquetes, n)

        elif op == 2:
            """
                2 - Mostrar los datos ordenados por ID de menor a mayor.
                - Solo muestres los que esten entre una cantidad de dias "d1" y "d2" que se cargan por teclado
                
            """
            ordenar_arreglo(v_paquetes)

            d1 = int(input("cantidad de dias a superar: "))
            d2 = int(input("cantidad de dias a ser menor: "))
            mostrar_arreglo(v_paquetes, d1, d2)

        elif op == 3:
            pass

        elif op == 4:
            pass


if __name__ == '__main__':
    principal()