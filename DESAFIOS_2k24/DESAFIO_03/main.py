

import soporte
# from soporte import *


def main():
    n = 300000
    v_conteo = [0] * n

    # indices       0    1   2
    # v_conteo = [  0,   3,  2 ]

    v_lista = soporte.vector_known_range(300000)

    for i in v_lista:
        # i = 2, 1,     2, 1, 1
        v_conteo[i] += 1

    # Para calcular la cantidad de numeros distintos que aparecieron
    cont = 0

    # Para calcular modal
    mayor = None
    modal = None

    for i in range(len(v_conteo)):
        # i = 0, 1, 2
        # Para calcular la cantidad de numeros distintos que aparecieron
        if v_conteo[i] > 0:
            cont += 1

        # Para calcular modal
        if mayor is None or v_conteo[i] > mayor:
            mayor = v_conteo[i]
            modal = i

    # calcular si la modal se repite
    se_repite_mayor = 0
    for i in v_conteo:
        # i = 600, 640, 647
        if mayor == i:
            se_repite_mayor += 1

    print()
    print("=" * 100)
    print("=" * 100)
    print()

    # Para calcular la cantidad de numeros distintos que aparecieron
    print("La cantidad de numeros diferentes es:", cont)

    if se_repite_mayor == 1:
        print("La Modal es:", modal)
        print("La frecuencia de aparicion es:", mayor)
    else:
        print("La Modal es:", 0)
        print("La frecuencia de aparicion es:", 0, "porque hay mas de un modal")


def main2():

    # v_lista = [10, 15, 10, 5, 3, 10, 15]
    v_lista = soporte.vector_unknown_range(300000)

    # indices   0   1
    # v_num = [   10, 15,   5, 3]      # len = 0
    # v_cont = [  3 , 2,    1,  1]
    v_num = []
    v_cont = []

    for num in v_lista:
        # num = 10, 15, 10  , ..., 15
        pos = -1
        for i in range(len(v_num)):   # pos = posicion
            # i = 0,    1

            if v_num[i] == num:
                pos = i
                break       # Romper ciclos

        # Condiciones para segun pos
        if pos >= 0:
            v_cont[pos] += 1

        else:
            v_num.append(num)
            v_cont.append(1)

        # v_num = []
        # v_cont = []


    # Mostrar los datos de los vectores paralelos

    # Para calcular modal
    mayor = None
    modal = None

    for i in range(len(v_num)):
        # i = 0, 1, 2
        print("Para el numero:", v_num[i], "tiene una cantidad de", v_cont[i])

        # Para calcular modal
        if mayor is None or v_cont[i] > mayor:
            mayor = v_cont[i]
            modal = v_num[i]


    # calcular si la modal se repite
    se_repite_mayor = 0
    for i in v_cont:
        # i = 600, 640, 647
        if mayor == i:
            se_repite_mayor += 1


    print()
    print("=" * 100)
    print("=" * 100)
    print()

    print("La cantidad de numeros diferentes en v_num:", len(v_num))

    if se_repite_mayor == 1:
        print("La Modal es:", modal)
        print("La frecuencia de aparicion es:", mayor)
    else:
        print("La Modal es:", 0)
        print("La frecuencia de aparicion es:", 0, "porque hay mas de un modal")





if __name__ == '__main__':
    main()










"""
# crear una lista vacía
v_lista = []        # list()

# .append()     # agregar elementos al final de la lista pero conservando el contenido anterior

#
v_lista.append(30)
v_lista.append(50)
v_lista.append(70)


# indices    0   1   2
# v_lista = [30, 50, 70]

# v_lista[0] += 5

# len(v_lista) = Nos devuelve el tamaño de la lista que esta dado por su cantidad de elementos
for i in range(len(v_lista)):       # range(3)
    # i = 0,    1,  2       -> Toma valores de indices
    v_lista[i] += 1
    # v_lista = [31, 51, 71]
    

for i in v_lista:
    # i = 31, 51, 71  --> La "i" vale como caada elemento del arreglo/lista/vector
    print(i)
"""