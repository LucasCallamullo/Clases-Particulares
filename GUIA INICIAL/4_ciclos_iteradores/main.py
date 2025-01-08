import random


def main():
    # para controlar que estamos viendo
    op = 2

    # Ciclo for
    if op == 0:

        # Contador de vueltas
        cont = 0

        # Acumulador de vueltas
        acum = 0

        # n = int(input("Ingrese cuantas vueltas va a dar: "))

        # Promedio
        # prom = sumariamos un acumulacion/total  /  dividimos por la cantidad de elementos que sumamos

        # vector / lista arreglo
        #    0      1       2
        v = [5,     7,      9]                       # [99, 58, 42 , 99, 58, 42]


        #  0 1 2
        for i in range(3):              # 0       1       2
            # i = 0                 1                   2
            print("La i vale:", i)
            print("el vector en el indice:", v[i])
            acum += v[i]         # v[0] = 5
            cont += 1

        print("El contador es:", cont)
        print("El acumulador es:", acum)


    # Ciclo for
    elif op == 1:

        # Cadena
        # cadena = input("Ingresar palabra: ")

        # Tupla       0         1        2         3         4              # Tuplas no se puede modificar.
        # Tupla
        # nombres = ("Lucas", "Matias", "Tomas", "Mariano", "Jere")

        # Lista - Vector - Arreglo

        #             0         1         2         3        4
        nombres = ["Lucas", "Matias", "Tomas", "Mariano", "Jere"]
        numeros = [0,           58,       99,      45]
        # numeros = [OBJ,           OBJ,       OBJ,      OBJ]
        name = random.choice(nombres)

        for i in nombres:
            # i = "Lucas",      "Matias" ...
            if i == "Tomas":
                print(i)
                # break
            else:
                print("No es Tomas")


        # 012345678910
        cadena = input("Ingresemos la palabra: ")
        #
        # Hola MUndo

        vocales = "aeiou"

        # i.lower()
        # Hola Mundo   ==  hola mundo

        # i.upper()
        # hola mundo   == HOLA MUNDO

        # cont
        cant_vocales = 0

        for i in cadena:
            # i = H, o , l ,a, " ",
            if i.lower() in vocales:
                cant_vocales += 1

        print("La palabra es:", cadena)
        print("Las vocales que hay son:", cant_vocales)





    # Ciclo while
    elif op == 2:

        # Acumulador
        acum = 0
        infinito = False         # Tipo de variable = bool / bandera

        # while infinito:       # mientras infinito sea true
        while not infinito:       # mientras infinito sea false

            num = random.randint(25, 25)
            acum += num
            print("El numero es:", num)
            print("El acumulador parcial es:", acum)

            if acum > 100:
                # infinito = True
                break


        print("=" * 50)
        print("El acumulador final es:", acum)



    # Romper Ciclo while o for
    elif op == 3:

        acum = 0
        while not acum < 0:         # cuando no sea menor a 0
            acum += random.randint(10, 10)
            print("El acumulador actualmente es:", acum)

            if acum >= 100:
                # romper ciclo
                print("Se rompio el ciclo")
                break

        print("=" * 50)
        print("El acumulador con el que rompio ciclo es:", acum)


if __name__ == '__main__':
    main()
