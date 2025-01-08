

from funciones import *


def menu():
    print()
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

    # Opcion 1
    fd = "envios-tp3.txt"

    tc = "HC"

    v_envios = []

    acumulador_op7 = None

    op = -1
    while op != 0:  # mientras op sea distinto de cero que ingrese al ciclo

        op = menu()     # 1

        if op == 1:
            v_envios, tc = cargar_arreglo(v_envios, fd, tc)
            print("Se cargaron la cantidad de", len(v_envios), "envios en el arreglo.")

        elif op == 2:
            cargar_envio_manual(v_envios)
            print("Se cargo 1 registro nuevo en el arreglo.")

        elif op == 3:
            if len(v_envios) > 0:
                ordenar_arreglo(v_envios)
                mostrar_datos(v_envios)
            else:
                print("Todavia no hay datos cargados en el arreglo...")
                print()

        elif op == 4:
            if len(v_envios) > 0:
                d = input("Ingresar direccion a buscar: ")
                e = int(input("Ingresar tipo de envio a buscar (0, 6): "))
                pos = busqueda_scuencial_op4(v_envios, d, e)
                if pos >= 0:
                    print(v_envios[pos])
                else:
                    print("No se encontro un resultado")

            else:
                print("Todavia no hay datos cargados en el arreglo...")
                print()

        elif op == 5:
            if len(v_envios) > 0:
                cp = input("Ingrese CP a buscar: ")
                pos = busqueda_secuencial_op5(v_envios, cp)

                # efectuar_cambios_op5(v_envios, pos)
                if pos >= 0:
                    print("Datos Viejos: ", v_envios[pos])

                    if v_envios[pos].forma_pago == 1:
                        v_envios[pos].forma_pago = 2
                    else:
                        v_envios[pos].forma_pago = 1

                    print("Registro Actualizado: ", v_envios[pos])

                else:
                    print("No se encontro un resultado")
            else:
                print("Todavia no hay datos cargados en el arreglo...")
                print()

        elif op == 6:
            if len(v_envios) > 0:
                generar_vector_conteo(v_envios, tc)
            else:
                print("Todavia no hay datos cargados en el arreglo...")
                print()

        elif op == 7:
            if len(v_envios) > 0:
                acumulador_op7 = generar_vector_acum(v_envios, tc)
            else:
                print("Todavia no hay datos cargados en el arreglo...")
                print()

        elif op == 8:
            if acumulador_op7 is None:
                print("Primero debe ingresar a la opcion 7.")
            else:
                opcion8(acumulador_op7)

        elif op == 9:
            if len(v_envios) > 0:
                promedio = calc_prom_op9(v_envios)
                opcion9(v_envios, promedio)
            else:
                print("Todavia no hay datos cargados en el arreglo...")
                print()

        elif op == 10:
            print("Salio del menu.")

        else:
            print("Ingrese una opcion correcta.")


if __name__ == '__main__':
    principal()
