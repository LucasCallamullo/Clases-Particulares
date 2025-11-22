

def menu():
    print("1 - Cargar arreglo.")
    print("2 - Ordenar arreglo.")
    print("3 - Vector de conteo o acum.")
    print("4 - Busqueda secuencial.")
    print("0 - Salir.")
    op = int(input("Ingresar una opcion: "))  # 3
    return op  # 3


def principal():
    op = -1

    while op != 0:  # mientras "op" sea distinto de cero, ingresar al ciclo while

        op = menu()  # 3

        if op == 1:
            pass

        elif op == 2:
            pass

        elif op == 3:
            pass

        elif op == 4:
            pass


if __name__ == '__main__':
    principal()