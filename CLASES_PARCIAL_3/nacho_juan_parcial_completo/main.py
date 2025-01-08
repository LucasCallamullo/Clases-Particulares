

from funciones import *


def menu():
    print("1 - Cargar Arreglo.")
    print("2 - Mostrar Arreglo.")
    print("3 - Vector De conteo / Acum.")
    print("4 - Busqueda Secuencial")
    print("0 - Salir.")
    op = int(input("Ingresar la opcion: "))     # 2
    return op


def principal():

    # vector/arreglo/lista de trabajo
    v_errores = []      # list()

    op = -1
    while op != 0:

        # si una variable es igual a un funcion es porque espero que la funcion devuelva algo
        op = menu()     # 2

        if op == 1:
            n = validar_n()
            """
                1 - Cada vez que se ingrese a esta opcion debe crear nuevamente el arreglo.
            """
            v_errores = []
            cargar_arreglo(v_errores, n)

        elif op == 2:
            """
                2 - Mostrar el arreglo ordenado por codigo.
                - Solo mostrar los importes que superan un valor "t" que se carga por teclado
            """
            ordenar_arreglo(v_errores)

            t = float(input("Ingresar importe a superar: "))
            mostrar_arreglo(v_errores, t)

        elif op == 3:
            """
                3 - Determinar y mostrar la cantidad de errores por cada hora posible (24 contadores)
                - Solo mostar los contadores que superen una cantidad "m".  
            """
            m = int(input("Ingresar cantidad a superar: "))
            generar_vector_conteo(v_errores, m)

        elif op == 4:
            """
            4 - Busqueda secuencial 
            Determinar si existe un error cuyo codigo sea "cod" y que este entre la hora 10 y 15
            - Si existe modificar su importe por un valor "imp" que se carga por teclado, despues mostrar
            los datos modificados
            - Si no existe INFORMAR
            - Que se detenga al primero resultado que encontremos
            """
            cod = int(input("Ingresar codigo a buscar: "))
            pos = busqueda_secuencial(v_errores, cod)

            if pos >= 0:
                print("Datos No Modificados: ", v_errores[pos])

                imp = float(input("Ingresar nuevo importe: "))
                v_errores[pos].importe = imp

                print("Datos Modificados: ", v_errores[pos])

                # aumentar un 10% el importe
                v_errores[pos].importe += v_errores[pos].importe * 0.1

                # Solo mostrar el codigo, y la hora
                print("Codigo:", v_errores[pos].codigo, "y su hora es:", v_errores[pos].hora)

            else:
                print("No existe.")


if __name__ == '__main__':
    principal()


