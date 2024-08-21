from funciones import *


def menu():
    print("=" * 50)
    print("1 - Cargar arreglo"
          "\n 2 - Mostrar datos"
          "\n 3 -  Contadores"
          "\n 4 -  "
          "\n 0 -  ")
    return int(input("Ingresar opcion: "))


def main():

    # Vector principal
    v_error = []

    op = -1
    while op != 0:
        op = menu()

        if op == 1:
            n = validar_n()
            cargar_arreglo(v_error, n)

        elif op == 2:
            ordenar_cod_error(v_error)

            s1 = int(input("Ingrese valor a de segundos s1 a comparar: "))
            s2 = int(input("Ingrese valor a de segundos s2 a comparar: "))

            mostrar_datos_op2(v_error, s1, s2)

        elif op == 3:
            completar_contadores_op3(v_error)

        elif op == 4:
            num = int(input("Ingresar numero de sistema: "))
            des = input("Ingresar descripcion: ")

            pos = busqueda_lineal(v_error, num, des)

            if pos >= 0:
                print(v_error[pos])
            else:
                print("No se encontro el error buscado.")

        # pero deberian borrar esto antes de entregar
        elif op == 6:
            for i in v_error:
                print(i)


if __name__ == '__main__':
    main()

