

from registro import *
from funciones import *


# =====================================================================
#                       Opcion 1
# =====================================================================
def cargar_arreglo(v_envios):
    fd = "envios-tp3.txt"  # file description
    m = open(fd, "rt")
    cont_lineas = 0

    for linea in m:
        cont_lineas += 1

        if cont_lineas == 1:
            pass

        else:
            cod_postal = linea[0:9].strip()
            direccion = linea[9:29].rstrip()
            tipo_envio = int(linea[29])
            forma_pago = int(linea[30])
            envio = Envio(cod_postal, direccion, tipo_envio, forma_pago)
            v_envios.append(envio)
            # v_envios = [ E1, E2, E3, ..., ]

    print("Se cargaron la cantidad de envios: ", cont_lineas-1)


# =======================================================================
#                       Opcion 2
# =======================================================================
def cargar_manualmente(v_envios):
    pass
    # cod_postal ) input
    # tipo_envio = int(input(
    # while tipo_envio tiene que ser entre 0  y 6)
    #       tipo_envio = int(input(
    # envio = Envio(cod_postal, direccion, tipo_envio, forma_pago)
    # v_envios.append(envio)
    #


# =======================================================================
#                       Opcion 5
# =======================================================================
def busqueda_secuencial_op5(v_envios, cp):
    pos = -1
    # indices      0   1   2
    # v_envios = [E1, E2, E3]
    for i in range(len(v_envios)):  # 3
        # i = 0, 1, 2            x
        if v_envios[i].cod_postal == cp:
            pos = i
            break   # romper ciclos

    return pos      # 0 >=    ;   -1




def menu():
    # ctrl + d
    print("1 - Cargar Arreglo.")
    print("2 - ")
    print("3 - Mostrar Datos. ")
    print("5 - Busqueda Secuencial")
    print("0 - Salir. ")

    op = int(input("Ingresar opcion: "))    # 4
    return op    # 4       # devolver / retornar


def principal():

    v_envios = []

    op = -1
    while op != 0:          # mientras op sea distinto de cero, ingreso al ciclo while

        # si igualamos una variable a una funcion, es porque espero que la funcion me devuelva algun valor
        op = menu()

        if op == 1:
            cargar_arreglo(v_envios)

        elif op == 2:
            cargar_manualmente(v_envios)

        elif op == 3:
            # ordenar_arreglo(v_envios)
            shell_sort(v_envios)

            # menu
            #
            # while
            #   if op 1
            #       m = int(input
            #        mostrar_datos ( v_Envios, m )
            #   op = 2
            #      mostrar_datos(v_envios, 0)
            mostrar_datos(v_envios)

        elif op == 4:
            pass

        elif op == 5:
            cp = input("Ingresar cod postal a buscar: ")

            pos = busqueda_secuencial_op5(v_envios, cp)

            if pos >= 0:
                print("Datos Viejos:", v_envios[pos])

                # v_envios[pos].importe += 0.1 * v_envios[pos].importe
                # v_envios[pos].importe = int(input("Ingrese nuevo importe: "))

                if v_envios[pos].forma_pago == 1:
                    v_envios[pos].forma_pago = 2
                else:       # cuando es 2
                    v_envios[pos].forma_pago = 1

                print("Datos Actualizados:", v_envios[pos])

            else:
                print("No se encontro un envio con ese codigo postal.")


        elif op == 0:
            print("Gracias por usar el menu.")
        else:
            print("INgrese un numero valido.")


if __name__ == '__main__':
    principal()
