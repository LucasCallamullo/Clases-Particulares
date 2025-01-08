

from funciones import *

def menu():
    # ctrl + d
    print("1 - Cargar arreglo")
    print("2 - Mostrar arreglo")
    print("3 - Vector de Conteo / Acum ")
    print("4 - Busqueda Secuencial")
    print("0 - Salir.")
    op = int(input("Ingresar opcion: "))  # 2
    return op


def principal():

    v_termos = []       # list()

    op = -1
    while op != 0:      # mientras op sea distinto de cero, ingreso al ciclo while

        # si una variable esta igualada a una funcion es porque espero que me devuelva algun valor
        op = menu()     # 2

        if op == 1:
            """
                1 - Al ingresar esta opcion el arreglo debe ser creado nuevamente
            """

            n = validar_n()
            v_termos = []
            cargar_arreglo(v_termos, n)

        elif op == 2:
            """
                2 - Solo Mostrar los datos que superan un precio "t" que se carga por teclado.
                Ordenar antes de mostrar por el atributo MARCA de menor a mayor
            """
            ordenar_arreglo(v_termos)

            t = float(input("Ingresar importe a superar: "))
            mostrar_datos(v_termos, t)

        elif op == 3:
            pass
        elif op == 4:
            pass
        elif op == 0:
            pass


if __name__ == '__main__':
    principal()
