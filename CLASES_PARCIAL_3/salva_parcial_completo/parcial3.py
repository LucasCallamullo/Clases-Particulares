

from funciones import *


def menu():
    # ctrl + d
    print("1 - Cargar Arreglo.")
    print("2 - Mostrar Arreglo.")
    print("3 - Vector de Conteo.")
    print("4 - Busqueda Secuencial.")
    print("0 - Salir.")

    op = int(input("Ingresar opcion: "))  # 2
    return op


def principal():

    # crear nuestra lista/vector/arreglo de trabajo
    v_figuritas = []

    op = -1
    while op != 0:  # mientras op sea distinto de cero, ingresar al ciclo

        # si una variable esta igualada a una funcion, significa que espera la funcion retorne algo
        op = menu()

        if op == 1:
            """ 1- Cargar arreglo. n por teclado
                - Cada vez que se elija esta opcion debe crearse nuevamente el arreglo.
            """
            n = validar_n()
            v_figuritas = []
            cargar_arreglo(v_figuritas, n)

        elif op == 2:
            """
                2 - Mostrar los datos ordenados por Nombre de menor a mayor.
                - Solo mostrar las figuritas que superen un importe "x"
                
            """
            ordenar_arreglo(v_figuritas)

            x = float(input("Ingresar cantidad de importe a superar: "))
            mostrar_datos(v_figuritas, x)

        elif op == 3:
            """
                3 - vector de conteo - acum
                - Determines y muestras la cantidad de figuritas por cada posicion posible
                posicion(1, 4) un vector con 4 contadores
                - Solo mostrar los contadores que superen un valor "m" que se ingresa por teclado.
            """
            m = int(input("Ingresar cantidad a superar: "))
            generar_vector_conteo(v_figuritas, m)

        elif op == 4:
            """
            4 - Determinar si existe una figurita cuyo pais sea "p" que se ingresa por teclado, y que juegan en la 
            posicion de "Delantero"
            - Si existe modificar su importe por un valor imp que se carga por teclado, despues mostrar el registro
            modifcado
            - Si no existe, informar
            - Tambien detener la busqueda al primer resultado
            """
            p = int(input("Ingresar un pais a buscar: "))
            pos = busqueda_secuencial(v_figuritas, p)

            if pos >= 0:

                print("Datos Sin Modificar:", v_figuritas[pos])

                imp = float(input("Ingresar nuevo importe: "))
                v_figuritas[pos].importe = imp

                print("Datos Modificados:", v_figuritas[pos])

                # aumentes un 10% su importe
                v_figuritas[pos].importe += v_figuritas[pos].importe * 0.1

                # Si existe solo mostrar su nombre y su importe
                print("Nombre:", v_figuritas[pos].nombre, "Y su importe:", v_figuritas[pos].importe)

            else:
                print("No existe.")


if __name__ == '__main__':
    principal()