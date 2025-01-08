

from funciones import *


def menu():
    # ctrl + d
    print(" 1 - Cargar Arreglo.")
    print(" 2 - Mostrar Arreglo.")
    print(" 3 - Vector de conteo/acum.")
    print(" 4 - Busqueda secuencial.")
    print(" 0 - Salir.")
    op = int(input("Ingrese una opcion: "))  # 2
    return op


def principal():

    # arreglo - lista - vector - array      - - de trabajo
    v_figuritas = []

    op = -1
    while op != 0:      # mientras op sea distinto de CERO, ingrese al ciclo while

        # si una variable esta igualada a una funcion es porque espero que devuelva algun resultado
        op = menu()

        if op == 1:
            n = validar_n()
            cargar_arreglo(v_figuritas, n)

        elif op == 2:

            """
                2 - Mostrar el arreglo ordenado por nombre,
                - Mostrar solo los que superen un importe "v" que se ingresa por teclado
                
            """
            ordenar_arreglo(v_figuritas)

            v = float(input("Ingresar importe a superar: "))
            mostrar_arreglo(v_figuritas, v)

        elif op == 3:

            """ 3 - Determinar y mostrar la cantidad de figuritas por cada posibles pais
             # Solo mostrar los contadores que superan una cantidad "c" que se ingresa por teclado. 
             """
            c = int(input("Ingresar cantidad a superar: "))
            generar_vector_conteo(v_figuritas, c)

        elif op == 4:
            """
                4 - Determinar si existe un registro cuyo num jugador sea igual a "j" que se ingresa por teclado
                y que ademas juegue en la posicion de "Arquero" o "Defensor"
                
                - Si existe, modificar su precio por un valor "imp" que se carga por teclado
                - Si no existe, informar
                - que se debe detener al primer resultado que encuentre.
            """
            j = int(input("Ingresar numero de jugador a buscar ( 1, 19): "))

            pos = busqueda_secuencial(v_figuritas, j)

            if pos >= 0:
                print("Datos viejos:", v_figuritas[pos])

                imp = float(input("Ingresar nuevo precio a cargar: "))
                v_figuritas[pos].importe = imp

                print("Datos Actualizados:", v_figuritas[pos])

                # auentes su precio por un 10%
                # v_figuritas[pos].importe += v_figuritas[pos].importe * 0.1

                # solo muestre el nombre y el importe
                # print("Nombre:", v_figuritas[pos].nombre, "Y su importe es:", v_figuritas[pos].importe)

            else:
                print("No se encontro una figurita que cumpla.")


if __name__ == '__main__':
    principal()
