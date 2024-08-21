from funciones import *


def menu():
    print("=" * 50)
    # alt + 92 = \
    print(" 1 - Cargar Arreglo."
          "\n 2 - Mostrar Datos."
          "\n 3 - "
          "\n 4 - Busqueda lineal."
          "\n 5 - Vector contadores."
          "\n 0 - Salir.")
    op = int(input("Ingresar una opcion: "))
    return op


def main():

    # vector/arreglo/lista principal con la que vamos a trabajar
    v_trabajo = []              # list()


    op = -1
    while op != 0:

        op = menu()

        if op == 1:
            n = validar_n()
            cargar_arreglo(v_trabajo, n)

        elif op == 2:
            ordenar(v_trabajo)

            # mostrar los datos que superen un importe t, donde t es un valor ingresado por el usuario
            t = float(input("Ingresar un importe a comparar: "))
            mostrar_datos(v_trabajo, t)

        elif op == 3:
            calcular_mayor_op3(v_trabajo)

        elif op == 4:
            # descripcion, importe
            d = input("Ingresar descripcion a buscar (A, B, C, D): ")
            # importe a superar
            t = float(input("Ingresar importe a superar: "))

            pos = busqueda_lineal(v_trabajo, d, t)

            if pos >= 0:
                print("La posicion es: ", pos)
                print(v_trabajo[pos])
            else:
                print("No se encontro.")

        elif op == 5:
            v_contadores_op5(v_trabajo)

        elif op == 0:
            print("Gracias por usar el programa.")

        elif op == 6:
            for i in v_trabajo:
                print(i)


        else:
            print("Por favor elija una opcion correcta.")


# main
if __name__ == '__main__':
    main()
