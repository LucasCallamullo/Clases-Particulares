

from funciones import *


def menu():
    # ctrl + d
    print("1 - Cargar Arreglo.")
    print("2 - Mostrar Arreglo.")
    print("3 - Vector de conteo/acum.")
    print("4 - Busqueda Secuencial.")
    print("0 - Salir.")
    op = int(input("Ingresar un valor: "))  # 3
    return op   # 3     # devolver valores


def principal():

    # crear nuestra lista/vector/arreglo de trabajo
    v_juicios = []


    op = -1
    while op != 0:  # mientras op sea distinto de cero, ingresa al ciclo

        # si una variable esta igualada a una funcion es porque espera que la funcion nos devuelva algo
        op = menu()

        if op == 1:
            n = validar_n()
            cargar_arreglo(v_juicios, n)

        elif op == 2:
            """
            2 - mostrar los datos ordenados por descripcion de menor a mayor 
            - Solo mostrar los que superen un monto "mon" que se carga por teclado
            """
            ordenar_arreglo(v_juicios)

            mon = float(input("Ingresar monto a superar: "))
            mostrar_datos(v_juicios, mon)

        elif op == 3:
            """
            3 - determinar y mostrar la cantidad de juicios por cada tipo de juicio
            - Mostrar solo los que sean mayores a una cantidad c que se ingresa por teclado
            
            """
            c = int(input("Cantidad a superar de los contadores: "))
            generar_vector_conteo(v_juicios, c)

        elif op == 4:
            """
            4- Determinar si existe algun Juicio con un codigo "cod" que se carga por teclado y un}
            tipo "t" que se carga por teclado
            - Si existe modificar su valor de importe por un "imp" que se ingresa por teclado, y despues
            mostrar sus datos modificados
            """
            cod = int(input("Ingresar codigo a buscar: "))
            t = int(input("Ingresar tipo a buscar: "))
            pos = busqueda_secuencial(v_juicios, cod, t)

            if pos >= 0:

                print("Sin Modificar:", v_juicios[pos])
                imp = float(input("Ingresar nuevo importe: "))
                v_juicios[pos].importe = imp

                print("Datos Modificados:", v_juicios[pos])

                # Aumentar el importe un 10%
                v_juicios[pos].importe += v_juicios[pos].importe * 0.1

            else:
                print("No existe.")


if __name__ == '__main__':
    principal()
