














def principal2():

    n = 4
    notas = n * [0]
    for i in range(n):
        notas[i] = input("Ingrese la notas: ")

    del notas[3]
    print(notas)

    num = 10
    cadena = []
    #
    for i in range(1, num + 1):     # 1, 11
        cadena.append(i)
    print("lista de 1 a 10: ", cadena)

    #           0  1  2
    # cadena = [1, 2, 3, ..., 10]

    for i in range(len(cadena)):        # 10

        # i = 0, 1, 2, 3, ..., 9
        if cadena[i] % 2 == 0:
            print("numeros par:", cadena[i], end=" ")


    lis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("lista original: ", lis)
    lis[2:4] = ["a", "b"]       # 3, 4
    print("lista modificada 1:", lis)
    lis[2:4] = ["a", "b", "c", ]
    print("lista modificada 2:", lis)
    lis[2:] = ["lucas"]
    print("lista modificada 3:", lis)
    lis[:2] = ["brian"]
    print("lista modificada 4:", lis)
    lis[1:1] = [1, 2, 2, 3]
    print("lista modificada 5:", lis)
    lis[:] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("lista modificada 6:", lis)
    nueva_lis = lis * 2 + ["hola bebe"]
    print("lista modificada 7:", nueva_lis)


def principal():

    # tuplas
    # tuplas = ()

    # listas / vector / arreglo
    listas = []         #       lista vacía
    listas = [15, 37]   # tiene 2 elementos

    # agregar elementos al final de la lista
    listas.append(25)         # append -> anexar

    #           0    1    2
    # listas = [15, 37, 25]

    for i in listas:
        # i = 15, 37, 25
        print(i)

    for i in range(len(listas)):        # 3
        # i =  0, 1, 2
        listas.append(i)
        print(i)
        # print(listas[i])        # 0,

    suma = 0
    for i in listas:
        suma += i

    print(listas)


if __name__ == '__main__':
    principal()
