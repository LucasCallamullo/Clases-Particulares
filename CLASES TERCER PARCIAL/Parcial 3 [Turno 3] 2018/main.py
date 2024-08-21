

from funciones import *


def menu():
    print("=" * 50)
    # alt 92 = \\\
    print(" 1 - Cargar Arreglo."
          # Con ctrl + d copias la linea anterior
          "\n 2 - Mostrar Datos"
          "\n 3 -  "
          "\n 4 - "
          "\n 0 - Salir")
    return int(input("Ingresar una opcion: "))


def principal():

    # vector principal con el que trabajamos
    v_paq = []

    op = -1
    while op != 0:

        op = menu()

        if op == 1:
            n = validar_n()
            cargar_arreglo(v_paq, n)

        elif op == 2:
            # ordenarlo por cant de dias
            ordenar(v_paq)

            # si no podian que mostremos los datos mayores a t, donde t es un importe cargado por teclado.
            t = float(input("Ingresar un importe a comparar: "))
            mostrar_datos(v_paq, t)

        elif op == 3:
            v_contadores_op3(v_paq)

        elif op == 4:
            x = int(input("Ingresar id: "))
            t = float(input("Ingresar importe: "))
            pos = busqueda_secuencial(v_paq, x, t)

            if pos >= 0:
                print(v_paq[pos])
            else:
                print("No se encontro la busqueda.")


        # calcular el mayor importe y mostrar solo el que contenga el mayor importe no importa si existe mas de uno
        # mostrar solo el primero
        elif op == 5:
            calcular_mayor(v_paq)


        # al final borrar esta funcion/opcion
        elif op == 6:
            for i in v_paq:
                print(i)


# main
if __name__ == '__main__':
    principal()
