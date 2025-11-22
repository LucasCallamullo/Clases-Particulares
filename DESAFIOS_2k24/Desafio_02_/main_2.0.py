





def orden_descendente(res):

    n = len(res)        # 5423  ['5', '4',

    #       0
    # res = 5432
    for i in range(n - 1):
        # i = 0,    1, 2

        for j in range(i + 1, n):
            # j = 1,    2, 3

            if res[i:i] < res[j:j]:
                res[i:i], res[j:j] = res[j:j], res[i:i]

    return int(res)


def main():

    res = 5423
    res = str(res)
    num_mayor = orden_descendente(res)  # 8730
    print(num_mayor)
    """ 
    while res != 6174:
        # num_mayor los dígitos del num ordenados de forma descendente
        res = str(res)      # "5423"

        num_mayor = orden_descendente(res)        # 8730 
        num_menor = orden_ascendente(lista)         # 378
        res = num_mayor - num_menor
        print(num_mayor, '-', num_menor, '=', res)

    print("res:", res)
    """


if __name__ == '__main__':
    main()