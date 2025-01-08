

from funciones import *


def menu():
    # ctrl + alt + l        # para corregir los errores pip

    # ctrl + d
    print("1 - Cargar Arreglo")
    print("2 - Mostrar Arreglo")
    print("3 - Vector de Conteo / Acum")
    print("4 - Busqueda Secuencial.")
    print("0 - Salir")

    op = int(input("Ingresar opcion:"))  # 2
    return op


def principal():
    # lista arreglo array vector
    v_estudiantes = []

    op = -1
    while op != 0:  # mientras op sea distinto de cero ingresa al ciclo

        op = menu()

        if op == 1:
            """ 
                1 - Cada vez que se ingrese a esta opcion debe crearse nuevamente el arreglo
            """
            n = validar_n()
            v_estudiantes = []
            cargar_arreglo(v_estudiantes, n)

        elif op == 2:
            """
                2- Mostrar el arreglo ordenado por legajo de menor a mayor.
                - Solo mostrar los que sean mas grandes que un importe "x".
            """
            ordenar_arreglo(v_estudiantes)

            x = float(input("Ingresar importe a superar: "))
            mostrar_arreglo(v_estudiantes, x)

        elif op == 3:

            """
                3 - Determinar y mostrar la cantidad de estudiantes por cada carrera(1, 4) posible
                
                - Solo mostrar los que tengan un contador mayor a "c" que se carga por teclado
                
            """

            c = int(input("Ingresar cantidad a superar: "))
            generar_vector_conteo(v_estudiantes, c)


        elif op == 4:
            """
                4 - buscar al estudiante con el legajo "t" donde t se ingresa por teclado y 
                de la carrera "Industrial".
                - Si existe debe mostrar sus datos y luego cambiar su carrera por una nueva carrera 
                que se ingresa por teclado, y despues mostrar los datos actualizados
            """
            t = int(input("Legajo a buscar: "))
            pos = busqueda_secuencial(v_estudiantes, t)

            if pos >= 0:
                print("Datos viejos:", v_estudiantes[pos])

                car = int(input("Ingresar carrera a elegir (1, 4):"))
                v_estudiantes[pos].carrera = car

                # hacer un aumento en el importe de un 10%
                v_estudiantes[pos].importe += 0.1 * v_estudiantes[pos].importe

                print("Datos Actualizados:", v_estudiantes[pos])

                # solo debe mostrar su nombre y su cuota
                # print("Nombre:", v_estudiantes[pos].nombre, "Cuota:", v_estudiantes[pos].importe)

            else:
                print("No se encontro resultados.")




if __name__ == '__main__':
    principal()
