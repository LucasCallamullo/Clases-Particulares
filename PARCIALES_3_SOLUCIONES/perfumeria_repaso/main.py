from funciones import *


def menu():
    print("=" * 50)
    print(" 1 - Cargar Arreglo"
          "\n 2 - Mostrar Datos"     # Alt + 92 == \
          "\n 3 - Opcion3 Datos"     
          "\n 4 - Opcion4 Datos"     
          "\n 5 - Opcion5 Datos")
    op = int(input("Ingresar opcion: "))
    return op


def main():

    # Arreglo inicial con el vamos a trabajar
    v_venta = []

    # Bandera para opcion 1
    b_op1 = False

    op = -1
    while op != 0:
        op = menu()

        if not b_op1:
            if op == 1:
                n = int(input("Ingresar cant de ventas a cargar: "))
                cargar_arreglo(v_venta, n)
                b_op1 = True
            else:
                print("Primero debe cargar el arreglo en la opcion 1.")

        else:
            if op == 1:
                n = int(input("Ingresar cant de ventas a cargar: "))
                cargar_arreglo(v_venta, n)
                b_op1 = True

            elif op == 2:
                # Funcion de ordenamiento
                sort(v_venta)

                # Buscar valores por teclado
                # Importe
                x = float(input("Ingrese por teclado un importe: "))
                # Tipo de factura
                # t = input("Ingrese una factura: ")
                t = validar_t()

                mostrar_datos_op2(v_venta, x, t)

            elif op == 3:
                z = int(input("Ingresar numero: "))
                funcion_op3(v_venta, z)

            elif op == 4:
                funcion_op4(v_venta)

            elif op == 5:
                # Num Factura
                n = int(input("Ingresar numero de fact: "))
                # Importe
                p = float(input("Ingresar importe: "))

                pos = funcion_op5(v_venta, n, p)
                if pos >= 0:
                    print("Se encontro uno que coincida")
                    print(v_venta[pos])
                else:
                    print("No se encontro")


            elif op == 0:
                print("Gracias por usar el programa.")


if __name__ == '__main__':
    main()
