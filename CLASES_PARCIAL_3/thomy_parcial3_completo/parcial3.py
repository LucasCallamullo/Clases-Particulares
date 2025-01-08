

from funciones import *


def menu():
    # ctrl + d
    print("1 - Cargar Arreglo.")
    print("2 - Mostrar Arreglo.")
    print("3 - Vector de Conteo/Acum.")
    print("4 - Busqueda Secuencial.")
    print("0 - Salir.")

    op = int(input("INgresar opcion: "))    # 3
    return op       # retorar o devolver OP


def principal():

    # arreglo - vector - lista de trabajo
    v_figus = []

    op = -1
    while op != 0:  # mientras op sea distinto de cero, ingresar al ciclo

        # si una variable esta igualada a una funcion es porque esperas que devuelva algun valor
        op = menu()

        if op == 1:
            """
                1 - Cada vez que se ingrese a esta opcion el arreglo debe ser creado de nuevo.
            """
            n = validar_n()
            v_figus = []
            cargar_arreglo(v_figus, n)

        elif op == 2:
            """
                - Mostrar el arreglo ordenado por nombre.
                - Solo muestres los que superan un pais "p" que se ingresa por teclado
            """
            ordenar_arreglo(v_figus)

            p = int(input("Ingresar pais a superar: "))
            mostrar_arreglo(v_figus, p)

        elif op == 3:
            """
                3 - determinar la cantidad de figuritas por cada posibles pais (1, 32) 32 contadores
                 - Solo mostrar los contadores que son mayores a una cantidad "c" que se carga por teclado
            """
            c = int(input("Ingresar cantidad de conteo a superar: "))
            generar_vector_conteo(v_figus, c)

        elif op == 4:
            """
            4 - Busqueda Secuencial.
            - Determinar si existe una figurita con el nombre "nom" que se carga pór teclado, que sea de 
            la posicion "arquero" o "defensor"
            """
            nom = input("Ingresar nombre a buscar: ")
            pos = busqueda_secuencial(v_figus, nom)

            if pos >= 0:
                print("Datos Sin Modificar: ", v_figus[pos])

                # Modificar importe por un valor "imp" que se carga por teclado
                imp = float(input("Ingresar Nuevo importe: "))
                v_figus[pos].importe = imp

                print("Datos Modificados: ", v_figus[pos])

                # Aumentar un 10% el importe
                v_figus[pos].importe += v_figus[pos].importe * 0.1

                # Solo muestres su pais y su num jugador
                print("Pais:", v_figus[pos].pais, "Y su Numero es:", v_figus[pos].num_jug)

            else:
                print("No existe.")


if __name__ == '__main__':
    principal()
