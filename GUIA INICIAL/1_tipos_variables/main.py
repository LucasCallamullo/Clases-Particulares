

def main():

    op = 2

    # Enteros
    if op == 0:
        n1 = int(input("Ingresar un numero: "))
        n2 = int(input("Ingresar un numero: "))
        res = n1 + n2

        print("El resultado de la suma es:", res)



    # Flotantes
    elif op == 1:
        n1 = float(input("Ingresar un numero: "))
        n2 = float(input("Ingresar un numero: "))
        res = n1 + n2

        print("El resultado de la suma es:", res)



    # Strings
    elif op == 2:
        cad1 = input("Ingresar una cadena para unir: ")
        cad2 = input("Ingresar una cadena para unir: ")
        res = cad1 + cad2
        print(res)


if __name__ == '__main__':
    main()


