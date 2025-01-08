

from funciones import *


def menu():
    print("1 - Cargar Arreglo")
    print("2 - Mostrar Arreglo")
    print("3 - Vector de conteo")
    print("4 - Busqueda Secuencial Arreglo")
    print("0 - Salir")
    op = int(input("Ingresar opcion: "))
    return op


def principal():

    # lista / arreglo / array / vector
    v_teles = []        # list()


    op = -1
    while op != 0:      # mientras op sea distinto de cero

        op = menu()     # 5

        if op == 1:
            """ Cargar "n" cantidad de registros en el arreglo, donde "n" es una cantidad ingresada por el
            usuario, Cada vez qeu se ingrese a la opcion 1 debe crearse nuevamente el arreglo."""
            n = int(input("Ingresar cantidad de Teles a cargar: "))
            #  Cada vez qeu se ingrese a la opcion 1 debe crearse nuevamente el arreglo.
            v_teles = []
            cargar_arreglo(v_teles, n)

        elif op == 2:
            """
            Mostrar los datos de todos las teles cuyas pulgadas estén entre los valores s1 y s2
(ambos incluidos) que se cargan por teclado, y ordenados de menor a mayor por ID. Indique al
final el promedio de los importes mostrados en este listado.
            """
            ordenar_arreglo(v_teles)
            s1 = int(input("Cantidad inferior de pulgadas: "))
            s2 = int(input("Cantidad superior de pulgadas: "))
            mostrar_arreglo(v_teles, s1, s2)

        elif op == 3:
            """
            Determinar cuantas teles hay por cada cantidad de pulgadas (19 contadores ), 
            Solo Mostrar todos los conteos que sean superiores a "x" que se ingresa por teclado.

            Al final de este listado, mostrar cual es la pulgada con mayor cantidad de teles
            """
            x = int(input("Cantidad a superar: "))
            generar_vector_conteo(v_teles, x)

        elif op == 4:
            """
            Determinar si existe una tele cuyo número de identificación sea igual a "x" y que tenga un
importe a cobrar igual o mayor a "t", siendo "x" y "t" dos valores que se cargan por teclado. 
Si existe, mostrar sus datos. Si no existe, informar con un mensaje. 
Si existe más de un registro que coincida con esos parámetros de búsqueda, debe mostrar sólo el primero que encuentre.
            """
            x = int(input("Ingresar ID a buscar: "))
            t = float(input("Ingresar Importe a superar o igualar: "))
            pos = busqueda_secuencial(v_teles, x, t)

            if pos >= 0:

                # Solo mostrar el ID y la Marca
                # print("Marca:", v_teles[pos].marca, " ID:", v_teles[pos].id)

                print("Datos Viejos: ", v_teles[pos])

                # Modificar el valor del importe por un valor "imp" que se ingresa por teclado
                imp = float(input("Ingresar nuevo importe: "))
                v_teles[pos].importe = imp

                # Agregar un 10% al importe encontrado
                # v_teles[pos].importe += v_teles[pos].importe * 0.1

                print("Datos Actualizados: ", v_teles[pos])

            else:
                print("No se encontro un registro.")



        elif op == 0:
            pass


if __name__ == '__main__':
    principal()
