

from funciones import *


def menu():
    print("=" * 50)
    print(" 1- Cargar Arreglo."
          "\n 2- Mostrar datos"
          "\n 3- Mostrar datos"
          "\n 4- Mostrar datos"
          "\n 0- Salir")
    return int(input("Ingresar opcion: "))


def main():

    # vector con el que vaamos a trabajar
    v_paseo = []

    op = -1
    while op != 0:

        op = menu()

        if op == 1:
            n = validar_n()
            cargar_arreglo(v_paseo, n)

        elif op == 2:
            ordenar(v_paseo)
            mostrar_datos(v_paseo)

        elif op == 3:
            v_acum = acumuladores_op3(v_paseo)
            c = float(input("Ingresar importe a comparar: "))
            mostrar_acum_op3(v_acum, c)

        elif op == 4:
            nom = input("Ingresar nombre a buscar: ")
            pos = busqueda_secuencial(v_paseo, nom)

            if pos >= 0:
                print("Id:", v_paseo[pos].id, "Importe:", v_paseo[pos].importe)
            else:
                print("No se encontro el nombre.")

        # elif op == 6:
        #    for i in range(len(v_paseo)):
        #        print(v_paseo[i])


if __name__ == '__main__':
    main()
