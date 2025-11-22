


def sumar(n1, n2):
    x = n1 + n2     # 5
    return x        # 5


def menu():
    print("1 - Sumar numeros.")
    print("2 - Restar numeros.")
    print("0 - Salir")
    op = int(input("Ingresar opcion: "))  # str  1
    return op


def principal():
    # for --> bucle finitos, sabes de antemano cuantas vueltas vas a dar
    # while --> bucle infinito, NO sabes de antemano cuantas vueltas vas a dar

    op = -1
    while op != 0:      # mientras op sea distinto de cero ingreso al ciclo

        op = menu()

        n1 = int(input("Ingresar numero 1: "))      # 3
        n2 = int(input("Ingresar numero 2: "))      # 2
        # op = 1

        if op == 1:
            # si una variable esta igualada a una funcion es porque espero que la funcion retorne algo
            res = sumar(n1, n2)
            # res = 5
            print("El resultado es:", res)

        elif op == 2:
            print("eligio opcion 2")

        # op = 0


if __name__ == "__main__":
    principal()

