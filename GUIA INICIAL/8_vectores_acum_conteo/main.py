import random


def crear_lista(v1):
    for i in range(10):
        # 0 1 2 3 4 5
        num = random.randint(0, 5)
        v1.append(num)


def sort(v_conteo2, v_conteo3):
    n = len(v_conteo2)
    for i in range(n-1):
        for j in range(i+1, n):
            if v_conteo2[i] > v_conteo2[j]:
                v_conteo2[i], v_conteo2[j] = v_conteo2[j], v_conteo2[i]
                v_conteo3[i], v_conteo3[j] = v_conteo3[j], v_conteo3[i]

    print("=" * 50)
    print(v_conteo2)
    print(v_conteo3)


def main():
    # crear lista
    # v1 = []
    # crear_lista(v1)
    # print(v1)

    op = 1
    if op == 1:
        # vector conteo

        v_conteo = [0] * 6
        print(v_conteo)


        # v_years(2000, 2005)   #

        #       2000        2001                          2005
        #          0       1       2       3       4       5
        #         [0,       0,      0,      0,      0,      0]

        v_years = [2000, 2001, 2001, 2005, 2000, 2001]

        for i in v_years:
            # 2000, 2001, etc
            v_conteo[i - 2000] += 1

        print(v_conteo)








        #  0  1
        # [3, 3, 3, 4, 2, 3, 2, 0, 0, 4]
        '''
        for i in range(len(v1)):
            # i = 1
            v_conteo[v1[i] - 2000] += 1

        


        for i in range(len(v_conteo)):
            # i = 0
            if v_conteo[i] > 0:
                print("El año", i+2000, " aparecio:", v_conteo[i], "tantas veces")
        '''

    elif op == 2:

        # vector contador con arreglo paralelo
        v_conteo2 = list()
        v_conteo3 = list()

        # [5, 4, 0, 3, 5, 0, 4, 0, 3, 3]

        # v2 = 5 4 0 3                          # 4
        # v3 = 2 1 2 1

        # i = 5
        for i in v1:
            if i not in v_conteo2:
                v_conteo2.append(i)
                v_conteo3.append(1)
            else:
                for j in range(len(v_conteo2)):
                    # j = 0
                    if v_conteo2[j] == i:
                        v_conteo3[j] += 1
                        break

        print(v_conteo2)
        print(v_conteo3)

        sort(v_conteo2, v_conteo3)


    '''
    for i in range(len(v1)):
        if v1[i] in v_acum:
            for j in range(len(v_acum)):
                if v1[i] == v_acum[j]:
                    v_acum[j] += v1[i]
        else:
            v_acum.append(v1[i])

    print(v_acum)
    '''





if __name__ == '__main__':
    main()
