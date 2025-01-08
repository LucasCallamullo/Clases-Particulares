

from funciones import *


# Opcion 4
def busqueda_secuencial(v_figus, nom, j):   # nom = A
    pos = -1
    # indices       0       1       2
    # v_figus = [   F1,     F2,     F3]
    # nom            S      A       B
    for i in range(len(v_figus)):
        # i = 0, 1, 2, 3
        if v_figus[i].nombre == nom and v_figus[i].num_jug == j:
            pos = i
            break   # romper ciclos

    return pos  # 0 o + SI EXISTE / -1 NO EXISTE


def busqueda_secuencial2(v_figus, nom):
    bandera = False
    for i in v_figus:
        if i.nombre == nom:
            print(i)
            i.importe = 5
            bandera = True
            break

    if not bandera:
        print("No se encontro")


def menu():
    # ctrl + d
    print(" 1 - Cargar arreglo.")
    print(" 2 - Mostrar arreglo.")
    print(" 3 - Vector de conteo Acum.")
    print(" 4 - Busqueda Secuencial.")
    print(" 0 - Salir.")
    op = int(input("Ingresar opcion: "))    # 1
    return op   # retornar, devolver algo


def principal():

    # vector/arreglo/lista de trabajo
    v_figus = []

    bandera_op1 = False

    op = -1
    while op != 0:  # mientras op sea distinto de cero, ingresa al ciclo while

        # si una variable esta igualada a una funcion, que espera que la funcion me retorne algo
        op = menu()  # 1 - > o sea lo que devuelva menu

        if not bandera_op1:
            if op == 1:
                """
                1 - cargar arreglo con n figuritas
                - Cada que se selecciona esta opcion debe generar nuevamente el arreglo
                """
                n = validar_n()
                v_figus = []
                cargar_arreglo(v_figus, n)
                bandera_op1 = True
            else:
                print("Ingresar opcion 1")

        else:
            if op == 1:
                """
                1 - cargar arreglo con n figuritas
                - Cada que se selecciona esta opcion debe generar nuevamente el arreglo
                """
                n = validar_n()
                v_figus = []
                cargar_arreglo(v_figus, n)

            elif op == 2:
                """
                2 - Mostrar el arreglo ordenado por nombre.
                - Solo mostrar los pais que sean mayores a "p" que se carga por teclado
                -
                """
                if len(v_figus) > 0:
                    ordenar_arreglo(v_figus)

                    p = int(input("Ingresar pais a superar: "))
                    mostrar_arreglo(v_figus, p)

                else:
                    print("Primero ingrese a la opcion 1.")

            elif op == 3:
                if len(v_figus) > 0:
                    """
                    3 - Determinar y mostrar la cantidad de figuritas por cada pais posible (1, 32) , 
                    32 contadores
                    - solo mostrar los contadores que tengan una cantidad mayor a "m"
                    """
                    m = int(input("Ingresar cantidad a superar: "))
                    generar_vector_conteo(v_figus, m)

                else:
                    print("Primero ingrese a la opcion 1")

            elif op == 4:
                """
                    4 - Determinar si existe una figurita cuyo nombre sea igual "nom" y cuyo num jugador
                    sea igual a "j" ambos valores se cargan por teclado
                    - Si existe modificar el importe por un valor "imp" que se carga por teclado y luego
                    mostrar los datos modificados
                    - Si no existe, informar 
                    - Detener la busqueda al primer resultado
                """
                nom = input("Ingresar nombre a buscar: ")
                j = int(input("Ingresar num jugador a buscar: "))

                pos = busqueda_secuencial(v_figus, nom, j)

                if pos >= 0:
                    print("Datos sin modificar:", v_figus[pos])

                    imp = float(input("Ingresar nuevo importe: "))
                    v_figus[pos].importe = imp

                    print("Datos modificados:", v_figus[pos])

                    # aumentar 10% el importe
                    v_figus[pos].importe += v_figus[pos].importe * 0.1

                    # solo mostrar su pais y su importe
                    print("Pais:", v_figus[pos].pais, "y tiene un importe de:", v_figus[pos].importe)

                else:
                    print("No existe.")


if __name__ == '__main__':
    principal()
