from funciones import *


def menu():
    print("=" * 50)
    print(" 1 - Cargar arreglo."
          "\n 2 - Mostrar datos."
          "\n 3 - "
          "\n 4 - "
          "\n 0 - Salir")
    return int(input("Ingresar opcion: "))


def main():

    v_servicio = []

    op = -1
    while op != 0:

        op = menu()

        if op == 1:
            n = validar_n()
            cargar_arreglo(v_servicio, n)

        elif op == 2:
            ordenar(v_servicio)
            mostrar_datos(v_servicio)

        elif op == 3:
            v_contadores_op3(v_servicio)

        elif op == 4:
            d = input("INgrese desc a buscar: ")
            p = int(input("Ingrese cant personas a superar: "))

            pos = busqueda_lineal(v_servicio, d, p)

            if pos >= 0:
                print("La posicion es:", pos)

                print(v_servicio[pos])
            else:
                print("No se encontro Servicio.")

        elif op == 6:
            for i in v_servicio:
                print(i)


if __name__ == '__main__':
    main()
