
from funciones import *


def menu():
    print("Trabajo Practico 3")
    print("1. Cargar arreglo desde archivo de texto")
    print("2. Cargar arreglo desde teclado")
    print("3. Listado ordenado")
    print("4. Busqueda por direccion")
    print("5. Busqueda por codigo postal")
    print("6. Cantidad de envios con direccion válida")
    print("7. Importe final acumulado")
    print("8. Envio con mayor importe")
    print("9. Importe final promedio")
    print("10. Salir")
    op = int(input("Ingrese numero de opcion: "))
    return op


def principal():
    # variable para almacenar en forma centralizada el nombre fisico del archivo de texto...
    fd = "envios-tp3.txt"

    # variable para guardar en forma centralizada el tipo de control de direcciones vigente (por default, "HC")...
    tc = "HC"

    # la referencia al arreglo...
    v_envios = []

    entro_op7 = False

    op = 0
    while op != 10:
        op = menu()

        if op == 1:
            v_envios, tc = opcion1(v_envios, tc, fd)

        elif op == 2:
            opcion2(v_envios)

        elif op == 3:
            if len(v_envios) != 0:
                opcion3(v_envios)
            else:
                print("Todavia no hay datos cargados en el arreglo...")
                print()

        elif op == 4:
            pass

        elif op == 5:
            cp = input("Ingresar codigo postal a buscar: ")
            # busqueda secuencial
            pos = opcion5(v_envios, cp)

            if pos >= 0:
                print("Registro Sin Modificar:", v_envios[pos])

                if v_envios[pos].pago == 1:
                    v_envios[pos].pago = 2
                else:
                    v_envios[pos].pago = 1

                print("Registro Modificado:", v_envios[pos])

            else:
                print("No existe.")

        elif op == 6:

            if len(v_envios) != 0:
                # generar vector conteo
                opcion6(v_envios, tc)
            else:
                print("Todavia no hay datos cargados en el arreglo...")
                print()

        elif op == 7:
            v_acum = opcion7(v_envios, tc)
            entro_op7 = True

        elif op == 8:
            if entro_op7:
                opcion8(v_acum)
            else:
                print("Ingrese primero a la opcion 7.")

        elif op == 9:
            pass

        else:
            print("Ingrese una opción correcta.")


if __name__ == "__main__":
    principal()
