




def orden_ascendente(lista):
    # indice   0  1  2  3
    # lista = [5, 4, 2, 3]
    n = len(lista)      # 4 - 1 = 3

    for i in range(n-1):
        # i = 0,    1, 2

        for j in range(i+1, n):
            # j = 1,    2, 3

            # lista[0] = 5
            # lista[1] = 4
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]

    # termina este for, # [5, 4, 3, 2]
    numero = ''
    for num in lista:
        numero += str(num)
    # numero = "5432"
    numero = int(numero)  # 5432
    return numero


def orden_descendente(lista):
    # indice   0  1  2  3
    # lista = [5, 4, 2, 3]
    n = len(lista)      # 4 - 1 = 3

    for i in range(n-1):
        # i = 0,    1, 2

        for j in range(i+1, n):
            # j = 1,    2, 3

            # lista[0] = 5
            # lista[1] = 4
            if lista[i] < lista[j]:
                lista[i], lista[j] = lista[j], lista[i]

    # termina este for, # [5, 4, 3, 2]
    numero = ''
    for num in lista:
        numero += str(num)
    # numero = "5432"
    numero = int(numero)    # 378
    return numero


def main():

    # res = 5423
    # res = int(input("Ingresar numero: "))

    cont_6174 = 0
    cont_0 = 0

    # buscar el mayor
    cant_mayor_pasos = None
    res_mayor_pasos = None

    # promedio de cantidad de pasos sobre total de numeros
    # (total de iteraciones // cantidad de números).
    acum_pasos = 0
    cant_numeros = 9000

    cont_num = 0

    for num in range(1000, 10000):    # desde el 1000 hasta el 9999
        res = num
        # res = 1001
        pasos = 0
        cont_num += 1

        while res != 6174 and res != 0:
            # num_mayor los dígitos del num ordenados de forma descendente
            lista = []
            for i in str(res):  # "1001"
                # i = "1" "0" "0" "1"
                lista.append(int(i))

            num_mayor = orden_descendente(lista)        # 9811
            num_menor = orden_ascendente(lista)         # 1189

            res = num_mayor - num_menor     # xxxx

            # Si vos quisieras conservar el 0
            # res = str(res)  # '999'
            # if len(res) != 4:
            #    res = '0' + str(res)        # '0999'
            # res = int(res)

            pasos += 1


            # print(num_mayor, '-', num_menor, '=', res)

        # Fuera del ciclo while
        if res == 6174:
            cont_6174 += 1

        elif res == 0:
            cont_0 += 1

        # 1000: pasos 1
        # 1001: pasos 9
        if cant_mayor_pasos is None or cant_mayor_pasos < pasos:
            cant_mayor_pasos = pasos  # 5
            res_mayor_pasos = num

        acum_pasos += pasos

    print("Cantidad de veces que termina en 6174:", cont_6174)
    print("Cantidad de veces que termina en 0:", cont_0)
    print("cant_mayor_pasos:", cant_mayor_pasos)

    print("acum_pasos:", acum_pasos)
    print("Total de numeros analizados:", cont_num)
    # print("res_mayor_pasos:", res_mayor_pasos)

    promedio = acum_pasos // cont_num
    print('Promedio:', promedio)







if __name__ == '__main__':
    main()

