

def main():
    # Para controlar cual vamos a ver
    op = 0

    # Condiciones Simples
    if op == 0:

        if op == 1:
            pass
        elif op == 2:
            pass
        elif op == 3:
            pass




        n1 = int(input("Ingresar un número: "))
        n2 = int(input("Ingresar un número: "))
        res = n1 + n2

        if res < 10:
            print("El resultado es menor a 10.")
        elif res <= 20:
            print("El resultado esta entre 10 y 20.")
        else:
            cadena = "El resultado es mayor a 20."
            print(cadena)

    # Condiciones compuestas (and)
    elif op == 1:

        n1 = int(input("Ingresar un número: "))
        n2 = int(input("Ingresar un número: "))
        res = n1 + n2

        if res <= 10 and res % 2 == 0:
            print("El resultado es " + str(res) + " y es menor a 10 y par.")

        elif res <= 10 and res % 2 != 0:
            print("El resultado es " + str(res) + " y es menor a 10 e impar.")

        else:
            print("El resultado es " + str(res) + " y es mayor a 10.")


    # Condiciones compuestas (or)
    elif op == 2:

        n1 = int(input("Ingresar un número: "))
        n2 = int(input("Ingresar un número: "))
        res = n1 + n2

        if res <= 10 or res % 2 == 0:
            # res
            print("El resultado es " + str(res) + " y es menor a 10 y par.")

        elif res <= 10 or res % 2 != 0:
            print("El resultado es " + str(res) + " y es menor a 10 e impar.")

        else:
            print("El resultado es " + str(res) + " y es mayor a 10.")



    # if not

    elif op == 3:

        num = int(input("Ingresar un número: "))
        if not num == 0:
            print("El numero no es 0.")
        else:
            print("El numero es 0.")





if __name__ == '__main__':
    main()
