

from funciones import *


def menu():
    # ctrl + d
    print("1 - Cargar Arreglo.")
    print("2 - Mostrar Datos")
    print("3 - Vector de conteo")
    print("4 - Busqueda Secuencial")
    print("0 - Salir.")
    op = int(input("Ingresar opcion: "))  # 1
    return op     # devolver retornar algun valor


def principal():

    # crear nuestro arreglo con el que vamos a trabajar
    v_teles = []

    op = -1
    while op != 0:  # mientras op sea distinto de cero, ingreso al ciclo while

        # si una variable esta igualada a una funcion es porque espero que la funcion me devuelva algo
        op = menu() # 1

        if op == 1:
            """
                1 - Cada vez que se ingresa a esta opcion se debe generar el arreglo de nuevo
            """

            n = validar_n()
            v_teles = []
            cargar_arreglo(v_teles, n)

        elif op == 2:
            """
                2 - Mostrar el arreglo ordenado por ID de menor a mayor, a razon de uno por linea.
                Solo mostrar los que superan un importe "t" que se ingresa por teclado
            """
            ordenar_arreglo(v_teles)

            t = float(input("Ingresar importe a superar: "))
            mostrar_datos(v_teles, t)


if __name__ == "__main__":
    principal()
