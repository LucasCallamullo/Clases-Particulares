

from funciones import *


def menu():
    # ctrl + d
    print(" 1 - Cargar Arreglo.")
    print(" 2 - Mostrar Arreglo.")
    print(" 3 - Vector de Conteo/Acum.")
    print(" 4 - Busqueda Secuencial.")
    print(" 0 - Salir.")

    op = int(input("Ingresar opcion: "))        # op = 2
    return op             # devolver / retornar


def principal():

    # vector - arreglo - lista // de trabajo
    v_celus = []

    op = -1
    while op != 0:      # mientras op sea distinto de 0, quiero que ingrese a mi ciclo

        # si una variable esta igulada a una funcion es porque espero que la funcion me retorne algo
        op = menu()     # 2

        if op == 1:
            """
                1 - Cargar arreglo con n celulares
            """
            n = validar_n()     # 3
            cargar_arreglo(v_celus, n)

        elif op == 2:
            """
                2 - Mostrar el arreglo ordenado por ID de menor a mayor
                - Solo mostrar las que superan la cantidad de pulgadas "x" que se ingresa por teclado
                
            """
            ordenar_arreglo(v_celus)

            x = int(input("Ingresar cantidad de pulgadas a superar: "))
            mostrar_datos(v_celus, x)

        elif op == 3:
            pass

        elif op == 4:
            pass


if __name__ == '__main__':
    principal()

