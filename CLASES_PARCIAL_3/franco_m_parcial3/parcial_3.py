

from funciones import *


def menu():
    # redeclarar la variable op
    print("=" * 50)
    print("1 - Cargar Arreglo.")
    print("2 - Mostrar Arreglo.")
    print("3 - Vector de Conteo/acumulacion.")
    print("4 - Busqueda Secuencial.")
    print("0 - Salir.")
    op = int(input("Ingresar opcion: "))  # 1, 2, 3, 4, 0
    return op


def principal():

    # vector/arreglo/array/lista    vacía
    v_estudiantes = []

    # Menu de opciones
    op = -1
    while op != 0:          # mientras op sea != 0: ingrese al ciclo

        # si una variable se iguala a un funcion, significa que espero que la funcion me devuelva algo
        op = menu()

        if op == 1:
            """
            1 - Cargar un ESTUDIANTE con legajo, nombre una cadena, tipo de carrera del 1 al 4 que corresponden
            tupla_carreras = ("Sistemas", "Civil", "Industrial", "Quimica") y tienen una cuota 
            importe superior a 0
            """
            n = validar_n()

            # cada vez que se ingrese a  esta opcion el arreglo debe ser creado de nuevo
            v_estudiantes = []

            cargar_arreglo(v_estudiantes, n)
            # v_estudiantes = cargar_arreglo(v_estudiantes, n)

        elif op == 2:
            """
            2 - Mostrar el arreglo pero ordenado por legajo de menor a mayor, 
            - Solo debe mostrar los estudiantes que superen una cuota "t1" y "t2", donde "t" es un valor que se 
            ingresa por teclado. Al final debe mostrar un promedio de las cuotas de los estudiantes que
            se mostraron
            """
            # if v_estudiantes:
            if len(v_estudiantes) > 0:
                ordenar_arreglo(v_estudiantes)

                t = float(input("Ingresar cuota a superar: "))
                t2 = float(input("Ingresar cuota a ser menor: "))
                mostrar_arreglo(v_estudiantes, t, t2)

            else:
                print("No hay estudiantes cargados ingrese a la opcion 1.")

        elif op == 3:
            """     # Carrea (1, 4)    # 4 contadores
                Determines la cantidad de estudiantes por cada posible carrera, (hacer 4 contadores),
                - Al final debe mostrar solo las carreras que tengan una cantidad de estudiantes 
                mayor a "x", que es un valor que se ingresa por teclado.
                - Solo debe mostrar las carreras de Industrial y Quimica
            """
            if len(v_estudiantes) > 0:
                x = int(input("Ingresar cantidad a superar: "))
                generar_vector_conteo(v_estudiantes, x)

            else:
                print("No hay estudiantes cargados ingrese a la opcion 1.")

        elif op == 4:
            """
                4 - Buscar un Estudiante con un legajo "leg" que se ingresa por teclado, y que pertenezca
                a la carrera de "Sistemas", Se detenga al primer resultado, informar si no existe,  
                - si existe, mostrar sus datos, y luego modificar su cuota por un valor "imp" que se
                ingresa por teclado, y despues mostrar los datos actualizados 

                if i.carrera == "Sistemas" con 1
            """
            if len(v_estudiantes) > 0:
                leg = int(input("Ingresar Legajo a buscar: "))

                pos = busqueda_secuencial(v_estudiantes, leg)

                if pos >= 0:
                    # encontre un resultado
                    print("Datos Viejos:", v_estudiantes[pos])

                    imp = float(input("Ingrese nueva cuota del estudiante: "))
                    v_estudiantes[pos].importe = imp

                    # incrementes su cuota por un 10%
                    v_estudiantes[pos].importe += 0.1 * v_estudiantes[pos].importe

                    print("Datos Actualizados:", v_estudiantes[pos])

                    # Solo mostrar su nombre y su cuota
                    print("Nombre:", v_estudiantes[pos].nombre, "y su cuota es:", v_estudiantes[pos].importe)

                else:
                    print("No se encontro un resultado")

            else:
                print("No hay estudiantes cargados ingrese a la opcion 1.")

        elif op == 0:
            print("Gracias por usar el menu.")

        else:
            print("ingrese una opcion correcta")


if __name__ == '__main__':
    principal()
