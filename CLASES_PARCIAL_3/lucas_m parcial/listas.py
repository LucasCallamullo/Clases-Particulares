



def listas_orden():

    # indices
    listita = [10, 5, 8, 4]

    for i in listita:
        # i --> vale como cada elemento de la lista
        # 10, 5 ,8 , 4
        pass

    print(listita)
    # ordenarlo de menor a mayor

    # indices    0     1       2       3
    # listita = [4,    5,      8,      10]

    n = len(listita)    # 4
    for i in range(n - 1):      # 3
        # i --> toma los valores de indice comenzando por el cero
        # i = 0, 1,         2

        for j in range(i+1, n):     # 4
            # j = 1, 2, 3
            # j = 2, 3

            # if 5 > 4:
            if listita[i] > listita[j]:
                listita[i], listita[j] = listita[j], listita[i]

    print(listita)


def listas():

    # arreglo - listas - vector - arrays

    # lista --> un tipo de variable mutable --> que se puede modificar a lo largo del programa

    # crear una lista
    listita = []        # inicia una lista      --> list()
    # print(listita)

    # agregar elementos al final de la lista
    listita.append(5)
    # print(listita)      # [ 5 ]

    listita.append(3)
    listita.append(7)
    # print(listita)  # [ 5,  3,  7 ]

    # indice        0       1,      2
    # listita = [   5,      3,      7 ]

    # print(listita[2])       # 7
    # listita[2] = "Lucas"
    # print(listita[2])       # Lucas

    #
    # como recorrer una lista
    for i in "Lucas":
        # i = L, u, c, a, s
        pass

    for i in listita:        # = [   5,      3,      7 ]
        # i = 5,    3   ,   7
        print(i)        # 5
                        # 3
                        # 7

    #
    # como recorrer una lista
    n = len(listita)    # el tamaño de la lista que esta dado por su cantidad de elementos
    # n = 3

    # indices         0       1         2
    # listita   = [   5,      3,        7 ]
    # multiplicar todos los elementos que sean multiplos de 5 por 2
    for i in range(n):      # 3
        # la i en un ciclo for i in range --> adopta el valor de indices
        # i = 0,            1,     2

        if listita[i] % 5 == 0:
            listita[i] = listita[i] * 2     # 3

    # listita   = [   10,      3,        7 ]
    print(listita)


if __name__ == '__main__':
    # listas()
    listas_orden()