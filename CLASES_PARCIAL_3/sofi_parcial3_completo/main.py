

from funciones import *


def menu():
    print("1 - Cargar Arreglo.")
    print("2 - Mostrar Arreglo.")
    print("3 - Vector de Conteo.")
    print("4 - Busqueda Secuencial.")
    print("0 - Salir.")
    op = int(input("Ingresar opcion: "))     # 3
    return op        # devolver este valor x


def main():

    # arreglo - vector - lista de trabajo
    v_errores = []      # list()

    op = -1
    while op != 0:

        # si una variable esta igualada a una funcion es porque espero que devuelva algun resultado
        op = menu()     # 3

        if op == 1:
            """ 1 - cada vez que se ingrese a esta opcion el arreglo debe reiniciarse. """
            n = validar_n()
            v_errores = []
            cargar_arreglo(v_errores, n)

        elif op == 2:
            """
            - Muestre el arreglo ordenado por codigo de menor a mayor.
            - Solo mostrar los que tengan una hora entre s1 y s2 ( se cargan por teclado ).
            """
            if len(v_errores) > 0:

                ordenar_arreglo(v_errores)

                s1 = int(input("Ingresar hora a superar: "))
                s2 = int(input("Ingresar hora a ser menor: "))
                mostrar_arreglo(v_errores, s1, s2)

            else:
                print("Todavia no ingreso a la opcion 1.")

        elif op == 3:
            """
                Determinar la cantidad de errores por hora (24 contadores)
                
            """
            generar_vector_conteo(v_errores)


        elif op == 4:
            """ 
                4 - Determinar si existe un error con un mensaje "m", y el error "Error 404"
                - Si existe modificar su importe por un valor "imp" que se carga por teclado, y despues
                mostrar el registro modificado
            """
            m = input("Mensaje a buscar: ")
            pos = busqueda_secuencial(v_errores, m)

            if pos >= 0:
                print("Datos Viejos:", v_errores[pos])

                imp = float(input("Ingresar nuevo importe: "))
                # v_errores = [E1, E2, E3 ]
                v_errores[pos].importe = imp

                print("Datos Actualizados:", v_errores[pos])

                # Aumentes un 10% el valor del importe
                v_errores[pos].importe += v_errores[pos].importe * 0.1

                # Si existe, solo mostrar su codigo y su hora
                print("Codigo:", v_errores[pos].codigo, "y su Hora:", v_errores[pos].hora)

            else:
                print("No existe.")


        elif op == 5:
            for i in v_errores:
                print(i)


if __name__ == '__main__':
    main()
