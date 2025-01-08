

from funciones import *


def menu():
    # ctrl + d
    print("1 - Cargar Arreglo ")
    print("2 - Ordenar y Mostrar el arreglo ")
    print("3 - Vector De conteo/Acum")
    print("4 - Busqueda Secuencial")
    print("0 - ")
    op = int(input("Ingresar opcion: "))  # 3
    return op


def principal():

    # arreglo / vector / lista
    v_figuritas = []        # list()

    op = -1
    while op != 0:          # mientras op sea distinto de cero que ingrese al ciclo

        # Si yo igualo una variable a una funcion es porque estoy esperando que me retorne algun valor
        op = menu()     # 3

        if op == 1:
            """
                1. Cada vez que se ingrese a esta opcion, se debe generar un arreglo nuevo desde cero.
            """
            v_figuritas = []
            n = validar_n()
            cargar_arreglo(v_figuritas, n)

        elif op == 2:
            """
                2. Ordenar el arreglo por nombre de menor a mayor y luego mostrarlo a razon de un por linea, solo
                debe mostrar las figuritas que 'superen un importe "x"', al final debe mostrar el promedio de los 
                importes de las figuritas mostradas
            """
            ordenar_arreglo(v_figuritas)

            x = float(input("Importe a superar: "))
            mostrar_datos(v_figuritas, x)

        elif op == 3:
            pass
        elif op == 4:
            pass
        elif op == 0:
            pass


if __name__ == '__main__':
    principal()
