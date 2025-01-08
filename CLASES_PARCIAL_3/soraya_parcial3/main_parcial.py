

from funciones import *


def menu():
    # ctrl + d
    print("1 - Cargar Arreglo")
    print("2 - Mostrar Arreglo")
    print("3 - Vector Conteo/Acum")
    print("4 - Busqueda Secuencial")
    print("0 - Salir")
    op = int(input("Ingresar opcion: "))        # 4
    return op


def principal():

    # Opcion 1 - Tenes que crear una lista vacía - lista / arreglo / array / vector
    v_paquetes = []         # ó list()

    op = -1
    while op != 0:          # mientras op sea distinto de cero

        op = menu()     # 4

        if op == 1:
            n = int(input("Cantidad de paquetes a cargar: "))       # 5
            cargar_arreglo(v_paquetes, n)

        elif op == 2:
            ordenar_arreglo(v_paquetes)

            """ 
                Solo mostrar los Paquetes que superen un importe "t" que se ingresa por teclado y ademas
                al final de listado mostrar cuantos registros se mostraron.
            """
            t = float(input("Ingresar la cantidad de importe a superar: "))
            mostrar_arreglo(v_paquetes, t)

        elif op == 3:
            """
            Mostrar todos los conteos que sean diferentes de cero. Al final de este listado, 
            mostrar cual fue el tipo de paquete con la mayor cantidad de paquetes. 
            """
            generar_vector_conteo(v_paquetes)

        elif op == 4:
            """ 
                Determinar si existe un paquete cuyo número de identificación sea igual a "x" y que tenga un
importe a cobrar igual o mayor a "t", siendo x y t dos valores que se cargan por teclado. 
    Si existe, mostrar sus datos. Si no existe, informar con un mensaje. 
    Si existe más de un registro que coincida con esos parámetros de búsqueda, debe mostrar 
    sólo el primero que encuentre.
            """
            x = int(input("Ingrese numero de ID a buscar: "))
            t = float(input("Ingresar la cantidad de importe a superar: "))

            pos = busqueda_secuencial(v_paquetes, x, t)

            if pos >= 0:
                print("Datos viejos:", v_paquetes[pos])
                """ Si encontraste un registro cambiar aumentar su precio un 10% """
                v_paquetes[pos].importe += v_paquetes[pos].importe * 0.1
                print("Datos Actualizados:", v_paquetes[pos])

            else:   # cuando pos es = -1
                print("No se encontro un registro.")

        elif op == 0:
            print("Gracias por usar el menu.")


if __name__ == '__main__':
    principal()
