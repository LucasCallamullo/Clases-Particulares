from funciones import *


def menu():
    print("=" * 50)
    # alt + 92 = \              ; ctrl + d
    print(" 1 - Cargar Arreglo."
          "\n 2 - Mostrar Datos."
          "\n 3 - Comparar cant_dias."
          "\n 4 - Busqueda Lineal."
          "\n 0 - Salir.")

    return int(input("Ingresar opcion: "))


def main():

    # vector/lista/arreglo principal
    v_equipo = []       # = list()

    op = -1
    while op != 0:

        op = menu()

        if op == 1:
            n = validar_n()
            cargar_arreglo(v_equipo, n)

        elif op == 2:
            ordenar(v_equipo)

            # Mostrar solo los que superan un importe t donde t es un valor ingresado por teclado
            t = float(input("Ingresar importe a comparar: "))
            mostrar_datos(v_equipo, t)

        elif op == 3:
            d = int(input("Ingresar cant dias a comparar: "))
            funcion_op3(v_equipo, d)

        elif op == 4:
            c = input("Ingresar desc a buscar: ")
            pos = busqueda_lineal(v_equipo, c)

            if pos >= 0:
                print(v_equipo[pos])
            else:
                print("No se encontro el equipo con esa desc.")

        elif op == 6:
            for i in v_equipo:
                print(i)


if __name__ == '__main__':
    main()
