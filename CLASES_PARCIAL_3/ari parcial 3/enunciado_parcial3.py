

from funciones import *


def menu():
    # ctrl + d
    print("1 - Cargar Arreglo.")
    print("2 - Mostrar Arreglo.")
    print("3 - Vector de conteo/Acum.")
    print("4 - Busqueda Secuencial.")
    print("0 - Salir.")

    op = int(input("Ingresar su opcion: "))  # 4
    return op               # retornar, devolver, 4


def principal():

    # arreglo / array / lista / vector
    v_tablets = []

    op = -1
    while op != 0:  # mientras op sea distinta de cero

        # Cuando igualas una variable a un funcion es porque esperas que esa funcion te devuelva algo
        op = menu()  # 4

        if op == 1:
            """ 
            Cargar "n" tablets en un arreglo
            """
            n = int(input("Cantidad de tablets a cargar: ")) # 5
            cargar_arreglo(v_tablets, n)

        elif op == 2:
            """ 
                mostrar los datos del arreglo cargado, pero ordenador de menor a mayor por ID,
                - Solo mostrar los que sean mayores a un importe "t1" y que sean menores a un importe "t2",
                t1 y t2 se piden por teclado
            """
            ordenar_arreglo(v_tablets)

            t1 = float(input("Ingresa importe a superar: "))
            t2 = float(input("Ingresa importe al que debe ser menor: "))
            mostrar_datos(v_tablets, t1, t2)

        elif op == 3:
            """     # Marca (1, 4)   1 2 3 4
                3 - Determinar y mostrar la sumatoria de los precios de las tablets por cada tipo de marca
                posible, es decir 4 contadores,
                Solo mostrar aquellos que superen un acumulado "x" donde x se carga por teclado.
                y ademas que sean de la marca Samsung o Apple.
                
            """
            x = float(input("Ingresar acumulado a superar: "))
            generar_vector_acum(v_tablets, x)

        elif op == 4:
            """
                4 - Encontrar una tablet que tenga un id igual a "f" y que sea de la marca
                "Samsung"
                - Si se encontro, debe mostrar los datos y luego modificar su importe por un valor
                "imp" que se ingresa por teclado, despues msotrar los datos actualizados
            """
            f = int(input("Num ID a buscar: "))
            pos = busqueda_secuencial(v_tablets, f)     # 2

            if pos >= 0:
                print("Datos Viejos:", v_tablets[pos])

                imp = float(input("Ingresar nuevo precio de la tablet: "))
                v_tablets[pos].importe = imp

                print("Datos Actualizados: ", v_tablets[pos])

                # incremente su importe por un 10%
                calcular_10_por_ciento = v_tablets[pos].importe * 10 / 100
                v_tablets[pos].importe += calcular_10_por_ciento

                # v_tablets[pos].importe += 0.1 * v_tablets[pos].tablets

                # Mostrar solo el precio y el peso de la tablet
                print("Precio", v_tablets[pos].precio, "Y su peso es:", v_tablets[pos].peso)

            else:
                print("No se encontro resultados.")






        elif op == 0:
            print("Gracias por usar el menu.")


if __name__ == '__main__':
    principal()




