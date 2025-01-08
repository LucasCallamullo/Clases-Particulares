

from funciones import *


def menu():
    # ctrl + d
    print("1 - Cargar Arreglo. ")
    print("2 - Mostrar Datos. ")
    print("3 - ")
    print("4 - ")
    print("0 - Salir.")
    op = int(input("Ingresar opcion: "))    # 2
    return op           # retornar o devolver op


def principal():

    v_parlantes = []

    op = -1
    while op != 0:

        op = menu()     # 2

        if op == 1:
            n = int(input("Ingresar parlantes a cargar: "))     # 4
            cargar_arreglo(v_parlantes, n)

        elif op == 2:
            """
                2. Mostrar los datos de los parlantes que superen un importe "t" donde t se carga por teclado
                Al final debe mostrar el promedio de los parlantes que se mostraron, 
                En vez de mostrar el numero de color, Se debe mostrar el color asociado que tiene cada entero.
                - Debe mostrar el arreglo ordenado por ID antes de mostrarlo.
            """
            ordenar_arreglo(v_parlantes)

            t = float(input("Ingresar el importe a superar: "))
            mostrar_datos(v_parlantes, t)

        elif op == 3:
            pass
        elif op == 4:
            pass
        elif op == 0:
            print("Gracias por usar el menu.")


if __name__ == "__main__":
    principal()